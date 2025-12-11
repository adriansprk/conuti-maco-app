# Prozessdaten aktualiseren

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /updateProcessData:
    post:
      summary: Prozessdaten aktualiseren
      deprecated: false
      description: Aktualisieren der Prozessdaten anhand des BusinessKey.
      operationId: AKTUALISIEREN_PROZESSDATEN
      tags:
        - Schnittstellen/Prozessdaten MSB (Backend)
        - AKTUALISIEREN | UPDATE
      parameters:
        - name: command
          in: query
          description: >
            Name der Operation | Name of the operation (MACO APP internal
            assignment  between process and interface)
          required: true
          schema:
            type: string
            default: AKTUALISIEREN_PROZESSDATEN
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Prozessdaten%20aktualiseren%20MSB'
            example: ''
      responses:
        '200':
          description: Erfolgreiches Aktualisieren des MDOCS
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apidog-orders: []
                x-apidog-ignore-properties: []
          headers: {}
          x-apidog-name: OK
        '422':
          description: Fehler beim Aktualisieren des MDOCS
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apidog-orders: []
                x-apidog-ignore-properties: []
          headers: {}
          x-apidog-name: Parameter Error
      security:
        - bearer: []
      x-apidog-folder: Schnittstellen/Prozessdaten MSB (Backend)
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14669402-run
components:
  schemas:
    Prozessdaten aktualiseren MSB:
      allOf:
        - anyOf:
            - $ref: '#/components/schemas/PI_55555'
            - $ref: '#/components/schemas/PI_55559'
            - &ref_0
              $ref: '#/components/schemas/PI_55644'
            - $ref: '#/components/schemas/PI_55645'
            - $ref: '#/components/schemas/PI_55646'
            - $ref: '#/components/schemas/PI_55647'
            - $ref: '#/components/schemas/PI_55648'
            - $ref: '#/components/schemas/PI_55654'
            - $ref: '#/components/schemas/PI_55655'
            - $ref: '#/components/schemas/PI_55656'
            - $ref: '#/components/schemas/PI_55657'
            - $ref: '#/components/schemas/PI_55633'
            - $ref: '#/components/schemas/PI_55634'
            - $ref: '#/components/schemas/PI_55635'
            - $ref: '#/components/schemas/PI_55636'
            - $ref: '#/components/schemas/PI_55638'
            - $ref: '#/components/schemas/PI_55177'
            - $ref: '#/components/schemas/PI_21047'
            - *ref_0
            - $ref: '#/components/schemas/PI_55664'
            - $ref: '#/components/schemas/PI_55665'
            - $ref: '#/components/schemas/PI_55667'
            - $ref: '#/components/schemas/PI_55666'
            - $ref: '#/components/schemas/PI_55669'
            - $ref: '#/components/schemas/PI_21039'
        - $ref: '#/components/schemas/ZUSATZDATEN%20(%20SST%20Aktualisieren)'
      x-apidog-folder: ''
    ZUSATZDATEN ( SST Aktualisieren):
      type: object
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
              nullable: true
            businessKey:
              type: string
              description: Id des Prozesses, welcher aktuell den Aufruf durchführt
              x-apidog-mock: '{{$string.uuid}}'
              nullable: true
            targetBusinessKey:
              type: string
              description: Id des initial referenzierenden Prozesses
              x-apidog-mock: '{{$string.uuid}}'
              nullable: true
          x-apidog-orders:
            - prozessId
            - businessKey
            - targetBusinessKey
          required:
            - businessKey
            - targetBusinessKey
          x-apidog-ignore-properties: []
      x-apidog-orders:
        - zusatzdaten
      required:
        - zusatzdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_21039:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            kategorie:
              type: string
              description: Kategorie EDIFACT BGM+Z33
            dokumentennummer:
              type: string
              description: Dokumentennummer EDIFACT BGM+Z33+Nummer
            nachrichtendatum:
              type: string
              description: Nachrichtendatum EDIFACT DTM+137
              format: date-time
            empfaenger:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: MP-ID EDIFACT SG1. NAD+MR+MP-ID
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: >-
                    Rollencodetyp Sparte Strom und Gas EDIFACT SG1.
                    NAD+MR+MP-ID: 9 / 293/ 332
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
                - rollencodenummer
                - rollencodetyp
              description: Nachrichtenempfänger EDIFACT SG1. NAD+MR
              x-apidog-ignore-properties: []
            absender:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: MP-ID EDIFACT SG1. NAD+MS+MP-ID
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: >-
                    Rollencodetyp Sparte Strom oder Gas EDIFACT SG1.
                    NAD+MS+MP-ID: 9/293/332
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
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: Kontakt EDIFACT SG2. CTA+IC+Kontaktname
                    eMailAdresse:
                      type: string
                      description: Kommunikationsadresse EDIFACT SG2. COM + eMail EM
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  description: Informationskontakt EDIFACT SG2. CTA+IC
                  required:
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: string
                        description: Rufnummer EDIFACT SG2. COM+Rufnummer
                      nummerntyp:
                        type: string
                        description: >-
                          Rufnummerntyp - EDIFACT SG2. COM+Rufnummer: FX TE AJ
                          AL
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    required:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                  description: Rufnummern - EDIFACT SG2. COM + Rufnummer
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
                - ansprechpartner
                - rufnummern
              description: 'Nachrichtenabsender EDIFACT SG1. NAD+MS '
              required:
                - rufnummern
              x-apidog-ignore-properties: []
            antwortstatus:
              type: string
              description: >-
                Code des Prüfschritts EDIFACT SG15. STS+Z37/ Z38+Z13/ Z14/
                Z32+CODE
            antwortstatusCodeliste:
              type: string
              description: EBD EDIFACT SG15. STS+Z37/ Z38+Z13/ Z14/ Z32+CODE:EBD
            pruefidentifikator:
              type: string
              description: Prüfidentifikator EDIFACT SG15. RFF+Z13
            fertigstellungsdatum:
              type: string
              description: Fertigstellungsdatum EDIFACT SG15. DTM+293
              format: date-time
            sendungsposition:
              type: integer
              description: Sendungsposition EDIFACT SG25. GID+Position
          x-apidog-orders:
            - kategorie
            - dokumentennummer
            - nachrichtendatum
            - empfaenger
            - absender
            - antwortstatus
            - antwortstatusCodeliste
            - pruefidentifikator
            - fertigstellungsdatum
            - sendungsposition
          description: Transaktionsdaten
          required:
            - kategorie
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            STATUSMITTEILUNG:
              type: array
              items:
                type: object
                properties:
                  positionsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        allgemeineInformationen:
                          type: object
                          properties:
                            info1:
                              type: string
                              description: >-
                                1 Freier Text zur weiteren Erklärung EDIFACT
                                SG25. FTX+ACB+++Info1
                            info2:
                              type: string
                              description: >-
                                2 Freier Text zur weiteren Erklärung EDIFACT
                                SG25. FTX+ACB+++Info1:Info2
                            info3:
                              type: string
                              description: >-
                                3 Freier Text zur weiteren Erklärung  EDIFACT
                                SG25. FTX+ACB+++Info1:Info2:Info3
                            info4:
                              type: string
                              description: >-
                                4 Freier Text zur weiteren Erklärung EDIFACT
                                SG25. FTX+ACB+++Info1:Info2:Info3:Info4
                            info5:
                              type: string
                              description: >-
                                5 Freier Text zur weiteren Erklärung EDIFACT
                                SG25. FTX+ACB+++Info1:Info2:Info3:Info4:Info5
                          x-apidog-orders:
                            - info1
                            - info2
                            - info3
                            - info4
                            - info5
                          description: Freier Text EDIFACT SG25. FTX+ACB
                          x-apidog-ignore-properties: []
                        positionsnummer:
                          type: integer
                          description: Positionsnummer EDIFACT SG14. CNI+1
                      x-apidog-orders:
                        - allgemeineInformationen
                        - positionsnummer
                      x-apidog-ignore-properties: []
                    description: Positionsdaten
                x-apidog-orders:
                  - positionsdaten
                x-apidog-ignore-properties: []
              description: BO Statusmitteilung
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: Marktlokations-ID EDIFACT SG14. LOC+172
                x-apidog-orders:
                  - marktlokationsId
                x-apidog-ignore-properties: []
              description: BO Marktlokation
          x-apidog-orders:
            - STATUSMITTEILUNG
            - MARKTLOKATION
          description: Stammdaten
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 21039 - Auftragsstatus (Sperren) NB an LF / MSB / ÜNB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55669:
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
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z45|Z46]
                      gewerbekennzeichnung:
                        type: boolean
                        description: >-
                          Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
                          (gewerbeKennzeichnung = true)

                          oder eine Privatperson handelt. (gewerbeKennzeichnung
                          = false) | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]
                      partneradresse:
                        type: object
                        properties:
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z45|Z46]
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
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]'
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z45|Z46]
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]'
                          postleitzahl:
                            type: string
                            description: >-
                              Postleitzahl | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z45|Z46]
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]'
                        x-apidog-orders:
                          - landescode
                          - postfach
                          - ortsteil
                          - hausnummer
                          - ort
                          - postleitzahl
                          - strasse
                        x-apidog-ignore-properties: []
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]'
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z45|Z46]
                    x-apidog-orders:
                      - anrede
                      - gewerbekennzeichnung
                      - partneradresse
                      - name3
                      - name1
                      - name4
                      - name2
                    x-apidog-ignore-properties: []
                  messadresse:
                    type: object
                    properties:
                      strasse:
                        type: string
                        description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z43|Z44]'
                      zusatzInformation:
                        type: object
                        properties:
                          zusatz2:
                            type: string
                            description: >-
                              Adresszusatz 2 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z43|Z44]
                          zusatz1:
                            type: string
                            description: >-
                              Adresszusatz 1 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z43|Z44]
                          zusatz4:
                            type: string
                            description: >-
                              Adresszusatz 4 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z43|Z44]
                          zusatz5:
                            type: string
                            description: >-
                              Adresszusatz 5 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z43|Z44]
                          zusatz3:
                            type: string
                            description: >-
                              Adresszusatz 3 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z43|Z44]
                        x-apidog-orders:
                          - zusatz2
                          - zusatz1
                          - zusatz4
                          - zusatz5
                          - zusatz3
                        x-apidog-ignore-properties: []
                      hausnummer:
                        type: string
                        description: >-
                          Hausnummer und Ergänzung | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z43|Z44]
                      ortsteil:
                        type: string
                        description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z43|Z44]'
                      ort:
                        type: string
                        description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z43|Z44]'
                      postleitzahl:
                        type: string
                        description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+[Z43|Z44]'
                      postfach:
                        type: string
                        description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z43|Z44]'
                      landescode:
                        type: string
                        title: Landescode
                        description: >-
                          Der ISO-Landescode als Enumeration | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z43|Z44]
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
                    x-apidog-orders:
                      - strasse
                      - zusatzInformation
                      - hausnummer
                      - ortsteil
                      - ort
                      - postleitzahl
                      - postfach
                      - landescode
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG6|ZG7],
                      SG4.IDE+24.SG12.NAD+[Z43|Z44],
                      SG4.IDE+24.SG12.NAD+[Z45|Z46]
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
                  netzebenemessung:
                    type: string
                    title: Netzebene
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++E04.CAV'
                    enum:
                      - NSP
                      - MSP
                      - HSP
                      - HSS
                      - MSP_NSP_UMSP
                      - HSP_MSP_UMSP
                      - HSS_HSP_UMSP
                      - HD
                      - MD
                      - ND
                  messlokationsId:
                    type: string
                    description: >-
                      Die Messlokations-Identifikation. Das ist die frühere
                      Zählpunktbezeichnung,

                      z.B. DE 47108151234567 | EDIFACT: SG4.IDE+24.SG5.LOC+Z17
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG6|ZG7],
                          SG4.IDE+24.SG12.NAD+[Z43|Z44].RFF+Z46,
                          SG4.IDE+24.SG12.NAD+[Z45|Z46].RFF+Z46
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - ablesekartenempfaenger
                  - messadresse
                  - datenqualitaet
                  - netzebenemessung
                  - messlokationsId
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            ZAEHLER:
              type: array
              items:
                type: object
                properties:
                  zaehlerauspraegung:
                    type: string
                    title: Zaehlerauspraegung
                    description: >-
                      Zaehlerauspraegung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+[ERZ|ZRZ]
                    enum:
                      - EINRICHTUNGSZAEHLER
                      - ZWEIRICHTUNGSZAEHLER
                  geraete:
                    type: array
                    items:
                      type: object
                      properties:
                        geraeteeigenschaften:
                          type: object
                          properties:
                            faktor:
                              type: number
                              description: >-
                                faktor | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZB9|ZC0].SG10.CCI+++Z25.CAV
                              format: float
                            geraetemerkmal:
                              type: string
                              title: Geraetemerkmal
                              description: >-
                                Geraetemerkmal | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZB9|ZC0].SG10.CCI+++Z25.CAV,
                                SG4.IDE+24.SG8.SEQ+[ZB7|ZB8].SG10.CCI+++Z26.CAV,
                                SG4.IDE+24.SG8.SEQ+[ZC1|ZC2].SG10.CCI+++Z27.CAV
                              enum:
                                - EINTARIF
                                - ZWEITARIF
                                - MEHRTARIF
                                - GAS_G2P5
                                - GAS_G4
                                - GAS_G6
                                - GAS_G10
                                - GAS_G16
                                - GAS_G25
                                - GAS_G40
                                - GAS_G65
                                - GAS_G100
                                - GAS_G160
                                - GAS_G250
                                - GAS_G350
                                - GAS_G400
                                - GAS_G4000
                                - GAS_G650
                                - GAS_G6500
                                - GAS_G1000
                                - GAS_G10000
                                - GAS_G12500
                                - GAS_G1600
                                - GAS_G16000
                                - GAS_G2500
                                - IMPULSGEBER_G4_G100
                                - IMPULSGEBER_G100
                                - MODEM_GSM
                                - MODEM_GPRS
                                - MODEM_FUNK
                                - MODEM_GSM_O_LG
                                - MODEM_GSM_M_LG
                                - MODEM_FESTNETZ
                                - MODEM_GPRS_M_LG
                                - PLC_COM
                                - ETHERNET_KOM
                                - DSL_KOM
                                - LTE_KOM
                                - RUNDSTEUEREMPFAENGER
                                - TARIFSCHALTGERAET
                                - ZUSTANDS_MU
                                - TEMPERATUR_MU
                                - KOMPAKT_MU
                                - SYSTEM_MU
                                - UNBESTIMMT
                                - WASSER_MWZW
                                - WASSER_WZWW
                                - WASSER_WZ01
                                - WASSER_WZ02
                                - WASSER_WZ03
                                - WASSER_WZ04
                                - WASSER_WZ05
                                - WASSER_WZ06
                                - WASSER_WZ07
                                - WASSER_WZ08
                                - WASSER_WZ09
                                - WASSER_WZ10
                                - WASSER_VWZ04
                                - WASSER_VWZ05
                                - WASSER_VWZ06
                                - WASSER_VWZ07
                                - WASSER_VWZ10
                                - DICHTEMENGENUMWERTER
                                - TEMPERATURMENGENUMWERTER
                                - ZUSTANDSMENGENUMWERTER
                                - BLOCKSTROMWANDLER
                                - MESSWANDLERSATZ_IMS_MME
                                - KOMBIMESSWANDLER
                                - SPANNUNGSWANDLER
                          x-apidog-orders:
                            - faktor
                            - geraetemerkmal
                          x-apidog-ignore-properties: []
                        geraetetyp:
                          type: string
                          title: Geraetetyp
                          description: >-
                            Auflistung möglicher abzurechnender Gerätetypen |
                            EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+[MG|Z14],
                            SG4.IDE+24.SG8.SEQ+[ZH3|ZH4].RFF+Z14,
                            SG4.IDE+24.SG8.SEQ+[ZH3|ZH4].SG10.CCI+++Z76.CAV+Z30
                          enum:
                            - WECHSELSTROMZAEHLER
                            - DREHSTROMZAEHLER
                            - ZWEIRICHTUNGSZAEHLER
                            - RLM_ZAEHLER
                            - IMS_ZAEHLER
                            - BALGENGASZAEHLER
                            - MAXIMUMZAEHLER
                            - MULTIPLEXANLAGE
                            - PAUSCHALANLAGE
                            - VERSTAERKERANLAGE
                            - SUMMATIONSGERAET
                            - IMPULSGEBER
                            - EDL_21_ZAEHLERAUFSATZ
                            - VIER_QUADRANTEN_LASTGANGZAEHLER
                            - MENGENUMWERTER
                            - STROMWANDLER
                            - SPANNUNGSWANDLER
                            - DATENLOGGER
                            - KOMMUNIKATIONSANSCHLUSS
                            - MODEM
                            - TELEKOMMUNIKATIONSEINRICHTUNG
                            - KOMMUNIKATIONSEINRICHTUNG
                            - DREHKOLBENGASZAEHLER
                            - TURBINENRADGASZAEHLER
                            - ULTRASCHALLZAEHLER
                            - WIRBELGASZAEHLER
                            - MODERNE_MESSEINRICHTUNG
                            - ELEKTRONISCHER_HAUSHALTSZAEHLER
                            - STEUEREINRICHTUNG
                            - TECHNISCHESTEUEREINRICHTUNG
                            - TARIFSCHALTGERAET
                            - RUNDSTEUEREMPFAENGER
                            - OPTIONALE_ZUS_ZAEHLEINRICHTUNG
                            - MESSWANDLERSATZ_IMS_MME
                            - KOMBIMESSWANDLER_IMS_MME
                            - TARIFSCHALTGERAET_IMS_MME
                            - RUNDSTEUEREMPFAENGER_IMS_MME
                            - TEMPERATUR_KOMPENSATION
                            - HOECHSTBELASTUNGS_ANZEIGER
                            - SONSTIGES_GERAET
                            - SMARTMETERGATEWAY
                            - STEUERBOX
                            - BLOCKSTROMWANDLER
                            - KOMBIMESSWANDLER
                            - MODEM_GSM
                            - ETHERNET_KOM
                            - PLC_COM
                            - MODEM_FESTNETZ
                            - DSL_KOM
                            - LTE_KOM
                            - DICHTEMENGENUMWERTER
                            - TEMPERATURMENGENUMWERTER
                            - ZUSTANDSMENGENUMWERTER
                            - MESSDATENREGISTRIERGERAET
                            - WANDLER
                        geraetenummer:
                          type: string
                          description: >-
                            Die auf dem Geräte aufgedruckte Nummer, die vom MSB
                            vergeben wird. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+[MG|Z14],
                            SG4.IDE+24.SG8.SEQ+[ZB9|ZC0].SG10.CCI+++Z25.CAV+Z30,
                            SG4.IDE+24.SG8.SEQ+[ZB7|ZB8].SG10.CCI+++Z26.CAV+Z30,
                            SG4.IDE+24.SG8.SEQ+[ZC1|ZC2].SG10.CCI+++Z27.CAV+Z30,
                            SG4.IDE+24.SG8.SEQ+[ZC3|ZC4].SG10.CCI+++Z75.CAV+Z30,
                            SG4.IDE+24.SG8.SEQ+[ZH3|ZH4].RFF+Z14,
                            SG4.IDE+24.SG8.SEQ+[ZH3|ZH4].SG10.CCI+++Z76.CAV+Z30
                      x-apidog-orders:
                        - geraeteeigenschaften
                        - geraetetyp
                        - geraetenummer
                      x-apidog-ignore-properties: []
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+Z39
                              properties:
                                boTyp:
                                  type: string
                                  title: BOTyp
                                  description: Typ des BO
                                  enum:
                                    - ZAEHLZEITDEFINITION
                                versionStruktur:
                                  type: string
                                  description: versionStruktur
                                  default: '1'
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                            register:
                              type: object
                              title: Zaehlzeitregister
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+Z38
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - zaehlzeitDefinition
                            - register
                          x-apidog-ignore-properties: []
                        schwachlastfaehig:
                          type: string
                          title: Schwachlastfaehig
                          description: >-
                            Schwachlastfaehig | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+Z10
                          enum:
                            - SCHWACHLASTFAEHIG
                            - NICHT_SCHWACHLASTFAEHIG
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].PIA+5
                        vorkommastelle:
                          type: integer
                          description: >-
                            vorkommastelle | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+11++Z33.CAV
                        nachkommastelle:
                          type: integer
                          description: >-
                            nachkommastelle | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+11++Z33.CAV
                        bezeichnung:
                          type: string
                          description: >-
                            Externe Bezeichnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+++Z63
                        wertegranularitaet:
                          type: string
                          title: Wertegranularitaet
                          description: >-
                            Wertegranularitaet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+++ZE4.CAV
                          enum:
                            - JAEHRLICH
                            - HALBJAEHRLICH
                            - QUARTALSWEISE
                            - MONATLICH
                        konfiguration:
                          type: string
                          title: AenderungsmoeglichkeitKonfiguration
                          description: >-
                            AenderungsmoeglichkeitKonfiguration | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+AGK
                          enum:
                            - ERFORDERLICH
                            - NICHT_ERFORDERLICH
                      x-apidog-orders:
                        - zaehlzeiten
                        - schwachlastfaehig
                        - obisKennzahl
                        - vorkommastelle
                        - nachkommastelle
                        - bezeichnung
                        - wertegranularitaet
                        - konfiguration
                      x-apidog-ignore-properties: []
                  zaehlertyp:
                    type: string
                    title: Zaehlertyp
                    description: >-
                      Zaehlertyp | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+[AHZ|WSZ|LAZ|MAZ|MME|EHZ|IVA]
                    enum:
                      - DREHSTROMZAEHLER
                      - BALGENGASZAEHLER
                      - DREHKOLBENZAEHLER
                      - SMARTMETER
                      - LEISTUNGSZAEHLER
                      - MAXIMUMZAEHLER
                      - TURBINENRADGASZAEHLER
                      - ULTRASCHALLGASZAEHLER
                      - WECHSELSTROMZAEHLER
                      - WIRBELGASZAEHLER
                      - MESSDATENREGISTRIERGERAET
                      - ELEKTRONISCHERHAUSHALTSZAEHLER
                      - SONDERAUSSTATTUNG
                      - WASSERZAEHLER
                      - MODERNEMESSEINRICHTUNG
                  zaehlertypspezifikation:
                    type: string
                    title: ZaehlertypSpezifikation
                    description: >-
                      ZaehlertypSpezifikation | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+[AHZ|WSZ|LAZ|MAZ|MME|EHZ|IVA]
                    enum:
                      - EDL40
                      - EDL21
                      - SONSTIGER_EHZ
                      - MME_STANDARD
                      - MME_MEDA
                  fernschaltung:
                    type: string
                    title: Fernschaltung
                    description: >-
                      Fernschaltung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+Z58
                    enum:
                      - VORHANDEN
                      - NICHT_VORHANDEN
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA3|ZA4],
                      SG4.IDE+24.SG8.SEQ+[ZA5|ZA6],
                      SG4.IDE+24.SG8.SEQ+[ZB9|ZC0],
                      SG4.IDE+24.SG8.SEQ+[ZB7|ZB8],
                      SG4.IDE+24.SG8.SEQ+[ZC1|ZC2],
                      SG4.IDE+24.SG8.SEQ+[ZC3|ZC4], SG4.IDE+24.SG8.SEQ+[ZH3|ZH4]
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA3|ZA4],
                          SG4.IDE+24.SG8.SEQ+[ZA5|ZA6],
                          SG4.IDE+24.SG8.SEQ+[ZB9|ZC0],
                          SG4.IDE+24.SG8.SEQ+[ZB7|ZB8],
                          SG4.IDE+24.SG8.SEQ+[ZC1|ZC2],
                          SG4.IDE+24.SG8.SEQ+[ZC3|ZC4],
                          SG4.IDE+24.SG8.SEQ+[ZH3|ZH4]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  gateway:
                    type: string
                    description: >-
                      Angabe eines SMGW, mit dem der Zaehler parametrisiert ist
                      | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].RFF+Z14,
                      SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+[MG|Z14]
                  befestigungsart:
                    type: string
                    title: Befestigungsart
                    description: >-
                      Befestigungsart von Zählern | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++Z28.CAV+[BKE|DPA|HUT]
                    enum:
                      - STECKTECHNIK
                      - DREIPUNKT
                      - HUTSCHIENE
                      - EINSTUTZEN
                      - ZWEISTUTZEN
                  zaehlernummer:
                    type: string
                    description: >-
                      Die Nummer des zu sperrenden Zählers | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+Z30,
                      SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+[MG|Z14],
                      SG4.IDE+24.SG8.SEQ+[ZB9|ZC0].RFF+MG,
                      SG4.IDE+24.SG8.SEQ+[ZB7|ZB8].RFF+MG,
                      SG4.IDE+24.SG8.SEQ+[ZC1|ZC2].RFF+MG
                  tarifart:
                    type: string
                    title: Tarifart
                    description: >-
                      Tarifart | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+[ETZ|ZTZ|NTZ
                    enum:
                      - EINTARIF
                      - ZWEITARIF
                      - MEHRTARIF
                      - SMART_METER
                      - LEISTUNGSGEMESSEN
                  messwerterfassung:
                    type: string
                    title: Messwerterfassung
                    description: >-
                      Die Messwerterfassung des Zählers | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E12.CAV+[AMR|MMR]
                    enum:
                      - FERNAUSLESBAR
                      - MANUELL_AUSGELESENE
                x-apidog-orders:
                  - zaehlerauspraegung
                  - geraete
                  - zaehlwerke
                  - zaehlertyp
                  - zaehlertypspezifikation
                  - fernschaltung
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - gateway
                  - befestigungsart
                  - zaehlernummer
                  - tarifart
                  - messwerterfassung
                x-apidog-ignore-properties: []
            MESSSTELLENBETRIEBSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  korrespondenzpartner:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z41|Z42]
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]'
                          postleitzahl:
                            type: string
                            description: >-
                              Postleitzahl | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z41|Z42]
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]'
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z41|Z42]
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
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]'
                        x-apidog-orders:
                          - hausnummer
                          - ortsteil
                          - postleitzahl
                          - strasse
                          - postfach
                          - landescode
                          - ort
                        x-apidog-ignore-properties: []
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]'
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z41|Z42]
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z41|Z42]
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]
                    x-apidog-orders:
                      - partneradresse
                      - name1
                      - name4
                      - anrede
                      - name2
                      - name3
                    x-apidog-ignore-properties: []
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z39|Z40]'
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen

                            beispielsweise der Nachname dargestellt werden.
                            Beispiele: Yellow Strom GmbH

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z39|Z40]
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z39|Z40]
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z39|Z40]
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z39|Z40]
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z39|Z40]
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
                      x-apidog-orders:
                        - name4
                        - name1
                        - name2
                        - name3
                        - anrede
                        - geschaeftspartnerrolle
                      x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z39|Z40].RFF+Z46,
                          SG4.IDE+24.SG12.NAD+[Z41|Z42].RFF+Z46
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG12.NAD+[Z39|Z40],
                      SG4.IDE+24.SG12.NAD+[Z41|Z42]
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
                x-apidog-orders:
                  - korrespondenzpartner
                  - vertragspartner2
                  - gueltigkeitszeitraum
                  - datenqualitaet
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                x-apidog-orders:
                  - zeitraumId
                  - verwendungBis
                  - verwendungAb
                  - datenqualitaet
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MESSLOKATION
            - ZAEHLER
            - MESSSTELLENBETRIEBSVERTRAG
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                  x-apidog-orders:
                    - eMailAdresse
                    - nachname
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - liste
                  - code
                  - zeitraumId
                x-apidog-ignore-properties: []
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - empfaenger
            - anfragereferenznummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - antwortStatusZeitraum
            - transaktionsgrund
            - pruefidentifikator
            - dokumentennummer
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55669 - weiterer MSB an MSB - Bestellung einer Änderung von Stammdaten
        vom weiteren MSB an MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55666:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++[ZA7|ZA8]'
                    enum:
                      - NB
                      - LF
                      - MSB
                      - MSBA
                      - GMSB
                      - MDL
                      - DL
                      - BKV
                      - BKO
                      - UENB
                      - KUNDE-SELBST-NN
                      - MGV
                      - EIV
                      - RB
                      - KUNDE
                      - INTERESSENT
                      - KN
                      - UBA
                      - BIKO
                      - ESA
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2],
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  zugeordneteDefinition:
                    type: object
                    properties:
                      schaltzeitdefinition:
                        type: object
                        title: Schaltzeitdefinition
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+[Z52|Z53]
                        properties:
                          boTyp:
                            type: string
                            title: BOTyp
                            description: Typ des BO
                            enum:
                              - SCHALTZEITDEFINITION
                          versionStruktur:
                            type: string
                            description: versionStruktur
                            default: '1'
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                      leistungskurvendefinition:
                        type: object
                        title: Leistungskurvendefinition
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+[Z52|Z53]
                        properties:
                          boTyp:
                            type: string
                            title: BOTyp
                            description: Typ des BO
                            enum:
                              - LEISTUNGSKURVENDEFINITION
                          versionStruktur:
                            type: string
                            description: versionStruktur
                            default: '1'
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - schaltzeitdefinition
                      - leistungskurvendefinition
                    x-apidog-ignore-properties: []
                  auftraggebenderMarktpartner:
                    type: object
                    properties:
                      rollencodenummer:
                        type: string
                        description: >-
                          Gibt die Codenummer der Marktrolle an. | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                      marktrolle:
                        type: string
                        title: Marktrolle
                        description: >-
                          Diese Rollen kann ein Marktteilnehmer einnehmen |
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                        enum:
                          - NB
                          - LF
                          - MSB
                          - MSBA
                          - GMSB
                          - MDL
                          - DL
                          - BKV
                          - BKO
                          - UENB
                          - KUNDE-SELBST-NN
                          - MGV
                          - EIV
                          - RB
                          - KUNDE
                          - INTERESSENT
                          - KN
                          - UBA
                          - BIKO
                          - ESA
                    x-apidog-orders:
                      - rollencodenummer
                      - marktrolle
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2],
                      SG4.IDE+24.SG8.SEQ+[ZB3|ZB4]
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
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].PIA+5
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                  steuerkanal:
                    type: object
                    title: AdHocSteuerkanal
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2].SG10.CCI+Z49.CAV+ZF2'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - AD_HOC_STEUERKANAL
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - produktdatenRelevanteRolle
                  - gueltigkeitszeitraum
                  - zugeordneteDefinition
                  - auftraggebenderMarktpartner
                  - datenqualitaet
                  - konfigurationsprodukt
                  - ressourcenId
                  - steuerkanal
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - STEUERBARE_RESSOURCE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55666 - weiterer MSB an MSB - Bestellung einer Änderung von Stammdaten
        vom weiteren MSB an MSB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55667:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+[Z99|ZA0].SG10.CCI+++ZA8.CAV,
                                    SG4.IDE+24.SG8.SEQ+[Z99|ZA0].SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[Z99|ZA0].SG10.CCI+++ZA8.CAV,
                                  SG4.IDE+24.SG8.SEQ+[Z99|ZA0].SG10.CCI+++ZA7.CAV
                                enum:
                                  - NB
                                  - LF
                                  - MSB
                                  - MSBA
                                  - GMSB
                                  - MDL
                                  - DL
                                  - BKV
                                  - BKO
                                  - UENB
                                  - KUNDE-SELBST-NN
                                  - MGV
                                  - EIV
                                  - RB
                                  - KUNDE
                                  - INTERESSENT
                                  - KN
                                  - UBA
                                  - BIKO
                                  - ESA
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z99|ZA0].PIA+5
                      x-apidog-orders:
                        - verwendungszwecke
                        - obisKennzahl
                      x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z99|ZA0]'
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
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z99|ZA0]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zaehlwerke
                  - datenqualitaet
                  - tranchenId
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - TRANCHE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55667 - weiterer MSB an MSB - Bestellung einer Änderung von Stammdaten
        vom weiteren MSB an MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55665:
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
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].PIA+5
                        wertegranularitaet:
                          type: string
                          title: Wertegranularitaet
                          description: >-
                            Wertegranularitaet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZE4.CAV+[ZD9|ZE8|ZE9|ZB7]
                          enum:
                            - JAEHRLICH
                            - HALBJAEHRLICH
                            - QUARTALSWEISE
                            - MONATLICH
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+Z39
                              properties:
                                boTyp:
                                  type: string
                                  title: BOTyp
                                  description: Typ des BO
                                  enum:
                                    - ZAEHLZEITDEFINITION
                                versionStruktur:
                                  type: string
                                  description: versionStruktur
                                  default: '1'
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                            register:
                              type: object
                              title: Zaehlzeitregister
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+Z38
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - zaehlzeitDefinition
                            - register
                          x-apidog-ignore-properties: []
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZA8.CAV,
                                    SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZA8.CAV,
                                  SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZA7.CAV
                                enum:
                                  - NB
                                  - LF
                                  - MSB
                                  - MSBA
                                  - GMSB
                                  - MDL
                                  - DL
                                  - BKV
                                  - BKO
                                  - UENB
                                  - KUNDE-SELBST-NN
                                  - MGV
                                  - EIV
                                  - RB
                                  - KUNDE
                                  - INTERESSENT
                                  - KN
                                  - UBA
                                  - BIKO
                                  - ESA
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - obisKennzahl
                        - wertegranularitaet
                        - zaehlzeiten
                        - verwendungszwecke
                      x-apidog-ignore-properties: []
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z51|Z52],
                      SG4.IDE+24.SG8.SEQ+[ZA1|ZA2], SG4.IDE+24.SG8.SEQ+[ZB5|ZB6]
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z51|Z52],
                          SG4.IDE+24.SG8.SEQ+[ZA1|ZA2],
                          SG4.IDE+24.SG8.SEQ+[ZB5|ZB6]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+++[ZA7|ZA8]'
                    enum:
                      - NB
                      - LF
                      - MSB
                      - MSBA
                      - GMSB
                      - MDL
                      - DL
                      - BKV
                      - BKO
                      - UENB
                      - KUNDE-SELBST-NN
                      - MGV
                      - EIV
                      - RB
                      - KUNDE
                      - INTERESSENT
                      - KN
                      - UBA
                      - BIKO
                      - ESA
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].PIA+5,
                      SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+11
                  leistungskurvendefinition:
                    type: object
                    title: Leistungskurvendefinition
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+Z53'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - LEISTUNGSKURVENDEFINITION
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zaehlwerke
                  - marktlokationsId
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - produktdatenRelevanteRolle
                  - konfigurationsprodukt
                  - leistungskurvendefinition
                x-apidog-ignore-properties: []
            MESSSTELLENBETRIEBSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragskonditionen:
                    type: object
                    properties:
                      geplanteTurnusablesung:
                        type: object
                        properties:
                          ableseZeitraum:
                            type: string
                            description: >-
                              ableseZeitraum | EDIFACT:
                              SG4.IDE+24.SG6.RFF+[Z51|Z52].DTM+752
                        x-apidog-orders:
                          - ableseZeitraum
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - geplanteTurnusablesung
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragskonditionen
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - MESSSTELLENBETRIEBSVERTRAG
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55665 - weiterer MSB an MSB - Bestellung einer Änderung von Stammdaten
        vom weiteren MSB an MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55664:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  auftraggebenderMarktpartner:
                    type: object
                    properties:
                      marktrolle:
                        type: string
                        title: Marktrolle
                        description: >-
                          Diese Rollen kann ein Marktteilnehmer einnehmen |
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                        enum:
                          - NB
                          - LF
                          - MSB
                          - MSBA
                          - GMSB
                          - MDL
                          - DL
                          - BKV
                          - BKO
                          - UENB
                          - KUNDE-SELBST-NN
                          - MGV
                          - EIV
                          - RB
                          - KUNDE
                          - INTERESSENT
                          - KN
                          - UBA
                          - BIKO
                          - ESA
                      rollencodenummer:
                        type: string
                        description: >-
                          Gibt die Codenummer der Marktrolle an. | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                    x-apidog-orders:
                      - marktrolle
                      - rollencodenummer
                    x-apidog-ignore-properties: []
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].PIA+5
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].SG10.CCI+++ZA8.CAV,
                                    SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].SG10.CCI+++ZA8.CAV,
                                  SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].SG10.CCI+++ZA7.CAV
                                enum:
                                  - NB
                                  - LF
                                  - MSB
                                  - MSBA
                                  - GMSB
                                  - MDL
                                  - DL
                                  - BKV
                                  - BKO
                                  - UENB
                                  - KUNDE-SELBST-NN
                                  - MGV
                                  - EIV
                                  - RB
                                  - KUNDE
                                  - INTERESSENT
                                  - KN
                                  - UBA
                                  - BIKO
                                  - ESA
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - obisKennzahl
                        - verwendungszwecke
                      x-apidog-ignore-properties: []
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++ZA7'
                    enum:
                      - NB
                      - LF
                      - MSB
                      - MSBA
                      - GMSB
                      - MDL
                      - DL
                      - BKV
                      - BKO
                      - UENB
                      - KUNDE-SELBST-NN
                      - MGV
                      - EIV
                      - RB
                      - KUNDE
                      - INTERESSENT
                      - KN
                      - UBA
                      - BIKO
                      - ESA
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0],
                          SG4.IDE+24.SG8.SEQ+[ZA7|ZA8],
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  steuerkanal:
                    type: object
                    title: AdHocSteuerkanal
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0].SG10.CCI+Z49'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - AD_HOC_STEUERKANAL
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18
                  keinKonfigurationsprodukt:
                    type: boolean
                    description: >-
                      keinKonfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+11
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0],
                      SG4.IDE+24.SG8.SEQ+[ZA7|ZA8], SG4.IDE+24.SG8.SEQ+[ZG8|ZG9]
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
                  leistungskurvendefinition:
                    type: object
                    title: Leistungskurvendefinition
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+Z53'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - LEISTUNGSKURVENDEFINITION
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].PIA+5
                x-apidog-orders:
                  - auftraggebenderMarktpartner
                  - zaehlwerke
                  - produktdatenRelevanteRolle
                  - gueltigkeitszeitraum
                  - steuerkanal
                  - netzlokationsId
                  - keinKonfigurationsprodukt
                  - datenqualitaet
                  - leistungskurvendefinition
                  - konfigurationsprodukt
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55664 - weiterer MSB an MSB - Bestellung einer Änderung von Stammdaten
        vom weiteren MSB an MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_21047:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            vorgangsreferenznummer:
              type: string
              description: >-
                Referenznummer des Vorgangs der Anmeldung nach WiM / ORDERS
                RFF+Z41 / IFTSTA RFF+ACW | EDIFACT:
                SG14.CNI.SG15.STS+Z43.RFF+ACW
            absender:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG1.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG1.NAD+MS.SG2.CTA+IC
                  x-apidog-orders:
                    - nachname
                  x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG1.NAD+MS'
              x-apidog-orders:
                - rollencodetyp
                - ansprechpartner
                - rollencodenummer
              x-apidog-ignore-properties: []
            antwortstatusCodeliste:
              type: string
              description: >-
                Antwortstatus Codeliste / STS+E01 | EDIFACT:
                SG14.CNI.SG15.STS+Z43
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            empfaenger:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG1.NAD+MR'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG1.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            transaktionsdaten:
              type: object
              properties:
                absender:
                  type: object
                  properties:
                    ansprechpartner:
                      type: object
                      properties:
                        rufnummern:
                          type: array
                          items:
                            type: object
                            properties:
                              rufnummer:
                                type: object
                                title: Rufnummer
                                description: >-
                                  EDIFACT:
                                  SG1.NAD+MS.SG2.CTA+IC.COM+[EM|FX|TE|AJ|AL]
                                x-apidog-orders: []
                                properties: {}
                                x-apidog-ignore-properties: []
                              nummerntyp:
                                type: string
                                title: Rufnummernart
                                description: >-
                                  EDIFACT:
                                  SG1.NAD+MS.SG2.CTA+IC.COM+[EM|FX|TE|AJ|AL]
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
                        eMailAdresse:
                          type: string
                          description: >-
                            E-Mail Adresse | EDIFACT:
                            SG1.NAD+MS.SG2.CTA+IC.COM+[EM|FX|TE|AJ|AL]
                      x-apidog-orders:
                        - rufnummern
                        - eMailAdresse
                      x-apidog-ignore-properties: []
                  x-apidog-orders:
                    - ansprechpartner
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - absender
              x-apidog-ignore-properties: []
            sendungsposition:
              type: string
              description: 'Sendungsposition / GID | EDIFACT: SG14.CNI.SG15.STS+Z43.SG25.GID'
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+Z33'
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG14.CNI.SG15.STS+Z43.RFF+Z13
            antwortstatus:
              type: string
              description: 'Antwortstatus / STS+E01 | EDIFACT: SG14.CNI.SG15.STS+Z43'
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
          x-apidog-orders:
            - vorgangsreferenznummer
            - absender
            - antwortstatusCodeliste
            - nachrichtendatum
            - empfaenger
            - transaktionsdaten
            - sendungsposition
            - dokumentennummer
            - pruefidentifikator
            - antwortstatus
            - nachrichtenreferenznummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            STATUSMITTEILUNG:
              type: array
              items:
                type: object
                properties:
                  auftragsstatus:
                    type: string
                    title: Auftragsstatus
                    description: 'Auftragsstatus | EDIFACT: SG14.CNI.SG15.STS+Z43'
                    enum:
                      - GESCHEITERT
                      - ERFOLGREICH
                      - LIEFERUNG_GEPLANT
                      - GEPLANT
                      - ZUGESTIMMT
                      - WIDERSPROCHEN
                      - STOERUNGSFREI
                      - GESTOERT
                      - FESTGESTELLTE_STOERUNG
                      - VERMUTETE_STOERUNG
                      - ABGELEHNT
                      - BEENDET
                      - ANTWORT_DRITTER
                      - BESTAETIGT
                      - UMGESETZT
                      - ENFG_STROMSPEICHER_UND_VERLUSTENERGIE
                      - ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
                      - >-
                        ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN
                      - ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF
                      - ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN
                      - >-
                        ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN
                      - ENFG_SCHIENENBAHNEN
                      - ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR
                      - ENFG_LANDSTROMANLAGEN
                      - AENDERUNG_DER_DATEN
                      - KEINE_AENDERUNG_DER_DATEN
                  positionsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        allgemeineInformationen:
                          type: object
                          properties:
                            info3:
                              type: string
                              description: >-
                                Allgemeine Info 3 | EDIFACT:
                                SG14.CNI.SG15.STS+Z43.SG25.GID.FTX+ACB
                            info1:
                              type: string
                              description: >-
                                Allgemeine Info 1 | EDIFACT:
                                SG14.CNI.SG15.STS+Z43.SG25.GID.FTX+ACB
                            info2:
                              type: string
                              description: >-
                                Allgemeine Info 2 | EDIFACT:
                                SG14.CNI.SG15.STS+Z43.SG25.GID.FTX+ACB
                            info4:
                              type: string
                              description: >-
                                Allgemeine Info 4 | EDIFACT:
                                SG14.CNI.SG15.STS+Z43.SG25.GID.FTX+ACB
                            info5:
                              type: string
                              description: >-
                                Allgemeine Info 5 | EDIFACT:
                                SG14.CNI.SG15.STS+Z43.SG25.GID.FTX+ACB
                          x-apidog-orders:
                            - info3
                            - info1
                            - info2
                            - info4
                            - info5
                          x-apidog-ignore-properties: []
                        positionsnummer:
                          type: integer
                          description: 'Positionsnummer / LIN | EDIFACT: SG14.CNI'
                      x-apidog-orders:
                        - allgemeineInformationen
                        - positionsnummer
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - auftragsstatus
                  - positionsdaten
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - STATUSMITTEILUNG
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 21047 - NB an ÜNB - Bearbeitungsstand zur Rückmeldung
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55177:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - vorgangsnummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
          x-apidog-ignore-properties: []
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
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16,
                      SG4.IDE+24.SG5.LOC+Z22
                x-apidog-orders:
                  - marktlokationsId
                x-apidog-ignore-properties: []
            LOKATIONSBUENDEL:
              type: array
              items:
                type: object
                properties:
                  lokationsbuendelNummer:
                    type: integer
                    description: >-
                      lokationsbuendelNummer | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZC7|ZC8].RFF+[Z31|Z39]
                  lokationsbuendelstrukturId:
                    type: string
                    description: >-
                      lokationsbuendelstrukturId | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZC7|ZC8].RFF+[Z31|Z39]
                  standardisierteLokationsbuendelstruktur:
                    type: boolean
                    description: >-
                      standardisierteLokationsbuendelstruktur | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZC7|ZC8].RFF+[Z31|Z39]
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZC7|ZC8],
                      SG4.IDE+24.SG8.SEQ+[ZC9|ZD0]
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZC7|ZC8],
                          SG4.IDE+24.SG8.SEQ+[ZC9|ZD0]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - lokationsbuendelNummer
                  - lokationsbuendelstrukturId
                  - standardisierteLokationsbuendelstruktur
                  - datenqualitaet
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
              properties:
                zuordnungObjectcode:
                  type: array
                  items:
                    type: object
                    properties:
                      objectcode:
                        type: array
                        items:
                          type: object
                          properties:
                            lokationsbuendelNummer:
                              type: integer
                              description: >-
                                lokationsbuendelNummer | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+Z33
                            objectcode:
                              type: object
                              title: Objectcode
                              description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+Z33'
                              x-apidog-orders: []
                          x-apidog-orders:
                            - lokationsbuendelNummer
                            - objectcode
                      vorgelagerteLokationId:
                        type: string
                        description: >-
                          vorgelagerteLokationId | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+[Z34|Z35]
                      referenzMarktlokationTechnischeRessource:
                        type: array
                        items:
                          type: array
                          description: >-
                            referenzMarktlokationTechnischeRessource | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+Z16
                          items:
                            type: string
                      referenzLokationsTyp:
                        type: string
                        title: Lokationstyp
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+[Z32|Z18|Z19|Z37]
                        enum:
                          - MALO
                          - MELO
                          - NELO
                          - TECHNISCHE_RESSOURCE
                      vorgelagerteLokationTyp:
                        type: string
                        title: Lokationstyp
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+[Z34|Z35]'
                        enum:
                          - MALO
                          - MELO
                          - NELO
                          - TECHNISCHE_RESSOURCE
                      referenzLokationsId:
                        type: string
                        description: >-
                          referenzLokationsId | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+[Z32|Z18|Z19|Z37]
                    x-apidog-orders:
                      - objectcode
                      - vorgelagerteLokationId
                      - referenzMarktlokationTechnischeRessource
                      - referenzLokationsTyp
                      - vorgelagerteLokationTyp
                      - referenzLokationsId
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18
                x-apidog-orders:
                  - netzlokationsId
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
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
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
            - LOKATIONSBUENDEL
            - NETZLOKATION
            - STEUERBARE_RESSOURCE
            - VERWENDUNGSZEITRAUM
            - MESSLOKATION
            - TECHNISCHE_RESSOURCE
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55177 - MSB an NB - Bestellung einer Änderung von Stammdaten vom MSB an
        NB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55638:
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
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+ZF0
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+Z91
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+ZF0
                          enum:
                            - NB
                            - LF
                            - MSB
                            - MSBA
                            - GMSB
                            - MDL
                            - DL
                            - BKV
                            - BKO
                            - UENB
                            - KUNDE-SELBST-NN
                            - MGV
                            - EIV
                            - RB
                            - KUNDE
                            - INTERESSENT
                            - KN
                            - UBA
                            - BIKO
                            - ESA
                      x-apidog-orders:
                        - rollencodenummer
                        - weiterverpflichtet
                        - messstellenbetreiberEigenschaft
                        - marktrolle
                      x-apidog-ignore-properties: []
                  betriebszustand:
                    type: string
                    title: Betriebszustand
                    description: >-
                      Betriebszustand | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+Z32
                    enum:
                      - GESPERRT_NICHT_ENTSPERREN
                      - GESPERRT
                      - REGELBETRIEB
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG6|ZG7]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  messlokationsId:
                    type: string
                    description: >-
                      Die Messlokations-Identifikation. Das ist die frühere
                      Zählpunktbezeichnung,

                      z.B. DE 47108151234567 | EDIFACT: SG4.IDE+24.SG5.LOC+Z17
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG6|ZG7]'
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
                x-apidog-orders:
                  - marktrollen
                  - betriebszustand
                  - gueltigkeitszeitraum
                  - messlokationsId
                  - datenqualitaet
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MESSLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55638 - MSB an NB - Bestellung einer Änderung von Stammdaten vom MSB an
        NB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55636:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2]'
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
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZB1|ZB2].SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - NB
                            - LF
                            - MSB
                            - MSBA
                            - GMSB
                            - MDL
                            - DL
                            - BKV
                            - BKO
                            - UENB
                            - KUNDE-SELBST-NN
                            - MGV
                            - EIV
                            - RB
                            - KUNDE
                            - INTERESSENT
                            - KN
                            - UBA
                            - BIKO
                            - ESA
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZB1|ZB2].SG10.CCI+++ZB3.CAV+Z91
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZB1|ZB2].SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                      x-apidog-orders:
                        - marktrolle
                        - rollencodenummer
                        - messstellenbetreiberEigenschaft
                      x-apidog-ignore-properties: []
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                x-apidog-orders:
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                  - ressourcenId
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - STEUERBARE_RESSOURCE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55636 - MSB an NB - Bestellung einer Änderung von Stammdaten vom MSB an
        NB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55635:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - vorgangsnummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            TECHNISCHE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  weitereEinrichtung:
                    type: boolean
                    description: >-
                      weitereEinrichtung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+Z63.CAV+[ZH7|ZH8]
                  nennleistung:
                    type: object
                    properties:
                      aufnahme:
                        type: number
                        description: >-
                          Aufnahme der Nennleistung | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG9.QTY+Z43
                        format: float
                      abgabe:
                        type: object
                        title: Konzessionsabgabe
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG9.QTY+Z44'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - aufnahme
                      - abgabe
                    x-apidog-ignore-properties: []
                  referenzNetzlokation:
                    type: string
                    description: >-
                      referenzNetzlokation | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].RFF+Z32
                  speicherkapazitaet:
                    type: number
                    description: >-
                      Speicherkapazität

                      Beispiel: QTY+Z42:100:KWH' | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG9.QTY+Z42
                    format: float
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG4|ZG5]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  erzeugungsart:
                    type: string
                    title: Erzeugungsart
                    description: >-
                      Auflistung der Erzeugungsarten von Energie. | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56].CAV+[ZF5|ZF6|ZG0|ZG1|ZG5]
                    enum:
                      - EEG
                      - KWK
                      - EEG_DV
                      - KWK_DV
                      - WIND
                      - SOLAR
                      - KERNKRAFT
                      - WASSER
                      - GEOTHERMIE
                      - BIOMASSE
                      - KOHLE
                      - GAS
                      - SONSTIGE
                      - SONSTIGE_EEG
                      - SONSTIGE_ERZEUGUNGSART
                  referenzSteuerbareRessource:
                    type: string
                    description: >-
                      referenzSteuerbareRessource | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].RFF+Z38
                  speicherart:
                    type: string
                    title: Speicherart
                    description: >-
                      Speicherart | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56].CAV+[ZF7|ZF8|ZF9|ZG6]
                    enum:
                      - WASSERSTOFFSPEICHER
                      - PUMPSPEICHER
                      - BATTERIESPEICHER
                      - SONSTIGE_SPEICHERART
                  art:
                    type: string
                    title: AbgabeArt
                    description: >-
                      Art der Konzessionsabgabe | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56]
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
                  waermenutzung:
                    type: string
                    title: Waermenutzung
                    description: >-
                      Waermenutzung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56].CAV
                    enum:
                      - SPEICHERHEIZUNG
                      - WAERMEPUMPE
                      - DIREKTHEIZUNG
                      - WAERMEPUMPE_WAERME_KAELTE
                      - WAERMEPUMPE_KAELTE
                      - WAERMEPUMPE_WAERME
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG4|ZG5]'
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
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z20'
                  verbrauchsart:
                    type: string
                    title: Verbrauchsart
                    description: >-
                      Verbrauchsart | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56].CAV+[Z64|Z65|ZE5|ZA8]
                    enum:
                      - KL
                      - W
                      - EMOB
                      - SB
                      - SW
                      - WK
                x-apidog-orders:
                  - weitereEinrichtung
                  - nennleistung
                  - referenzNetzlokation
                  - speicherkapazitaet
                  - gueltigkeitszeitraum
                  - erzeugungsart
                  - referenzSteuerbareRessource
                  - speicherart
                  - art
                  - waermenutzung
                  - datenqualitaet
                  - ressourcenId
                  - verbrauchsart
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - TECHNISCHE_RESSOURCE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55635 - MSB an NB - Bestellung einer Änderung von Stammdaten vom MSB an
        NB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55634:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
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

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z51|Z52]
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z51|Z52]
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z51|Z52]
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
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z51|Z52]
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z51|Z52]'
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z51|Z52]
                      x-apidog-orders:
                        - name1
                        - anrede
                        - geschaeftspartnerrolle
                        - name3
                        - name4
                        - name2
                      x-apidog-ignore-properties: []
                  korrespondenzpartner:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]'
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]'
                          postleitzahl:
                            type: string
                            description: >-
                              Postleitzahl | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z53|Z54]
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z53|Z54]
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
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]'
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z53|Z54]
                        x-apidog-orders:
                          - postfach
                          - ortsteil
                          - postleitzahl
                          - landescode
                          - ort
                          - strasse
                          - hausnummer
                        x-apidog-ignore-properties: []
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z53|Z54]
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z53|Z54]
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]'
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]
                    x-apidog-orders:
                      - partneradresse
                      - name2
                      - anrede
                      - name4
                      - name3
                      - name1
                    x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z51|Z52].RFF+Z46,
                          SG4.IDE+24.SG12.NAD+[Z53|Z54].RFF+Z46
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG12.NAD+[Z51|Z52],
                      SG4.IDE+24.SG12.NAD+[Z53|Z54]
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
                x-apidog-orders:
                  - vertragspartner2
                  - korrespondenzpartner
                  - gueltigkeitszeitraum
                  - datenqualitaet
                x-apidog-ignore-properties: []
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  lastprofile:
                    type: array
                    items:
                      type: object
                      properties:
                        bezeichnung:
                          type: string
                          description: >-
                            Externe Bezeichnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z85|Z86].SG10.CCI+[Z02|Z04]].CAV,
                            SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+[Z03|Z05].CAV
                        referenzprofilbezeichnung:
                          type: string
                          description: >-
                            Bezeichnung des Referenzprofils | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z89|Z90].SG10.CCI+Z05.CAV
                        verfahren:
                          type: string
                          title: Profilverfahren
                          description: >-
                            Profilverfahren | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z85|Z86].SG10.CCI+[Z02|Z04]],
                            SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+[Z03|Z05]
                          enum:
                            - SYNTHETISCH
                            - ANALYTISCH
                        einspeisung:
                          type: boolean
                          description: >-
                            Kennzeichen Einspeisung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z85|Z86].SG10.CCI+[Z02|Z04]],
                            SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+[Z03|Z05]
                        profilart:
                          type: string
                          title: Profilart
                          description: >-
                            Profilart | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z85|Z86].SG10.CCI+[Z02|Z04]],
                            SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+[Z03|Z05]
                          enum:
                            - ART_STANDARDLASTPROFIL
                            - ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL
                            - ART_LASTPROFIL
                      x-apidog-orders:
                        - bezeichnung
                        - referenzprofilbezeichnung
                        - verfahren
                        - einspeisung
                        - profilart
                      x-apidog-ignore-properties: []
                  prognosegrundlage:
                    type: string
                    title: Prognosegrundlage
                    description: >-
                      Prognosegrundlage | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI
                    enum:
                      - WERTE
                      - PROFILE
                  temperaturarbeit:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG9.QTY+[Z10|265|Z08]
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG9.QTY+[Z10|265|Z08]
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
                    x-apidog-orders:
                      - wert
                      - einheit
                    x-apidog-ignore-properties: []
                  jahresverbrauchsprognose:
                    type: object
                    properties:
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG9.QTY+31
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
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG9.QTY+31'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - einheit
                      - wert
                    x-apidog-ignore-properties: []
                  abwicklungsmodell:
                    type: string
                    title: Abwicklungsmodell
                    description: >-
                      Abwicklungsmodell | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+ZA2++[ZE9|ZF0]
                    enum:
                      - MODELL_1_BILANZIERUNG_AN_MARKTLOKATION
                      - MODELL_2_BILANZIERUNG_IM_BILANZIERUNGSGEBIET
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z85|Z86],
                          SG4.IDE+24.SG8.SEQ+[Z87|Z88],
                          SG4.IDE+24.SG8.SEQ+[Z89|Z90]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z85|Z86],
                      SG4.IDE+24.SG8.SEQ+[Z87|Z88], SG4.IDE+24.SG8.SEQ+[Z89|Z90]
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
                  detailsPrognosegrundlage:
                    type: array
                    items:
                      type: array
                      description: >-
                        Prognosegrundlage - Besteht der Bedarf ein
                        tagesparameteräbhängiges Lastprofil mit gemeinsamer
                        Messung anzugeben, so ist dies über die 2 -malige
                        Wiederholung des CAV Segments mit der Angabe der Codes
                        E02 und E14 möglich. | EDIFACT:
                        SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI.CAV+[E02|E14|Z36]
                      items:
                        type: string
                        title: Profiltyp
                        description: Profiltyp
                        enum:
                          - SLP_SEP
                          - TLP_TEP
                          - TEP
                x-apidog-orders:
                  - lastprofile
                  - prognosegrundlage
                  - temperaturarbeit
                  - jahresverbrauchsprognose
                  - abwicklungsmodell
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - detailsPrognosegrundlage
                x-apidog-ignore-properties: []
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
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z80|Z81],
                      SG4.IDE+24.SG12.NAD+[Z55|Z56],
                      SG4.IDE+24.SG12.NAD+[Z57|Z58]
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
                  hausverwalter:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z57|Z58]'
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z57|Z58]
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
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z57|Z58]'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z57|Z58]'
                          postleitzahl:
                            type: string
                            description: >-
                              Postleitzahl | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z57|Z58]
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z57|Z58]
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z57|Z58]'
                        x-apidog-orders:
                          - ortsteil
                          - landescode
                          - strasse
                          - postfach
                          - postleitzahl
                          - hausnummer
                          - ort
                        x-apidog-ignore-properties: []
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z57|Z58]
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z57|Z58]'
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z57|Z58]
                      gewerbekennzeichnung:
                        type: boolean
                        description: >-
                          Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
                          (gewerbeKennzeichnung = true)

                          oder eine Privatperson handelt. (gewerbeKennzeichnung
                          = false) | EDIFACT: SG4.IDE+24.SG12.NAD+[Z57|Z58]
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z57|Z58]
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+[Z57|Z58]
                    x-apidog-orders:
                      - partneradresse
                      - name1
                      - name4
                      - anrede
                      - gewerbekennzeichnung
                      - name2
                      - name3
                    x-apidog-ignore-properties: []
                  eigentuemer:
                    type: object
                    properties:
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]'
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z55|Z56]
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]
                      partneradresse:
                        type: object
                        properties:
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]'
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]'
                          postleitzahl:
                            type: string
                            description: >-
                              Postleitzahl | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z55|Z56]
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z55|Z56]
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z55|Z56]
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
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]'
                        x-apidog-orders:
                          - strasse
                          - postfach
                          - ort
                          - postleitzahl
                          - hausnummer
                          - landescode
                          - ortsteil
                        x-apidog-ignore-properties: []
                      gewerbekennzeichnung:
                        type: boolean
                        description: >-
                          Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
                          (gewerbeKennzeichnung = true)

                          oder eine Privatperson handelt. (gewerbeKennzeichnung
                          = false) | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z55|Z56]
                    x-apidog-orders:
                      - name3
                      - name4
                      - name2
                      - name1
                      - partneradresse
                      - gewerbekennzeichnung
                      - anrede
                    x-apidog-ignore-properties: []
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z91
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z90,
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - NB
                            - LF
                            - MSB
                            - MSBA
                            - GMSB
                            - MDL
                            - DL
                            - BKV
                            - BKO
                            - UENB
                            - KUNDE-SELBST-NN
                            - MGV
                            - EIV
                            - RB
                            - KUNDE
                            - INTERESSENT
                            - KN
                            - UBA
                            - BIKO
                            - ESA
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z90,
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z91
                      x-apidog-orders:
                        - messstellenbetreiberEigenschaft
                        - weiterverpflichtet
                        - marktrolle
                        - rollencodenummer
                      x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z80|Z81],
                          SG4.IDE+24.SG12.NAD+[Z55|Z56].RFF+Z46,
                          SG4.IDE+24.SG12.NAD+[Z57|Z58].RFF+Z46
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  energieherkunft:
                    type: array
                    items:
                      type: object
                      properties:
                        erzeugungsart:
                          type: string
                          title: Erzeugungsart
                          description: >-
                            Auflistung der Erzeugungsarten von Energie. |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++Z34.CAV
                          enum:
                            - EEG
                            - KWK
                            - EEG_DV
                            - KWK_DV
                            - WIND
                            - SOLAR
                            - KERNKRAFT
                            - WASSER
                            - GEOTHERMIE
                            - BIOMASSE
                            - KOHLE
                            - GAS
                            - SONSTIGE
                            - SONSTIGE_EEG
                            - SONSTIGE_ERZEUGUNGSART
                      x-apidog-orders:
                        - erzeugungsart
                      x-apidog-ignore-properties: []
                  messtechnischeEinordnung:
                    type: string
                    title: MesstechnischeEinordnung
                    description: >-
                      MesstechnischeEinordnung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++Z83.CAV
                    enum:
                      - IMS
                      - KME_MME
                      - KEINE_MESSUNG
                  netzebene:
                    type: string
                    title: Netzebene
                    description: >-
                      Netzebene | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++E03.CAV
                    enum:
                      - NSP
                      - MSP
                      - HSP
                      - HSS
                      - MSP_NSP_UMSP
                      - HSP_MSP_UMSP
                      - HSS_HSP_UMSP
                      - HD
                      - MD
                      - ND
                x-apidog-orders:
                  - marktlokationsId
                  - datenqualitaet
                  - hausverwalter
                  - eigentuemer
                  - marktrollen
                  - gueltigkeitszeitraum
                  - energieherkunft
                  - messtechnischeEinordnung
                  - netzebene
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                x-apidog-orders:
                  - zeitraumId
                  - verwendungBis
                  - verwendungAb
                  - datenqualitaet
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZNUTZUNGSVERTRAG
            - BILANZIERUNG
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                  x-apidog-orders:
                    - eMailAdresse
                    - nachname
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - liste
                  - code
                  - zeitraumId
                x-apidog-ignore-properties: []
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - empfaenger
            - anfragereferenznummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - antwortStatusZeitraum
            - transaktionsgrund
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - dokumentennummer
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55634 - MSB an NB - Bestellung einer Änderung von Stammdaten vom MSB an
        NB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55633:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA9|ZB0].SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA9|ZB0].SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - NB
                            - LF
                            - MSB
                            - MSBA
                            - GMSB
                            - MDL
                            - DL
                            - BKV
                            - BKO
                            - UENB
                            - KUNDE-SELBST-NN
                            - MGV
                            - EIV
                            - RB
                            - KUNDE
                            - INTERESSENT
                            - KN
                            - UBA
                            - BIKO
                            - ESA
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA9|ZB0].SG10.CCI+++ZB3.CAV+Z91
                      x-apidog-orders:
                        - messstellenbetreiberEigenschaft
                        - marktrolle
                        - rollencodenummer
                      x-apidog-ignore-properties: []
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0]'
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
                x-apidog-orders:
                  - gueltigkeitszeitraum
                  - marktrollen
                  - netzlokationsId
                  - datenqualitaet
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55633 - MSB an NB - Bestellung einer Änderung von Stammdaten vom MSB an
        NB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55657:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+[Z99|ZA0].SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[Z99|ZA0].SG10.CCI+++ZA7.CAV
                                enum:
                                  - NB
                                  - LF
                                  - MSB
                                  - MSBA
                                  - GMSB
                                  - MDL
                                  - DL
                                  - BKV
                                  - BKO
                                  - UENB
                                  - KUNDE-SELBST-NN
                                  - MGV
                                  - EIV
                                  - RB
                                  - KUNDE
                                  - INTERESSENT
                                  - KN
                                  - UBA
                                  - BIKO
                                  - ESA
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z99|ZA0].PIA+5
                      x-apidog-orders:
                        - verwendungszwecke
                        - obisKennzahl
                      x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z99|ZA0]'
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
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z99|ZA0]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zaehlwerke
                  - datenqualitaet
                  - tranchenId
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - TRANCHE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55657 - LF an MSB - Bestellung einer Änderung von Stammdaten vom LF an
        MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55656:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++ZA7'
                    enum:
                      - NB
                      - LF
                      - MSB
                      - MSBA
                      - GMSB
                      - MDL
                      - DL
                      - BKV
                      - BKO
                      - UENB
                      - KUNDE-SELBST-NN
                      - MGV
                      - EIV
                      - RB
                      - KUNDE
                      - INTERESSENT
                      - KN
                      - UBA
                      - BIKO
                      - ESA
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2],
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  zugeordneteDefinition:
                    type: object
                    properties:
                      schaltzeitdefinition:
                        type: object
                        title: Schaltzeitdefinition
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+[Z52|Z53]
                        properties:
                          boTyp:
                            type: string
                            title: BOTyp
                            description: Typ des BO
                            enum:
                              - SCHALTZEITDEFINITION
                          versionStruktur:
                            type: string
                            description: versionStruktur
                            default: '1'
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                      leistungskurvendefinition:
                        type: object
                        title: Leistungskurvendefinition
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+[Z52|Z53]
                        properties:
                          boTyp:
                            type: string
                            title: BOTyp
                            description: Typ des BO
                            enum:
                              - LEISTUNGSKURVENDEFINITION
                          versionStruktur:
                            type: string
                            description: versionStruktur
                            default: '1'
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - schaltzeitdefinition
                      - leistungskurvendefinition
                    x-apidog-ignore-properties: []
                  auftraggebenderMarktpartner:
                    type: object
                    properties:
                      rollencodenummer:
                        type: string
                        description: >-
                          Gibt die Codenummer der Marktrolle an. | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                      marktrolle:
                        type: string
                        title: Marktrolle
                        description: >-
                          Diese Rollen kann ein Marktteilnehmer einnehmen |
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                        enum:
                          - NB
                          - LF
                          - MSB
                          - MSBA
                          - GMSB
                          - MDL
                          - DL
                          - BKV
                          - BKO
                          - UENB
                          - KUNDE-SELBST-NN
                          - MGV
                          - EIV
                          - RB
                          - KUNDE
                          - INTERESSENT
                          - KN
                          - UBA
                          - BIKO
                          - ESA
                    x-apidog-orders:
                      - rollencodenummer
                      - marktrolle
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2],
                      SG4.IDE+24.SG8.SEQ+[ZB3|ZB4]
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
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].PIA+5
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                  steuerkanal:
                    type: object
                    title: AdHocSteuerkanal
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2].SG10.CCI+Z49.CAV+ZF2'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - AD_HOC_STEUERKANAL
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - produktdatenRelevanteRolle
                  - gueltigkeitszeitraum
                  - zugeordneteDefinition
                  - auftraggebenderMarktpartner
                  - datenqualitaet
                  - konfigurationsprodukt
                  - ressourcenId
                  - steuerkanal
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - STEUERBARE_RESSOURCE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55656 - LF an MSB - Bestellung einer Änderung von Stammdaten vom LF an
        MSB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55655:
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
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].PIA+5
                        wertegranularitaet:
                          type: string
                          title: Wertegranularitaet
                          description: >-
                            Wertegranularitaet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZE4.CAV+[ZD9|ZE8|ZE9|ZB7]
                          enum:
                            - JAEHRLICH
                            - HALBJAEHRLICH
                            - QUARTALSWEISE
                            - MONATLICH
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+Z39
                              properties:
                                boTyp:
                                  type: string
                                  title: BOTyp
                                  description: Typ des BO
                                  enum:
                                    - ZAEHLZEITDEFINITION
                                versionStruktur:
                                  type: string
                                  description: versionStruktur
                                  default: '1'
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                            register:
                              type: object
                              title: Zaehlzeitregister
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+Z38
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - zaehlzeitDefinition
                            - register
                          x-apidog-ignore-properties: []
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZA7.CAV
                                enum:
                                  - NB
                                  - LF
                                  - MSB
                                  - MSBA
                                  - GMSB
                                  - MDL
                                  - DL
                                  - BKV
                                  - BKO
                                  - UENB
                                  - KUNDE-SELBST-NN
                                  - MGV
                                  - EIV
                                  - RB
                                  - KUNDE
                                  - INTERESSENT
                                  - KN
                                  - UBA
                                  - BIKO
                                  - ESA
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - obisKennzahl
                        - wertegranularitaet
                        - zaehlzeiten
                        - verwendungszwecke
                      x-apidog-ignore-properties: []
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z51|Z52],
                      SG4.IDE+24.SG8.SEQ+[ZA1|ZA2], SG4.IDE+24.SG8.SEQ+[ZB5|ZB6]
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z51|Z52],
                          SG4.IDE+24.SG8.SEQ+[ZA1|ZA2],
                          SG4.IDE+24.SG8.SEQ+[ZB5|ZB6]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+++ZA7'
                    enum:
                      - NB
                      - LF
                      - MSB
                      - MSBA
                      - GMSB
                      - MDL
                      - DL
                      - BKV
                      - BKO
                      - UENB
                      - KUNDE-SELBST-NN
                      - MGV
                      - EIV
                      - RB
                      - KUNDE
                      - INTERESSENT
                      - KN
                      - UBA
                      - BIKO
                      - ESA
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].PIA+5,
                      SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+11
                  leistungskurvendefinition:
                    type: object
                    title: Leistungskurvendefinition
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+Z53'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - LEISTUNGSKURVENDEFINITION
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zaehlwerke
                  - marktlokationsId
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - produktdatenRelevanteRolle
                  - konfigurationsprodukt
                  - leistungskurvendefinition
                x-apidog-ignore-properties: []
            MESSSTELLENBETRIEBSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragskonditionen:
                    type: object
                    properties:
                      geplanteTurnusablesung:
                        type: object
                        properties:
                          ableseZeitraum:
                            type: string
                            description: >-
                              ableseZeitraum | EDIFACT:
                              SG4.IDE+24.SG6.RFF+[Z51|Z52].DTM+752
                        x-apidog-orders:
                          - ableseZeitraum
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - geplanteTurnusablesung
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragskonditionen
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - MESSSTELLENBETRIEBSVERTRAG
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55655 - LF an MSB - Bestellung einer Änderung von Stammdaten vom LF an
        MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55654:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  auftraggebenderMarktpartner:
                    type: object
                    properties:
                      marktrolle:
                        type: string
                        title: Marktrolle
                        description: >-
                          Diese Rollen kann ein Marktteilnehmer einnehmen |
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                        enum:
                          - NB
                          - LF
                          - MSB
                          - MSBA
                          - GMSB
                          - MDL
                          - DL
                          - BKV
                          - BKO
                          - UENB
                          - KUNDE-SELBST-NN
                          - MGV
                          - EIV
                          - RB
                          - KUNDE
                          - INTERESSENT
                          - KN
                          - UBA
                          - BIKO
                          - ESA
                      rollencodenummer:
                        type: string
                        description: >-
                          Gibt die Codenummer der Marktrolle an. | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                    x-apidog-orders:
                      - marktrolle
                      - rollencodenummer
                    x-apidog-ignore-properties: []
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].PIA+5
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].SG10.CCI+++ZA7.CAV
                                enum:
                                  - NB
                                  - LF
                                  - MSB
                                  - MSBA
                                  - GMSB
                                  - MDL
                                  - DL
                                  - BKV
                                  - BKO
                                  - UENB
                                  - KUNDE-SELBST-NN
                                  - MGV
                                  - EIV
                                  - RB
                                  - KUNDE
                                  - INTERESSENT
                                  - KN
                                  - UBA
                                  - BIKO
                                  - ESA
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - obisKennzahl
                        - verwendungszwecke
                      x-apidog-ignore-properties: []
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++[ZA7|ZA8]'
                    enum:
                      - NB
                      - LF
                      - MSB
                      - MSBA
                      - GMSB
                      - MDL
                      - DL
                      - BKV
                      - BKO
                      - UENB
                      - KUNDE-SELBST-NN
                      - MGV
                      - EIV
                      - RB
                      - KUNDE
                      - INTERESSENT
                      - KN
                      - UBA
                      - BIKO
                      - ESA
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0],
                          SG4.IDE+24.SG8.SEQ+[ZA7|ZA8],
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  steuerkanal:
                    type: object
                    title: AdHocSteuerkanal
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0].SG10.CCI+Z49'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - AD_HOC_STEUERKANAL
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18
                  keinKonfigurationsprodukt:
                    type: boolean
                    description: >-
                      keinKonfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+11
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0],
                      SG4.IDE+24.SG8.SEQ+[ZA7|ZA8], SG4.IDE+24.SG8.SEQ+[ZG8|ZG9]
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
                  leistungskurvendefinition:
                    type: object
                    title: Leistungskurvendefinition
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+Z53'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - LEISTUNGSKURVENDEFINITION
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].PIA+5
                x-apidog-orders:
                  - auftraggebenderMarktpartner
                  - zaehlwerke
                  - produktdatenRelevanteRolle
                  - gueltigkeitszeitraum
                  - steuerkanal
                  - netzlokationsId
                  - keinKonfigurationsprodukt
                  - datenqualitaet
                  - leistungskurvendefinition
                  - konfigurationsprodukt
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55654 - LF an MSB - Bestellung einer Änderung von Stammdaten vom LF an
        MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55648:
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
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z45|Z46]
                      gewerbekennzeichnung:
                        type: boolean
                        description: >-
                          Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
                          (gewerbeKennzeichnung = true)

                          oder eine Privatperson handelt. (gewerbeKennzeichnung
                          = false) | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]
                      partneradresse:
                        type: object
                        properties:
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z45|Z46]
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
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]'
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z45|Z46]
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]'
                          postleitzahl:
                            type: string
                            description: >-
                              Postleitzahl | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z45|Z46]
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]'
                        x-apidog-orders:
                          - landescode
                          - postfach
                          - ortsteil
                          - hausnummer
                          - ort
                          - postleitzahl
                          - strasse
                        x-apidog-ignore-properties: []
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z45|Z46]'
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z45|Z46]
                    x-apidog-orders:
                      - anrede
                      - gewerbekennzeichnung
                      - partneradresse
                      - name3
                      - name1
                      - name4
                      - name2
                    x-apidog-ignore-properties: []
                  messadresse:
                    type: object
                    properties:
                      strasse:
                        type: string
                        description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z43|Z44]'
                      zusatzInformation:
                        type: object
                        properties:
                          zusatz2:
                            type: string
                            description: >-
                              Adresszusatz 2 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z43|Z44]
                          zusatz1:
                            type: string
                            description: >-
                              Adresszusatz 1 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z43|Z44]
                          zusatz4:
                            type: string
                            description: >-
                              Adresszusatz 4 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z43|Z44]
                          zusatz5:
                            type: string
                            description: >-
                              Adresszusatz 5 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z43|Z44]
                          zusatz3:
                            type: string
                            description: >-
                              Adresszusatz 3 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z43|Z44]
                        x-apidog-orders:
                          - zusatz2
                          - zusatz1
                          - zusatz4
                          - zusatz5
                          - zusatz3
                        x-apidog-ignore-properties: []
                      hausnummer:
                        type: string
                        description: >-
                          Hausnummer und Ergänzung | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z43|Z44]
                      ortsteil:
                        type: string
                        description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z43|Z44]'
                      ort:
                        type: string
                        description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z43|Z44]'
                      postleitzahl:
                        type: string
                        description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+[Z43|Z44]'
                      postfach:
                        type: string
                        description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z43|Z44]'
                      landescode:
                        type: string
                        title: Landescode
                        description: >-
                          Der ISO-Landescode als Enumeration | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z43|Z44]
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
                    x-apidog-orders:
                      - strasse
                      - zusatzInformation
                      - hausnummer
                      - ortsteil
                      - ort
                      - postleitzahl
                      - postfach
                      - landescode
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG6|ZG7],
                      SG4.IDE+24.SG12.NAD+[Z43|Z44],
                      SG4.IDE+24.SG12.NAD+[Z45|Z46]
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
                  netzebenemessung:
                    type: string
                    title: Netzebene
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++E04.CAV'
                    enum:
                      - NSP
                      - MSP
                      - HSP
                      - HSS
                      - MSP_NSP_UMSP
                      - HSP_MSP_UMSP
                      - HSS_HSP_UMSP
                      - HD
                      - MD
                      - ND
                  messlokationsId:
                    type: string
                    description: >-
                      Die Messlokations-Identifikation. Das ist die frühere
                      Zählpunktbezeichnung,

                      z.B. DE 47108151234567 | EDIFACT: SG4.IDE+24.SG5.LOC+Z17
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG6|ZG7],
                          SG4.IDE+24.SG12.NAD+[Z43|Z44].RFF+Z46,
                          SG4.IDE+24.SG12.NAD+[Z45|Z46].RFF+Z46
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - ablesekartenempfaenger
                  - messadresse
                  - datenqualitaet
                  - netzebenemessung
                  - messlokationsId
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            ZAEHLER:
              type: array
              items:
                type: object
                properties:
                  zaehlerauspraegung:
                    type: string
                    title: Zaehlerauspraegung
                    description: >-
                      Zaehlerauspraegung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+[ERZ|ZRZ]
                    enum:
                      - EINRICHTUNGSZAEHLER
                      - ZWEIRICHTUNGSZAEHLER
                  geraete:
                    type: array
                    items:
                      type: object
                      properties:
                        geraeteeigenschaften:
                          type: object
                          properties:
                            faktor:
                              type: number
                              description: >-
                                faktor | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZB9|ZC0].SG10.CCI+++Z25.CAV
                              format: float
                            geraetemerkmal:
                              type: string
                              title: Geraetemerkmal
                              description: >-
                                Geraetemerkmal | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZB9|ZC0].SG10.CCI+++Z25.CAV,
                                SG4.IDE+24.SG8.SEQ+[ZB7|ZB8].SG10.CCI+++Z26.CAV,
                                SG4.IDE+24.SG8.SEQ+[ZC1|ZC2].SG10.CCI+++Z27.CAV
                              enum:
                                - EINTARIF
                                - ZWEITARIF
                                - MEHRTARIF
                                - GAS_G2P5
                                - GAS_G4
                                - GAS_G6
                                - GAS_G10
                                - GAS_G16
                                - GAS_G25
                                - GAS_G40
                                - GAS_G65
                                - GAS_G100
                                - GAS_G160
                                - GAS_G250
                                - GAS_G350
                                - GAS_G400
                                - GAS_G4000
                                - GAS_G650
                                - GAS_G6500
                                - GAS_G1000
                                - GAS_G10000
                                - GAS_G12500
                                - GAS_G1600
                                - GAS_G16000
                                - GAS_G2500
                                - IMPULSGEBER_G4_G100
                                - IMPULSGEBER_G100
                                - MODEM_GSM
                                - MODEM_GPRS
                                - MODEM_FUNK
                                - MODEM_GSM_O_LG
                                - MODEM_GSM_M_LG
                                - MODEM_FESTNETZ
                                - MODEM_GPRS_M_LG
                                - PLC_COM
                                - ETHERNET_KOM
                                - DSL_KOM
                                - LTE_KOM
                                - RUNDSTEUEREMPFAENGER
                                - TARIFSCHALTGERAET
                                - ZUSTANDS_MU
                                - TEMPERATUR_MU
                                - KOMPAKT_MU
                                - SYSTEM_MU
                                - UNBESTIMMT
                                - WASSER_MWZW
                                - WASSER_WZWW
                                - WASSER_WZ01
                                - WASSER_WZ02
                                - WASSER_WZ03
                                - WASSER_WZ04
                                - WASSER_WZ05
                                - WASSER_WZ06
                                - WASSER_WZ07
                                - WASSER_WZ08
                                - WASSER_WZ09
                                - WASSER_WZ10
                                - WASSER_VWZ04
                                - WASSER_VWZ05
                                - WASSER_VWZ06
                                - WASSER_VWZ07
                                - WASSER_VWZ10
                                - DICHTEMENGENUMWERTER
                                - TEMPERATURMENGENUMWERTER
                                - ZUSTANDSMENGENUMWERTER
                                - BLOCKSTROMWANDLER
                                - MESSWANDLERSATZ_IMS_MME
                                - KOMBIMESSWANDLER
                                - SPANNUNGSWANDLER
                          x-apidog-orders:
                            - faktor
                            - geraetemerkmal
                          x-apidog-ignore-properties: []
                        geraetetyp:
                          type: string
                          title: Geraetetyp
                          description: >-
                            Auflistung möglicher abzurechnender Gerätetypen |
                            EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+[MG|Z14],
                            SG4.IDE+24.SG8.SEQ+[ZH3|ZH4].RFF+Z14,
                            SG4.IDE+24.SG8.SEQ+[ZH3|ZH4].SG10.CCI+++Z76.CAV+Z30
                          enum:
                            - WECHSELSTROMZAEHLER
                            - DREHSTROMZAEHLER
                            - ZWEIRICHTUNGSZAEHLER
                            - RLM_ZAEHLER
                            - IMS_ZAEHLER
                            - BALGENGASZAEHLER
                            - MAXIMUMZAEHLER
                            - MULTIPLEXANLAGE
                            - PAUSCHALANLAGE
                            - VERSTAERKERANLAGE
                            - SUMMATIONSGERAET
                            - IMPULSGEBER
                            - EDL_21_ZAEHLERAUFSATZ
                            - VIER_QUADRANTEN_LASTGANGZAEHLER
                            - MENGENUMWERTER
                            - STROMWANDLER
                            - SPANNUNGSWANDLER
                            - DATENLOGGER
                            - KOMMUNIKATIONSANSCHLUSS
                            - MODEM
                            - TELEKOMMUNIKATIONSEINRICHTUNG
                            - KOMMUNIKATIONSEINRICHTUNG
                            - DREHKOLBENGASZAEHLER
                            - TURBINENRADGASZAEHLER
                            - ULTRASCHALLZAEHLER
                            - WIRBELGASZAEHLER
                            - MODERNE_MESSEINRICHTUNG
                            - ELEKTRONISCHER_HAUSHALTSZAEHLER
                            - STEUEREINRICHTUNG
                            - TECHNISCHESTEUEREINRICHTUNG
                            - TARIFSCHALTGERAET
                            - RUNDSTEUEREMPFAENGER
                            - OPTIONALE_ZUS_ZAEHLEINRICHTUNG
                            - MESSWANDLERSATZ_IMS_MME
                            - KOMBIMESSWANDLER_IMS_MME
                            - TARIFSCHALTGERAET_IMS_MME
                            - RUNDSTEUEREMPFAENGER_IMS_MME
                            - TEMPERATUR_KOMPENSATION
                            - HOECHSTBELASTUNGS_ANZEIGER
                            - SONSTIGES_GERAET
                            - SMARTMETERGATEWAY
                            - STEUERBOX
                            - BLOCKSTROMWANDLER
                            - KOMBIMESSWANDLER
                            - MODEM_GSM
                            - ETHERNET_KOM
                            - PLC_COM
                            - MODEM_FESTNETZ
                            - DSL_KOM
                            - LTE_KOM
                            - DICHTEMENGENUMWERTER
                            - TEMPERATURMENGENUMWERTER
                            - ZUSTANDSMENGENUMWERTER
                            - MESSDATENREGISTRIERGERAET
                            - WANDLER
                        geraetenummer:
                          type: string
                          description: >-
                            Die auf dem Geräte aufgedruckte Nummer, die vom MSB
                            vergeben wird. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+[MG|Z14],
                            SG4.IDE+24.SG8.SEQ+[ZB9|ZC0].SG10.CCI+++Z25.CAV+Z30,
                            SG4.IDE+24.SG8.SEQ+[ZB7|ZB8].SG10.CCI+++Z26.CAV+Z30,
                            SG4.IDE+24.SG8.SEQ+[ZC1|ZC2].SG10.CCI+++Z27.CAV+Z30,
                            SG4.IDE+24.SG8.SEQ+[ZC3|ZC4].SG10.CCI+++Z75.CAV+Z30,
                            SG4.IDE+24.SG8.SEQ+[ZH3|ZH4].RFF+Z14,
                            SG4.IDE+24.SG8.SEQ+[ZH3|ZH4].SG10.CCI+++Z76.CAV+Z30
                      x-apidog-orders:
                        - geraeteeigenschaften
                        - geraetetyp
                        - geraetenummer
                      x-apidog-ignore-properties: []
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+Z39
                              properties:
                                boTyp:
                                  type: string
                                  title: BOTyp
                                  description: Typ des BO
                                  enum:
                                    - ZAEHLZEITDEFINITION
                                versionStruktur:
                                  type: string
                                  description: versionStruktur
                                  default: '1'
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                            register:
                              type: object
                              title: Zaehlzeitregister
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+Z38
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - zaehlzeitDefinition
                            - register
                          x-apidog-ignore-properties: []
                        schwachlastfaehig:
                          type: string
                          title: Schwachlastfaehig
                          description: >-
                            Schwachlastfaehig | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+Z10
                          enum:
                            - SCHWACHLASTFAEHIG
                            - NICHT_SCHWACHLASTFAEHIG
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].PIA+5
                        vorkommastelle:
                          type: integer
                          description: >-
                            vorkommastelle | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+11++Z33.CAV
                        nachkommastelle:
                          type: integer
                          description: >-
                            nachkommastelle | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+11++Z33.CAV
                        bezeichnung:
                          type: string
                          description: >-
                            Externe Bezeichnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+++Z63
                        wertegranularitaet:
                          type: string
                          title: Wertegranularitaet
                          description: >-
                            Wertegranularitaet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+++ZE4.CAV
                          enum:
                            - JAEHRLICH
                            - HALBJAEHRLICH
                            - QUARTALSWEISE
                            - MONATLICH
                        konfiguration:
                          type: string
                          title: AenderungsmoeglichkeitKonfiguration
                          description: >-
                            AenderungsmoeglichkeitKonfiguration | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+AGK
                          enum:
                            - ERFORDERLICH
                            - NICHT_ERFORDERLICH
                      x-apidog-orders:
                        - zaehlzeiten
                        - schwachlastfaehig
                        - obisKennzahl
                        - vorkommastelle
                        - nachkommastelle
                        - bezeichnung
                        - wertegranularitaet
                        - konfiguration
                      x-apidog-ignore-properties: []
                  zaehlertyp:
                    type: string
                    title: Zaehlertyp
                    description: >-
                      Zaehlertyp | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+[AHZ|WSZ|LAZ|MAZ|MME|EHZ|IVA]
                    enum:
                      - DREHSTROMZAEHLER
                      - BALGENGASZAEHLER
                      - DREHKOLBENZAEHLER
                      - SMARTMETER
                      - LEISTUNGSZAEHLER
                      - MAXIMUMZAEHLER
                      - TURBINENRADGASZAEHLER
                      - ULTRASCHALLGASZAEHLER
                      - WECHSELSTROMZAEHLER
                      - WIRBELGASZAEHLER
                      - MESSDATENREGISTRIERGERAET
                      - ELEKTRONISCHERHAUSHALTSZAEHLER
                      - SONDERAUSSTATTUNG
                      - WASSERZAEHLER
                      - MODERNEMESSEINRICHTUNG
                  zaehlertypspezifikation:
                    type: string
                    title: ZaehlertypSpezifikation
                    description: >-
                      ZaehlertypSpezifikation | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+[AHZ|WSZ|LAZ|MAZ|MME|EHZ|IVA]
                    enum:
                      - EDL40
                      - EDL21
                      - SONSTIGER_EHZ
                      - MME_STANDARD
                      - MME_MEDA
                  fernschaltung:
                    type: string
                    title: Fernschaltung
                    description: >-
                      Fernschaltung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+Z58
                    enum:
                      - VORHANDEN
                      - NICHT_VORHANDEN
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA3|ZA4],
                      SG4.IDE+24.SG8.SEQ+[ZA5|ZA6],
                      SG4.IDE+24.SG8.SEQ+[ZB9|ZC0],
                      SG4.IDE+24.SG8.SEQ+[ZB7|ZB8],
                      SG4.IDE+24.SG8.SEQ+[ZC1|ZC2],
                      SG4.IDE+24.SG8.SEQ+[ZC3|ZC4], SG4.IDE+24.SG8.SEQ+[ZH3|ZH4]
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA3|ZA4],
                          SG4.IDE+24.SG8.SEQ+[ZA5|ZA6],
                          SG4.IDE+24.SG8.SEQ+[ZB9|ZC0],
                          SG4.IDE+24.SG8.SEQ+[ZB7|ZB8],
                          SG4.IDE+24.SG8.SEQ+[ZC1|ZC2],
                          SG4.IDE+24.SG8.SEQ+[ZC3|ZC4],
                          SG4.IDE+24.SG8.SEQ+[ZH3|ZH4]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  gateway:
                    type: string
                    description: >-
                      Angabe eines SMGW, mit dem der Zaehler parametrisiert ist
                      | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].RFF+Z14,
                      SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+[MG|Z14]
                  befestigungsart:
                    type: string
                    title: Befestigungsart
                    description: >-
                      Befestigungsart von Zählern | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++Z28.CAV+[BKE|DPA|HUT]
                    enum:
                      - STECKTECHNIK
                      - DREIPUNKT
                      - HUTSCHIENE
                      - EINSTUTZEN
                      - ZWEISTUTZEN
                  zaehlernummer:
                    type: string
                    description: >-
                      Die Nummer des zu sperrenden Zählers | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+Z30,
                      SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+[MG|Z14],
                      SG4.IDE+24.SG8.SEQ+[ZB9|ZC0].RFF+MG,
                      SG4.IDE+24.SG8.SEQ+[ZB7|ZB8].RFF+MG,
                      SG4.IDE+24.SG8.SEQ+[ZC1|ZC2].RFF+MG
                  tarifart:
                    type: string
                    title: Tarifart
                    description: >-
                      Tarifart | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+[ETZ|ZTZ|NTZ
                    enum:
                      - EINTARIF
                      - ZWEITARIF
                      - MEHRTARIF
                      - SMART_METER
                      - LEISTUNGSGEMESSEN
                  messwerterfassung:
                    type: string
                    title: Messwerterfassung
                    description: >-
                      Die Messwerterfassung des Zählers | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E12.CAV+[AMR|MMR]
                    enum:
                      - FERNAUSLESBAR
                      - MANUELL_AUSGELESENE
                x-apidog-orders:
                  - zaehlerauspraegung
                  - geraete
                  - zaehlwerke
                  - zaehlertyp
                  - zaehlertypspezifikation
                  - fernschaltung
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - gateway
                  - befestigungsart
                  - zaehlernummer
                  - tarifart
                  - messwerterfassung
                x-apidog-ignore-properties: []
            MESSSTELLENBETRIEBSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  korrespondenzpartner:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z41|Z42]
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]'
                          postleitzahl:
                            type: string
                            description: >-
                              Postleitzahl | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z41|Z42]
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]'
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z41|Z42]
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
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]'
                        x-apidog-orders:
                          - hausnummer
                          - ortsteil
                          - postleitzahl
                          - strasse
                          - postfach
                          - landescode
                          - ort
                        x-apidog-ignore-properties: []
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]'
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z41|Z42]
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z41|Z42]
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+[Z41|Z42]
                    x-apidog-orders:
                      - partneradresse
                      - name1
                      - name4
                      - anrede
                      - name2
                      - name3
                    x-apidog-ignore-properties: []
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z39|Z40]'
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen

                            beispielsweise der Nachname dargestellt werden.
                            Beispiele: Yellow Strom GmbH

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z39|Z40]
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z39|Z40]
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z39|Z40]
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z39|Z40]
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z39|Z40]
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
                      x-apidog-orders:
                        - name4
                        - name1
                        - name2
                        - name3
                        - anrede
                        - geschaeftspartnerrolle
                      x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z39|Z40].RFF+Z46,
                          SG4.IDE+24.SG12.NAD+[Z41|Z42].RFF+Z46
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG12.NAD+[Z39|Z40],
                      SG4.IDE+24.SG12.NAD+[Z41|Z42]
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
                x-apidog-orders:
                  - korrespondenzpartner
                  - vertragspartner2
                  - gueltigkeitszeitraum
                  - datenqualitaet
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                x-apidog-orders:
                  - zeitraumId
                  - verwendungBis
                  - verwendungAb
                  - datenqualitaet
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MESSLOKATION
            - ZAEHLER
            - MESSSTELLENBETRIEBSVERTRAG
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                  x-apidog-orders:
                    - eMailAdresse
                    - nachname
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - liste
                  - code
                  - zeitraumId
                x-apidog-ignore-properties: []
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - empfaenger
            - anfragereferenznummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - antwortStatusZeitraum
            - transaktionsgrund
            - pruefidentifikator
            - dokumentennummer
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55648 - NB an MSB - Bestellung einer Änderung von Stammdaten vom NB an
        MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55647:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+[Z99|ZA0].SG10.CCI+++ZA8.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[Z99|ZA0].SG10.CCI+++ZA8.CAV
                                enum:
                                  - NB
                                  - LF
                                  - MSB
                                  - MSBA
                                  - GMSB
                                  - MDL
                                  - DL
                                  - BKV
                                  - BKO
                                  - UENB
                                  - KUNDE-SELBST-NN
                                  - MGV
                                  - EIV
                                  - RB
                                  - KUNDE
                                  - INTERESSENT
                                  - KN
                                  - UBA
                                  - BIKO
                                  - ESA
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z99|ZA0].PIA+5
                      x-apidog-orders:
                        - verwendungszwecke
                        - obisKennzahl
                      x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z99|ZA0]'
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
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z99|ZA0]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zaehlwerke
                  - datenqualitaet
                  - tranchenId
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - TRANCHE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55647 - NB an MSB - Bestellung einer Änderung von Stammdaten vom NB an
        MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55646:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++ZA8'
                    enum:
                      - NB
                      - LF
                      - MSB
                      - MSBA
                      - GMSB
                      - MDL
                      - DL
                      - BKV
                      - BKO
                      - UENB
                      - KUNDE-SELBST-NN
                      - MGV
                      - EIV
                      - RB
                      - KUNDE
                      - INTERESSENT
                      - KN
                      - UBA
                      - BIKO
                      - ESA
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2],
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  zugeordneteDefinition:
                    type: object
                    properties:
                      schaltzeitdefinition:
                        type: object
                        title: Schaltzeitdefinition
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+[Z52|Z53]
                        properties:
                          boTyp:
                            type: string
                            title: BOTyp
                            description: Typ des BO
                            enum:
                              - SCHALTZEITDEFINITION
                          versionStruktur:
                            type: string
                            description: versionStruktur
                            default: '1'
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                      leistungskurvendefinition:
                        type: object
                        title: Leistungskurvendefinition
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+[Z52|Z53]
                        properties:
                          boTyp:
                            type: string
                            title: BOTyp
                            description: Typ des BO
                            enum:
                              - LEISTUNGSKURVENDEFINITION
                          versionStruktur:
                            type: string
                            description: versionStruktur
                            default: '1'
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - schaltzeitdefinition
                      - leistungskurvendefinition
                    x-apidog-ignore-properties: []
                  auftraggebenderMarktpartner:
                    type: object
                    properties:
                      rollencodenummer:
                        type: string
                        description: >-
                          Gibt die Codenummer der Marktrolle an. | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                      marktrolle:
                        type: string
                        title: Marktrolle
                        description: >-
                          Diese Rollen kann ein Marktteilnehmer einnehmen |
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                        enum:
                          - NB
                          - LF
                          - MSB
                          - MSBA
                          - GMSB
                          - MDL
                          - DL
                          - BKV
                          - BKO
                          - UENB
                          - KUNDE-SELBST-NN
                          - MGV
                          - EIV
                          - RB
                          - KUNDE
                          - INTERESSENT
                          - KN
                          - UBA
                          - BIKO
                          - ESA
                    x-apidog-orders:
                      - rollencodenummer
                      - marktrolle
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2],
                      SG4.IDE+24.SG8.SEQ+[ZB3|ZB4]
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
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].PIA+5
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                  steuerkanal:
                    type: object
                    title: AdHocSteuerkanal
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2].SG10.CCI+Z49.CAV+ZF2'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - AD_HOC_STEUERKANAL
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - produktdatenRelevanteRolle
                  - gueltigkeitszeitraum
                  - zugeordneteDefinition
                  - auftraggebenderMarktpartner
                  - datenqualitaet
                  - konfigurationsprodukt
                  - ressourcenId
                  - steuerkanal
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - STEUERBARE_RESSOURCE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55646 - NB an MSB - Bestellung einer Änderung von Stammdaten vom NB an
        MSB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55645:
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
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].PIA+5
                        wertegranularitaet:
                          type: string
                          title: Wertegranularitaet
                          description: >-
                            Wertegranularitaet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZE4.CAV+[ZD9|ZE8|ZE9|ZB7]
                          enum:
                            - JAEHRLICH
                            - HALBJAEHRLICH
                            - QUARTALSWEISE
                            - MONATLICH
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+Z39
                              properties:
                                boTyp:
                                  type: string
                                  title: BOTyp
                                  description: Typ des BO
                                  enum:
                                    - ZAEHLZEITDEFINITION
                                versionStruktur:
                                  type: string
                                  description: versionStruktur
                                  default: '1'
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                            register:
                              type: object
                              title: Zaehlzeitregister
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+Z38
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - zaehlzeitDefinition
                            - register
                          x-apidog-ignore-properties: []
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZA8.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZA8.CAV
                                enum:
                                  - NB
                                  - LF
                                  - MSB
                                  - MSBA
                                  - GMSB
                                  - MDL
                                  - DL
                                  - BKV
                                  - BKO
                                  - UENB
                                  - KUNDE-SELBST-NN
                                  - MGV
                                  - EIV
                                  - RB
                                  - KUNDE
                                  - INTERESSENT
                                  - KN
                                  - UBA
                                  - BIKO
                                  - ESA
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - obisKennzahl
                        - wertegranularitaet
                        - zaehlzeiten
                        - verwendungszwecke
                      x-apidog-ignore-properties: []
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z51|Z52],
                      SG4.IDE+24.SG8.SEQ+[ZA1|ZA2], SG4.IDE+24.SG8.SEQ+[ZB5|ZB6]
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z51|Z52],
                          SG4.IDE+24.SG8.SEQ+[ZA1|ZA2],
                          SG4.IDE+24.SG8.SEQ+[ZB5|ZB6]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+++ZA8'
                    enum:
                      - NB
                      - LF
                      - MSB
                      - MSBA
                      - GMSB
                      - MDL
                      - DL
                      - BKV
                      - BKO
                      - UENB
                      - KUNDE-SELBST-NN
                      - MGV
                      - EIV
                      - RB
                      - KUNDE
                      - INTERESSENT
                      - KN
                      - UBA
                      - BIKO
                      - ESA
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].PIA+5,
                      SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+11
                  leistungskurvendefinition:
                    type: object
                    title: Leistungskurvendefinition
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+Z53'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - LEISTUNGSKURVENDEFINITION
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zaehlwerke
                  - marktlokationsId
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - produktdatenRelevanteRolle
                  - konfigurationsprodukt
                  - leistungskurvendefinition
                x-apidog-ignore-properties: []
            MESSSTELLENBETRIEBSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragskonditionen:
                    type: object
                    properties:
                      geplanteTurnusablesung:
                        type: object
                        properties:
                          ableseZeitraum:
                            type: string
                            description: >-
                              ableseZeitraum | EDIFACT:
                              SG4.IDE+24.SG6.RFF+[Z51|Z52].DTM+752
                        x-apidog-orders:
                          - ableseZeitraum
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - geplanteTurnusablesung
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragskonditionen
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - MESSSTELLENBETRIEBSVERTRAG
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55645 - NB an MSB - Bestellung einer Änderung von Stammdaten vom NB an
        MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55644:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  auftraggebenderMarktpartner:
                    type: object
                    properties:
                      marktrolle:
                        type: string
                        title: Marktrolle
                        description: >-
                          Diese Rollen kann ein Marktteilnehmer einnehmen |
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                        enum:
                          - NB
                          - LF
                          - MSB
                          - MSBA
                          - GMSB
                          - MDL
                          - DL
                          - BKV
                          - BKO
                          - UENB
                          - KUNDE-SELBST-NN
                          - MGV
                          - EIV
                          - RB
                          - KUNDE
                          - INTERESSENT
                          - KN
                          - UBA
                          - BIKO
                          - ESA
                      rollencodenummer:
                        type: string
                        description: >-
                          Gibt die Codenummer der Marktrolle an. | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                    x-apidog-orders:
                      - marktrolle
                      - rollencodenummer
                    x-apidog-ignore-properties: []
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].PIA+5
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].SG10.CCI+++ZA8.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].SG10.CCI+++ZA8.CAV
                                enum:
                                  - NB
                                  - LF
                                  - MSB
                                  - MSBA
                                  - GMSB
                                  - MDL
                                  - DL
                                  - BKV
                                  - BKO
                                  - UENB
                                  - KUNDE-SELBST-NN
                                  - MGV
                                  - EIV
                                  - RB
                                  - KUNDE
                                  - INTERESSENT
                                  - KN
                                  - UBA
                                  - BIKO
                                  - ESA
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - obisKennzahl
                        - verwendungszwecke
                      x-apidog-ignore-properties: []
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++ZA8'
                    enum:
                      - NB
                      - LF
                      - MSB
                      - MSBA
                      - GMSB
                      - MDL
                      - DL
                      - BKV
                      - BKO
                      - UENB
                      - KUNDE-SELBST-NN
                      - MGV
                      - EIV
                      - RB
                      - KUNDE
                      - INTERESSENT
                      - KN
                      - UBA
                      - BIKO
                      - ESA
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0],
                          SG4.IDE+24.SG8.SEQ+[ZA7|ZA8],
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  steuerkanal:
                    type: object
                    title: AdHocSteuerkanal
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0].SG10.CCI+Z49'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - AD_HOC_STEUERKANAL
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18
                  keinKonfigurationsprodukt:
                    type: boolean
                    description: >-
                      keinKonfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+11
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0],
                      SG4.IDE+24.SG8.SEQ+[ZA7|ZA8], SG4.IDE+24.SG8.SEQ+[ZG8|ZG9]
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
                  leistungskurvendefinition:
                    type: object
                    title: Leistungskurvendefinition
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+Z53'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - LEISTUNGSKURVENDEFINITION
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].PIA+5
                x-apidog-orders:
                  - auftraggebenderMarktpartner
                  - zaehlwerke
                  - produktdatenRelevanteRolle
                  - gueltigkeitszeitraum
                  - steuerkanal
                  - netzlokationsId
                  - keinKonfigurationsprodukt
                  - datenqualitaet
                  - leistungskurvendefinition
                  - konfigurationsprodukt
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55644 - NB an MSB - Bestellung einer Änderung von Stammdaten vom NB an
        MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55559:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            absender:
              type: object
              properties:
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
                x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
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
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZC5|ZC6]'
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZC5|ZC6]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  messstellenbetriebsabrechnungsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        anzahl:
                          type: string
                          title: Registeranzahl
                          description: >-
                            Registeranzahl | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZC5|ZC6].SG9.QTY+Z38
                          enum:
                            - EINTARIF
                            - MEHRTARIF
                            - ZWEITARIF
                        artikelId:
                          type: array
                          description: >-
                            ArtikelId gem. BDEW | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZC5|ZC6].PIA+[Z02|Z03]
                          items:
                            type: string
                        messstellenbetriebsabrechnung:
                          type: boolean
                          description: >-
                            messstellenbetriebsabrechnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZC5|ZC6].PIA+[Z02|Z03]
                        abschlag:
                          type: object
                          title: Abschlag
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZC5|ZC6].SG9.QTY+[Z35|Z46]
                          x-apidog-orders: []
                          properties: {}
                          x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - anzahl
                        - artikelId
                        - messstellenbetriebsabrechnung
                        - abschlag
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - marktlokationsId
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - messstellenbetriebsabrechnungsdaten
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55559 - NB an MSB - Bestellung einer Änderung von Stammdaten vom NB an
        MSB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55555:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            AD_HOC_STEUERKANAL:
              type: array
              items:
                type: object
                properties:
                  IPAdresseCLSDevice:
                    type: object
                    properties:
                      IPAdresseCLSDevice1:
                        type: string
                        description: 'IPAdresseCLSDevice1 | EDIFACT: SG4.IDE+24.FTX+Z18'
                      IPAdresseCLSDevice3:
                        type: string
                        description: 'IPAdresseCLSDevice3 | EDIFACT: SG4.IDE+24.FTX+Z18'
                      IPAdresseCLSDevice2:
                        type: string
                        description: 'IPAdresseCLSDevice2 | EDIFACT: SG4.IDE+24.FTX+Z18'
                      IPAdresseCLSDevice5:
                        type: string
                        description: 'IPAdresseCLSDevice5 | EDIFACT: SG4.IDE+24.FTX+Z18'
                      IPAdresseCLSDevice4:
                        type: string
                        description: 'IPAdresseCLSDevice4 | EDIFACT: SG4.IDE+24.FTX+Z18'
                    x-apidog-orders:
                      - IPAdresseCLSDevice1
                      - IPAdresseCLSDevice3
                      - IPAdresseCLSDevice2
                      - IPAdresseCLSDevice5
                      - IPAdresseCLSDevice4
                    x-apidog-ignore-properties: []
                  zieladresse:
                    type: object
                    properties:
                      zieladresse1:
                        type: string
                        description: 'zieladresse1 | EDIFACT: SG4.IDE+24.FTX+Z17'
                      zieladresse5:
                        type: string
                        description: 'zieladresse5 | EDIFACT: SG4.IDE+24.FTX+Z17'
                      zieladresse4:
                        type: string
                        description: 'zieladresse4 | EDIFACT: SG4.IDE+24.FTX+Z17'
                      zieladresse3:
                        type: string
                        description: 'zieladresse3 | EDIFACT: SG4.IDE+24.FTX+Z17'
                      zieladresse2:
                        type: string
                        description: 'zieladresse2 | EDIFACT: SG4.IDE+24.FTX+Z17'
                    x-apidog-orders:
                      - zieladresse1
                      - zieladresse5
                      - zieladresse4
                      - zieladresse3
                      - zieladresse2
                    x-apidog-ignore-properties: []
                  zertifikatsNutzer:
                    type: object
                    properties:
                      zertifikatsNutzer3:
                        type: string
                        description: 'zertifikatsNutzer3 | EDIFACT: SG4.IDE+24.FTX+Z23'
                      zertifikatsNutzer4:
                        type: string
                        description: 'zertifikatsNutzer4 | EDIFACT: SG4.IDE+24.FTX+Z23'
                      zertifikatsNutzer2:
                        type: string
                        description: 'zertifikatsNutzer2 | EDIFACT: SG4.IDE+24.FTX+Z23'
                      zertifikatsNutzer1:
                        type: string
                        description: 'zertifikatsNutzer1 | EDIFACT: SG4.IDE+24.FTX+Z23'
                      zertifikatsNutzer5:
                        type: string
                        description: 'zertifikatsNutzer5 | EDIFACT: SG4.IDE+24.FTX+Z23'
                    x-apidog-orders:
                      - zertifikatsNutzer3
                      - zertifikatsNutzer4
                      - zertifikatsNutzer2
                      - zertifikatsNutzer1
                      - zertifikatsNutzer5
                    x-apidog-ignore-properties: []
                  aussteller:
                    type: object
                    properties:
                      aussteller3:
                        type: string
                        description: 'aussteller3 | EDIFACT: SG4.IDE+24.FTX+Z24'
                      aussteller4:
                        type: string
                        description: 'aussteller4 | EDIFACT: SG4.IDE+24.FTX+Z24'
                      aussteller5:
                        type: string
                        description: 'aussteller5 | EDIFACT: SG4.IDE+24.FTX+Z24'
                      aussteller1:
                        type: string
                        description: 'aussteller1 | EDIFACT: SG4.IDE+24.FTX+Z24'
                      aussteller2:
                        type: string
                        description: 'aussteller2 | EDIFACT: SG4.IDE+24.FTX+Z24'
                    x-apidog-orders:
                      - aussteller3
                      - aussteller4
                      - aussteller5
                      - aussteller1
                      - aussteller2
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - IPAdresseCLSDevice
                  - zieladresse
                  - zertifikatsNutzer
                  - aussteller
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].PIA+5
                        wertegranularitaet:
                          type: string
                          title: Wertegranularitaet
                          description: >-
                            Wertegranularitaet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZE4.CAV+[ZD9|ZE8|ZE9|ZB7]
                          enum:
                            - JAEHRLICH
                            - HALBJAEHRLICH
                            - QUARTALSWEISE
                            - MONATLICH
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+Z39
                              properties:
                                boTyp:
                                  type: string
                                  title: BOTyp
                                  description: Typ des BO
                                  enum:
                                    - ZAEHLZEITDEFINITION
                                versionStruktur:
                                  type: string
                                  description: versionStruktur
                                  default: '1'
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                            register:
                              type: object
                              title: Zaehlzeitregister
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+Z38
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - zaehlzeitDefinition
                            - register
                          x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - obisKennzahl
                        - wertegranularitaet
                        - zaehlzeiten
                      x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA1|ZA2]'
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA1|ZA2]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zaehlwerke
                  - datenqualitaet
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            ZAEHLER:
              type: array
              items:
                type: object
                properties:
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA3|ZA4],
                          SG4.IDE+24.SG8.SEQ+[ZA5|ZA6]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+Z39
                              properties:
                                boTyp:
                                  type: string
                                  title: BOTyp
                                  description: Typ des BO
                                  enum:
                                    - ZAEHLZEITDEFINITION
                                versionStruktur:
                                  type: string
                                  description: versionStruktur
                                  default: '1'
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                            register:
                              type: object
                              title: Zaehlzeitregister
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+Z38
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - zaehlzeitDefinition
                            - register
                          x-apidog-ignore-properties: []
                        bezeichnung:
                          type: string
                          description: >-
                            Externe Bezeichnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+++Z63
                        wertegranularitaet:
                          type: string
                          title: Wertegranularitaet
                          description: >-
                            Wertegranularitaet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+++ZE4.CAV+[ZD9|ZE8|ZE9|ZB7]
                          enum:
                            - JAEHRLICH
                            - HALBJAEHRLICH
                            - QUARTALSWEISE
                            - MONATLICH
                        nachkommastelle:
                          type: integer
                          description: >-
                            nachkommastelle | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+11++Z33.CAV
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].PIA+5
                        vorkommastelle:
                          type: integer
                          description: >-
                            vorkommastelle | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].SG10.CCI+11++Z33.CAV
                        konfiguration:
                          type: string
                          title: AenderungsmoeglichkeitKonfiguration
                          description: >-
                            AenderungsmoeglichkeitKonfiguration | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+AGK
                          enum:
                            - ERFORDERLICH
                            - NICHT_ERFORDERLICH
                      x-apidog-orders:
                        - zaehlzeiten
                        - bezeichnung
                        - wertegranularitaet
                        - nachkommastelle
                        - obisKennzahl
                        - vorkommastelle
                        - konfiguration
                      x-apidog-ignore-properties: []
                  geraete:
                    type: array
                    items:
                      type: object
                      properties:
                        geraetetyp:
                          type: string
                          title: Geraetetyp
                          description: >-
                            Auflistung möglicher abzurechnender Gerätetypen |
                            EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+Z14
                          enum:
                            - WECHSELSTROMZAEHLER
                            - DREHSTROMZAEHLER
                            - ZWEIRICHTUNGSZAEHLER
                            - RLM_ZAEHLER
                            - IMS_ZAEHLER
                            - BALGENGASZAEHLER
                            - MAXIMUMZAEHLER
                            - MULTIPLEXANLAGE
                            - PAUSCHALANLAGE
                            - VERSTAERKERANLAGE
                            - SUMMATIONSGERAET
                            - IMPULSGEBER
                            - EDL_21_ZAEHLERAUFSATZ
                            - VIER_QUADRANTEN_LASTGANGZAEHLER
                            - MENGENUMWERTER
                            - STROMWANDLER
                            - SPANNUNGSWANDLER
                            - DATENLOGGER
                            - KOMMUNIKATIONSANSCHLUSS
                            - MODEM
                            - TELEKOMMUNIKATIONSEINRICHTUNG
                            - KOMMUNIKATIONSEINRICHTUNG
                            - DREHKOLBENGASZAEHLER
                            - TURBINENRADGASZAEHLER
                            - ULTRASCHALLZAEHLER
                            - WIRBELGASZAEHLER
                            - MODERNE_MESSEINRICHTUNG
                            - ELEKTRONISCHER_HAUSHALTSZAEHLER
                            - STEUEREINRICHTUNG
                            - TECHNISCHESTEUEREINRICHTUNG
                            - TARIFSCHALTGERAET
                            - RUNDSTEUEREMPFAENGER
                            - OPTIONALE_ZUS_ZAEHLEINRICHTUNG
                            - MESSWANDLERSATZ_IMS_MME
                            - KOMBIMESSWANDLER_IMS_MME
                            - TARIFSCHALTGERAET_IMS_MME
                            - RUNDSTEUEREMPFAENGER_IMS_MME
                            - TEMPERATUR_KOMPENSATION
                            - HOECHSTBELASTUNGS_ANZEIGER
                            - SONSTIGES_GERAET
                            - SMARTMETERGATEWAY
                            - STEUERBOX
                            - BLOCKSTROMWANDLER
                            - KOMBIMESSWANDLER
                            - MODEM_GSM
                            - ETHERNET_KOM
                            - PLC_COM
                            - MODEM_FESTNETZ
                            - DSL_KOM
                            - LTE_KOM
                            - DICHTEMENGENUMWERTER
                            - TEMPERATURMENGENUMWERTER
                            - ZUSTANDSMENGENUMWERTER
                            - MESSDATENREGISTRIERGERAET
                            - WANDLER
                        geraetenummer:
                          type: string
                          description: >-
                            Die auf dem Geräte aufgedruckte Nummer, die vom MSB
                            vergeben wird. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA5|ZA6].RFF+Z14
                      x-apidog-orders:
                        - geraetetyp
                        - geraetenummer
                      x-apidog-ignore-properties: []
                  gateway:
                    type: string
                    description: >-
                      Angabe eines SMGW, mit dem der Zaehler parametrisiert ist
                      | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].RFF+Z14
                  zaehlernummer:
                    type: string
                    description: >-
                      Die Nummer des zu sperrenden Zählers | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZA3|ZA4].SG10.CCI+++E13.CAV+Z30
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA3|ZA4],
                      SG4.IDE+24.SG8.SEQ+[ZA5|ZA6]
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
                x-apidog-orders:
                  - gueltigkeitszeitraum
                  - zaehlwerke
                  - geraete
                  - gateway
                  - zaehlernummer
                  - datenqualitaet
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - AD_HOC_STEUERKANAL
            - MARKTLOKATION
            - ZAEHLER
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ipAdresse:
                  type: string
                  description: 'ipAdresse | EDIFACT: SG4.IDE+24.FTX+Z27'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                ipRange:
                  type: object
                  properties:
                    obereGrenze:
                      type: string
                      description: 'obereGrenze | EDIFACT: SG4.IDE+24.FTX+Z28'
                    untereGrenze:
                      type: string
                      description: 'untereGrenze | EDIFACT: SG4.IDE+24.FTX+Z28'
                  x-apidog-orders:
                    - obereGrenze
                    - untereGrenze
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ipAdresse
                - ansprechpartner
                - rollencodetyp
                - ipRange
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - liste
                  - zeitraumId
                x-apidog-ignore-properties: []
            nachrichtenReferenzBestellbestaetigung:
              type: string
              description: >-
                Referenznummer der Nachricht der betroffenen Antwort auf
                Bestellung 'Bestellbestätigung' / ORDERS RFF+Z42 | EDIFACT:
                SG4.IDE+24.SG6.RFF+Z42
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            vorgangsReferenzBestellbestaetigung:
              type: string
              description: >-
                Referenznummer des Vorgangs der betroffenen Antwort auf
                Bestellung 'Bestellbestätigung' / ORDERS RFF+Z43 | EDIFACT:
                SG4.IDE+24.SG6.RFF+Z43
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - antwortStatusZeitraum
            - nachrichtenReferenzBestellbestaetigung
            - pruefidentifikator
            - vorgangsReferenzBestellbestaetigung
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55555 - weiterer MSB an MSB - Bestellung einer Änderung von Stammdaten
        vom weiteren MSB an MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
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
