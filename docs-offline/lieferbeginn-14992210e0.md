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
