# ECS Steuerprozess Lieferbeginn

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
      summary: ECS Steuerprozess Lieferbeginn
      deprecated: false
      description: Anmeldung Steuerprozess LW24 Strom (MaloIdent, Kündigung & Anmeldung)
      operationId: ECS_LIEFERBEGINN
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht LF
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BLF%5D%20ECS_LIEFERBEGINN'
            examples:
              '1':
                value:
                  stammdaten:
                    MARKTLOKATION:
                      - boTyp: MARKTLOKATION
                        versionStruktur: '1'
                        marktlokationsId: '57685676748'
                        sparte: STROM
                        energierichtung: AUSSP
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
                        lokationsadresse:
                          postleitzahl: '12117'
                          ort: Berlin
                          strasse: Reinhardtstraße
                          hausnummer: '32'
                          adresszusatz: Ausbau
                          landescode: DE
                        katasterinformation:
                          gemarkung_flur: Musterstadt
                          flurstueck: '123'
                          flurstueckNummer: '456'
                        geokoordinaten:
                          breitengrad: '52.5200'
                          laengengrad: '13.4050'
                          ostwert: '123456'
                          nordwert: '654321'
                          zone: UTMZone31
                          hochwert: '1234567'
                          rechtswert: '7654321'
                    TRANCHE:
                      - boTyp: TRANCHE
                        versionStruktur: '1'
                        tranchenId: '57685676742'
                    MESSLOKATION:
                      - boTyp: MESSLOKATION
                        versionStruktur: '1'
                        messlokationsId: DE00014545768S0000000000000003054
                    ZAEHLER:
                      - boTyp: ZAEHLER
                        versionStruktur: '1'
                        zaehlernummer: 1SM-8465929523
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
                        vertragspartner2:
                          - boTyp: GESCHAEFTSPARTNER
                            versionStruktur: '1'
                            anrede: Prof.Dr.
                            name1: Becker
                            name2: Michael
                            gewerbekennzeichnung: false
                            geschaeftspartnerrolle:
                              - KUNDE
                            externeReferenzen:
                              - exRefName: Kundennummer beim Altlieferanten
                                exRefWert: V567345345
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
                    transaktionsgrund: E03
                    transaktionsgrundergaenzung: ZW4
                    transaktionsgrundergaenzungBefristeteAnmeldung: E03
                    sparte: STROM
                    ausfuehrungsdatum: '2025-04-02T22:00:00Z'
                    absender:
                      rollencodenummer: '9904000000005'
                      rollencodetyp: BDEW
                    empfaenger:
                      rollencodenummer: '9900936000002'
                      rollencodetyp: BDEW
                    beteiligterMarktpartner:
                      rollencodenummer: '9900936000002'
                      rollencodetyp: BDEW
                    vertragsbeginn: '2025-10-31T23:00:00Z'
                    vertragsende: '2025-10-31T23:00:00Z'
                    endezumtermin: '2025-10-31T23:00:00Z'
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: ECS_LIEFERBEGINN
                summary: Maximum
              '2':
                value:
                  stammdaten:
                    MARKTLOKATION:
                      - boTyp: MARKTLOKATION
                        versionStruktur: '1'
                        marktlokationsId: '57685676748'
                        sparte: STROM
                        energierichtung: AUSSP
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
                        vertragspartner2:
                          - boTyp: GESCHAEFTSPARTNER
                            versionStruktur: '1'
                            anrede: Prof.Dr.
                            name1: Becker
                            name2: Michael
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
                    transaktionsgrund: E03
                    transaktionsgrundergaenzung: ZW4
                    sparte: STROM
                    absender:
                      rollencodenummer: '9904000000005'
                      rollencodetyp: BDEW
                    empfaenger:
                      rollencodenummer: '9900936000002'
                      rollencodetyp: BDEW
                    beteiligterMarktpartner:
                      rollencodenummer: '9900936000002'
                      rollencodetyp: BDEW
                    vertragsbeginn: '2025-10-31T23:00:00Z'
                    endezumtermin: '2025-10-31T23:00:00Z'
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: ECS_LIEFERBEGINN
                summary: Min Kdg u Anm
              '3':
                value:
                  stammdaten:
                    MARKTLOKATION:
                      - boTyp: MARKTLOKATION
                        versionStruktur: '1'
                        marktlokationsId: '57685676748'
                        sparte: STROM
                        energierichtung: AUSSP
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
                        vertragspartner2:
                          - boTyp: GESCHAEFTSPARTNER
                            versionStruktur: '1'
                            anrede: Prof.Dr.
                            name1: Becker
                            name2: Michael
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
                    transaktionsgrund: E03
                    transaktionsgrundergaenzung: ZW4
                    sparte: STROM
                    absender:
                      rollencodenummer: '9904000000005'
                      rollencodetyp: BDEW
                    empfaenger:
                      rollencodenummer: '9900936000002'
                      rollencodetyp: BDEW
                    vertragsbeginn: '2025-10-31T23:00:00Z'
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: ECS_LIEFERBEGINN
                summary: Min Anm
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14958780-run
components:
  schemas:
    '[LF] ECS_LIEFERBEGINN':
      type: object
      properties:
        stammdaten:
          type: object
          description: >
            Informationscontainer für Stammdaten, die zur Identifizierung
            genutzt werden
          properties:
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    pattern: \d{11}
                    description: >
                      Identifiziert die Marktlokation mittels einer eindeutigen
                      ID | Mapping auf
                      identificationParameterId.maloId                   
                    examples:
                      - '57685676748'
                  energierichtung:
                    $ref: '#/components/schemas/Energierichtung'
                    description: >
                      Energieflussrichtung der Marktlokation | Mapping auf
                      energyDirection                    
                  lokationsadresse:
                    $ref: '#/components/schemas/Adresse'
                    description: >
                      Angabe des Ortes, Postleitzahl, Ländercode, Straße,
                      Hausnummer, Hausnummernergänzung der Marktlokationsadresse
                      | Mapping auf
                      identificationParameterAddress                    
                  katasterinformation:
                    $ref: '#/components/schemas/Katasteradresse'
                    description: >
                      Angabe des Gemarkungsnamens, Flurnummer, Flurstücksnummer
                      (des Flurstücks) der Marktlokationsadresse | Mapping auf
                      identificationParameterAddress.landParcels                    
                  geokoordinaten:
                    $ref: '#/components/schemas/Geokoordinaten'
                    description: >
                      Angabe der Breite (Breitengrad), Angabe der Breite
                      (Breitengrad), UTM Ostwert, UTM Nordwert, Gauß-Krüger
                      Hochwert, Gauß-Krüger Rechtswert  | Mapping auf
                      identificationParameterAddress.geographicCoordinates                    
                  erforderlichesProduktpaket:
                    $ref: '#/components/schemas/Produktpaket'
                x-apidog-orders:
                  - marktlokationsId
                  - energierichtung
                  - lokationsadresse
                  - katasterinformation
                  - geokoordinaten
                  - erforderlichesProduktpaket
                required:
                  - energierichtung
                  - erforderlichesProduktpaket
                x-apidog-refs: {}
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  tranchenId:
                    type: string
                    pattern: \d{11}
                    description: >
                      Identifiziert die Tranche mittels einer eindeutigen ID |
                      Mapping auf
                      identificationParameterId.tranchenIds                    
                    examples:
                      - '57685676742'
                x-apidog-orders:
                  - tranchenId
                x-apidog-ignore-properties: []
            MESSLOKATION:
              type: array
              items:
                type: object
                properties:
                  messlokationsId:
                    type: string
                    pattern: DE\d{11}[A-Z,\d]{20}
                    description: >
                      Identifiziert die Messlokation mittels einer eindeutigen
                      ID | Mapping auf
                      identificationParameterId.meloIds                     
                    examples:
                      - DE00014545768S0000000000000003054
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
                    description: >
                      Identifiziert das Gerät der Messlokation mittels
                      Gerätenummer | Mapping auf
                      identificationParameterId.meterNumbers                  
                    examples:
                      - 1SM-8465929523
                x-apidog-orders:
                  - zaehlernummer
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
                            - GESCHAEFTSPARTNER
                          default: GESCHAEFTSPARTNER
                        versionStruktur:
                          type: string
                          enum:
                            - '1'
                          default: '1'
                        anrede:
                          type: string
                          description: >
                            Angabe des Titels der natürlichen Person | Mapping
                            auf
                            identificationParameterAddress.name.title                        
                          examples:
                            - Prof.Dr.
                        name1:
                          type: string
                          description: >
                            Angabe des Namen des Kunden | Mapping auf
                            identificationParameterAddress.name.surnames oder
                            identificationParameterAddress.name.company, wenn
                            gewerbekennzeichnung =
                            true                          
                          examples:
                            - Becker
                        name2:
                          type: string
                          description: >
                            Angabe des Vornamen des Kunden | Mapping auf
                            identificationParameterAddress.name.firstnames                               
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
                        externeReferenzen:
                          type: array
                          description: >
                            Zur Angabe der Kundennummer des Kunden beim
                            bisherigen Lieferanten (LFA)                        
                          items:
                            type: object
                            properties:
                              exRefName:
                                type: string
                                enum:
                                  - Kundennummer beim Altlieferanten
                                examples:
                                  - Kundennummer beim Altlieferanten
                              exRefWert:
                                type: string
                                description: >
                                  Kundennummer des Kunden beim bisherigen
                                  Lieferanten
                                  (LFA)                              
                                examples:
                                  - V567345345
                            x-apidog-orders:
                              - exRefName
                              - exRefWert
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - anrede
                        - name1
                        - name2
                        - gewerbekennzeichnung
                        - geschaeftspartnerrolle
                        - externeReferenzen
                      x-apidog-ignore-properties: []
                x-apidog-orders:
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
                  vertragsende:
                    type: string
                    format: date-time
                x-apidog-orders:
                  - vertragsart
                  - vertragsende
                required:
                  - vertragsende
                x-apidog-ignore-properties: []
          required:
            - MARKTLOKATION
          x-apidog-orders:
            - MARKTLOKATION
            - TRANCHE
            - MESSLOKATION
            - ZAEHLER
            - ENERGIELIEFERVERTRAG
            - NETZNUTZUNGSVERTRAG
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          description: >
            Informationscontainer für Daten zum Vorgang und beteiligten
            Marktpartnern
          properties:
            ausfuehrungsdatum:
              type: string
              pattern: >-
                20(\d{2}(\-(0[13578]|1[02])\-(0[1-9]|[12]\d|3[01])|\-02\-(0[1-9]|1\d|2[0-8])|\-(0[469]|11)\-(0[1-9]|[12]\d|30))|([02468][048]|[13579][26])\-02\-(29))T([01]\d|2[0-3]):[0-5]\d:[0-5]\dZ
              description: >
                Zeitpunkt zu dem die Identifikation stattfinden soll in
                angegeben in Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt
                ein Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit sein) |
                Format YYYY-MM-DD'T'HH:mm:ss'Z' 
              examples:
                - '2023-08-02T22:00:00Z'
            absender:
              type: object
              description: Eigene ILN und Rollencodetyp
              properties:
                rollencodenummer:
                  type: string
                  description: Eigene ILN
                  examples:
                    - '9979052000006'
                rollencodetyp: &ref_0
                  $ref: '#/components/schemas/Rollencodetyp'
              required:
                - rollencodenummer
                - rollencodetyp
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              description: >-
                ILN und Rollencodetyp des Netzbetreibers, an den die
                Identanfrage gestellt werden soll
              properties:
                rollencodenummer:
                  type: string
                  description: >-
                    ILN des Netzbetreibers, an den die Identanfrage gestellt
                    werden soll
                  examples:
                    - '9900683000008'
                rollencodetyp: *ref_0
              required:
                - rollencodenummer
                - rollencodetyp
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            beteiligterMarktpartner:
              type: object
              description: >-
                Identifiziert den LFA an den die Kündigung gesendet werden soll.
                Ist das Feld leer, wird keine Kündigung ausgelöst
              properties:
                rollencodenummer:
                  type: string
                  description: Identifiziert den Alterlieferanten (Marktpartner-ID).
                  examples:
                    - '9903526000002'
                rollencodetyp: *ref_0
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            vertragsbeginn:
              type: string
              pattern: >-
                20(\d{2}(\-(0[13578]|1[02])\-(0[1-9]|[12]\d|3[01])|\-02\-(0[1-9]|1\d|2[0-8])|\-(0[469]|11)\-(0[1-9]|[12]\d|30))|([02468][048]|[13579][26])\-02\-(29))T([01]\d|2[0-3]):[0-5]\d:[0-5]\dZ
              description: >
                Datum zur Anmeldung des Lieferbeginn (DTM+92) angegeben in
                Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt ein Tagesbeginn
                00:00 Uhr gesetzlicher deutscher Zeit sein) | Format
                YYYY-MM-DD'T'HH:mm:ss'Z' | Mapping auf
                identificationDateTime            
              examples:
                - '2023-08-02T22:00:00Z'
            vertragsende:
              type: string
              pattern: >-
                20(\d{2}(\-(0[13578]|1[02])\-(0[1-9]|[12]\d|3[01])|\-02\-(0[1-9]|1\d|2[0-8])|\-(0[469]|11)\-(0[1-9]|[12]\d|30))|([02468][048]|[13579][26])\-02\-(29))T([01]\d|2[0-3]):[0-5]\d:[0-5]\dZ
              description: >
                Kündigung zum fixen Termin (DTM+93) angegeben in Zeitzone UTC.
                (umgerechnet muss dieser Zeitpunkt ein Tagesbeginn 00:00 Uhr
                gesetzlicher deutscher Zeit sein) | Format
                YYYY-MM-DD'T'HH:mm:ss'Z' | Mapping auf identificationDateTime
              examples:
                - '2023-08-02T22:00:00Z'
            endezumtermin:
              type: string
              pattern: >-
                20(\d{2}(\-(0[13578]|1[02])\-(0[1-9]|[12]\d|3[01])|\-02\-(0[1-9]|1\d|2[0-8])|\-(0[469]|11)\-(0[1-9]|[12]\d|30))|([02468][048]|[13579][26])\-02\-(29))T([01]\d|2[0-3]):[0-5]\d:[0-5]\dZ
              description: >
                Kündigung zum nächstmöglichen Termin (DTM+471) ab diesem
                Zeitpunkt angegeben in Zeitzone UTC. (umgerechnet muss dieser
                Zeitpunkt ein Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit
                sein) | Format YYYY-MM-DD'T'HH:mm:ss'Z' 
              examples:
                - '2023-08-02T22:00:00Z'
            transaktionsgrund:
              type: string
              description: >
                Transaktionsgrund, der in Anmeldung gesendet werden soll : E01
                Ein-/Auszug (Umzug) / E03 Wechsel 
              examples:
                - E03
            transaktionsgrundergaenzung:
              type: string
              description: >
                Transaktionsgrundergaenzung der Anmeldung: ZW3 Erzeugende
                Marktlokation / ZW4 Verbrauchende Marktlokation / ZW5 Tranche /
                ZW6 Pauschale Marktlokation / ZW7 Gemessene Marktlokation / ZAP
                ruhende Marktlokation
              examples:
                - ZW4
            transaktionsgrundergaenzungBefristeteAnmeldung:
              type: string
              description: >
                Transaktionsgrundergaenzung befristete Anmeldung: E01
                Ein-/Auszug (Umzug) / E03 Wechsel      
              examples:
                - E01
            sparte:
              type: string
          required:
            - ausfuehrungsdatum
            - absender
            - empfaenger
            - transaktionsgrund
            - transaktionsgrundergaenzung
            - sparte
          x-apidog-orders:
            - ausfuehrungsdatum
            - absender
            - empfaenger
            - beteiligterMarktpartner
            - vertragsbeginn
            - vertragsende
            - endezumtermin
            - transaktionsgrund
            - transaktionsgrundergaenzung
            - transaktionsgrundergaenzungBefristeteAnmeldung
            - sparte
          x-apidog-ignore-properties: []
        zusatzdaten:
          type: object
          description: |
            Informationscontainer zur Identifikation des Prozesses
          properties:
            prozessId:
              type: string
              description: Id des Dokuments / Beleges im Backend.
              examples:
                - 00505688-E4A2-1EDF-A0C2-C81842E2515E
            eventname:
              type: string
              description: Name des Events
              enum:
                - ECS_LIEFERBEGINN
              default: ECS_LIEFERBEGINN
          required:
            - prozessId
            - eventname
          x-apidog-orders:
            - prozessId
            - eventname
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
        - zusatzdaten
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
        - zusatzdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Rollencodetyp:
      type: string
      title: Rollencodetyp
      description: Rollencodetyp
      enum:
        - BDEW
        - GS1
        - GLN
        - DVGW
      x-apidog-enum:
        - value: BDEW
          name: DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)
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
    Geokoordinaten:
      title: Geokoordinaten
      type: object
      properties:
        breitengrad:
          type: string
          description: Gibt den Breitengrad eines entsprechenden Ortes an.
        laengengrad:
          type: string
          description: Gibt den Längengrad eines entsprechenden Ortes an.
        ostwert:
          type: string
          description: Gibt den Ostwert eines entsprechenden Ortes an.
        nordwert:
          type: string
          description: Gibt den Nordwert eines entsprechenden Ortes an.
        zone:
          $ref: '#/components/schemas/Zone'
          description: UTM Zone 31, 32, 33
        hochwert:
          type: string
          description: Gibt den Hochwert eines entsprechenden Ortes an.
        rechtswert:
          type: string
          description: Gibt den Rechtswert eines entsprechenden Ortes an.
      x-apidog-orders:
        - breitengrad
        - laengengrad
        - ostwert
        - nordwert
        - zone
        - hochwert
        - rechtswert
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zone:
      title: Zone
      type: string
      enum:
        - UTMZone31
        - UTMZone32
        - UTMZone33
      description: Zone
      x-apidog-folder: ''
    Katasteradresse:
      title: Katasteradresse
      type: object
      properties:
        gemarkung_flur:
          type: string
          description: Gemarkung Flur
        flurstueck:
          type: string
          description: Flurstück Name
        flurstueckNummer:
          type: string
          description: Flurstück Nummer
      x-apidog-orders:
        - gemarkung_flur
        - flurstueck
        - flurstueckNummer
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Adresse:
      title: Adresse
      type: object
      properties:
        postleitzahl:
          type: string
          description: Postleitzahl
        ort:
          type: string
          description: Ort
        strasse:
          type: string
          description: Strasse
        hausnummer:
          type: string
          description: Hausnummer und Ergänzung
        postfach:
          type: string
          description: Postfach
        adresszusatz:
          type: string
          description: Adresszusatz
        coErgaenzung:
          type: string
          description: coErgaenzung
        landescode:
          $ref: '#/components/schemas/Landescode'
          description: Landescode
        ortsteil:
          type: string
          description: Ortsteil
        zusatzInformation:
          $ref: '#/components/schemas/AdresszusatzInformation'
          description: Zusatzinformation zur Identifizierung, Zeile für Name und Anschrift
      x-apidog-orders:
        - postleitzahl
        - ort
        - strasse
        - hausnummer
        - postfach
        - adresszusatz
        - coErgaenzung
        - landescode
        - ortsteil
        - zusatzInformation
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    AdresszusatzInformation:
      title: AdresszusatzInformation
      type: object
      properties:
        zusatz1:
          type: string
          description: Adresszusatz 1
        zusatz2:
          type: string
          description: Adresszusatz 2
        zusatz3:
          type: string
          description: Adresszusatz 3
        zusatz4:
          type: string
          description: Adresszusatz 4
        zusatz5:
          type: string
          description: Adresszusatz 5
      x-apidog-orders:
        - zusatz1
        - zusatz2
        - zusatz3
        - zusatz4
        - zusatz5
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Landescode:
      title: Landescode
      type: string
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
      description: Der ISO-Landescode als Enumeration
      x-apidog-folder: ''
    Energierichtung:
      type: string
      title: Energierichtung
      description: Spezifiziert die Energierichtung einer Markt- und/oder Messlokation
      enum:
        - AUSSP
        - EINSP
      x-apidog-enum:
        - value: AUSSP
          name: Verbrauch
          description: 'Z07 / Z71 '
        - value: EINSP
          name: Erzeugung
          description: 'Z06 / Z72 '
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
