# Ersatz-/Grundversorgung

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
      summary: Ersatz-/Grundversorgung
      deprecated: false
      description: Prozess zur Anmeldung von Ersatz-/Grundversorgung starten.
      operationId: START_EOG
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BNB%5D%20START_EOG'
            examples: {}
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
      x-apidog-folder: Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14984068-run
components:
  schemas:
    '[NB] START_EOG':
      allOf:
        - $ref: '#/components/schemas/PI_55013'
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
                eventname:
                  type: string
                  description: Name des Events
                  const: START_EOG
                  default: START_EOG
              x-apidog-orders:
                - prozessId
                - eventname
              required:
                - prozessId
                - eventname
              x-apidog-ignore-properties: []
          x-apidog-refs: {}
          x-apidog-orders:
            - zusatzdaten
          required:
            - zusatzdaten
          x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55013:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
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

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z65
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z65
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z65'
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z65
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
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z65
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z65
                      x-apidog-orders:
                        - name1
                        - name3
                        - name4
                        - geschaeftspartnerrolle
                        - name2
                        - anrede
                      x-apidog-ignore-properties: []
                  korrespondenzpartner:
                    type: object
                    properties:
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z66
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                      partneradresse:
                        type: object
                        properties:
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z66
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
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z66
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                        x-apidog-orders:
                          - landescode
                          - ortsteil
                          - hausnummer
                          - ort
                          - postleitzahl
                          - strasse
                          - postfach
                        x-apidog-ignore-properties: []
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z66
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z66
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z66
                    x-apidog-orders:
                      - name3
                      - name4
                      - partneradresse
                      - name1
                      - anrede
                      - name2
                    x-apidog-ignore-properties: []
                  enFG:
                    type: array
                    items:
                      type: object
                      properties:
                        grundlageVerringerungUmlagen:
                          type: string
                        grund:
                          type: string
                      x-apidog-orders:
                        - grundlageVerringerungUmlagen
                        - grund
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

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z67
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z67
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z67
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

                            oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z67
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z67'
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z67
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
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z68
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
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z68
                        x-apidog-orders:
                          - postfach
                          - ortsteil
                          - postleitzahl
                          - ort
                          - landescode
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
                          SG4.IDE+24.SG12.NAD+Z68
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z68
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z68
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z68
                    x-apidog-orders:
                      - partneradresse
                      - name2
                      - anrede
                      - name4
                      - name3
                      - name1
                    x-apidog-ignore-properties: []
                  vertragskonditionen:
                    type: object
                    properties:
                      haushaltskunde:
                        type: boolean
                    x-apidog-orders:
                      - haushaltskunde
                    required:
                      - haushaltskunde
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragsart
                  - vertragspartner2
                  - korrespondenzpartner
                  - vertragskonditionen
                required:
                  - vertragsart
                  - vertragskonditionen
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
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG12.NAD+Z69,
                      SG4.IDE+24.SG12.NAD+Z70, SG4.IDE+24.SG12.NAD+Z63
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
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z70
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
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z70
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
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

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z70
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z70
                      gewerbekennzeichnung:
                        type: boolean
                        description: >-
                          Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
                          (gewerbeKennzeichnung = true)

                          oder eine Privatperson handelt. (gewerbeKennzeichnung
                          = false) | EDIFACT: SG4.IDE+24.SG12.NAD+Z70
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z70
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z70
                    x-apidog-orders:
                      - partneradresse
                      - name1
                      - name4
                      - anrede
                      - gewerbekennzeichnung
                      - name2
                      - name3
                    x-apidog-ignore-properties: []
                  lokationsadresse:
                    type: object
                    properties:
                      landescode:
                        type: string
                        title: Landescode
                        description: >-
                          Der ISO-Landescode als Enumeration | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z63
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
                      zusatzInformation:
                        type: object
                        properties:
                          zusatz4:
                            type: string
                            description: 'Adresszusatz 4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                          zusatz1:
                            type: string
                            description: 'Adresszusatz 1 | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                          zusatz2:
                            type: string
                            description: 'Adresszusatz 2 | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                          zusatz5:
                            type: string
                            description: 'Adresszusatz 5 | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                          zusatz3:
                            type: string
                            description: 'Adresszusatz 3 | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                        x-apidog-orders:
                          - zusatz4
                          - zusatz1
                          - zusatz2
                          - zusatz5
                          - zusatz3
                        x-apidog-ignore-properties: []
                      ortsteil:
                        type: string
                        description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                      postleitzahl:
                        type: string
                        description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                      strasse:
                        type: string
                        description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                      hausnummer:
                        type: string
                        description: >-
                          Hausnummer und Ergänzung | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z63
                      ort:
                        type: string
                        description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                      postfach:
                        type: string
                        description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                    x-apidog-orders:
                      - landescode
                      - zusatzInformation
                      - ortsteil
                      - postleitzahl
                      - strasse
                      - hausnummer
                      - ort
                      - postfach
                    x-apidog-ignore-properties: []
                  eigentuemer:
                    type: object
                    properties:
                      boTyp:
                        type: string
                      versionStruktur:
                        type: string
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z69
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z69
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z69
                      partneradresse:
                        type: object
                        properties:
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z69
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z69
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
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
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
                          = false) | EDIFACT: SG4.IDE+24.SG12.NAD+Z69
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z69
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                      - name3
                      - name4
                      - name2
                      - name1
                      - partneradresse
                      - gewerbekennzeichnung
                      - anrede
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                        versionStruktur:
                          type: string
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
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
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - messstellenbetreiberEigenschaft
                        - weiterverpflichtet
                        - marktrolle
                        - rollencodenummer
                      x-apidog-ignore-properties: []
                  sperrstatus:
                    type: string
                    title: Sperrstatus
                    description: 'Sperrstatus | EDIFACT: SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+Z42'
                    enum:
                      - ENTSPERRT
                      - GESPERRT
                  netzebene:
                    type: string
                    title: Netzebene
                    description: >-
                      Netzebene | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++E03.CAV
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
                  - lokationsadresse
                  - eigentuemer
                  - marktrollen
                  - sperrstatus
                  - netzebene
                required:
                  - marktlokationsId
                  - datenqualitaet
                  - sperrstatus
                  - netzebene
                x-apidog-ignore-properties: []
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
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18,
                      SG4.IDE+24.SG8.SEQ+ZD7.RFF+Z32
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                        versionStruktur:
                          type: string
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZD7.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZD7.SG10.CCI+++ZB3.CAV+Z91
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZD7.SG10.CCI+++ZB3.CAV+Z91
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
                        - boTyp
                        - versionStruktur
                        - messstellenbetreiberEigenschaft
                        - rollencodenummer
                        - marktrolle
                      required:
                        - boTyp
                        - versionStruktur
                      x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                x-apidog-orders:
                  - netzlokationsId
                  - marktrollen
                  - datenqualitaet
                x-apidog-ignore-properties: []
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: >-
                      ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19,
                      SG4.IDE+24.SG8.SEQ+ZF1.RFF+Z38
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                        versionStruktur:
                          type: string
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF1.SG10.CCI+++ZB3.CAV+Z91
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
                            SG4.IDE+24.SG8.SEQ+ZF1.SG10.CCI+++ZB3.CAV+Z91
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF1.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - messstellenbetreiberEigenschaft
                      required:
                        - boTyp
                        - versionStruktur
                      x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                x-apidog-orders:
                  - ressourcenId
                  - marktrollen
                  - datenqualitaet
                x-apidog-ignore-properties: []
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  datenqualitaet:
                    type: string
                  prognosegrundlage:
                    type: string
                    title: Prognosegrundlage
                    description: >-
                      Prognosegrundlage | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI
                    enum:
                      - WERTE
                      - PROFILE
                  temperaturarbeit:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z98.SG9.QTY+[265|Z08]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z98.SG9.QTY+[265|Z08]
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
                          SG4.IDE+24.SG8.SEQ+Z98.SG9.QTY+31
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
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z98.SG9.QTY+31'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - einheit
                      - wert
                    x-apidog-ignore-properties: []
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
                        SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI.CAV+[E02|E14]
                      items:
                        type: string
                        title: Profiltyp
                        description: Profiltyp
                        enum:
                          - SLP_SEP
                          - TLP_TEP
                          - TEP
                x-apidog-orders:
                  - datenqualitaet
                  - prognosegrundlage
                  - temperaturarbeit
                  - jahresverbrauchsprognose
                  - detailsPrognosegrundlage
                required:
                  - datenqualitaet
                  - prognosegrundlage
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

                      z.B. DE 47108151234567 | EDIFACT: SG4.IDE+24.SG5.LOC+Z17,
                      SG4.IDE+24.SG8.SEQ+ZF3.RFF+Z19
                  datenqualitaet:
                    type: string
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                        versionStruktur:
                          type: string
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+ZF0
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91
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
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+ZF0
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
                        - boTyp
                        - versionStruktur
                        - weiterverpflichtet
                        - rollencodenummer
                        - messstellenbetreiberEigenschaft
                        - marktrolle
                      required:
                        - boTyp
                        - versionStruktur
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - messlokationsId
                  - datenqualitaet
                  - marktrollen
                required:
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
            - ENERGIELIEFERVERTRAG
            - NETZNUTZUNGSVERTRAG
            - MARKTLOKATION
            - NETZLOKATION
            - STEUERBARE_RESSOURCE
            - BILANZIERUNG
            - MESSLOKATION
            - TECHNISCHE_RESSOURCE
          required:
            - ENERGIELIEFERVERTRAG
            - NETZNUTZUNGSVERTRAG
            - MARKTLOKATION
            - BILANZIERUNG
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            vertragsende:
              type: string
              description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
              format: date-time
            transaktionsgrundergaenzungBefristeteAnmeldung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund bei befristeten An-/Abmeldungen
                / UTILMD STS+7++E01+ZW4+### | EDIFACT: SG4.IDE+24.STS+7
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
                marktrolle:
                  type: string
                boTyp:
                  type: string
                versionStruktur:
                  type: string
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
                - marktrolle
                - boTyp
                - versionStruktur
              required:
                - rollencodetyp
                - rollencodenummer
                - marktrolle
                - boTyp
                - versionStruktur
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
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
                marktrolle:
                  type: string
                boTyp:
                  type: string
                versionStruktur:
                  type: string
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
                - marktrolle
                - boTyp
                - versionStruktur
              required:
                - rollencodenummer
                - rollencodetyp
                - marktrolle
                - boTyp
                - versionStruktur
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
            vertragsbeginn:
              type: string
              description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
              format: date-time
            sparte:
              type: string
          x-apidog-orders:
            - vertragsende
            - transaktionsgrundergaenzungBefristeteAnmeldung
            - empfaenger
            - anfragereferenznummer
            - absender
            - transaktionsgrund
            - transaktionsgrundergaenzung
            - vertragsbeginn
            - sparte
          required:
            - empfaenger
            - absender
            - transaktionsgrund
            - transaktionsgrundergaenzung
            - vertragsbeginn
            - sparte
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
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
