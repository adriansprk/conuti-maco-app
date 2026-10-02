# Stammdaten der identifiz. MaLo

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getMaloidentMarketlocation:
    get:
      summary: Stammdaten der identifiz. MaLo
      deprecated: false
      description: >-
        `LESEN_MALOIDENT_MARKTLOKATION`


        Lesen der Stammdaten der identifierten Marktlokation für die positive
        Antwort mittels LokationsId (Parameter1) zum Zeitpunkt (Parameter2)
      operationId: LESEN_MALOIDENT_MARKTLOKATION
      tags:
        - Schnittstellen/MaloIdent NB (Backend)
        - MALODATEN
      parameters:
        - name: parameter1
          in: query
          description: LokationsId der Marktlokation
          required: true
          schema:
            type: string
            default: '74018657187'
            examples:
              - '74018657187'
        - name: parameter3
          in: query
          description: Datum (Stichtag)
          required: true
          schema:
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            type: string
            examples:
              - '2024-06-28T12:18:00Z'
      responses:
        '200':
          description: Erfolgreiches Lesen der Marktlokationsdaten
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MaloIdent%20Marktlokation'
              example:
                stammdaten:
                  MARKTLOKATION:
                    - boTyp: MARKTLOKATION
                      versionStruktur: '1'
                      marktlokationsId: '57685676748'
                      energierichtung: EINSP
                      messtechnischeEinordnung: IMS
                      marktlokationsTyp:
                        - typ: STANDARD_MARKTLOKATION
                          gueltigAb: '2023-08-01T22:00:00Z'
                          gueltigBis: '2023-09-01T22:00:00Z'
                        - typ: RUHENDE_MARKTLOKATION
                          gueltigAb: '2023-09-01T22:00:00Z'
                          gueltigBis: '2023-10-01T22:00:00Z'
                        - typ: KUNDENANLAGE
                          gueltigAb: '2023-10-01T22:00:00Z'
                          gueltigBis: '2023-11-01T22:00:00Z'
                      marktrollen:
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          rollencodenummer: '9800172600001'
                          marktrolle: NB
                          zuordnungVon: '2023-09-01T22:00:00Z'
                          zuordnungBis: '2023-10-01T22:00:00Z'
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          rollencodenummer: '9800172600002'
                          marktrolle: MSB
                          zuordnungVon: '2023-09-01T22:00:00Z'
                          zuordnungBis: '2023-10-01T22:00:00Z'
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          rollencodenummer: '9800172600003'
                          marktrolle: UENB
                          zuordnungVon: '2023-09-01T22:00:00Z'
                          zuordnungBis: '2023-10-01T22:00:00Z'
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          rollencodenummer: '9800172600004'
                          marktrolle: LF
                          zuordnungVon: '2023-09-01T22:00:00Z'
                          zuordnungBis: '2023-10-01T22:00:00Z'
                      lokationsadresse:
                        postleitzahl: '12117'
                        ort: Berlin
                        strasse: Reinhardtstraße
                        hausnummer: '32'
                        adresszusatz: F
                        landescode: DE
                      katasterinformation:
                        gemarkung_flur: Eine Gemarkung
                        flurstueck: Ein Stueck
                        flurstueckNummer: '123'
                      geokoordinaten:
                        breitengrad: '48.1351'
                        laengengrad: '11.5820'
                        ostwert: '692200'
                        nordwert: '5334180'
                        zone: UTMZone31
                        hochwert: '5334010'
                        rechtswert: '4481220'
                  BILANZIERUNG:
                    - boTyp: BILANZIERUNG
                      versionStruktur: '1'
                      wahlrechtPrognosegrundlage: DURCH_LF
                  TRANCHE:
                    - boTyp: TRANCHE
                      versionStruktur: '1'
                      tranchenId: '57685676742'
                      bildungTranchengroesse: PROZENTUAL
                      aufteilungsmenge:
                        wert: 12.5
                        einheit: PROZENT
                      marktrollen:
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          rollencodenummer: '9800172600005'
                          marktrolle: LF
                          zuordnungVon: '2023-09-01T22:00:00Z'
                          zuordnungBis: '2023-10-01T22:00:00Z'
                  MESSLOKATION:
                    - boTyp: MESSLOKATION
                      versionStruktur: '1'
                      messlokationsId: DE00014545768S0000000000000003054
                      marktrollen:
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          rollencodenummer: '9800172600005'
                          marktrolle: MSB
                          zuordnungVon: '2023-09-01T22:00:00Z'
                          zuordnungBis: '2023-10-01T22:00:00Z'
                  ENERGIELIEFERVERTRAG:
                    - boTyp: VERTRAG
                      versionStruktur: '1'
                      vertragsart: ENERGIELIEFERVERTRAG
                      vertragspartner2:
                        - boTyp: GESCHAEFTSPARTNER
                          versionStruktur: '1'
                          anrede: Prof.Dr.
                          name1: Becker
                          name2: Michael
                          gewerbekennzeichnung: false
                          geschaeftspartnerrolle:
                            - KUNDE
                  TECHNISCHE_RESSOURCE:
                    - boTyp: TECHNISCHE_RESSOURCE
                      versionStruktur: '1'
                      ressourcenId: D417MLM8164
                  STEUERBARE_RESSOURCE:
                    - boTyp: STEUERBARE_RESSOURCE
                      versionStruktur: '1'
                      ressourcenId: C81641SBT77
                      marktrollen:
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          marktrolle: MSB
                          rollencodenummer: '9980000000026'
                          zuordnungVon: '2023-09-01T22:00:00Z'
                          zuordnungBis: '2023-10-01T22:00:00Z'
                  NETZLOKATION:
                    - boTyp: NETZLOKATION
                      versionStruktur: '1'
                      netzlokationsId: E1688117482
                      marktrollen:
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          marktrolle: MSB
                          rollencodenummer: '9980000000029'
                          zuordnungVon: '2023-09-01T22:00:00Z'
                          zuordnungBis: '2023-10-01T22:00:00Z'
          headers: {}
          x-apidog-name: OK
        '400':
          description: Fehler bei Ausführung
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apidog-orders: []
                x-apidog-ignore-properties: []
          headers: {}
          x-apidog-name: Bad Request
      security:
        - bearer: []
      x-apidog-folder: Schnittstellen/MaloIdent NB (Backend)
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14666444-run
components:
  schemas:
    MaloIdent Marktlokation:
      description: >-
        LESEN_MALOIDENT_MARKTLOKATION - Stammdaten, die identifizierte
        Marktlokation beschreiben
      type: object
      properties:
        stammdaten:
          type: object
          description: >
            Informationscontainer für Stammdaten, die identifizierte
            Marktlokation beschreiben
          properties:
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  boTyp:
                    type: string
                    enum:
                      - MARKTLOKATION
                    examples:
                      - MARKTLOKATION
                  versionStruktur:
                    type: string
                    enum:
                      - '1'
                    examples:
                      - '1'
                  marktlokationsId:
                    type: string
                    pattern: \d{11}
                    description: >
                      Identifiziert die Marktlokation mittels einer eindeutigen
                      ID | Mapping auf
                      dataMarketLocation.maloId                   
                    examples:
                      - '57685676748'
                  energierichtung:
                    type: object
                    properties: {}
                    x-apidog-orders: []
                    x-apidog-ignore-properties: []
                  messtechnischeEinordnung:
                    type: object
                    properties: {}
                    x-apidog-orders: []
                    x-apidog-ignore-properties: []
                  marktlokationsTyp:
                    type: array
                    items:
                      type: object
                      properties:
                        typ:
                          type: object
                          properties: {}
                          x-apidog-orders: []
                          x-apidog-ignore-properties: []
                        gueltigAb:
                          type: string
                          description: >-
                            Beginnzeitpunkt, Zeitpunkt zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden.
                            Dieser Zeitpunkt muss ein Tagesbeginn 00:00 Uhr
                            gesetzlicher deutscher Zeit sein.
                          examples:
                            - '2023-08-01T22:00:00Z'
                        gueltigBis:
                          type: string
                          description: >-
                            Endezeitpunkt, Zeitpunkt bis zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden.
                            Dieser Zeitpunkt muss ein Tagesbeginn 00:00 Uhr
                            gesetzlicher deutscher Zeit sein.
                          examples:
                            - '2023-09-01T22:00:00Z'
                      x-apidog-orders:
                        - typ
                        - gueltigAb
                        - gueltigBis
                      x-apidog-ignore-properties: []
                  lokationsadresse:
                    type: object
                    properties: {}
                    x-apidog-orders: []
                    x-apidog-ignore-properties: []
                  marktrollen:
                    type: array
                    description: >
                      Identifiziert die Marktpartner der Marktlokation. |
                      Mapping auf
                      dataMarketLocation.dataMarketLocationSuppliers/dataMarketLocationTransmissionSystemOperators/dataMarketLocationMeasuringPointOperators/dataMarketLocationNetworkOperators/dataMarketLocationSuppliers                             
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                          enum:
                            - MARKTTEILNEHMER
                          examples:
                            - MARKTTEILNEHMER
                        versionStruktur:
                          type: string
                          enum:
                            - '1'
                          examples:
                            - '1'
                        marktrolle:
                          type: object
                          properties: {}
                          x-apidog-orders: []
                          x-apidog-ignore-properties: []
                        rollencodenummer:
                          type: string
                          description: Identifiziert den Marktpartner (Marktpartner-ID).
                          examples:
                            - '9980000000029'
                        zuordnungVon:
                          type: string
                          description: >-
                            Beginnzeitpunkt, Zeitpunkt zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden in
                            Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt ein
                            Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit
                            sein)
                          pattern: >-
                            20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
                          examples:
                            - '2023-09-01T00:00:00Z'
                        zuordnungBis:
                          type: string
                          description: >-
                            Endezeitpunkt, Zeitpunkt bis zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden in
                            Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt ein
                            Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit
                            sein)
                          pattern: >-
                            20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
                          examples:
                            - '2023-10-01T00:00:00Z'
                      required:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - zuordnungVon
                        - zuordnungBis
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - zuordnungVon
                        - zuordnungBis
                      x-apidog-ignore-properties: []
                  katasterinformation:
                    type: object
                    properties: {}
                    x-apidog-orders: []
                    x-apidog-ignore-properties: []
                  geokoordinaten:
                    type: object
                    properties: {}
                    x-apidog-orders: []
                    x-apidog-ignore-properties: []
                required:
                  - boTyp
                  - versionStruktur
                  - marktlokationsId
                  - energierichtung
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - marktlokationsId
                  - energierichtung
                  - messtechnischeEinordnung
                  - marktlokationsTyp
                  - lokationsadresse
                  - marktrollen
                  - katasterinformation
                  - geokoordinaten
                x-apidog-ignore-properties: []
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  boTyp:
                    type: string
                    enum:
                      - BILANZIERUNG
                    examples:
                      - BILANZIERUNG
                  versionStruktur:
                    type: string
                    enum:
                      - '1'
                    examples:
                      - '1'
                  wahlrechtPrognosegrundlage:
                    type: object
                    properties: {}
                    x-apidog-orders: []
                    x-apidog-ignore-properties: []
                required:
                  - boTyp
                  - versionStruktur
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - wahlrechtPrognosegrundlage
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  boTyp:
                    type: string
                    enum:
                      - TRANCHE
                    examples:
                      - TRANCHE
                  versionStruktur:
                    type: string
                    enum:
                      - '1'
                    examples:
                      - '1'
                  tranchenId:
                    type: string
                    pattern: \d{11}
                    description: >
                      Identifiziert die Tranche mittels einer eindeutigen ID |
                      Mapping auf identificationParameterId.tranchenIds    
                    examples:
                      - '57685676742'
                  bildungTranchengroesse:
                    type: object
                    properties: {}
                    x-apidog-orders: []
                    x-apidog-ignore-properties: []
                  aufteilungsmenge:
                    type: object
                    properties: {}
                    x-apidog-orders: []
                    x-apidog-ignore-properties: []
                  marktrollen:
                    type: array
                    description: >
                      Identifiziert die Lieferanten der Tranche | Mapping auf
                      dataTranches.dataTrancheSuppliers                                   
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                          enum:
                            - MARKTTEILNEHMER
                          examples:
                            - MARKTTEILNEHMER
                        versionStruktur:
                          type: string
                          enum:
                            - '1'
                          examples:
                            - '1'
                        marktrolle:
                          type: string
                          enum:
                            - LF
                          examples:
                            - LF
                        rollencodenummer:
                          type: string
                          description: Identifiziert den Marktpartner (Marktpartner-ID).
                          examples:
                            - '9980000000029'
                        zuordnungVon:
                          type: string
                          description: >-
                            Beginnzeitpunkt, Zeitpunkt zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden in
                            Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt ein
                            Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit
                            sein)
                          pattern: >-
                            20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
                          examples:
                            - '2023-09-01T00:00:00Z'
                        zuordnungBis:
                          type: string
                          description: >-
                            Endezeitpunkt, Zeitpunkt bis zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden in
                            Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt ein
                            Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit
                            sein)
                          pattern: >-
                            20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
                          examples:
                            - '2023-10-01T00:00:00Z'
                      required:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - zuordnungVon
                        - zuordnungBis
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - zuordnungVon
                        - zuordnungBis
                      x-apidog-ignore-properties: []
                required:
                  - boTyp
                  - versionStruktur
                  - tranchenId
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - tranchenId
                  - bildungTranchengroesse
                  - aufteilungsmenge
                  - marktrollen
                x-apidog-ignore-properties: []
            MESSLOKATION:
              type: array
              items:
                type: object
                properties:
                  boTyp:
                    type: string
                    enum:
                      - MESSLOKATION
                    examples:
                      - MESSLOKATION
                  versionStruktur:
                    type: string
                    enum:
                      - '1'
                    examples:
                      - '1'
                  messlokationsId:
                    type: string
                    pattern: DE\d{11}[A-Z,\d]{20}
                    description: >
                      Identifiziert die Messlokation mittels einer eindeutigen
                      ID | Mapping auf identificationParameterId.meloIds 
                    examples:
                      - DE00014545768S0000000000000003054
                  messlokationszaehler:
                    description: >-
                      Identifiziert das Gerät der Messlokation mittels
                      Gerätenummer.
                    type: array
                    items:
                      type: string
                      examples:
                        - 1SM-8465929523
                  marktrollen:
                    type: array
                    description: >
                      Identifiziert den MSB der Messlokation | Mapping auf
                      dataMeterLocations.dataMeterLocationMeasuringPointOperators                                 
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                          enum:
                            - MARKTTEILNEHMER
                          examples:
                            - MARKTTEILNEHMER
                        versionStruktur:
                          type: string
                          enum:
                            - '1'
                          examples:
                            - '1'
                        marktrolle:
                          type: string
                          enum:
                            - MSB
                          examples:
                            - MSB
                        rollencodenummer:
                          type: string
                          description: Identifiziert den Marktpartner (Marktpartner-ID).
                          examples:
                            - '9980000000029'
                        zuordnungVon:
                          type: string
                          description: >-
                            Beginnzeitpunkt, Zeitpunkt zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden in
                            Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt ein
                            Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit
                            sein)
                          pattern: >-
                            20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
                          examples:
                            - '2023-09-01T00:00:00Z'
                        zuordnungBis:
                          type: string
                          description: >-
                            Endezeitpunkt, Zeitpunkt bis zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden in
                            Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt ein
                            Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit
                            sein)
                          pattern: >-
                            20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
                          examples:
                            - '2023-10-01T00:00:00Z'
                      required:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - zuordnungVon
                        - zuordnungBis
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - zuordnungVon
                        - zuordnungBis
                      x-apidog-ignore-properties: []
                required:
                  - boTyp
                  - versionStruktur
                  - messlokationsId
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - messlokationsId
                  - messlokationszaehler
                  - marktrollen
                x-apidog-ignore-properties: []
            ENERGIELIEFERVERTRAG:
              type: array
              items:
                type: object
                properties:
                  boTyp:
                    type: string
                    enum:
                      - VERTRAG
                    examples:
                      - VERTRAG
                  versionStruktur:
                    type: string
                    enum:
                      - '1'
                    examples:
                      - '1'
                  vertragsart:
                    type: string
                    enum:
                      - ENERGIELIEFERVERTRAG
                    examples:
                      - ENERGIELIEFERVERTRAG
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                          enum:
                            - GESCHAEFTSPARTNER
                          examples:
                            - GESCHAEFTSPARTNER
                        versionStruktur:
                          type: string
                          enum:
                            - '1'
                          examples:
                            - '1'
                        anrede:
                          type: string
                          description: >
                            Angabe des Titels der natürlichen Person | Mapping
                            auf
                            dataMarketLocationAddress.title                        
                          examples:
                            - Prof.Dr.
                        name1:
                          type: string
                          description: >
                            Angabe des Namen des Kunden | Mapping auf
                            dataMarketLocationAddress.surnames oder
                            dataMarketLocationAddress.company, wenn
                            gewerbekennzeichnung =
                            true                          
                          examples:
                            - Becker
                        name2:
                          type: string
                          description: >
                            Angabe des Vornamen des Kunden | Mapping auf
                            dataMarketLocationAddress.firstnames                               
                          examples:
                            - Michael
                        gewerbekennzeichnung:
                          type: boolean
                          description: >
                            Angabe ob gewerblicher oder private
                            Kunde                    
                          examples:
                            - false
                        geschaeftspartnerrolle:
                          type: array
                          items:
                            type: string
                            enum:
                              - KUNDE
                            examples:
                              - KUNDE
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - anrede
                        - name1
                        - name2
                        - gewerbekennzeichnung
                        - geschaeftspartnerrolle
                      x-apidog-ignore-properties: []
                required:
                  - boTyp
                  - versionStruktur
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - vertragsart
                  - vertragspartner2
                x-apidog-ignore-properties: []
            TECHNISCHE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  boTyp:
                    type: string
                    enum:
                      - TECHNISCHE_RESSOURCE
                    examples:
                      - TECHNISCHE_RESSOURCE
                  versionStruktur:
                    type: string
                    enum:
                      - '1'
                    examples:
                      - '1'
                  ressourcenId:
                    type: string
                    description: >
                      Identifiziert die Technische Ressource mittels einer
                      eindeutigen ID | Mapping auf
                      dataTechnicalResources.trId                     
                    examples:
                      - D417MLM8164
                required:
                  - boTyp
                  - versionStruktur
                  - ressourcenId
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - ressourcenId
                x-apidog-ignore-properties: []
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  boTyp:
                    type: string
                    enum:
                      - STEUERBARE_RESSOURCE
                    examples:
                      - STEUERBARE_RESSOURCE
                  versionStruktur:
                    type: string
                    enum:
                      - '1'
                    examples:
                      - '1'
                  ressourcenId:
                    type: string
                    description: >
                      Identifiziert die Steuerbare Ressource mittels einer
                      eindeutigen ID | Mapping auf
                      dataControllableResources.srId                           
                    examples:
                      - C81641SBT77
                  marktrollen:
                    type: array
                    description: >
                      Identifiziert den MSB der steuerbaren Ressource | Mapping
                      auf
                      dataControllableResources.dataControllableResourceMeasuringPointOperators                       
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                          enum:
                            - MARKTTEILNEHMER
                          examples:
                            - MARKTTEILNEHMER
                        versionStruktur:
                          type: string
                          enum:
                            - '1'
                          examples:
                            - '1'
                        marktrolle:
                          type: string
                          enum:
                            - MSB
                          examples:
                            - MSB
                        rollencodenummer:
                          type: string
                          description: Identifiziert den Marktpartner (Marktpartner-ID).
                          examples:
                            - '9980000000029'
                        zuordnungVon:
                          type: string
                          description: >-
                            Beginnzeitpunkt, Zeitpunkt zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden in
                            Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt ein
                            Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit
                            sein)
                          pattern: >-
                            20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
                          examples:
                            - '2023-09-01T00:00:00Z'
                        zuordnungBis:
                          type: string
                          description: >-
                            Endezeitpunkt, Zeitpunkt bis zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden in
                            Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt ein
                            Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit
                            sein)
                          pattern: >-
                            20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
                          examples:
                            - '2023-10-01T00:00:00Z'
                      required:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - zuordnungVon
                        - zuordnungBis
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - zuordnungVon
                        - zuordnungBis
                      x-apidog-ignore-properties: []
                required:
                  - boTyp
                  - versionStruktur
                  - ressourcenId
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - ressourcenId
                  - marktrollen
                x-apidog-ignore-properties: []
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  boTyp:
                    type: string
                    enum:
                      - NETZLOKATION
                    examples:
                      - NETZLOKATION
                  versionStruktur:
                    type: string
                    enum:
                      - '1'
                    examples:
                      - '1'
                  netzlokationsId:
                    type: string
                    description: >
                      Identifiziert die Netzlokation mittels einer eindeutigen
                      ID. | Mapping auf
                      dataNetworkLocations.neloId                    
                    examples:
                      - E1688117482
                  marktrollen:
                    type: array
                    description: >
                      Identifiziert den MSB der Netzlokation | Mapping auf
                      dataNetworkLocations.dataNetworkLocationMeasuringPointOperators                                
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                          enum:
                            - MARKTTEILNEHMER
                          examples:
                            - MARKTTEILNEHMER
                        versionStruktur:
                          type: string
                          enum:
                            - '1'
                          examples:
                            - '1'
                        marktrolle:
                          type: string
                          enum:
                            - MSB
                          examples:
                            - MSB
                        rollencodenummer:
                          type: string
                          description: Identifiziert den Marktpartner (Marktpartner-ID).
                          examples:
                            - '9980000000029'
                        zuordnungVon:
                          type: string
                          description: >-
                            Beginnzeitpunkt, Zeitpunkt zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden in
                            Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt ein
                            Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit
                            sein)
                          pattern: >-
                            20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
                          examples:
                            - '2023-09-01T00:00:00Z'
                        zuordnungBis:
                          type: string
                          description: >-
                            Endezeitpunkt, Zeitpunkt bis zu dem die zugeordneten
                            Marktpartner oder Lokationen zugeordnet werden in
                            Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt ein
                            Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit
                            sein)
                          pattern: >-
                            20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
                          examples:
                            - '2023-10-01T00:00:00Z'
                      required:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - zuordnungVon
                        - zuordnungBis
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - zuordnungVon
                        - zuordnungBis
                      x-apidog-ignore-properties: []
                required:
                  - boTyp
                  - versionStruktur
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - netzlokationsId
                  - marktrollen
                x-apidog-ignore-properties: []
          required:
            - MARKTLOKATION
          x-apidog-orders:
            - MARKTLOKATION
            - BILANZIERUNG
            - TRANCHE
            - MESSLOKATION
            - ENERGIELIEFERVERTRAG
            - TECHNISCHE_RESSOURCE
            - STEUERBARE_RESSOURCE
            - NETZLOKATION
          x-apidog-ignore-properties: []
      required:
        - stammdaten
      x-apidog-orders:
        - stammdaten
      title: ''
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
