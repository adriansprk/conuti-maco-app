# Lieferbeginn

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /inbound:
    post:
      summary: Lieferbeginn
      deprecated: false
      description: >-
        Prozess zur Anmeldung einer erzeugenden oder verbrauchenden
        Marktlokation.
      operationId: START_LIEFERBEGINN
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht LF
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BLF%5D%20START_LIEFERBEGINN'
            examples:
              '1':
                value:
                  stammdaten:
                    MARKTLOKATION:
                      - boTyp: MARKTLOKATION
                        versionStruktur: '1'
                        marktlokationsId: '50754496000'
                        erforderlichesProduktpaket:
                          - produktpaketId: 1
                            produkt:
                              - produktCode: '9991000002082'
                                wertedetails: 11Y0-0000-0077-K
                              - produktCode: '9991000002008'
                                codeProdukteigenschaft: '9991000002115'
                            umsetzungsgradvorgabe: ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
                        marktlokationsTyp:
                          - typ: STANDARD_MARKTLOKATION
                    NETZNUTZUNGSVERTRAG:
                      - boTyp: VERTRAG
                        versionStruktur: '1'
                        vertragsart: NETZNUTZUNGSVERTRAG
                        sparte: STROM
                        vertragskonditionen:
                          haushaltskunde: true
                    ENERGIELIEFERVERTRAG:
                      - boTyp: VERTRAG
                        versionStruktur: '1'
                        vertragsart: ENERGIELIEFERVERTRAG
                        sparte: STROM
                        vertragspartner2:
                          - boTyp: GESCHAEFTSPARTNER
                            versionStruktur: '1'
                            anrede: Herr
                            name1: Glöppel
                            name2: Walter
                            gewerbekennzeichnung: false
                            geschaeftspartnerrolle:
                              - KUNDE
                        korrespondenzpartner:
                          boTyp: GESCHAEFTSPARTNER
                          versionStruktur: '1'
                          name1: Glöppel
                          gewerbekennzeichnung: false
                          partneradresse:
                            postleitzahl: '41515'
                            ort: Grevenbroich
                            strasse: Bahnstraße
                            hausnummer: '49'
                            landescode: DE
                        enFG:
                          - grundlageVerringerungUmlagen: ERFUELLT_VORAUSSETZUNG_NACH_ENFG
                            grund:
                              - ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
                  transaktionsdaten:
                    transaktionsgrund: E01
                    transaktionsgrundergaenzung: ZW4
                    sparte: STROM
                    vertragsbeginn: '2025-10-31T23:00:00Z'
                    absender:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      rollencodenummer: '9903526000002'
                      rollencodetyp: BDEW
                    empfaenger:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      rollencodenummer: '9900683000008'
                      rollencodetyp: BDEW
                    kategorie: E01
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_LIEFERBEGINN
                summary: Anmeldung verbr. Marktlokation Strom
              '2':
                value:
                  stammdaten:
                    MARKTLOKATION:
                      - boTyp: MARKTLOKATION
                        versionStruktur: '1'
                        marktlokationsId: '50754496001'
                        erforderlichesProduktpaket:
                          - produktpaketId: 1
                            produkt:
                              - produktCode: '9991000002082'
                                wertedetails: 11Y0-0000-0077-K
                              - produktCode: '9991000002008'
                                codeProdukteigenschaft: '9991000002115'
                              - produktCode: '9991000002769'
                                codeProdukteigenschaft: '9991000002933'
                            umsetzungsgradvorgabe: ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
                        marktlokationsTyp:
                          - typ: RUHENDE_MARKTLOKATION
                    NETZNUTZUNGSVERTRAG:
                      - boTyp: VERTRAG
                        versionStruktur: '1'
                        vertragsart: NETZNUTZUNGSVERTRAG
                        sparte: STROM
                        vertragskonditionen:
                          haushaltskunde: true
                    ENERGIELIEFERVERTRAG:
                      - boTyp: VERTRAG
                        versionStruktur: '1'
                        vertragsart: ENERGIELIEFERVERTRAG
                        sparte: STROM
                        vertragspartner2:
                          - boTyp: GESCHAEFTSPARTNER
                            versionStruktur: '1'
                            anrede: Herr
                            name1: Glöppel
                            name2: Walter
                            gewerbekennzeichnung: false
                            geschaeftspartnerrolle:
                              - KUNDE
                        korrespondenzpartner:
                          boTyp: GESCHAEFTSPARTNER
                          versionStruktur: '1'
                          name1: Glöppel
                          gewerbekennzeichnung: false
                          partneradresse:
                            postleitzahl: '41515'
                            ort: Grevenbroich
                            strasse: Bahnstraße
                            hausnummer: '49'
                            landescode: DE
                        enFG:
                          - grundlageVerringerungUmlagen: ERFUELLT_VORAUSSETZUNG_NACH_ENFG
                            grund:
                              - ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
                  transaktionsdaten:
                    transaktionsgrund: E01
                    transaktionsgrundergaenzung: ZAP
                    transaktionsgrundergaenzungBefristeteAnmeldung: E03
                    sparte: STROM
                    vertragsbeginn: '2025-10-31T23:00:00Z'
                    vertragsende: '2025-12-31T23:00:00Z'
                    absender:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      rollencodenummer: '9979052000006'
                      rollencodetyp: BDEW
                    empfaenger:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      rollencodenummer: '9900683000008'
                      rollencodetyp: BDEW
                    kategorie: E01
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_LIEFERBEGINN
                summary: Anmeldung ruhende Marktlokation Strom befristet
      responses:
        '201':
          description: Erfolg | Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EVENT_SUCCESS'
          headers: {}
          x-apidog-name: Created
        '400':
          description: Fehler | Fail
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EVENT_FAIL'
          headers: {}
          x-apidog-name: Bad Request
      security:
        - bearer: []
      x-apidog-folder: Schnittstellen/Trigger (MACO APP)/Einzelansicht LF
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14992210-run
components:
  schemas:
    '[LF] START_LIEFERBEGINN':
      allOf:
        - oneOf:
            - $ref: '#/components/schemas/PI_55001'
            - $ref: '#/components/schemas/PI_55077'
            - $ref: '#/components/schemas/PI_55600'
            - $ref: '#/components/schemas/PI_55601'
            - $ref: '#/components/schemas/44001_Anmeldung'
        - type: object
          properties:
            zusatzdaten:
              type: object
              properties:
                prozessId:
                  type: string
                  description: >-
                    Id des Dokuments / Beleges im Backend. Wird genutzt um die
                    Antwort zuzuordnen.
                  x-apidog-mock: '{{$string.uuid}}'
                  examples:
                    - 00505688-E4A2-1EDF-A0C2-C81842E2515E
                  title: >-
                    ID of the document / record in the backend. Used to map the
                    response.
                eventname:
                  type: string
                  description: Name des Events
                  default: START_LIEFERBEGINN
                  title: name of event
              x-apidog-orders:
                - prozessId
                - eventname
              required:
                - prozessId
                - eventname
              title: additional event data
              x-apidog-ignore-properties: []
          x-apidog-refs: {}
          x-apidog-orders:
            - zusatzdaten
          required:
            - zusatzdaten
          x-apidog-ignore-properties: []
      x-apidog-folder: ''
    44001_Anmeldung:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            MESSLOKATION:
              type: array
              items:
                type: object
                properties:
                  ablesekartenempfaenger:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          postfach:
                            type: string
                            description: |-
                              Postfach | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                          ort:
                            type: object
                            title: Sort
                            description: |-

                              <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                            x-apidog-orders: []
                            properties: {}
                            x-apidog-ignore-properties: []
                          hausnummer:
                            type: string
                            description: |-
                              Hausnummer und Ergänzung | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                          landescode:
                            type: string
                            title: Landescode
                            description: |-
                              Der ISO-Landescode als Enumeration | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                            enum:
                              - AC
                              - AD
                              - AE
                              - AF
                              - AG
                              - AI
                              - AL
                              - AM
                              - AN
                              - AO
                              - AQ
                              - AR
                              - AS
                              - AT
                              - AU
                              - AW
                              - AX
                              - AZ
                              - BA
                              - BB
                              - BD
                              - BE
                              - BF
                              - BG
                              - BH
                              - BI
                              - BJ
                              - BL
                              - BM
                              - BN
                              - BO
                              - BQ
                              - BR
                              - BS
                              - BT
                              - BU
                              - BV
                              - BW
                              - BY
                              - BZ
                              - CA
                              - CC
                              - CD
                              - CF
                              - CG
                              - CH
                              - CI
                              - CK
                              - CL
                              - CM
                              - CN
                              - CO
                              - CP
                              - CR
                              - CS
                              - CU
                              - CV
                              - CW
                              - CX
                              - CY
                              - CZ
                              - DE
                              - DG
                              - DJ
                              - DK
                              - DM
                              - DO
                              - DZ
                              - EA
                              - EC
                              - EE
                              - EG
                              - EH
                              - ER
                              - ES
                              - ET
                              - EU
                              - FI
                              - FJ
                              - FK
                              - FM
                              - FO
                              - FR
                              - FX
                              - GA
                              - GB
                              - GD
                              - GE
                              - GF
                              - GG
                              - GH
                              - GI
                              - GL
                              - GM
                              - GN
                              - GP
                              - GQ
                              - GR
                              - GS
                              - GT
                              - GU
                              - GW
                              - GY
                              - HK
                              - HM
                              - HN
                              - HR
                              - HT
                              - HU
                              - IC
                              - ID
                              - IE
                              - IL
                              - IM
                              - IN
                              - IO
                              - IQ
                              - IR
                              - IS
                              - IT
                              - JE
                              - JM
                              - JO
                              - JP
                              - KE
                              - KG
                              - KH
                              - KI
                              - KM
                              - KN
                              - KP
                              - KR
                              - KW
                              - KY
                              - KZ
                              - LA
                              - LB
                              - LC
                              - LI
                              - LK
                              - LR
                              - LS
                              - LT
                              - LU
                              - LV
                              - LY
                              - MA
                              - MC
                              - MD
                              - ME
                              - MF
                              - MG
                              - MH
                              - MK
                              - ML
                              - MM
                              - MN
                              - MO
                              - MP
                              - MQ
                              - MR
                              - MS
                              - MT
                              - MU
                              - MV
                              - MW
                              - MX
                              - MY
                              - MZ
                              - NA
                              - NC
                              - NE
                              - NF
                              - NG
                              - NI
                              - NL
                              - 'NO'
                              - NP
                              - NR
                              - NT
                              - NU
                              - NZ
                              - OM
                              - PA
                              - PE
                              - PF
                              - PG
                              - PH
                              - PK
                              - PL
                              - PM
                              - PN
                              - PR
                              - PS
                              - PT
                              - PW
                              - PY
                              - QA
                              - RE
                              - RO
                              - RS
                              - RU
                              - RW
                              - SA
                              - SB
                              - SC
                              - SD
                              - SE
                              - SF
                              - SG
                              - SH
                              - SI
                              - SJ
                              - SK
                              - SL
                              - SM
                              - SN
                              - SO
                              - SR
                              - SS
                              - ST
                              - SU
                              - SV
                              - SX
                              - SY
                              - SZ
                              - TA
                              - TC
                              - TD
                              - TF
                              - TG
                              - TJ
                              - TK
                              - TL
                              - TM
                              - TN
                              - TO
                              - TP
                              - TR
                              - TT
                              - TV
                              - TW
                              - TZ
                              - UA
                              - UG
                              - UK
                              - UM
                              - US
                              - UY
                              - UZ
                              - VA
                              - VC
                              - VE
                              - VG
                              - VI
                              - VN
                              - VU
                              - WF
                              - WS
                              - XK
                              - YE
                              - YT
                              - YU
                              - ZA
                              - ZM
                              - ZR
                              - ZW
                            x-apidog-folder: Bo4e/ENUM
                          strasse:
                            type: string
                            description: |-
                              Strasse | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                          ortsteil:
                            type: string
                            description: |-
                              Ortsteil | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                          postleitzahl:
                            type: string
                            description: |-
                              Postleitzahl | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                        x-apidog-orders:
                          - postfach
                          - ort
                          - hausnummer
                          - landescode
                          - strasse
                          - ortsteil
                          - postleitzahl
                        x-apidog-ignore-properties: []
                      gewerbekennzeichnung:
                        type: boolean
                        description: >-
                          Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
                          (gewerbeKennzeichnung = true)

                          oder eine Privatperson handelt. (gewerbeKennzeichnung
                          = false)

                          Z01 Struktur von Personennamen

                          Z02 Struktur der Firmenbezeichnung | 

                          <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                      name4:
                        type: string
                        description: |-
                          Name 4 | 
                          <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder bei Privatpersonen
                          beispielsweise der Vorname dargestellt werden.
                          Beispiele: Bereich Süd oder Nina | 

                          <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen beispielsweise der Nachname
                          dargestellt werden. Beispiele: Yellow Strom GmbH oder
                          Hagen | 

                          <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder bei Privatpersonen
                          Zusätze zum  Namen dargestellt werden. Beispiele: und
                          Afrika oder Sängerin | 

                          <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                      anrede:
                        type: string
                        description: |-
                          Die Anrede für den GePa, Z.B. Herr.
                          Z04 Korrespondenzanschrift des Kunden des Lieferanten
                          PI 55001 55600 55601 55013 55014 55043 55168 55169 | 
                          <TipInfo>SG4.IDE+24.SG12.NAD+Z05</TipInfo>
                    x-apidog-orders:
                      - partneradresse
                      - gewerbekennzeichnung
                      - name4
                      - name2
                      - name1
                      - name3
                      - anrede
                    x-apidog-ignore-properties: []
                  messlokationsId:
                    type: string
                    description: >-
                      Angabe der ID der Messlokation,  für die die Stammdaten
                      gelten. Die ID dient der eindeutigen Identifikation einer
                      Messlokation und wird spätestens bei der Bestätigung vom
                      NB mitgeliefert.

                      LOC Z17

                      PI 55002 55078 55600 55602 55601 55603 55013 55607 55611
                      55620 55626 55632 55638 55175 55180 55173 55177 55690
                      55643 55648 55653 55658 55663 55669 55035 55095 55060
                      55039 55040 55041 55042 55043 55044 55168 55169 55170
                      55051 55052 55053 55074 55075 55076

                      RFF Z19

                      PI 55002 55078 55602 55603 55013 55607 55690 55035 55095
                      55060 55194 55043 55168 55169 

                      RFF Z46

                      PI 55643 55648 55663 55669 

                      RFF Z19 ORDERS 

                      PI 17121 17134

                      IFTSTA 

                      LOC 172

                      PI 21000 21001 21002 21003 21004 21005 21007 21009 21010
                      21011 21012 21013 21015 21018 21024 21025 21026 21027
                      21036 21028 21029 21030 21031 21033 

                      QUOTES

                      LOC 172 

                      PI 15001 15003 15004

                      LOC 172 INVOIC

                      PI 31003 31009 31004  | 

                      <TipInfo>SG4.IDE+24.SG5.LOC+172,
                      SG4.IDE+24.SG12.NAD+Z05.RFF+Z19</TipInfo>
                x-apidog-orders:
                  - ablesekartenempfaenger
                  - messlokationsId
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  lokationsadresse:
                    type: object
                    properties:
                      zusatzInformation:
                        type: object
                        properties:
                          landescode:
                            type: string
                            title: Landescode
                            description: |-
                              Der ISO-Landescode als Enumeration | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                            enum:
                              - AC
                              - AD
                              - AE
                              - AF
                              - AG
                              - AI
                              - AL
                              - AM
                              - AN
                              - AO
                              - AQ
                              - AR
                              - AS
                              - AT
                              - AU
                              - AW
                              - AX
                              - AZ
                              - BA
                              - BB
                              - BD
                              - BE
                              - BF
                              - BG
                              - BH
                              - BI
                              - BJ
                              - BL
                              - BM
                              - BN
                              - BO
                              - BQ
                              - BR
                              - BS
                              - BT
                              - BU
                              - BV
                              - BW
                              - BY
                              - BZ
                              - CA
                              - CC
                              - CD
                              - CF
                              - CG
                              - CH
                              - CI
                              - CK
                              - CL
                              - CM
                              - CN
                              - CO
                              - CP
                              - CR
                              - CS
                              - CU
                              - CV
                              - CW
                              - CX
                              - CY
                              - CZ
                              - DE
                              - DG
                              - DJ
                              - DK
                              - DM
                              - DO
                              - DZ
                              - EA
                              - EC
                              - EE
                              - EG
                              - EH
                              - ER
                              - ES
                              - ET
                              - EU
                              - FI
                              - FJ
                              - FK
                              - FM
                              - FO
                              - FR
                              - FX
                              - GA
                              - GB
                              - GD
                              - GE
                              - GF
                              - GG
                              - GH
                              - GI
                              - GL
                              - GM
                              - GN
                              - GP
                              - GQ
                              - GR
                              - GS
                              - GT
                              - GU
                              - GW
                              - GY
                              - HK
                              - HM
                              - HN
                              - HR
                              - HT
                              - HU
                              - IC
                              - ID
                              - IE
                              - IL
                              - IM
                              - IN
                              - IO
                              - IQ
                              - IR
                              - IS
                              - IT
                              - JE
                              - JM
                              - JO
                              - JP
                              - KE
                              - KG
                              - KH
                              - KI
                              - KM
                              - KN
                              - KP
                              - KR
                              - KW
                              - KY
                              - KZ
                              - LA
                              - LB
                              - LC
                              - LI
                              - LK
                              - LR
                              - LS
                              - LT
                              - LU
                              - LV
                              - LY
                              - MA
                              - MC
                              - MD
                              - ME
                              - MF
                              - MG
                              - MH
                              - MK
                              - ML
                              - MM
                              - MN
                              - MO
                              - MP
                              - MQ
                              - MR
                              - MS
                              - MT
                              - MU
                              - MV
                              - MW
                              - MX
                              - MY
                              - MZ
                              - NA
                              - NC
                              - NE
                              - NF
                              - NG
                              - NI
                              - NL
                              - 'NO'
                              - NP
                              - NR
                              - NT
                              - NU
                              - NZ
                              - OM
                              - PA
                              - PE
                              - PF
                              - PG
                              - PH
                              - PK
                              - PL
                              - PM
                              - PN
                              - PR
                              - PS
                              - PT
                              - PW
                              - PY
                              - QA
                              - RE
                              - RO
                              - RS
                              - RU
                              - RW
                              - SA
                              - SB
                              - SC
                              - SD
                              - SE
                              - SF
                              - SG
                              - SH
                              - SI
                              - SJ
                              - SK
                              - SL
                              - SM
                              - SN
                              - SO
                              - SR
                              - SS
                              - ST
                              - SU
                              - SV
                              - SX
                              - SY
                              - SZ
                              - TA
                              - TC
                              - TD
                              - TF
                              - TG
                              - TJ
                              - TK
                              - TL
                              - TM
                              - TN
                              - TO
                              - TP
                              - TR
                              - TT
                              - TV
                              - TW
                              - TZ
                              - UA
                              - UG
                              - UK
                              - UM
                              - US
                              - UY
                              - UZ
                              - VA
                              - VC
                              - VE
                              - VG
                              - VI
                              - VN
                              - VU
                              - WF
                              - WS
                              - XK
                              - YE
                              - YT
                              - YU
                              - ZA
                              - ZM
                              - ZR
                              - ZW
                            x-apidog-folder: Bo4e/ENUM
                          postleitzahl:
                            type: string
                            description: |-
                              Postleitzahl | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                          strasse:
                            type: string
                            description: |-
                              Strasse | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                          zusatz5:
                            type: string
                            description: |-
                              Adresszusatz 5 | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                          zusatz4:
                            type: string
                            description: |-
                              Adresszusatz 4 | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                          ortsteil:
                            type: string
                            description: |-
                              Ortsteil | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                          postfach:
                            type: string
                            description: |-
                              Postfach | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                          hausnummer:
                            type: string
                            description: |-
                              Hausnummer und Ergänzung | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                          zusatz2:
                            type: string
                            description: |-
                              Adresszusatz 2 | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                          zusatz3:
                            type: string
                            description: |-
                              Adresszusatz 3 | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                          ort:
                            type: object
                            title: Sort
                            description: |-

                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                            x-apidog-orders: []
                            properties: {}
                            x-apidog-ignore-properties: []
                          zusatz1:
                            type: string
                            description: |-
                              Adresszusatz 1 | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+DP</TipInfo>
                        x-apidog-orders:
                          - landescode
                          - postleitzahl
                          - strasse
                          - zusatz5
                          - zusatz4
                          - ortsteil
                          - postfach
                          - hausnummer
                          - zusatz2
                          - zusatz3
                          - ort
                          - zusatz1
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - zusatzInformation
                    x-apidog-ignore-properties: []
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | 

                      <TipInfo>SG4.IDE+24.SG5.LOC+172</TipInfo>
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        konzessionsabgabe:
                          type: object
                          properties:
                            kosten:
                              type: number
                              description: >-
                                Konzessionsabgabe in Euro/kWh | 

                                <TipInfo>SG4.IDE+24.SG8.SEQ+Z07.SG10.CCI+++Z08.CAV</TipInfo>
                              format: float
                            satz:
                              type: string
                              title: AbgabeArt
                              description: >-
                                Gruppen der KAV

                                CAV KAS | 

                                <TipInfo>SG4.IDE+24.SG8.SEQ+Z07.SG10.CCI+++Z08.CAV</TipInfo>
                              enum:
                                - KAS
                                - SA
                                - SAS
                                - TA
                                - TAS
                                - TK
                                - TKS
                                - TS
                                - TSS
                              x-apidog-enum:
                                - value: KAS
                                  name: >-
                                    für alle konzessionsvertraglichen
                                    Sonderregelungen, die nicht in die
                                    Systematik der KAV eingegliedert sind
                                  description: KAS
                                - value: SA
                                  name: >-
                                    Sondervertragskunden < 1 kV nach § 2 (7) und
                                    > 1 kV, Preis nach § 2 (3) (für Strom 0,11
                                    ct/ kWh und für Gas 0,03 ct/kWh)
                                  description: SA
                                - value: SAS
                                  name: >-
                                    Kennzeichnung, dass ein abweichender Preis
                                    für Sondervertragskunden vorliegt
                                  description: SAS
                                - value: TA
                                  name: >-
                                    Tarifkunden, für Strom § 2. (2) 1b HT bzw.
                                    ET (hohe KA) und für Gas § 2 (2) 2b
                                  description: TA
                                - value: TAS
                                  name: >-
                                    Kennzeichnung, dass ein abweichender Preis
                                    für Tarifkunden vorliegt
                                  description: TAS
                                - value: TK
                                  name: >-
                                    für Gas nach KAV § 2 (2) 2a bei
                                    ausschließlicher Nutzung zum Kochen und
                                    Warmwassererzeugung
                                  description: TK
                                - value: TKS
                                  name: >-
                                    Kennzeichnung, wenn nach KAV § 2 (2) 2a ein
                                    anderer Preis zu verwenden ist
                                  description: TKS
                                - value: TS
                                  name: ''
                                  description: ''
                                - value: TSS
                                  name: ''
                                  description: ''
                              x-apidog-folder: Bo4e/ENUM
                            kategorie:
                              type: string
                              title: Anfragekategorie
                              description: >-
                                Anfragekategorie | 

                                <TipInfo>SG4.IDE+24.SG8.SEQ+Z07.SG10.CCI+++Z08.CAV</TipInfo>
                              enum:
                                - PROZESSDATENBERICHT
                                - GERAETEUEBERNAHME
                                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                                - AENDERUNG_MELO
                                - STAMMDATEN_MALO_ODER_MELO
                                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                                - >-
                                  AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                                - AENDERUNG_GERAETEKONFIGURATION
                                - REKLAMATION_VON_WERTEN
                                - LASTGANG_MALO_TRANCHE
                                - SPERRUNG
                                - ENTSPERRUNG
                                - REKLAMATION_ZAEHLZEITDEFINITION
                                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                                - GERAETEWECHSELABSICHT
                                - AENDERUNG_KONZESSIONSABGABE
                                - AENDERUNG_ZAEHLZEITDEFINITION
                                - UEBERMITTLUNG_WERTE_AN_ESA
                                - AENDERUNG
                                - BILANZKREISZUORDNUNGSLISTE
                                - CLEARINGLISTE
                                - NORMIERTES_PROFIL_PROFILSCHAR
                                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                                - REKLAMATION_PROFIL_PROFILSCHAR
                                - STAMMDATEN_MALO
                                - STAMMDATEN_MELO
                                - STAMMDATEN_TRANCHE
                                - BEENDIGUNG_EINER_KONFIGURATION
                                - BESTELLUNG_EINER_KONFIGURATION
                                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                                - REKLAMATION_EINER_KONFIGURATION
                                - >-
                                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                                - >-
                                  EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                                - REKLAMATION_DEFINITION
                              x-apidog-folder: Bo4e/ENUM
                          x-apidog-orders:
                            - kosten
                            - satz
                            - kategorie
                          x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - konzessionsabgabe
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - lokationsadresse
                  - marktlokationsId
                  - zaehlwerke
                x-apidog-ignore-properties: []
            ENERGIELIEFERVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        hausnummer:
                          type: string
                          description: |-
                            Hausnummer und Ergänzung | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        postfach:
                          type: string
                          description: |-
                            Postfach | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder bei Privatpersonen
                            Zusätze zum  Namen dargestellt werden. Beispiele:
                            und Afrika oder Sängerin | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        landescode:
                          type: string
                          title: Landescode
                          description: |-
                            Der ISO-Landescode als Enumeration | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                          enum:
                            - AC
                            - AD
                            - AE
                            - AF
                            - AG
                            - AI
                            - AL
                            - AM
                            - AN
                            - AO
                            - AQ
                            - AR
                            - AS
                            - AT
                            - AU
                            - AW
                            - AX
                            - AZ
                            - BA
                            - BB
                            - BD
                            - BE
                            - BF
                            - BG
                            - BH
                            - BI
                            - BJ
                            - BL
                            - BM
                            - BN
                            - BO
                            - BQ
                            - BR
                            - BS
                            - BT
                            - BU
                            - BV
                            - BW
                            - BY
                            - BZ
                            - CA
                            - CC
                            - CD
                            - CF
                            - CG
                            - CH
                            - CI
                            - CK
                            - CL
                            - CM
                            - CN
                            - CO
                            - CP
                            - CR
                            - CS
                            - CU
                            - CV
                            - CW
                            - CX
                            - CY
                            - CZ
                            - DE
                            - DG
                            - DJ
                            - DK
                            - DM
                            - DO
                            - DZ
                            - EA
                            - EC
                            - EE
                            - EG
                            - EH
                            - ER
                            - ES
                            - ET
                            - EU
                            - FI
                            - FJ
                            - FK
                            - FM
                            - FO
                            - FR
                            - FX
                            - GA
                            - GB
                            - GD
                            - GE
                            - GF
                            - GG
                            - GH
                            - GI
                            - GL
                            - GM
                            - GN
                            - GP
                            - GQ
                            - GR
                            - GS
                            - GT
                            - GU
                            - GW
                            - GY
                            - HK
                            - HM
                            - HN
                            - HR
                            - HT
                            - HU
                            - IC
                            - ID
                            - IE
                            - IL
                            - IM
                            - IN
                            - IO
                            - IQ
                            - IR
                            - IS
                            - IT
                            - JE
                            - JM
                            - JO
                            - JP
                            - KE
                            - KG
                            - KH
                            - KI
                            - KM
                            - KN
                            - KP
                            - KR
                            - KW
                            - KY
                            - KZ
                            - LA
                            - LB
                            - LC
                            - LI
                            - LK
                            - LR
                            - LS
                            - LT
                            - LU
                            - LV
                            - LY
                            - MA
                            - MC
                            - MD
                            - ME
                            - MF
                            - MG
                            - MH
                            - MK
                            - ML
                            - MM
                            - MN
                            - MO
                            - MP
                            - MQ
                            - MR
                            - MS
                            - MT
                            - MU
                            - MV
                            - MW
                            - MX
                            - MY
                            - MZ
                            - NA
                            - NC
                            - NE
                            - NF
                            - NG
                            - NI
                            - NL
                            - 'NO'
                            - NP
                            - NR
                            - NT
                            - NU
                            - NZ
                            - OM
                            - PA
                            - PE
                            - PF
                            - PG
                            - PH
                            - PK
                            - PL
                            - PM
                            - PN
                            - PR
                            - PS
                            - PT
                            - PW
                            - PY
                            - QA
                            - RE
                            - RO
                            - RS
                            - RU
                            - RW
                            - SA
                            - SB
                            - SC
                            - SD
                            - SE
                            - SF
                            - SG
                            - SH
                            - SI
                            - SJ
                            - SK
                            - SL
                            - SM
                            - SN
                            - SO
                            - SR
                            - SS
                            - ST
                            - SU
                            - SV
                            - SX
                            - SY
                            - SZ
                            - TA
                            - TC
                            - TD
                            - TF
                            - TG
                            - TJ
                            - TK
                            - TL
                            - TM
                            - TN
                            - TO
                            - TP
                            - TR
                            - TT
                            - TV
                            - TW
                            - TZ
                            - UA
                            - UG
                            - UK
                            - UM
                            - US
                            - UY
                            - UZ
                            - VA
                            - VC
                            - VE
                            - VG
                            - VI
                            - VN
                            - VU
                            - WF
                            - WS
                            - XK
                            - YE
                            - YT
                            - YU
                            - ZA
                            - ZM
                            - ZR
                            - ZW
                          x-apidog-folder: Bo4e/ENUM
                        postleitzahl:
                          type: string
                          description: |-
                            Postleitzahl | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        name4:
                          type: string
                          description: |-
                            Name 4 | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        exRefWert:
                          type: string
                          description: >-
                            Kundennummer beim Altieferanten - Angabe von
                            Referenzen für Rückmeldungen und Anfragen

                            PI 55109 55137 

                            ORDERS PI 17101 | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09.RFF+AVC,
                            SG4.IDE+24.SG12.NAD+Z09.RFF+Z01</TipInfo>
                        exRefName:
                          type: string
                          description: >-
                            Bezeichnung der externen Referenz, Kundennummer beim
                            Lieferanten, bezieht sich auf das vorangegangene NAD
                            Segment

                            RFF AVC

                            PI 55109 55137 

                            RFF AVC Kundennummer beim Lieferanten ORDERS

                            PI 17101 | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09.RFF+AVC,
                            SG4.IDE+24.SG12.NAD+Z09.RFF+Z01</TipInfo>
                          enum:
                            - Kundennummer beim Lieferanten
                            - Kundennummer beim Altlieferanten
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr.

                            Z04 Korrespondenzanschrift des Kunden des
                            Lieferanten

                            PI 55001 55600 55601 55013 55014 55043 55168 55169
                            | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        ortsteil:
                          type: string
                          description: |-
                            Ortsteil | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        strasse:
                          type: string
                          description: |-
                            Strasse | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder bei Privatpersonen
                            beispielsweise der Vorname dargestellt werden.
                            Beispiele: Bereich Süd oder Nina | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        ort:
                          type: object
                          title: Sort
                          description: |-

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                          x-apidog-orders: []
                          properties: {}
                          x-apidog-ignore-properties: []
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen beispielsweise der Nachname
                            dargestellt werden. Beispiele: Yellow Strom GmbH
                            oder Hagen | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        gewerbekennzeichnung:
                          type: boolean
                          description: >-
                            Kennzeichnung ob es sich um einen
                            Gewerbe/Unternehmen (gewerbeKennzeichnung = true)

                            oder eine Privatperson handelt.
                            (gewerbeKennzeichnung = false)

                            Z01 Struktur von Personennamen

                            Z02 Struktur der Firmenbezeichnung | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                      x-apidog-orders:
                        - hausnummer
                        - postfach
                        - name3
                        - landescode
                        - postleitzahl
                        - name4
                        - exRefWert
                        - exRefName
                        - anrede
                        - ortsteil
                        - strasse
                        - name2
                        - ort
                        - name1
                        - gewerbekennzeichnung
                      x-apidog-ignore-properties: []
                  korrespondenzpartner:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          postleitzahl:
                            type: string
                            description: |-
                              Postleitzahl | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                          ort:
                            type: object
                            title: Sort
                            description: |-

                              <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                            x-apidog-orders: []
                            properties: {}
                            x-apidog-ignore-properties: []
                          hausnummer:
                            type: string
                            description: |-
                              Hausnummer und Ergänzung | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                          landescode:
                            type: string
                            title: Landescode
                            description: |-
                              Der ISO-Landescode als Enumeration | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                            enum:
                              - AC
                              - AD
                              - AE
                              - AF
                              - AG
                              - AI
                              - AL
                              - AM
                              - AN
                              - AO
                              - AQ
                              - AR
                              - AS
                              - AT
                              - AU
                              - AW
                              - AX
                              - AZ
                              - BA
                              - BB
                              - BD
                              - BE
                              - BF
                              - BG
                              - BH
                              - BI
                              - BJ
                              - BL
                              - BM
                              - BN
                              - BO
                              - BQ
                              - BR
                              - BS
                              - BT
                              - BU
                              - BV
                              - BW
                              - BY
                              - BZ
                              - CA
                              - CC
                              - CD
                              - CF
                              - CG
                              - CH
                              - CI
                              - CK
                              - CL
                              - CM
                              - CN
                              - CO
                              - CP
                              - CR
                              - CS
                              - CU
                              - CV
                              - CW
                              - CX
                              - CY
                              - CZ
                              - DE
                              - DG
                              - DJ
                              - DK
                              - DM
                              - DO
                              - DZ
                              - EA
                              - EC
                              - EE
                              - EG
                              - EH
                              - ER
                              - ES
                              - ET
                              - EU
                              - FI
                              - FJ
                              - FK
                              - FM
                              - FO
                              - FR
                              - FX
                              - GA
                              - GB
                              - GD
                              - GE
                              - GF
                              - GG
                              - GH
                              - GI
                              - GL
                              - GM
                              - GN
                              - GP
                              - GQ
                              - GR
                              - GS
                              - GT
                              - GU
                              - GW
                              - GY
                              - HK
                              - HM
                              - HN
                              - HR
                              - HT
                              - HU
                              - IC
                              - ID
                              - IE
                              - IL
                              - IM
                              - IN
                              - IO
                              - IQ
                              - IR
                              - IS
                              - IT
                              - JE
                              - JM
                              - JO
                              - JP
                              - KE
                              - KG
                              - KH
                              - KI
                              - KM
                              - KN
                              - KP
                              - KR
                              - KW
                              - KY
                              - KZ
                              - LA
                              - LB
                              - LC
                              - LI
                              - LK
                              - LR
                              - LS
                              - LT
                              - LU
                              - LV
                              - LY
                              - MA
                              - MC
                              - MD
                              - ME
                              - MF
                              - MG
                              - MH
                              - MK
                              - ML
                              - MM
                              - MN
                              - MO
                              - MP
                              - MQ
                              - MR
                              - MS
                              - MT
                              - MU
                              - MV
                              - MW
                              - MX
                              - MY
                              - MZ
                              - NA
                              - NC
                              - NE
                              - NF
                              - NG
                              - NI
                              - NL
                              - 'NO'
                              - NP
                              - NR
                              - NT
                              - NU
                              - NZ
                              - OM
                              - PA
                              - PE
                              - PF
                              - PG
                              - PH
                              - PK
                              - PL
                              - PM
                              - PN
                              - PR
                              - PS
                              - PT
                              - PW
                              - PY
                              - QA
                              - RE
                              - RO
                              - RS
                              - RU
                              - RW
                              - SA
                              - SB
                              - SC
                              - SD
                              - SE
                              - SF
                              - SG
                              - SH
                              - SI
                              - SJ
                              - SK
                              - SL
                              - SM
                              - SN
                              - SO
                              - SR
                              - SS
                              - ST
                              - SU
                              - SV
                              - SX
                              - SY
                              - SZ
                              - TA
                              - TC
                              - TD
                              - TF
                              - TG
                              - TJ
                              - TK
                              - TL
                              - TM
                              - TN
                              - TO
                              - TP
                              - TR
                              - TT
                              - TV
                              - TW
                              - TZ
                              - UA
                              - UG
                              - UK
                              - UM
                              - US
                              - UY
                              - UZ
                              - VA
                              - VC
                              - VE
                              - VG
                              - VI
                              - VN
                              - VU
                              - WF
                              - WS
                              - XK
                              - YE
                              - YT
                              - YU
                              - ZA
                              - ZM
                              - ZR
                              - ZW
                            x-apidog-folder: Bo4e/ENUM
                          ortsteil:
                            type: string
                            description: |-
                              Ortsteil | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                          postfach:
                            type: string
                            description: |-
                              Postfach | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                          strasse:
                            type: string
                            description: |-
                              Strasse | 
                              <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                        x-apidog-orders:
                          - postleitzahl
                          - ort
                          - hausnummer
                          - landescode
                          - ortsteil
                          - postfach
                          - strasse
                        x-apidog-ignore-properties: []
                      gewerbekennzeichnung:
                        type: boolean
                        description: >-
                          Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
                          (gewerbeKennzeichnung = true)

                          oder eine Privatperson handelt. (gewerbeKennzeichnung
                          = false)

                          Z01 Struktur von Personennamen

                          Z02 Struktur der Firmenbezeichnung | 

                          <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder bei Privatpersonen
                          beispielsweise der Vorname dargestellt werden.
                          Beispiele: Bereich Süd oder Nina | 

                          <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                      anrede:
                        type: string
                        description: |-
                          Die Anrede für den GePa, Z.B. Herr.
                          Z04 Korrespondenzanschrift des Kunden des Lieferanten
                          PI 55001 55600 55601 55013 55014 55043 55168 55169 | 
                          <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen beispielsweise der Nachname
                          dargestellt werden. Beispiele: Yellow Strom GmbH oder
                          Hagen | 

                          <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                      name4:
                        type: string
                        description: |-
                          Name 4 | 
                          <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder bei Privatpersonen
                          Zusätze zum  Namen dargestellt werden. Beispiele: und
                          Afrika oder Sängerin | 

                          <TipInfo>SG4.IDE+24.SG12.NAD+Z04</TipInfo>
                    x-apidog-orders:
                      - partneradresse
                      - gewerbekennzeichnung
                      - name2
                      - anrede
                      - name1
                      - name4
                      - name3
                    x-apidog-ignore-properties: []
                  vertragskonditionen:
                    type: object
                    properties:
                      abrechnungsintervall:
                        type: integer
                        description: |-
                          Abrechnungsintervall des LF in Monaten
                          DTM Z20
                          PI 44109 44137 44138 44001 44002 44014  | 
                          <TipInfo>SG4.IDE+24.SG6.RFF+Z18.DTM+Z20</TipInfo>
                    x-apidog-orders:
                      - abrechnungsintervall
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragspartner2
                  - korrespondenzpartner
                  - vertragskonditionen
                x-apidog-ignore-properties: []
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  bilanzkreis:
                    type: object
                    title: Bilanzkreis
                    description: |-

                      <TipInfo>SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z19</TipInfo>
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  fallgruppenzuordnung:
                    type: string
                    title: Fallgruppenzuordnung
                    description: |-
                      Fallgruppenzuordnung | 
                      <TipInfo>SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++Z17</TipInfo>
                    enum:
                      - GABI_RLMmT
                      - GABI_RLMoT
                      - GABI_RLMNEV
                    x-apidog-enum:
                      - value: GABI_RLMmT
                        name: RLM-Kunde in Tagesregime - Exit
                        description: GABi-RLMmT
                      - value: GABI_RLMoT
                        name: GABi-RLMoT
                        description: RLM-Kunde im Stundenregime - Exit
                      - value: GABI_RLMNEV
                        name: >-
                          Nominierungsersatzverfahren - Exit (Hinweis: Dieser
                          Code darf nur für Liefermonate vor dem 01.10.2016
                          genutzt werden)
                        description: GABi-RLMNEV
                    x-apidog-folder: Bo4e/ENUM
                  lastprofile:
                    type: array
                    items:
                      type: object
                      properties:
                        verfahren:
                          type: string
                          title: Profilverfahren
                          description: >-
                            Profilverfahren | 

                            <TipInfo>SG4.IDE+24.SG8.SEQ+Z35.SG10.CCI+Z12</TipInfo>
                          enum:
                            - SYNTHETISCH
                            - ANALYTISCH
                          x-apidog-folder: Bo4e/ENUM
                        bezeichnung:
                          type: string
                          description: >-
                            Externe Bezeichnung | 

                            <TipInfo>SG4.IDE+24.SG8.SEQ+Z35.SG10.CCI+Z12.CAV</TipInfo>
                        herausgeber:
                          type: string
                          title: Herausgeber
                          description: >-
                            Herausgeber | 

                            <TipInfo>SG4.IDE+24.SG8.SEQ+Z35.SG10.CCI+Z12.CAV</TipInfo>
                          enum:
                            - NB
                            - BDEW
                            - TUM
                          x-apidog-enum:
                            - value: NB
                              name: Vergeben vom Händler (hier Netzbetreiber)
                              description: '89'
                            - value: BDEW
                              name: >-
                                DE, BDEW (Bundesverband der Energie- und
                                Wasserwirtschaft e.V.)
                              description: '293'
                            - value: TUM
                              name: ''
                              description: ''
                          x-apidog-folder: Bo4e/ENUM
                      x-apidog-orders:
                        - verfahren
                        - bezeichnung
                        - herausgeber
                      x-apidog-ignore-properties: []
                  jahresverbrauchsprognose:
                    type: object
                    properties:
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | 

                          <TipInfo>SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+31</TipInfo>
                        enum:
                          - W
                          - WH
                          - KW
                          - KWH
                          - KVARH
                          - MW
                          - MWH
                          - STUECK
                          - KUBIKMETER
                          - STUNDE
                          - TAG
                          - MONAT
                          - JAHR
                          - PROZENT
                          - ANZAHL
                          - VAR
                          - KVAR
                          - VARH
                          - KWHK
                          - Z16
                          - KWT
                        x-apidog-enum:
                          - value: W
                            name: ''
                            description: ''
                          - value: WH
                            name: ''
                            description: ''
                          - value: KW
                            name: ''
                            description: ''
                          - value: KWH
                            name: Kilowattstunde
                            description: KWH
                          - value: KVARH
                            name: ''
                            description: ''
                          - value: MW
                            name: ''
                            description: ''
                          - value: MWH
                            name: ''
                            description: ''
                          - value: STUECK
                            name: Stück
                            description: H87
                          - value: KUBIKMETER
                            name: ''
                            description: ''
                          - value: STUNDE
                            name: ''
                            description: ''
                          - value: TAG
                            name: Tag
                            description: ZD8
                          - value: MONAT
                            name: ''
                            description: ''
                          - value: JAHR
                            name: ''
                            description: ''
                          - value: PROZENT
                            name: Prozent
                            description: P1
                          - value: ANZAHL
                            name: ''
                            description: ''
                          - value: VAR
                            name: ''
                            description: ''
                          - value: KVAR
                            name: ''
                            description: ''
                          - value: VARH
                            name: ''
                            description: ''
                          - value: KWHK
                            name: ''
                            description: ''
                          - value: Z16
                            name: kWh/K (Kilowatt-Stunde/Kelvin)
                            description: Z16
                          - value: KWT
                            name: Kilowatt
                            description: ''
                        x-apidog-folder: Bo4e/ENUM
                      wert:
                        type: object
                        title: Schwellwert
                        description: |-

                          <TipInfo>SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+31</TipInfo>
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - einheit
                      - wert
                    x-apidog-ignore-properties: []
                  kundenwert:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: |-

                          <TipInfo>SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+Y02</TipInfo>
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - wert
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - bilanzkreis
                  - fallgruppenzuordnung
                  - lastprofile
                  - jahresverbrauchsprognose
                  - kundenwert
                x-apidog-ignore-properties: []
            ZAEHLER:
              type: array
              items:
                type: object
                properties:
                  zaehlernummer:
                    type: string
                    description: >-
                      Die Nummer des zu sperrenden Zählers | 

                      <TipInfo>SG4.IDE+24.SG8.SEQ+Z03.SG10.CCI+++E13.CAV+Z30</TipInfo>
                x-apidog-orders:
                  - zaehlernummer
                x-apidog-ignore-properties: []
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragskonditionen:
                    type: object
                    properties:
                      netznutzungsvertrag:
                        type: string
                        title: Netznutzungsvertrag
                        description: >-
                          Netznutzungsvertrag | 

                          <TipInfo>SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++Z88.CAV+Z74</TipInfo>
                        enum:
                          - KUNDEN_NB
                          - LIEFERANTEN_NB
                        x-apidog-enum:
                          - value: KUNDEN_NB
                            name: Direkter Vertrag zwischen Kunden und NB
                            description: Z08
                          - value: LIEFERANTEN_NB
                            name: Vertrag zwischen Lieferanten und NB
                            description: Z09
                        x-apidog-folder: Bo4e/ENUM
                      netznutzungszahler:
                        type: string
                        title: Netznutzungszahler
                        description: >-
                          Netznutzungszahler | 

                          <TipInfo>SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++Z88.CAV+Z73</TipInfo>
                        enum:
                          - KUNDE
                          - LIEFERANT
                        x-apidog-enum:
                          - value: KUNDE
                            name: Kunde
                            description: Z10
                          - value: LIEFERANT
                            name: Lieferant
                            description: Z11
                        x-apidog-folder: Bo4e/ENUM
                      haushaltskunde:
                        type: boolean
                        description: >-
                          Gruppenzuordnung, kennzeichnet ob es sich um einen
                          Haushaltskunden handelt oder nicht.

                          Z15 Haushaltskunde gem. EnWG

                          Z18 Kein Haushaltskunde gem. EnWG

                          CCI Z15

                          PI 55001 55600 55013 55014 55109 55137  | 

                          <TipInfo>SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI</TipInfo>
                    x-apidog-orders:
                      - netznutzungsvertrag
                      - netznutzungszahler
                      - haushaltskunde
                    x-apidog-ignore-properties: []
                  vertragsende:
                    type: string
                    description: >-
                      Gibt das Ende der Netznutzung oder einer Zuordnung an. 

                      DTM 93

                      PI 55016 55017 55001 55002 55600 55602 55013 55014 55607
                      55608 55010 55011 55004 55005 55007 55008 55039 55040
                      55051 55052 55240 55241 55242 55243 55236 55237 | 

                      <TipInfo>SG4.IDE+24.DTM+93</TipInfo>
                    format: date-time
                  vertragsbeginn:
                    type: string
                    description: >-
                      Gibt an, wann der Vertrag oder die Zuordnung beginnt.

                      DTM 92

                      PI 55001 55002 55077 55078 55600 55602 55601 55603 55013
                      55014 55607 55608 55004 55005 55051 55052 55238 55239
                      55235 55237 | 

                      <TipInfo>SG4.IDE+24.DTM+92</TipInfo>
                    format: date-time
                  gemeinderabatt:
                    type: integer
                    description: >-
                      Gemeinderabatt - Angabe zum Preisnachlass der
                      Netznutzungsentgelte

                      QTY Z16

                      PI 44112 44139 44142 44001 44002 44013 44014 44035 | 

                      <TipInfo>SG4.IDE+24.SG8.SEQ+Z12.SG9.QTY+Z16</TipInfo>
                x-apidog-orders:
                  - vertragskonditionen
                  - vertragsende
                  - vertragsbeginn
                  - gemeinderabatt
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MESSLOKATION
            - MARKTLOKATION
            - ENERGIELIEFERVERTRAG
            - BILANZIERUNG
            - ZAEHLER
            - NETZNUTZUNGSVERTRAG
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            nachrichtenreferenznummer:
              type: string
              description: |-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | 
                <TipInfo>UNH</TipInfo>
            kategorie:
              type: string
              title: Anfragekategorie
              description: |-
                Anfragekategorie | 
                <TipInfo>BGM+E01</TipInfo>
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
              x-apidog-folder: Bo4e/ENUM
            nachrichtendatum:
              type: string
              description: |-
                Erstellungdatum der EDIFact / DTM+137 | 
                <TipInfo>DTM+137</TipInfo>
              format: date-time
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: >-

                          <TipInfo>SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]</TipInfo>
                        enum:
                          - RUF_ZENTRALE
                          - FAX_ZENTRALE
                          - SAMMELRUF
                          - SAMMELFAX
                          - ABTEILUNGRUF
                          - ABTEILUNGFAX
                          - RUF_DURCHWAHL
                          - FAX_DURCHWAHL
                          - MOBIL_NUMMER
                        x-apidog-enum:
                          - value: RUF_ZENTRALE
                            name: weiteres Telefon
                            description: AJ
                          - value: FAX_ZENTRALE
                            name: ''
                            description: ''
                          - value: SAMMELRUF
                            name: ''
                            description: ''
                          - value: SAMMELFAX
                            name: ''
                            description: ''
                          - value: ABTEILUNGRUF
                            name: ''
                            description: ''
                          - value: ABTEILUNGFAX
                            name: ''
                            description: ''
                          - value: RUF_DURCHWAHL
                            name: ''
                            description: ''
                          - value: FAX_DURCHWAHL
                            name: Telefax
                            description: FX
                          - value: MOBIL_NUMMER
                            name: Handy
                            description: AL
                        x-apidog-folder: Bo4e/ENUM
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: >-

                          <TipInfo>SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]</TipInfo>
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: |-
                        Nachname (Familienname) des Ansprechpartners | 
                        <TipInfo>SG2.NAD+MS.SG3.CTA</TipInfo>
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | 

                        <TipInfo>SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]</TipInfo>
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: |-
                    Gibt die Codenummer der Marktrolle an - MP ID
                    NAD Z31 Übertragungsnetzbetreiber ORDERS
                    PI 17134
                    NAD DEB Messstellenbetreiber ORDERS
                    PI 17003 17134 17135
                    NAD DEB Messstellenbetreiber IFTSTA 
                    PI 21007 21015 21018 | 
                    <TipInfo>SG2.NAD+MS, SG2.NAD+MR</TipInfo>
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: |-
                    Rollencodetyp | 
                    <TipInfo>SG2.NAD+MS, SG2.NAD+MR</TipInfo>
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                  x-apidog-enum:
                    - value: BDEW
                      name: >-
                        DE, BDEW (Bundesverband der Energie- und
                        Wasserwirtschaft e.V.)
                      description: '293'
                    - value: GS1
                      name: GS1
                      description: '9'
                    - value: GLN
                      name: ''
                      description: ''
                    - value: DVGW
                      name: DE, DVGW Service & Consult GmbH
                      description: '332'
                  x-apidog-folder: Bo4e/ENUM
              x-apidog-orders:
                - rufnummern
                - ansprechpartner
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzung:
              type: string
              description: |-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 | 
                <TipInfo>SG4.IDE+24.STS+Z17</TipInfo>
            dokumentennummer:
              type: string
              description: |-
                EDIFact Referenz aus dem BGM Segment / BGM | 
                <TipInfo>BGM+E01</TipInfo>
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | 

                <TipInfo>SG4.IDE+24.STS+7</TipInfo>
            vertragsbeginn:
              type: string
              description: >-
                Gibt an, wann der Vertrag oder die Zuordnung beginnt.

                DTM 92

                PI 55001 55002 55077 55078 55600 55602 55601 55603 55013 55014
                55607 55608 55004 55005 55051 55052 55238 55239 55235 55237 | 

                <TipInfo>SG4.IDE+24.DTM+92</TipInfo>
              format: date-time
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC
                | 

                <TipInfo>SG4.IDE+24</TipInfo>
            vertragsende:
              type: string
              description: >-
                Gibt das Ende der Netznutzung oder einer Zuordnung an. 

                DTM 93

                PI 55016 55017 55001 55002 55600 55602 55013 55014 55607 55608
                55010 55011 55004 55005 55007 55008 55039 55040 55051 55052
                55240 55241 55242 55243 55236 55237 | 

                <TipInfo>SG4.IDE+24.DTM+93</TipInfo>
              format: date-time
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | 

                <TipInfo>SG4.IDE+24.SG6.RFF+Z13</TipInfo>
            bilanzkreis:
              type: array
              items:
                type: object
                properties:
                  prioritaet:
                    type: integer
                    description: |-
                      prioritaet | 
                      <TipInfo>SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z19.CAV</TipInfo>
                x-apidog-orders:
                  - prioritaet
                x-apidog-ignore-properties: []
            freitext:
              type: object
              title: Freitext
              description: |-

                <TipInfo>SG4.IDE+24.FTX+ACB</TipInfo>
              x-apidog-orders: []
              properties: {}
              x-apidog-ignore-properties: []
          x-apidog-orders:
            - nachrichtenreferenznummer
            - kategorie
            - nachrichtendatum
            - absender
            - transaktionsgrundergaenzung
            - dokumentennummer
            - transaktionsgrund
            - vertragsbeginn
            - vorgangsnummer
            - vertragsende
            - pruefidentifikator
            - bilanzkreis
            - freitext
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 44001 - Anmeldung [LF an NB] UTILMD AHB Gas
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55601:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                    enum:
                      - ERWARTETE_DATEN
                      - IM_SYSTEM_VORHANDENE_DATEN
                      - INFORMATIVE_DATEN
                      - GUELTIGE_DATEN
                      - KEINE_DATEN
                      - IM_SYSTEM_KEINE_DATEN_VORHANDEN
                      - KEINE_DATEN_ERWARTET
                      - DIFFERENZ_DATEN
                      - DIFFERENZ_ERWARTETE_DATEN
                      - DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN
                  lokationsadresse:
                    type: object
                    properties:
                      zusatzInformation:
                        type: object
                        properties:
                          zusatz3:
                            type: string
                            description: 'Adresszusatz 3 | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                          zusatz1:
                            type: string
                            description: 'Adresszusatz 1 | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                          zusatz5:
                            type: string
                            description: 'Adresszusatz 5 | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                          zusatz4:
                            type: string
                            description: 'Adresszusatz 4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                          zusatz2:
                            type: string
                            description: 'Adresszusatz 2 | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                        x-apidog-orders:
                          - zusatz3
                          - zusatz1
                          - zusatz5
                          - zusatz4
                          - zusatz2
                        x-apidog-ignore-properties: []
                      ortsteil:
                        type: string
                        description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                      postleitzahl:
                        type: string
                        description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                      strasse:
                        type: string
                        description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                      landescode:
                        type: string
                        title: Landescode
                        description: >-
                          Der ISO-Landescode als Enumeration | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z60
                        enum:
                          - AC
                          - AD
                          - AE
                          - AF
                          - AG
                          - AI
                          - AL
                          - AM
                          - AN
                          - AO
                          - AQ
                          - AR
                          - AS
                          - AT
                          - AU
                          - AW
                          - AX
                          - AZ
                          - BA
                          - BB
                          - BD
                          - BE
                          - BF
                          - BG
                          - BH
                          - BI
                          - BJ
                          - BL
                          - BM
                          - BN
                          - BO
                          - BQ
                          - BR
                          - BS
                          - BT
                          - BU
                          - BV
                          - BW
                          - BY
                          - BZ
                          - CA
                          - CC
                          - CD
                          - CF
                          - CG
                          - CH
                          - CI
                          - CK
                          - CL
                          - CM
                          - CN
                          - CO
                          - CP
                          - CR
                          - CS
                          - CU
                          - CV
                          - CW
                          - CX
                          - CY
                          - CZ
                          - DE
                          - DG
                          - DJ
                          - DK
                          - DM
                          - DO
                          - DZ
                          - EA
                          - EC
                          - EE
                          - EG
                          - EH
                          - ER
                          - ES
                          - ET
                          - EU
                          - FI
                          - FJ
                          - FK
                          - FM
                          - FO
                          - FR
                          - FX
                          - GA
                          - GB
                          - GD
                          - GE
                          - GF
                          - GG
                          - GH
                          - GI
                          - GL
                          - GM
                          - GN
                          - GP
                          - GQ
                          - GR
                          - GS
                          - GT
                          - GU
                          - GW
                          - GY
                          - HK
                          - HM
                          - HN
                          - HR
                          - HT
                          - HU
                          - IC
                          - ID
                          - IE
                          - IL
                          - IM
                          - IN
                          - IO
                          - IQ
                          - IR
                          - IS
                          - IT
                          - JE
                          - JM
                          - JO
                          - JP
                          - KE
                          - KG
                          - KH
                          - KI
                          - KM
                          - KN
                          - KP
                          - KR
                          - KW
                          - KY
                          - KZ
                          - LA
                          - LB
                          - LC
                          - LI
                          - LK
                          - LR
                          - LS
                          - LT
                          - LU
                          - LV
                          - LY
                          - MA
                          - MC
                          - MD
                          - ME
                          - MF
                          - MG
                          - MH
                          - MK
                          - ML
                          - MM
                          - MN
                          - MO
                          - MP
                          - MQ
                          - MR
                          - MS
                          - MT
                          - MU
                          - MV
                          - MW
                          - MX
                          - MY
                          - MZ
                          - NA
                          - NC
                          - NE
                          - NF
                          - NG
                          - NI
                          - NL
                          - 'NO'
                          - NP
                          - NR
                          - NT
                          - NU
                          - NZ
                          - OM
                          - PA
                          - PE
                          - PF
                          - PG
                          - PH
                          - PK
                          - PL
                          - PM
                          - PN
                          - PR
                          - PS
                          - PT
                          - PW
                          - PY
                          - QA
                          - RE
                          - RO
                          - RS
                          - RU
                          - RW
                          - SA
                          - SB
                          - SC
                          - SD
                          - SE
                          - SF
                          - SG
                          - SH
                          - SI
                          - SJ
                          - SK
                          - SL
                          - SM
                          - SN
                          - SO
                          - SR
                          - SS
                          - ST
                          - SU
                          - SV
                          - SX
                          - SY
                          - SZ
                          - TA
                          - TC
                          - TD
                          - TF
                          - TG
                          - TJ
                          - TK
                          - TL
                          - TM
                          - TN
                          - TO
                          - TP
                          - TR
                          - TT
                          - TV
                          - TW
                          - TZ
                          - UA
                          - UG
                          - UK
                          - UM
                          - US
                          - UY
                          - UZ
                          - VA
                          - VC
                          - VE
                          - VG
                          - VI
                          - VN
                          - VU
                          - WF
                          - WS
                          - XK
                          - YE
                          - YT
                          - YU
                          - ZA
                          - ZM
                          - ZR
                          - ZW
                      hausnummer:
                        type: string
                        description: >-
                          Hausnummer und Ergänzung | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z60
                      ort:
                        type: string
                        description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                      postfach:
                        type: string
                        description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                    x-apidog-orders:
                      - zusatzInformation
                      - ortsteil
                      - postleitzahl
                      - strasse
                      - landescode
                      - hausnummer
                      - ort
                      - postfach
                    x-apidog-ignore-properties: []
                  erforderlichesProduktpaket:
                    type: array
                    items:
                      type: object
                      properties:
                        produktpaket:
                          type: object
                          properties:
                            priorisierung:
                              type: string
                              title: Priorisierung
                              description: >-
                                Priorisierung | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+ZH0.SG10.CCI+Z65.CAV
                              enum:
                                - PRIORITAET1
                                - PRIORITAET2
                                - PRIORITAET3
                                - PRIORITAET4
                                - PRIORITAET5
                            produktpaketId:
                              type: integer
                              description: >-
                                produktpaketId | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z79, SG4.IDE+24.SG8.SEQ+ZH0
                            umsetzungsgradvorgabe:
                              type: string
                              title: Umsetzungsgradvorgabe
                              description: >-
                                Umsetzungsgradvorgabe | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+ZH0.SG10.CCI+Z65
                              enum:
                                - ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
                                - >-
                                  ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR
                          x-apidog-orders:
                            - priorisierung
                            - produktpaketId
                            - umsetzungsgradvorgabe
                          required:
                            - produktpaketId
                            - umsetzungsgradvorgabe
                          x-apidog-ignore-properties: []
                        produkt:
                          type: array
                          items:
                            type: object
                            properties:
                              produkt:
                                type: object
                                properties:
                                  wertedetails:
                                    type: string
                                    description: >-
                                      wertedetails | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.SG10.CCI+Z66.CAV+ZV4
                                  produktCode:
                                    type: string
                                    description: >-
                                      produktCode | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.PIA+5
                                  codeProdukteigenschaft:
                                    type: string
                                    description: >-
                                      codeProdukteigenschaft | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.SG10.CCI+Z66.CAV+ZH9
                                x-apidog-orders:
                                  - wertedetails
                                  - produktCode
                                  - codeProdukteigenschaft
                                required:
                                  - wertedetails
                                  - produktCode
                                  - codeProdukteigenschaft
                                x-apidog-ignore-properties: []
                            x-apidog-orders:
                              - produkt
                            required:
                              - produkt
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - produktpaket
                        - produkt
                      required:
                        - produktpaket
                        - produkt
                      x-apidog-ignore-properties: []
                  foerderungsLand:
                    type: string
                    description: >-
                      foerderungsLand | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z23
                x-apidog-orders:
                  - marktlokationsId
                  - datenqualitaet
                  - lokationsadresse
                  - erforderlichesProduktpaket
                  - foerderungsLand
                required:
                  - erforderlichesProduktpaket
                x-apidog-ignore-properties: []
            ENERGIELIEFERVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsart:
                    type: string
                    enum:
                      - ENERGIELIEFERVERTRAG
                    x-apidog-enum:
                      - value: ENERGIELIEFERVERTRAG
                        name: ''
                        description: ''
                    default: ENERGIELIEFERVERTRAG
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen

                            beispielsweise der Nachname dargestellt werden.
                            Beispiele: Yellow Strom GmbH

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z09
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z09
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                          enum:
                            - KUNDE
                            - LIEFERANT
                            - DIENSTLEISTER
                            - INTERESSENT
                            - MARKTPARTNER
                            - EIGENTUEMER
                            - HAUSVERWALTER
                            - KORRESPONDENZEMPFAENGER
                            - ABLESEKARTENEMPFAENGER
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z09'
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                        gewerbekennzeichnung:
                          type: boolean
                      x-apidog-orders:
                        - name1
                        - name3
                        - anrede
                        - geschaeftspartnerrolle
                        - name4
                        - name2
                        - gewerbekennzeichnung
                      x-apidog-ignore-properties: []
                  korrespondenzpartner:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z04
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z04
                            enum:
                              - AC
                              - AD
                              - AE
                              - AF
                              - AG
                              - AI
                              - AL
                              - AM
                              - AN
                              - AO
                              - AQ
                              - AR
                              - AS
                              - AT
                              - AU
                              - AW
                              - AX
                              - AZ
                              - BA
                              - BB
                              - BD
                              - BE
                              - BF
                              - BG
                              - BH
                              - BI
                              - BJ
                              - BL
                              - BM
                              - BN
                              - BO
                              - BQ
                              - BR
                              - BS
                              - BT
                              - BU
                              - BV
                              - BW
                              - BY
                              - BZ
                              - CA
                              - CC
                              - CD
                              - CF
                              - CG
                              - CH
                              - CI
                              - CK
                              - CL
                              - CM
                              - CN
                              - CO
                              - CP
                              - CR
                              - CS
                              - CU
                              - CV
                              - CW
                              - CX
                              - CY
                              - CZ
                              - DE
                              - DG
                              - DJ
                              - DK
                              - DM
                              - DO
                              - DZ
                              - EA
                              - EC
                              - EE
                              - EG
                              - EH
                              - ER
                              - ES
                              - ET
                              - EU
                              - FI
                              - FJ
                              - FK
                              - FM
                              - FO
                              - FR
                              - FX
                              - GA
                              - GB
                              - GD
                              - GE
                              - GF
                              - GG
                              - GH
                              - GI
                              - GL
                              - GM
                              - GN
                              - GP
                              - GQ
                              - GR
                              - GS
                              - GT
                              - GU
                              - GW
                              - GY
                              - HK
                              - HM
                              - HN
                              - HR
                              - HT
                              - HU
                              - IC
                              - ID
                              - IE
                              - IL
                              - IM
                              - IN
                              - IO
                              - IQ
                              - IR
                              - IS
                              - IT
                              - JE
                              - JM
                              - JO
                              - JP
                              - KE
                              - KG
                              - KH
                              - KI
                              - KM
                              - KN
                              - KP
                              - KR
                              - KW
                              - KY
                              - KZ
                              - LA
                              - LB
                              - LC
                              - LI
                              - LK
                              - LR
                              - LS
                              - LT
                              - LU
                              - LV
                              - LY
                              - MA
                              - MC
                              - MD
                              - ME
                              - MF
                              - MG
                              - MH
                              - MK
                              - ML
                              - MM
                              - MN
                              - MO
                              - MP
                              - MQ
                              - MR
                              - MS
                              - MT
                              - MU
                              - MV
                              - MW
                              - MX
                              - MY
                              - MZ
                              - NA
                              - NC
                              - NE
                              - NF
                              - NG
                              - NI
                              - NL
                              - 'NO'
                              - NP
                              - NR
                              - NT
                              - NU
                              - NZ
                              - OM
                              - PA
                              - PE
                              - PF
                              - PG
                              - PH
                              - PK
                              - PL
                              - PM
                              - PN
                              - PR
                              - PS
                              - PT
                              - PW
                              - PY
                              - QA
                              - RE
                              - RO
                              - RS
                              - RU
                              - RW
                              - SA
                              - SB
                              - SC
                              - SD
                              - SE
                              - SF
                              - SG
                              - SH
                              - SI
                              - SJ
                              - SK
                              - SL
                              - SM
                              - SN
                              - SO
                              - SR
                              - SS
                              - ST
                              - SU
                              - SV
                              - SX
                              - SY
                              - SZ
                              - TA
                              - TC
                              - TD
                              - TF
                              - TG
                              - TJ
                              - TK
                              - TL
                              - TM
                              - TN
                              - TO
                              - TP
                              - TR
                              - TT
                              - TV
                              - TW
                              - TZ
                              - UA
                              - UG
                              - UK
                              - UM
                              - US
                              - UY
                              - UZ
                              - VA
                              - VC
                              - VE
                              - VG
                              - VI
                              - VN
                              - VU
                              - WF
                              - WS
                              - XK
                              - YE
                              - YT
                              - YU
                              - ZA
                              - ZM
                              - ZR
                              - ZW
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                        x-apidog-orders:
                          - ortsteil
                          - hausnummer
                          - landescode
                          - ort
                          - strasse
                          - postfach
                          - postleitzahl
                        x-apidog-ignore-properties: []
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z04
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z04
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z04
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z04
                      gewerbekennzeichnung:
                        type: boolean
                    x-apidog-orders:
                      - partneradresse
                      - name3
                      - name4
                      - name2
                      - name1
                      - anrede
                      - gewerbekennzeichnung
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragsart
                  - vertragspartner2
                  - korrespondenzpartner
                required:
                  - vertragsart
                x-apidog-ignore-properties: []
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                x-apidog-orders:
                  - ressourcenId
                x-apidog-ignore-properties: []
            MESSLOKATION:
              type: array
              items:
                type: object
                properties:
                  messlokationsId:
                    type: string
                    description: >-
                      Die Messlokations-Identifikation. Das ist die frühere
                      Zählpunktbezeichnung,

                      z.B. DE 47108151234567 | EDIFACT: SG4.IDE+24.SG5.LOC+Z17
                x-apidog-orders:
                  - messlokationsId
                x-apidog-ignore-properties: []
            ZAEHLER:
              type: array
              items:
                type: object
                properties:
                  zaehlernummer:
                    type: string
                    description: >-
                      Die Nummer des zu sperrenden Zählers | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+ZA4.SG10.CCI+++E13.CAV+Z30
                  datenqualitaet:
                    type: string
                x-apidog-orders:
                  - zaehlernummer
                  - datenqualitaet
                x-apidog-ignore-properties: []
            TECHNISCHE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z20'
                x-apidog-orders:
                  - ressourcenId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - ENERGIELIEFERVERTRAG
            - STEUERBARE_RESSOURCE
            - MESSLOKATION
            - ZAEHLER
            - TECHNISCHE_RESSOURCE
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            freitext:
              type: string
            absender:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        enum:
                          - RUF_ZENTRALE
                          - FAX_ZENTRALE
                          - SAMMELRUF
                          - SAMMELFAX
                          - ABTEILUNGRUF
                          - ABTEILUNGFAX
                          - RUF_DURCHWAHL
                          - FAX_DURCHWAHL
                          - MOBIL_NUMMER
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
                - rufnummern
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
            abtretungserklaerung:
              type: object
              properties:
                link3:
                  type: string
                  description: 'Link Zeile 3 | EDIFACT: SG4.IDE+24.FTX+Z13'
                link1:
                  type: string
                  description: 'Link Zeile 1 | EDIFACT: SG4.IDE+24.FTX+Z13'
                passwort:
                  type: string
                  description: 'Passwort zum Abruf | EDIFACT: SG4.IDE+24.FTX+Z13'
                link5:
                  type: string
                  description: 'Link Zeile 5 | EDIFACT: SG4.IDE+24.FTX+Z13'
                link2:
                  type: string
                  description: 'Link Zeile 2 | EDIFACT: SG4.IDE+24.FTX+Z13'
                link4:
                  type: string
                  description: 'Link Zeile 4 | EDIFACT: SG4.IDE+24.FTX+Z13'
              x-apidog-orders:
                - link3
                - link1
                - passwort
                - link5
                - link2
                - link4
              x-apidog-ignore-properties: []
            vertragsbeginn:
              type: string
              description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
              format: date-time
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            sparte:
              type: string
          x-apidog-orders:
            - freitext
            - absender
            - abtretungserklaerung
            - vertragsbeginn
            - empfaenger
            - transaktionsgrundergaenzung
            - transaktionsgrund
            - sparte
          required:
            - absender
            - vertragsbeginn
            - empfaenger
            - sparte
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55601 - LF an NB - Anmeldung einer Zuordnung des LF zur Marktlokation
        bzw. Tranche
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55600:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                    enum:
                      - ERWARTETE_DATEN
                      - IM_SYSTEM_VORHANDENE_DATEN
                      - INFORMATIVE_DATEN
                      - GUELTIGE_DATEN
                      - KEINE_DATEN
                      - IM_SYSTEM_KEINE_DATEN_VORHANDEN
                      - KEINE_DATEN_ERWARTET
                      - DIFFERENZ_DATEN
                      - DIFFERENZ_ERWARTETE_DATEN
                      - DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN
                  lokationsadresse:
                    type: object
                    properties:
                      zusatzInformation:
                        type: object
                        properties:
                          zusatz3:
                            type: string
                            description: 'Adresszusatz 3 | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                          zusatz1:
                            type: string
                            description: 'Adresszusatz 1 | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                          zusatz5:
                            type: string
                            description: 'Adresszusatz 5 | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                          zusatz4:
                            type: string
                            description: 'Adresszusatz 4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                          zusatz2:
                            type: string
                            description: 'Adresszusatz 2 | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                        x-apidog-orders:
                          - zusatz3
                          - zusatz1
                          - zusatz5
                          - zusatz4
                          - zusatz2
                        x-apidog-ignore-properties: []
                      ortsteil:
                        type: string
                        description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                      postleitzahl:
                        type: string
                        description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                      strasse:
                        type: string
                        description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                      landescode:
                        type: string
                        title: Landescode
                        description: >-
                          Der ISO-Landescode als Enumeration | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z60
                        enum:
                          - AC
                          - AD
                          - AE
                          - AF
                          - AG
                          - AI
                          - AL
                          - AM
                          - AN
                          - AO
                          - AQ
                          - AR
                          - AS
                          - AT
                          - AU
                          - AW
                          - AX
                          - AZ
                          - BA
                          - BB
                          - BD
                          - BE
                          - BF
                          - BG
                          - BH
                          - BI
                          - BJ
                          - BL
                          - BM
                          - BN
                          - BO
                          - BQ
                          - BR
                          - BS
                          - BT
                          - BU
                          - BV
                          - BW
                          - BY
                          - BZ
                          - CA
                          - CC
                          - CD
                          - CF
                          - CG
                          - CH
                          - CI
                          - CK
                          - CL
                          - CM
                          - CN
                          - CO
                          - CP
                          - CR
                          - CS
                          - CU
                          - CV
                          - CW
                          - CX
                          - CY
                          - CZ
                          - DE
                          - DG
                          - DJ
                          - DK
                          - DM
                          - DO
                          - DZ
                          - EA
                          - EC
                          - EE
                          - EG
                          - EH
                          - ER
                          - ES
                          - ET
                          - EU
                          - FI
                          - FJ
                          - FK
                          - FM
                          - FO
                          - FR
                          - FX
                          - GA
                          - GB
                          - GD
                          - GE
                          - GF
                          - GG
                          - GH
                          - GI
                          - GL
                          - GM
                          - GN
                          - GP
                          - GQ
                          - GR
                          - GS
                          - GT
                          - GU
                          - GW
                          - GY
                          - HK
                          - HM
                          - HN
                          - HR
                          - HT
                          - HU
                          - IC
                          - ID
                          - IE
                          - IL
                          - IM
                          - IN
                          - IO
                          - IQ
                          - IR
                          - IS
                          - IT
                          - JE
                          - JM
                          - JO
                          - JP
                          - KE
                          - KG
                          - KH
                          - KI
                          - KM
                          - KN
                          - KP
                          - KR
                          - KW
                          - KY
                          - KZ
                          - LA
                          - LB
                          - LC
                          - LI
                          - LK
                          - LR
                          - LS
                          - LT
                          - LU
                          - LV
                          - LY
                          - MA
                          - MC
                          - MD
                          - ME
                          - MF
                          - MG
                          - MH
                          - MK
                          - ML
                          - MM
                          - MN
                          - MO
                          - MP
                          - MQ
                          - MR
                          - MS
                          - MT
                          - MU
                          - MV
                          - MW
                          - MX
                          - MY
                          - MZ
                          - NA
                          - NC
                          - NE
                          - NF
                          - NG
                          - NI
                          - NL
                          - 'NO'
                          - NP
                          - NR
                          - NT
                          - NU
                          - NZ
                          - OM
                          - PA
                          - PE
                          - PF
                          - PG
                          - PH
                          - PK
                          - PL
                          - PM
                          - PN
                          - PR
                          - PS
                          - PT
                          - PW
                          - PY
                          - QA
                          - RE
                          - RO
                          - RS
                          - RU
                          - RW
                          - SA
                          - SB
                          - SC
                          - SD
                          - SE
                          - SF
                          - SG
                          - SH
                          - SI
                          - SJ
                          - SK
                          - SL
                          - SM
                          - SN
                          - SO
                          - SR
                          - SS
                          - ST
                          - SU
                          - SV
                          - SX
                          - SY
                          - SZ
                          - TA
                          - TC
                          - TD
                          - TF
                          - TG
                          - TJ
                          - TK
                          - TL
                          - TM
                          - TN
                          - TO
                          - TP
                          - TR
                          - TT
                          - TV
                          - TW
                          - TZ
                          - UA
                          - UG
                          - UK
                          - UM
                          - US
                          - UY
                          - UZ
                          - VA
                          - VC
                          - VE
                          - VG
                          - VI
                          - VN
                          - VU
                          - WF
                          - WS
                          - XK
                          - YE
                          - YT
                          - YU
                          - ZA
                          - ZM
                          - ZR
                          - ZW
                      hausnummer:
                        type: string
                        description: >-
                          Hausnummer und Ergänzung | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z60
                      ort:
                        type: string
                        description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                      postfach:
                        type: string
                        description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z60'
                    x-apidog-orders:
                      - zusatzInformation
                      - ortsteil
                      - postleitzahl
                      - strasse
                      - landescode
                      - hausnummer
                      - ort
                      - postfach
                    x-apidog-ignore-properties: []
                  erforderlichesProduktpaket:
                    type: array
                    items:
                      type: object
                      properties:
                        produktpaket:
                          type: object
                          properties:
                            priorisierung:
                              type: string
                              title: Priorisierung
                              description: >-
                                Priorisierung | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+ZH0.SG10.CCI+Z65.CAV
                              enum:
                                - PRIORITAET1
                                - PRIORITAET2
                                - PRIORITAET3
                                - PRIORITAET4
                                - PRIORITAET5
                            produktpaketId:
                              type: integer
                              description: >-
                                produktpaketId | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z79, SG4.IDE+24.SG8.SEQ+ZH0
                            umsetzungsgradvorgabe:
                              type: string
                              title: Umsetzungsgradvorgabe
                              description: >-
                                Umsetzungsgradvorgabe | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+ZH0.SG10.CCI+Z65
                              enum:
                                - ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
                                - >-
                                  ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR
                          x-apidog-orders:
                            - priorisierung
                            - produktpaketId
                            - umsetzungsgradvorgabe
                          required:
                            - produktpaketId
                            - umsetzungsgradvorgabe
                          x-apidog-ignore-properties: []
                        produkt:
                          type: array
                          items:
                            type: object
                            properties:
                              produkt:
                                type: object
                                properties:
                                  wertedetails:
                                    type: string
                                    description: >-
                                      wertedetails | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.SG10.CCI+Z66.CAV+ZV4
                                  produktCode:
                                    type: string
                                    description: >-
                                      produktCode | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.PIA+5
                                  codeProdukteigenschaft:
                                    type: string
                                    description: >-
                                      codeProdukteigenschaft | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.SG10.CCI+Z66.CAV+ZH9
                                x-apidog-orders:
                                  - wertedetails
                                  - produktCode
                                  - codeProdukteigenschaft
                                required:
                                  - wertedetails
                                  - produktCode
                                  - codeProdukteigenschaft
                                x-apidog-ignore-properties: []
                            x-apidog-orders:
                              - produkt
                            required:
                              - produkt
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - produktpaket
                        - produkt
                      required:
                        - produktpaket
                        - produkt
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - marktlokationsId
                  - datenqualitaet
                  - lokationsadresse
                  - erforderlichesProduktpaket
                required:
                  - erforderlichesProduktpaket
                x-apidog-ignore-properties: []
            ENERGIELIEFERVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsart:
                    type: string
                    enum:
                      - ENERGIELIEFERVERTRAG
                    x-apidog-enum:
                      - value: ENERGIELIEFERVERTRAG
                        name: ''
                        description: ''
                    default: ENERGIELIEFERVERTRAG
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen

                            beispielsweise der Nachname dargestellt werden.
                            Beispiele: Yellow Strom GmbH

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z09
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z09
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                          enum:
                            - KUNDE
                            - LIEFERANT
                            - DIENSTLEISTER
                            - INTERESSENT
                            - MARKTPARTNER
                            - EIGENTUEMER
                            - HAUSVERWALTER
                            - KORRESPONDENZEMPFAENGER
                            - ABLESEKARTENEMPFAENGER
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z09'
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                        gewerbekennzeichnung:
                          type: string
                      x-apidog-orders:
                        - name1
                        - name3
                        - anrede
                        - geschaeftspartnerrolle
                        - name4
                        - name2
                        - gewerbekennzeichnung
                      required:
                        - name1
                        - geschaeftspartnerrolle
                        - gewerbekennzeichnung
                      x-apidog-ignore-properties: []
                  korrespondenzpartner:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z04
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z04
                            enum:
                              - AC
                              - AD
                              - AE
                              - AF
                              - AG
                              - AI
                              - AL
                              - AM
                              - AN
                              - AO
                              - AQ
                              - AR
                              - AS
                              - AT
                              - AU
                              - AW
                              - AX
                              - AZ
                              - BA
                              - BB
                              - BD
                              - BE
                              - BF
                              - BG
                              - BH
                              - BI
                              - BJ
                              - BL
                              - BM
                              - BN
                              - BO
                              - BQ
                              - BR
                              - BS
                              - BT
                              - BU
                              - BV
                              - BW
                              - BY
                              - BZ
                              - CA
                              - CC
                              - CD
                              - CF
                              - CG
                              - CH
                              - CI
                              - CK
                              - CL
                              - CM
                              - CN
                              - CO
                              - CP
                              - CR
                              - CS
                              - CU
                              - CV
                              - CW
                              - CX
                              - CY
                              - CZ
                              - DE
                              - DG
                              - DJ
                              - DK
                              - DM
                              - DO
                              - DZ
                              - EA
                              - EC
                              - EE
                              - EG
                              - EH
                              - ER
                              - ES
                              - ET
                              - EU
                              - FI
                              - FJ
                              - FK
                              - FM
                              - FO
                              - FR
                              - FX
                              - GA
                              - GB
                              - GD
                              - GE
                              - GF
                              - GG
                              - GH
                              - GI
                              - GL
                              - GM
                              - GN
                              - GP
                              - GQ
                              - GR
                              - GS
                              - GT
                              - GU
                              - GW
                              - GY
                              - HK
                              - HM
                              - HN
                              - HR
                              - HT
                              - HU
                              - IC
                              - ID
                              - IE
                              - IL
                              - IM
                              - IN
                              - IO
                              - IQ
                              - IR
                              - IS
                              - IT
                              - JE
                              - JM
                              - JO
                              - JP
                              - KE
                              - KG
                              - KH
                              - KI
                              - KM
                              - KN
                              - KP
                              - KR
                              - KW
                              - KY
                              - KZ
                              - LA
                              - LB
                              - LC
                              - LI
                              - LK
                              - LR
                              - LS
                              - LT
                              - LU
                              - LV
                              - LY
                              - MA
                              - MC
                              - MD
                              - ME
                              - MF
                              - MG
                              - MH
                              - MK
                              - ML
                              - MM
                              - MN
                              - MO
                              - MP
                              - MQ
                              - MR
                              - MS
                              - MT
                              - MU
                              - MV
                              - MW
                              - MX
                              - MY
                              - MZ
                              - NA
                              - NC
                              - NE
                              - NF
                              - NG
                              - NI
                              - NL
                              - 'NO'
                              - NP
                              - NR
                              - NT
                              - NU
                              - NZ
                              - OM
                              - PA
                              - PE
                              - PF
                              - PG
                              - PH
                              - PK
                              - PL
                              - PM
                              - PN
                              - PR
                              - PS
                              - PT
                              - PW
                              - PY
                              - QA
                              - RE
                              - RO
                              - RS
                              - RU
                              - RW
                              - SA
                              - SB
                              - SC
                              - SD
                              - SE
                              - SF
                              - SG
                              - SH
                              - SI
                              - SJ
                              - SK
                              - SL
                              - SM
                              - SN
                              - SO
                              - SR
                              - SS
                              - ST
                              - SU
                              - SV
                              - SX
                              - SY
                              - SZ
                              - TA
                              - TC
                              - TD
                              - TF
                              - TG
                              - TJ
                              - TK
                              - TL
                              - TM
                              - TN
                              - TO
                              - TP
                              - TR
                              - TT
                              - TV
                              - TW
                              - TZ
                              - UA
                              - UG
                              - UK
                              - UM
                              - US
                              - UY
                              - UZ
                              - VA
                              - VC
                              - VE
                              - VG
                              - VI
                              - VN
                              - VU
                              - WF
                              - WS
                              - XK
                              - YE
                              - YT
                              - YU
                              - ZA
                              - ZM
                              - ZR
                              - ZW
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                        x-apidog-orders:
                          - ortsteil
                          - hausnummer
                          - landescode
                          - ort
                          - strasse
                          - postfach
                          - postleitzahl
                        x-apidog-ignore-properties: []
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z04
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z04
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z04
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z04
                      gewerbekennzeichnung:
                        type: string
                    x-apidog-orders:
                      - partneradresse
                      - name3
                      - name4
                      - name2
                      - name1
                      - anrede
                      - gewerbekennzeichnung
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragsart
                  - vertragspartner2
                  - korrespondenzpartner
                required:
                  - vertragsart
                  - vertragspartner2
                x-apidog-ignore-properties: []
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsart:
                    type: string
                    enum:
                      - NETZNUTZUNGSVERTRAG
                    x-apidog-enum:
                      - value: NETZNUTZUNGSVERTRAG
                        name: ''
                        description: ''
                    default: NETZNUTZUNGSVERTRAG
                  vertragskonditionen:
                    type: object
                    properties:
                      haushaltskunde:
                        type: boolean
                        description: >-
                          haushaltskunde | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI
                    x-apidog-orders:
                      - haushaltskunde
                    required:
                      - haushaltskunde
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragsart
                  - vertragskonditionen
                required:
                  - vertragsart
                  - vertragskonditionen
                x-apidog-ignore-properties: []
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                x-apidog-orders:
                  - ressourcenId
                x-apidog-ignore-properties: []
            MESSLOKATION:
              type: array
              items:
                type: object
                properties:
                  messlokationsId:
                    type: string
                    description: >-
                      Die Messlokations-Identifikation. Das ist die frühere
                      Zählpunktbezeichnung,

                      z.B. DE 47108151234567 | EDIFACT: SG4.IDE+24.SG5.LOC+Z17
                x-apidog-orders:
                  - messlokationsId
                x-apidog-ignore-properties: []
            ZAEHLER:
              type: array
              items:
                type: object
                properties:
                  zaehlernummer:
                    type: string
                    description: >-
                      Die Nummer des zu sperrenden Zählers | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+ZA4.SG10.CCI+++E13.CAV+Z30
                  datenqualitaet:
                    type: string
                x-apidog-orders:
                  - zaehlernummer
                  - datenqualitaet
                x-apidog-ignore-properties: []
            TECHNISCHE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z20'
                x-apidog-orders:
                  - ressourcenId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - ENERGIELIEFERVERTRAG
            - NETZNUTZUNGSVERTRAG
            - STEUERBARE_RESSOURCE
            - MESSLOKATION
            - ZAEHLER
            - TECHNISCHE_RESSOURCE
          required:
            - MARKTLOKATION
            - ENERGIELIEFERVERTRAG
            - NETZNUTZUNGSVERTRAG
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            vertragsende:
              type: string
              description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
              format: date-time
            freitext:
              type: object
              properties:
                freitext2:
                  type: string
                  description: 'Freitext Zeile 2 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext1:
                  type: string
                  description: 'Freitext Zeile 1 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext4:
                  type: string
                  description: 'Freitext Zeile 4 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext5:
                  type: string
                  description: 'Freitext Zeile 5 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext3:
                  type: string
                  description: 'Freitext Zeile 3 | EDIFACT: SG4.IDE+24.FTX+ACB'
              x-apidog-orders:
                - freitext2
                - freitext1
                - freitext4
                - freitext5
                - freitext3
              x-apidog-ignore-properties: []
            absender:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        enum:
                          - RUF_ZENTRALE
                          - FAX_ZENTRALE
                          - SAMMELRUF
                          - SAMMELFAX
                          - ABTEILUNGRUF
                          - ABTEILUNGFAX
                          - RUF_DURCHWAHL
                          - FAX_DURCHWAHL
                          - MOBIL_NUMMER
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
                - rufnummern
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzungBefristeteAnmeldung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund bei befristeten An-/Abmeldungen
                / UTILMD STS+7++E01+ZW4+### | EDIFACT: SG4.IDE+24.STS+7
            vertragsbeginn:
              type: string
              description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
              format: date-time
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            sparte:
              type: string
          x-apidog-orders:
            - vertragsende
            - freitext
            - absender
            - transaktionsgrundergaenzungBefristeteAnmeldung
            - vertragsbeginn
            - empfaenger
            - transaktionsgrundergaenzung
            - transaktionsgrund
            - sparte
          required:
            - absender
            - vertragsbeginn
            - empfaenger
            - transaktionsgrundergaenzung
            - transaktionsgrund
            - sparte
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55600 - LF an NB - Anmeldung einer Zuordnung des LF zur Marktlokation
        bzw. Tranche
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55077:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  erforderlichesProduktpaket:
                    type: array
                    items:
                      type: object
                      properties:
                        produktpaket:
                          type: object
                          properties:
                            priorisierung:
                              type: string
                              title: Priorisierung
                              description: >-
                                Priorisierung | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+ZH0.SG10.CCI+Z65.CAV
                              enum:
                                - PRIORITAET1
                                - PRIORITAET2
                                - PRIORITAET3
                                - PRIORITAET4
                                - PRIORITAET5
                            produktpaketId:
                              type: integer
                              description: >-
                                produktpaketId | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z79, SG4.IDE+24.SG8.SEQ+ZH0
                            umsetzungsgradvorgabe:
                              type: string
                              title: Umsetzungsgradvorgabe
                              description: >-
                                Umsetzungsgradvorgabe | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+ZH0.SG10.CCI+Z65
                              enum:
                                - ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
                                - >-
                                  ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR
                          x-apidog-orders:
                            - priorisierung
                            - produktpaketId
                            - umsetzungsgradvorgabe
                          required:
                            - produktpaketId
                            - umsetzungsgradvorgabe
                          x-apidog-ignore-properties: []
                        produkt:
                          type: array
                          items:
                            type: object
                            properties:
                              produkt:
                                type: object
                                properties:
                                  wertedetails:
                                    type: string
                                    description: >-
                                      wertedetails | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.SG10.CCI+Z66.CAV+ZV4
                                  produktCode:
                                    type: string
                                    description: >-
                                      produktCode | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.PIA+5
                                  codeProdukteigenschaft:
                                    type: string
                                    description: >-
                                      codeProdukteigenschaft | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.SG10.CCI+Z66.CAV+ZH9
                                x-apidog-orders:
                                  - wertedetails
                                  - produktCode
                                  - codeProdukteigenschaft
                                required:
                                  - wertedetails
                                  - produktCode
                                  - codeProdukteigenschaft
                                x-apidog-ignore-properties: []
                            x-apidog-orders:
                              - produkt
                            required:
                              - produkt
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - produktpaket
                        - produkt
                      required:
                        - produktpaket
                        - produkt
                      x-apidog-ignore-properties: []
                  foerderungsLand:
                    type: string
                    description: >-
                      foerderungsLand | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z23
                x-apidog-orders:
                  - marktlokationsId
                  - erforderlichesProduktpaket
                  - foerderungsLand
                required:
                  - erforderlichesProduktpaket
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                x-apidog-orders:
                  - tranchenId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - TRANCHE
          required:
            - MARKTLOKATION
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            absender:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        enum:
                          - RUF_ZENTRALE
                          - FAX_ZENTRALE
                          - SAMMELRUF
                          - SAMMELFAX
                          - ABTEILUNGRUF
                          - ABTEILUNGFAX
                          - RUF_DURCHWAHL
                          - FAX_DURCHWAHL
                          - MOBIL_NUMMER
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
                - rufnummern
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
            abtretungserklaerung:
              type: object
              properties:
                link3:
                  type: string
                  description: 'Link Zeile 3 | EDIFACT: SG4.IDE+24.FTX+Z13'
                link1:
                  type: string
                  description: 'Link Zeile 1 | EDIFACT: SG4.IDE+24.FTX+Z13'
                passwort:
                  type: string
                  description: 'Passwort zum Abruf | EDIFACT: SG4.IDE+24.FTX+Z13'
                link5:
                  type: string
                  description: 'Link Zeile 5 | EDIFACT: SG4.IDE+24.FTX+Z13'
                link2:
                  type: string
                  description: 'Link Zeile 2 | EDIFACT: SG4.IDE+24.FTX+Z13'
                link4:
                  type: string
                  description: 'Link Zeile 4 | EDIFACT: SG4.IDE+24.FTX+Z13'
              x-apidog-orders:
                - link3
                - link1
                - passwort
                - link5
                - link2
                - link4
              x-apidog-ignore-properties: []
            vertragsbeginn:
              type: string
              description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
              format: date-time
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            sparte:
              type: string
          x-apidog-orders:
            - absender
            - abtretungserklaerung
            - vertragsbeginn
            - empfaenger
            - transaktionsgrundergaenzung
            - transaktionsgrund
            - sparte
          required:
            - absender
            - vertragsbeginn
            - empfaenger
            - transaktionsgrundergaenzung
            - transaktionsgrund
            - sparte
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55077 - LFN an NB - Anmeldung einer Zuordnung des LFN zur Marktlokation
        bzw. Tranche
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55001:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation für die angemeldet werden soll. |
                      EDIFACT: SG4.IDE+24.SG5.LOC+Z16, SG4.IDE+24.SG5.LOC+Z22
                    title: >-
                      The ID of the market location for which registration is to
                      be made.
                  marktlokationsTyp:
                    type: array
                    items:
                      $ref: '#/components/schemas/MarktlokationsTypisierung'
                    title: >-
                      Classification of the market location as standard market
                      location, dormant market location, or customer facility
                  erforderlichesProduktpaket:
                    $ref: '#/components/schemas/Produktpaket'
                x-apidog-orders:
                  - marktlokationsId
                  - marktlokationsTyp
                  - erforderlichesProduktpaket
                required:
                  - marktlokationsId
                  - marktlokationsTyp
                  - erforderlichesProduktpaket
                x-apidog-ignore-properties: []
            ENERGIELIEFERVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsart:
                    type: string
                    enum:
                      - ENERGIELIEFERVERTRAG
                    x-apidog-enum:
                      - value: ENERGIELIEFERVERTRAG
                        name: ''
                        description: ''
                    default: ENERGIELIEFERVERTRAG
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                          enum:
                            - VERTRAG
                          x-apidog-enum:
                            - value: VERTRAG
                              name: ''
                              description: ''
                          default: VERTRAG
                        versionStruktur:
                          type: string
                          default: '1'
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen

                            beispielsweise der Nachname dargestellt werden.
                            Beispiele: Yellow Strom GmbH

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z09
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z09
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                        geschaeftspartnerrolle:
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                          $ref: '#/components/schemas/Geschaeftspartnerrolle'
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z09'
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                        gewerbekennzeichnung:
                          type: boolean
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - name1
                        - name3
                        - anrede
                        - geschaeftspartnerrolle
                        - name4
                        - name2
                        - gewerbekennzeichnung
                      required:
                        - boTyp
                        - name1
                        - geschaeftspartnerrolle
                        - gewerbekennzeichnung
                      x-apidog-ignore-properties: []
                  korrespondenzpartner:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z04
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z04
                            enum:
                              - AC
                              - AD
                              - AE
                              - AF
                              - AG
                              - AI
                              - AL
                              - AM
                              - AN
                              - AO
                              - AQ
                              - AR
                              - AS
                              - AT
                              - AU
                              - AW
                              - AX
                              - AZ
                              - BA
                              - BB
                              - BD
                              - BE
                              - BF
                              - BG
                              - BH
                              - BI
                              - BJ
                              - BL
                              - BM
                              - BN
                              - BO
                              - BQ
                              - BR
                              - BS
                              - BT
                              - BU
                              - BV
                              - BW
                              - BY
                              - BZ
                              - CA
                              - CC
                              - CD
                              - CF
                              - CG
                              - CH
                              - CI
                              - CK
                              - CL
                              - CM
                              - CN
                              - CO
                              - CP
                              - CR
                              - CS
                              - CU
                              - CV
                              - CW
                              - CX
                              - CY
                              - CZ
                              - DE
                              - DG
                              - DJ
                              - DK
                              - DM
                              - DO
                              - DZ
                              - EA
                              - EC
                              - EE
                              - EG
                              - EH
                              - ER
                              - ES
                              - ET
                              - EU
                              - FI
                              - FJ
                              - FK
                              - FM
                              - FO
                              - FR
                              - FX
                              - GA
                              - GB
                              - GD
                              - GE
                              - GF
                              - GG
                              - GH
                              - GI
                              - GL
                              - GM
                              - GN
                              - GP
                              - GQ
                              - GR
                              - GS
                              - GT
                              - GU
                              - GW
                              - GY
                              - HK
                              - HM
                              - HN
                              - HR
                              - HT
                              - HU
                              - IC
                              - ID
                              - IE
                              - IL
                              - IM
                              - IN
                              - IO
                              - IQ
                              - IR
                              - IS
                              - IT
                              - JE
                              - JM
                              - JO
                              - JP
                              - KE
                              - KG
                              - KH
                              - KI
                              - KM
                              - KN
                              - KP
                              - KR
                              - KW
                              - KY
                              - KZ
                              - LA
                              - LB
                              - LC
                              - LI
                              - LK
                              - LR
                              - LS
                              - LT
                              - LU
                              - LV
                              - LY
                              - MA
                              - MC
                              - MD
                              - ME
                              - MF
                              - MG
                              - MH
                              - MK
                              - ML
                              - MM
                              - MN
                              - MO
                              - MP
                              - MQ
                              - MR
                              - MS
                              - MT
                              - MU
                              - MV
                              - MW
                              - MX
                              - MY
                              - MZ
                              - NA
                              - NC
                              - NE
                              - NF
                              - NG
                              - NI
                              - NL
                              - 'NO'
                              - NP
                              - NR
                              - NT
                              - NU
                              - NZ
                              - OM
                              - PA
                              - PE
                              - PF
                              - PG
                              - PH
                              - PK
                              - PL
                              - PM
                              - PN
                              - PR
                              - PS
                              - PT
                              - PW
                              - PY
                              - QA
                              - RE
                              - RO
                              - RS
                              - RU
                              - RW
                              - SA
                              - SB
                              - SC
                              - SD
                              - SE
                              - SF
                              - SG
                              - SH
                              - SI
                              - SJ
                              - SK
                              - SL
                              - SM
                              - SN
                              - SO
                              - SR
                              - SS
                              - ST
                              - SU
                              - SV
                              - SX
                              - SY
                              - SZ
                              - TA
                              - TC
                              - TD
                              - TF
                              - TG
                              - TJ
                              - TK
                              - TL
                              - TM
                              - TN
                              - TO
                              - TP
                              - TR
                              - TT
                              - TV
                              - TW
                              - TZ
                              - UA
                              - UG
                              - UK
                              - UM
                              - US
                              - UY
                              - UZ
                              - VA
                              - VC
                              - VE
                              - VG
                              - VI
                              - VN
                              - VU
                              - WF
                              - WS
                              - XK
                              - YE
                              - YT
                              - YU
                              - ZA
                              - ZM
                              - ZR
                              - ZW
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                        x-apidog-orders:
                          - ortsteil
                          - hausnummer
                          - landescode
                          - ort
                          - strasse
                          - postfach
                          - postleitzahl
                        x-apidog-ignore-properties: []
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z04
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z04
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z04
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z04
                      gewerbekennzeichnung:
                        type: boolean
                    x-apidog-orders:
                      - partneradresse
                      - name3
                      - name4
                      - name2
                      - name1
                      - anrede
                      - gewerbekennzeichnung
                    required:
                      - partneradresse
                      - name1
                      - gewerbekennzeichnung
                    x-apidog-ignore-properties: []
                  enFG:
                    type: array
                    items:
                      type: object
                      properties:
                        grund:
                          type: array
                          items:
                            title: Abweichungsgrund
                            description: >-
                              Abweichungsgrund | EDIFACT:
                              SG4.IDE+24.SG8.SEQ+Z75.SG10.CCI+Z61.CAV
                            $ref: >-
                              #/components/schemas/GrundlageVerringerungUmlagenGrund
                        grundlageVerringerungUmlagen:
                          type: string
                          title: GrundlageVerringerungUmlagen
                          description: >-
                            GrundlageVerringerungUmlagen | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z75.SG10.CCI+Z61
                          enum:
                            - ERFUELLT_VORAUSSETZUNG_NACH_ENFG
                            - ERFUELLT_NICHT_VORAUSSETZUNG_NACH_ENFG
                            - KEINE_ANGABE
                      x-apidog-orders:
                        - grund
                        - grundlageVerringerungUmlagen
                      required:
                        - grundlageVerringerungUmlagen
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragsart
                  - vertragspartner2
                  - korrespondenzpartner
                  - enFG
                required:
                  - vertragsart
                  - vertragspartner2
                  - enFG
                x-apidog-ignore-properties: []
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsart:
                    type: string
                    enum:
                      - NETZNUTZUNGSVERTRAG
                    x-apidog-enum:
                      - value: NETZNUTZUNGSVERTRAG
                        name: ''
                        description: ''
                    default: NETZNUTZUNGSVERTRAG
                    title: Contract Type
                  vertragskonditionen:
                    type: object
                    properties:
                      haushaltskunde:
                        type: boolean
                        description: >-
                          haushaltskunde | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI
                        title: Household Customer
                    x-apidog-orders:
                      - haushaltskunde
                    required:
                      - haushaltskunde
                    title: Contract Conditions
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragsart
                  - vertragskonditionen
                required:
                  - vertragsart
                  - vertragskonditionen
                x-apidog-ignore-properties: []
              title: Grid Usage Contracts
          x-apidog-orders:
            - MARKTLOKATION
            - ENERGIELIEFERVERTRAG
            - NETZNUTZUNGSVERTRAG
          title: Information container for master data belonging to the transaction
          description: Informationscontainer für Stammdaten, die zur Transaktion gehören
          required:
            - MARKTLOKATION
            - ENERGIELIEFERVERTRAG
            - NETZNUTZUNGSVERTRAG
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            vertragsende:
              type: string
              description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
              format: date-time
              pattern: >-
                20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
              title: Contract end date
            absender:
              type: object
              properties:
                boTyp:
                  type: string
                  enum:
                    - MARKTTEILNEHMER
                  x-apidog-enum:
                    - value: MARKTTEILNEHMER
                      name: ''
                      description: ''
                  default: MARKTTEILNEHMER
                versionStruktur:
                  type: string
                  default: '1'
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        enum:
                          - RUF_ZENTRALE
                          - FAX_ZENTRALE
                          - SAMMELRUF
                          - SAMMELFAX
                          - ABTEILUNGRUF
                          - ABTEILUNGFAX
                          - RUF_DURCHWAHL
                          - FAX_DURCHWAHL
                          - MOBIL_NUMMER
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
                - rufnummern
                - ansprechpartner
              title: message sender information
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzungBefristeteAnmeldung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund bei befristeten An-/Abmeldungen
                / UTILMD STS+7++E01+ZW4+### | EDIFACT: SG4.IDE+24.STS+7
              title: >-
                Supplement to the transaction reason for temporary
                registrations/deregistrations
            vertragsbeginn:
              type: string
              description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
              format: date-time
              pattern: >-
                20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
              title: Contract start date
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                  enum:
                    - MARKTTEILNEHMER
                  x-apidog-enum:
                    - value: MARKTTEILNEHMER
                      name: ''
                      description: ''
                  default: MARKTTEILNEHMER
                versionStruktur:
                  type: string
                  default: '1'
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              required:
                - boTyp
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              title: message receiver information
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
              title: Supplement to the transaction reason
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
              title: >-
                The transaction reason describes the business case in more
                detail
            sparte:
              $ref: '#/components/schemas/Sparte'
          x-apidog-orders:
            - vertragsende
            - absender
            - transaktionsgrundergaenzungBefristeteAnmeldung
            - vertragsbeginn
            - empfaenger
            - transaktionsgrundergaenzung
            - transaktionsgrund
            - sparte
          title: >-
            Information container for data on the transaction and market
            partners involved
          required:
            - absender
            - vertragsbeginn
            - empfaenger
            - transaktionsgrundergaenzung
            - transaktionsgrund
            - sparte
          description: >-
            Informationscontainer für Daten zum Vorgang und beteiligten
            Marktpartnern
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55001 - LFN an NB - Anmeldung einer Zuordnung des LFN zur Marktlokation
        bzw. Tranche / 

        55001 - LFN to DSO – Registration of an assignment of the LFN to the
        market location or tranche.
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Sparte:
      type: string
      title: Sparte
      description: Division
      enum:
        - STROM
        - GAS
        - FERNWAERME
        - NAHWAERME
        - WASSER
        - ABWASSER
      x-apidog-enum:
        - value: STROM
          name: Sparte Strom
          description: Represents electricity as the utility division
        - value: GAS
          name: Sparte Gas
          description: Represents natural gas as the utility division
        - value: FERNWAERME
          name: Sparte Fernwärme
          description: Represents district heating as the utility division
        - value: NAHWAERME
          name: Sparte Nahwärme
          description: Represents local heating as the utility division
        - value: WASSER
          name: Sparte Wasser
          description: Represents water supply as the utility division
        - value: ABWASSER
          name: Sparte Abwasser
          description: Represents wastewater services as the utility division
      examples:
        - STROM
      x-apidog-folder: ''
    GrundlageVerringerungUmlagenGrund:
      type: string
      title: GrundlageVerringerungUmlagenGrund
      description: GrundlageVerringerungUmlagenGrund
      enum:
        - ENFG_STROMSPEICHER_UND_VERLUSTENERGIE
        - ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
        - ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN
        - ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF
        - ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN
        - ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN
        - ENFG_SCHIENENBAHNEN
        - ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR
        - ENFG_LANDSTROMANLAGEN
      x-apidog-enum:
        - value: ENFG_STROMSPEICHER_UND_VERLUSTENERGIE
          name: § 21 EnFG Stromspeicher und Verlustenergie
          description: ZU5
        - value: ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
          name: § 22 EnFG elektrisch angetriebene Wärmepumpen
          description: ZU6
        - value: ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN
          name: § 23 EnFG Umlageerhebung bei Anlagen zur Verstromung von Kuppelgasen
          description: ZU7
        - value: ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF
          name: § 24 EnFG Herstellung von Grünen Wasserstof
          description: ZU8
        - value: ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN
          name: §§ 30 - 35 EnFG stromkostenintensive Unternehmen
          description: ZU9
        - value: >-
            ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN
          name: >-
            § 36 EnFG Herstellung von Wasserstoff in stromkostenintensiven
            Unternehmen
          description: ZV0
        - value: ENFG_SCHIENENBAHNEN
          name: § 37 EnFG Schienenbahnen
          description: ZV1
        - value: ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR
          name: § 38 EnFG elektrische betriebene Bussen im Linienverkehr
          description: ZV2
        - value: ENFG_LANDSTROMANLAGEN
          name: § 39 EnFG Landstromanlagen
          description: ZV3
      x-apidog-folder: ''
    Geschaeftspartnerrolle:
      type: string
      title: Geschaeftspartnerrolle
      description: Geschaeftspartnerrolle
      enum:
        - KUNDE
        - LIEFERANT
        - DIENSTLEISTER
        - INTERESSENT
        - MARKTPARTNER
        - EIGENTUEMER
        - HAUSVERWALTER
        - KORRESPONDENZEMPFAENGER
        - ABLESEKARTENEMPFAENGER
      x-apidog-enum:
        - value: KUNDE
          name: ''
          description: ''
        - value: LIEFERANT
          name: ''
          description: ''
        - value: DIENSTLEISTER
          name: ''
          description: ''
        - value: INTERESSENT
          name: ''
          description: ''
        - value: MARKTPARTNER
          name: ''
          description: ''
        - value: EIGENTUEMER
          name: ''
          description: ''
        - value: HAUSVERWALTER
          name: ''
          description: ''
        - value: KORRESPONDENZEMPFAENGER
          name: ''
          description: ''
        - value: ABLESEKARTENEMPFAENGER
          name: ''
          description: ''
      x-apidog-folder: ''
    Produktpaket:
      title: Produktpaket
      type: object
      properties:
        produktpaketId:
          type: integer
          description: >-
            Produkt-Code, Produkt-Codes sind in der Codeliste der
            Konfigurationen beschrieben

            PIA 5

            PI 55001 55077 55600 55601 55014 55608 

            Priorisierung erforderliches Produktpaket

            SEQ ZH0

            PI 55001 55077 55600 55601 55014 55608 
        produkt:
          type: array
          items:
            $ref: '#/components/schemas/Produkt'
          description: |-
            Produkt
            PIA Z11
            PI 55001 55077 55600 55601 55014 55608 
        umsetzungsgradvorgabe:
          $ref: '#/components/schemas/Umsetzungsgradvorgabe'
          description: >-
            Umsetzungsgradvorgabe des Produktpakets wird unterteilt in Z01
            Produktpaket ist vollumfänglich umzusetzen oder Z02 Produktpaket
            kann in Teilen umgesetzt werden zum Zuordnungsbeginn

            CCI Z65

            PI 55001 55077 55600 55601 55014 55608
        priorisierung:
          $ref: '#/components/schemas/Priorisierung'
          description: |-
            Priorisierung erforderliches Produktpaket
            CAV Z75 
      x-apidog-orders:
        - produktpaketId
        - produkt
        - umsetzungsgradvorgabe
        - priorisierung
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Priorisierung:
      type: string
      title: Priorisierung
      description: Priorisierung
      enum:
        - PRIORITAET1
        - PRIORITAET2
        - PRIORITAET3
        - PRIORITAET4
        - PRIORITAET5
      x-apidog-enum:
        - value: PRIORITAET1
          name: 1. Priorität
          description: Z75
        - value: PRIORITAET2
          name: 2. Priorität
          description: Z76
        - value: PRIORITAET3
          name: 3. Priorität
          description: Z77
        - value: PRIORITAET4
          name: 4. Priorität
          description: Z78
        - value: PRIORITAET5
          name: 5. Priorität
          description: Z79
      x-apidog-folder: ''
    Umsetzungsgradvorgabe:
      type: string
      title: Umsetzungsgradvorgabe
      description: Umsetzungsgradvorgabe
      enum:
        - ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
        - ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR
      x-apidog-enum:
        - value: ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
          name: Produktpaket ist vollumfänglich umzusetzen
          description: Z01
        - value: ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR
          name: Produktpaket kann in Teilen umgesetzt werden
          description: Z02
      x-apidog-folder: ''
    Produkt:
      title: Produkt
      type: object
      properties:
        produktCode:
          type: string
          description: |-
            Produkt-Code
            Erforderliches Produkt Abrechnungsdaten ORDERS
            PIA 5
            PI 17133
        codeProdukteigenschaft:
          type: string
          description: |-
            Code der Produkteigenschaft
            CAV ZH9
            PI 55001 55077 55600 55601 55014 55608 
        wertedetails:
          type: string
          description: >-
            Wertedetails zum Produkt, Wertedetails zum Produkt sind in der
            Codeliste der Konfigurationen beschrieben

            CAV ZV4

            PI 55001 55077 55600 55601 55014 55608 
      x-apidog-orders:
        - produktCode
        - codeProdukteigenschaft
        - wertedetails
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    MarktlokationsTypisierung:
      title: MarktlokationsTypisierung
      type: object
      properties:
        typ:
          $ref: '#/components/schemas/MarktlokationsTyp'
          description: >-
            Typisierung der Marktlokation als standard Marktlokation, ruhende
            Marktlokation oder Kundenanlage
        gueltigAb:
          type: string
          format: date-time
          description: Startdatum der Typisierung der Marktlokation
        gueltigBis:
          type: string
          format: date-time
          description: Enddatum der Typisierung der Marktlokation
      x-apidog-orders:
        - typ
        - gueltigAb
        - gueltigBis
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    MarktlokationsTyp:
      title: AbgabeArt
      type: string
      enum:
        - STANDARD_MARKTLOKATION
        - RUHENDE_MARKTLOKATION
        - KUNDENANLAGE
      description: AbgabeArt
      x-apidog-folder: ''
    EVENT_SUCCESS:
      type: object
      description: Erfolgsmeldung auf Prozessdaten API Aufruf
      properties:
        businessKey:
          description: Einzigartige Kennung des Geschäftsprozesses
          format: uuid
          type: string
          x-apidog-mock: '{{$string.uuid}}'
        message:
          description: Nachricht mit Details zum ausgelösten Even
          type: string
          examples:
            - >-
              received event XXXXXXXXXXXX with id at 2024-08-08T12:58:22Z and
              started process with businessKey
              4c7170ed-3518-41ee-8582-39ab65b00107
          x-apidog-mock: >-
            received event with id EVENT_NAME at {{$date.isoTimestamp}} and
            started process with businessKey {{$string.uuid}}
      required:
        - businessKey
        - message
      x-apidog-orders:
        - businessKey
        - message
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    EVENT_FAIL:
      type: object
      description: 'Fehlermeldung auf Prozessdaten API Aufruf '
      properties:
        errorCode:
          type: string
          description: Error identifier
          examples:
            - '400'
        message:
          type: string
          description: Technische Meldung
          examples:
            - Validation Failed
      x-apidog-orders:
        - errorCode
        - message
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers:
  - url: ''
    description: Cloud Mock
security:
  - bearer: []

```
