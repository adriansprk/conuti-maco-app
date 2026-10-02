# Identifizierung der MaLo

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /identifyMarketlocation:
    post:
      summary: Identifizierung der MaLo
      deprecated: false
      description: >-
        `LESEN_MALOIDENT_BASIS`


        Übergibt die Daten zur Identifikation aller Marktlokationen gemäß
        [Prozessbeschreibung](https://maloident.apidog.io/malo-ident-rolle-nb-860919m0),
        sowie aller Informationen zur Durchführung des EBD E_0594.
      operationId: LESEN_MALOIDENT_BASIS
      tags:
        - Schnittstellen/MaloIdent NB (Backend)
        - IDENTIFIZIERUNG
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LESEN_MALOIDENT_BASIS'
            example:
              stammdaten:
                MARKTLOKATION:
                  - boTyp: MARKTLOKATION
                    versionStruktur: '1'
                    marktlokationsId: '12345678901'
                    energierichtung: AUSSP
                    lokationsadresse:
                      postleitzahl: '76229'
                      ort: Karlsruhe
                      strasse: Greschbachstrasse
                      hausnummer: '3'
                      adresszusatz: ''
                      landescode: DE
              transaktionsdaten:
                ausfuehrungsdatum: '2024-11-07T23:00:00Z'
      responses:
        '200':
          description: Erfolg | Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LESEN_MALOIDENT_BASIS_RESP'
          headers: {}
          x-apidog-name: OK
        '400':
          description: Fehler | Fail
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14666443-run
components:
  schemas:
    LESEN_MALOIDENT_BASIS:
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
                required:
                  - boTyp
                  - versionStruktur
                  - energierichtung
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - marktlokationsId
                  - energierichtung
                  - lokationsadresse
                  - katasterinformation
                  - geokoordinaten
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
                      Mapping auf
                      identificationParameterId.tranchenIds                    
                    examples:
                      - '57685676742'
                required:
                  - boTyp
                  - versionStruktur
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - tranchenId
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
                      ID | Mapping auf
                      identificationParameterId.meloIds                     
                    examples:
                      - DE00014545768S0000000000000003054
                required:
                  - boTyp
                  - versionStruktur
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - messlokationsId
                x-apidog-ignore-properties: []
            ZAEHLER:
              type: array
              items:
                type: object
                properties:
                  boTyp:
                    type: string
                    enum:
                      - ZAEHLER
                    examples:
                      - ZAEHLER
                  versionStruktur:
                    type: string
                    enum:
                      - '1'
                    examples:
                      - '1'
                  zaehlernummer:
                    type: string
                    description: >
                      Identifiziert das Gerät der Messlokation mittels
                      Gerätenummer | Mapping auf
                      identificationParameterId.meterNumbers                  
                    examples:
                      - 1SM-8465929523
                required:
                  - boTyp
                  - versionStruktur
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - zaehlernummer
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
                required:
                  - boTyp
                  - versionStruktur
                x-apidog-orders:
                  - boTyp
                  - versionStruktur
                  - vertragsart
                  - vertragspartner2
                x-apidog-ignore-properties: []
          required:
            - MARKTLOKATION
          x-apidog-orders:
            - MARKTLOKATION
            - TRANCHE
            - MESSLOKATION
            - ZAEHLER
            - ENERGIELIEFERVERTRAG
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          description: >
            Informationscontainer für Daten zum Vorgang und beteiligten
            Marktpartnern
          properties:
            vorgangsnummer:
              type: string
              description: >
                Externe Transaktions-Id zur eindeutigen Identifikation der
                Anfrage der MaLo-ID der Marktlokation des sendenden
                Marktpartners. | Format $UUID RFC4122 | Mapping auf [header]
                transactionId
              examples:
                - f81d4fae-7dec-11d0-a765-00a0c91e6bf6
            nachrichtendatum:
              type: string
              pattern: >-
                20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
              description: >
                Zeitpunkt an dem der Aufruf erstellt wurde in Zeitzone UTC -
                falls der Wert aus dem Backend nicht befüllt ist, wird die
                MaloIdent Lösung das Datum zum Zeitpunkt des Empfang befüllen. |
                Format YYYY-MM-DD'T'HH:mm:ss'Z' | Mapping auf [header]
                creationDateTime
              examples:
                - '2023-08-01T12:30:00Z'
            ausfuehrungsdatum:
              type: string
              pattern: >-
                20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
              description: >
                Zeitpunkt zu dem die Identifikation stattfinden soll in
                angegeben in Zeitzone UTC. (umgerechnet muss dieser Zeitpunkt
                ein Tagesbeginn 00:00 Uhr gesetzlicher deutscher Zeit sein) |
                Format YYYY-MM-DD'T'HH:mm:ss'Z' | Mapping auf
                identificationDateTime
              examples:
                - '2023-08-02T22:00:00Z'
            idempodenzschluessel:
              type: string
              description: >
                Initiale Vorgangsnummer (Format $UUID RFC4122) zur Angabe des
                Idempodenzschlüssel im Falle eines Retry aus dem Backend |
                Format $UUID RFC4122 | Mapping auf [header] initialTransactionId
              examples:
                - f81d4fae-7dec-11d0-a765-00a0c91e6bf6
            absender:
              type: object
              description: Eigene ILN und Rollencodetyp
              properties:
                rollencodenummer:
                  type: string
                  description: Eigene ILN
                  examples:
                    - '9904000000005'
              required:
                - rollencodenummer
              x-apidog-orders:
                - rollencodenummer
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
                    - '9900936000002'
              required:
                - rollencodenummer
              x-apidog-orders:
                - rollencodenummer
              x-apidog-ignore-properties: []
          required:
            - vorgangsnummer
            - ausfuehrungsdatum
            - absender
            - empfaenger
          x-apidog-orders:
            - vorgangsnummer
            - nachrichtendatum
            - ausfuehrungsdatum
            - idempodenzschluessel
            - absender
            - empfaenger
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
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
    LESEN_MALOIDENT_BASIS_RESP:
      description: >-
        Schema für die Basis-Antwort der Maloident-Identifizierung. Das Ergebnis
        ist die Grundlage für die EBD Prüfung
      type: object
      properties:
        maloIdentDaten:
          type: array
          description: Liste von Treffern der Maloident-Suche
          items:
            type: object
            properties:
              lokationsId:
                type: string
                description: Die ID der Marktlokation
                examples:
                  - '74018657187'
              trefferMaloid:
                type: boolean
                description: >-
                  Gibt an, ob primäres Trefferkriterium MaloId ein Treffer war.
                  Die Übereinstimmung der MaLo-ID liegt vor, wenn die
                  vollständige, 11-stellige Zeichenkette übereinstimmt.
              trefferTrancheId:
                type: boolean
                description: >-
                  Gibt an, ob primäres Trefferkriterium TrancheId ein Treffer
                  war. Die Prüfung ist für jede angegebene Tranchen-ID
                  durchzuführen. Die Übereinstimmung der Tranchen-ID liegt vor,
                  wenn die vollständige 11-stellige Zeichenkette übereinstimmt.
              trefferAdresse1:
                type: boolean
                description: >
                  -Gibt an, ob primäres Trefferkriterium Adresse1 ein Treffer
                  war  Die zu prüfende Adresse der Marktlokation besteht aus
                  Straße, Hausnummer/Hausnummernergänzung, PLZ, Ort und
                  Ländercode.  · Bei Marktlokationen ohne zugeordnete
                  Adressdaten kann zudem über das Tupel bestehend aus Gemarkung,
                  Flurnummer und Flurstücknummer identifiziert werden.  · Es
                  kann auch eine Identifizierung über geographische Koordinaten
                  erfolgen.  Bei der Adressprüfung gelten die folgenden Regeln: 
                  · Die Zeichenketten „straße“, „str.“ oder „strasse“ am Ende
                  eines Straßennamens werden durch einen Stern „*“ ersetzt, um
                  damit alle Straßen zu finden, deren Name mit den links vom
                  Stern stehenden Buchstaben beginnen. Der Stern gilt somit als
                  Platzhalter. 
              trefferKundennummer:
                type: boolean
                description: >-
                  Gibt an, ob primäres Trefferkriterium Kundennummer ein Treffer
                  war. Übermittelt wird die Kundennummer des LFA. Die
                  Übereinstimmung der Kundennummer liegt vor, wenn die
                  Zeichenkette der Kundennummer, wie sie dem Kunden mitgeteilt
                  wurde übereinstimmt.
              trefferName:
                type: boolean
                description: >
                  - Gibt an, ob primäres Trefferkriterium Name ein Treffer war. 
                  Der zu prüfende Name besteht bei natürlichen Personen aus dem
                  Vor- und Nachnamen. Bei juristischen Personen aus dem Namen
                  der Firma.  Mindestens folgende Gegebenheiten sollten
                  abgefangen werden:  · Identifikation durch Vertauschen von
                  Vor- und Nachnamen  · Identifikation aus dem String "Vor- und
                  Nachname" gegen jeweils Vor- und Nachname in beide Richtungen
                  (z.B. für Kunden, die im Vor- und Nachnamen jeweils einen
                  kompletten Namen eingetragen haben (Wohngemeinschaften))  ·
                  Angabe der Firmenbezeichnung wird gegen Vor- und Nachnamen
                  sowie dem kompletten String aus "Vor- und Nachname"
                  verglichen.  · Angabe der Kundennummer wird gegen die
                  Kundennummer des LFA verglichen.  · Identifikation aus dem
                  String "Vor- und Nachname" gegen jeweils Vor- und Nachname in
                  beide Richtungen (z.B. für Kunden, die im Vor- und Nachnamen
                  jeweils einen kompletten Namen eingetragen haben
                  (Wohngemeinschaften))  · Angabe der Firmenbezeichnung wird
                  gegen Vor- und Nachnamen sowie dem kompletten String aus "Vor-
                  und Nachname" verglichen. 
              trefferGeraetenummer:
                type: boolean
                description: >
                  - Gibt an, ob primäres Trefferkriterium Gerätenummer ein
                  Treffer war. Die Prüfung ist für jede angegebene Gerätenummer
                  durchzuführen.   - Es sind alle Geräte vom Typ kME, mME und
                  Smart-Meter-Gateways mit der übergebenen Gerätenummer zu
                  suchen.   - Die Reihenfolge der Zeichen in der Gerätenummer
                  ist wichtig.   - Bei einer Prüfung der Gerätenummer ist es
                  wichtig, dass die Reihenfolge der Zeichen identisch ist.   -
                  Die Prüfung ist case-sensitiv.   - Zusätzlich sind schließende
                  Nullen ebenfalls zu ignorieren.   - Dabei sind für jeden
                  Zeichen in der Reihenfolge folgende Regeln zu beachten:   -
                  Zusammen mit schließenden Nullen werden auch alle Zeichen in
                  der Reihenfolge berücksichtigt.   - Eine Identifizierung soll
                  auch erfolgen, wenn ein Marktpartner einen Zähler/Gateway
                  sendet, der bereits im Rahmen eines Gerätewechsels innerhalb
                  der letzten 36 Monate ausgetauscht wurde (Ausnahme
                  Netzbetreiberwechsel).  - Die Übereinstimmung einer
                  Gerätenummer liegt vor, wenn alle Zeichen in genannter
                  Reihenfolge mit der aufgebrachten Nummer auf dem Gerät
                  identisch sind.   - Gegebenenfalls im System vorhandene Prä-
                  und Suffixe sind zu ignorieren. 
              trefferMeloid:
                type: boolean
                description: >-
                  Gibt an, ob primäres Trefferkriterium MeloId ein Treffer war.
                  Die Prüfung ist für jede angegebene MeLo-ID durchzuführen. Die
                  Übereinstimmung der MeLo-ID liegt vor, wenn die vollständige
                  33-stellige Zeichenkette übereinstimmt.
              trefferAdresse2:
                type: boolean
                description: >-
                  Gibt an, ob sekundäres Trefferkriterium zweite Adresse ein
                  Treffer war. Ermittlung, ob ermittelte Malo alle
                  Adressidentifizierungsparameter erfüllt  (Vollständige
                  Adrressprüfung)
              trefferMakorelevant:
                type: boolean
                description: >-
                  Gibt an, ob sekundäres Trefferkriterium Makorelevanz ein
                  Treffer war. Ermittlung, ob ermittelte Malo an der Mako
                  teilnimmt
              trefferStillgelegt:
                type: boolean
                description: >-
                  Gibt an, ob sekundäres Trefferkriterium Stilllegungsstatus ein
                  Treffer war. Ermittlung, ob ermittelte Malo stillgelegt ist.
              trefferNetzgebiet:
                type: boolean
                description: >-
                  Gibt an, ob sekundäres Trefferkriterium Netzgebiet ein Treffer
                  war. Ermittlung, ob ermittelte Malo zum Selektionszeitpunkt
                  einem Netz zugeordnet ist, welches durch eine Serviceanbieter
                  mit Kennzeichen „eigener Service“ versorgt wird.
              trefferNetzgebiet3KJ:
                type: boolean
                description: >-
                  Gibt an, ob sekundäres Trefferkriterium 3KJ-Netzgebiet ein
                  Treffer war.Ermittlung, ob ermittelte Malo zum innerhalb der
                  letzten 3 KJ einem Netz zugeordnet ist oder war, welches durch
                  eine Serviceanbieter mit Kennzeichen „eigener Service“
                  versorgt wird.
            required:
              - lokationsId
              - trefferMaloid
              - trefferTrancheId
              - trefferAdresse1
              - trefferKundennummer
              - trefferName
              - trefferGeraetenummer
              - trefferMeloid
              - trefferAdresse2
              - trefferMakorelevant
              - trefferStillgelegt
              - trefferNetzgebiet
              - trefferNetzgebiet3KJ
            x-apidog-orders:
              - lokationsId
              - trefferMaloid
              - trefferTrancheId
              - trefferAdresse1
              - trefferKundennummer
              - trefferName
              - trefferGeraetenummer
              - trefferMeloid
              - trefferAdresse2
              - trefferMakorelevant
              - trefferStillgelegt
              - trefferNetzgebiet
              - trefferNetzgebiet3KJ
            x-apidog-ignore-properties: []
      required:
        - maloIdentDaten
      x-apidog-orders:
        - maloIdentDaten
      examples:
        - maloIdentDaten:
            - lokationsId: '74018657187'
              trefferMaloid: true
              trefferTrancheId: false
              trefferAdresse1: true
              trefferKundennummer: false
              trefferName: false
              trefferGeraetenummer: false
              trefferMeloid: false
              trefferAdresse2: true
              trefferMakorelevant: true
              trefferStillgelegt: false
              trefferNetzgebiet: true
              trefferNetzgebiet3KJ: true
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
