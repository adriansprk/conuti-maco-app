# Prozessdaten aktualisieren

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
      summary: Prozessdaten aktualisieren
      deprecated: false
      description: >-
        `AKTUALISIEREN_PROZESSDATEN`


        Übergabe der Antwort des Netzbetreibers. Im positiven Fall mit den
        Stammdaten der identifizierten Marktlokation, den Informationen der
        Transaktion, sowie Referenz auf ursprüngliche Anfrage, die im Backend
        des Lieferanten verbucht werden sollen.
      operationId: AKTUALISIEREN_PROZESSDATEN
      tags:
        - Schnittstellen/MaLo-Ident
        - POSITIV
        - NEGATIV
        - LIEFERANT
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              oneOf:
                - $ref: >-
                    #/components/schemas/MaloIdent%20-%20negative%20Antwort%2003003
                - $ref: >-
                    #/components/schemas/MaloIdent%20-%20positive%20Antwort%2003002
            examples:
              '1':
                value:
                  transaktionsdaten:
                    vorgangsnummer: f81d4fae-7dec-11d0-a765-00a0c91e6bf6
                    nachrichtendatum: '2023-08-01T12:30:00Z'
                    idempodenzschluessel: f81d4fae-7dec-11d0-a765-00a0c91e6bf6
                    vorgangsreferenznummer: f81d4fae-7dec-11d0-a765-00a0c91e6bf7
                    antwortstatusCodeliste: E_0594
                    antwortstatus: A10
                    freitext:
                      freitext1: Ich bin ein Freitext
                    beteiligterMarktpartner:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      marktrolle: NB
                      rollencodenummer: '9900987654321'
                    absender:
                      rollencodenummer: '9900936000002'
                    empfaenger:
                      rollencodenummer: '9904000000005'
                    pruefidentifikator: '03003'
                  zusatzdaten:
                    referenzProzessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    targetBusinessKey: f81d4fae-7dec-11d0-a765-00a0c91e6bf6
                summary: '03003'
              '2':
                value:
                  data:
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
                    transaktionsdaten:
                      vorgangsnummer: f81d4fae-7dec-11d0-a765-00a0c91e6bf6
                      nachrichtendatum: '2023-08-01T12:30:00Z'
                      idempodenzschluessel: f81d4fae-7dec-11d0-a765-00a0c91e6bf6
                      vorgangsreferenznummer: f81d4fae-7dec-11d0-a765-00a0c91e6bf7
                      absender:
                        rollencodenummer: '9900936000002'
                      empfaenger:
                        rollencodenummer: '9904000000005'
                      pruefidentifikator: '03002'
                    zusatzdaten:
                      referenzProzessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                      targetBusinessKey: f81d4fae-7dec-11d0-a765-00a0c91e6bf6
                summary: '03002'
      responses:
        '201':
          description: Die Antwort wurde erfolgreich empfangen und zur Verbuchung übergeben
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apidog-orders: []
                x-apidog-ignore-properties: []
          headers: {}
          x-apidog-name: Created
        '400':
          description: >-
            Fehler - die Antwort konnte nicht erfolgreich zur Verbuchung
            übergeben werden
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
      x-apidog-folder: Schnittstellen/MaLo-Ident
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-15144289-run
components:
  schemas:
    MaloIdent - positive Antwort 03002:
      description: Schema positive Antwort auf eine MaloIdent Anfrage via API-Webdienst
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
            vorgangsreferenznummer:
              type: string
              description: >
                Externe Vorgangsreferenz zur eindeutigen Identifikation der
                ursprünglichen Anfrage (Wert aus transactionId, Schritt1 des UC
                Ermittlung der MaLo-ID der Marktlokation). | Format $UUID
                RFC4122 | Mapping auf [query] referenceID
              examples:
                - f81d4fae-7dec-11d0-a765-00a0c91e6bf6
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
              description: >-
                ILN und Rollencodetyp des Netzbetreibers, der auf die MaloIdent
                Anfrage geantwortet hat
              properties:
                rollencodenummer:
                  type: string
                  description: >-
                    ILN des Netzbetreibers, der auf die MaloIdent Anfrage
                    geantwortet hat
                  examples:
                    - '9900936000002'
              required:
                - rollencodenummer
              x-apidog-orders:
                - rollencodenummer
              x-apidog-ignore-properties: []
            empfaenger:
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
            pruefidentifikator:
              type: string
              description: Enthält den intern vergebenen Prüfidentifikator 03002
          required:
            - vorgangsnummer
            - absender
            - empfaenger
            - pruefidentifikator
          x-apidog-orders:
            - vorgangsnummer
            - nachrichtendatum
            - vorgangsreferenznummer
            - idempodenzschluessel
            - absender
            - empfaenger
            - pruefidentifikator
          x-apidog-ignore-properties: []
        zusatzdaten:
          type: object
          description: |
            Informationscontainer zur Identifikation des Prozesses
          properties:
            prozessId:
              type: string
              description: >-
                Referenz Id der Anfrage Dokuments / Beleges im Backend. Kann
                genutzt werden um die Antwort zuzuordnen.
              examples:
                - 00505688-E4A2-1EDF-A0C2-C81842E2515E
              x-apidog-mock: '{{$string.uuid}}'
              nullable: true
            targetBusinessKey:
              type: string
              x-apidog-mock: '{{$string.uuid}}'
              description: BusinessKey des initialen Prozesses
              nullable: true
          required:
            - prozessId
            - targetBusinessKey
          x-apidog-orders:
            - prozessId
            - targetBusinessKey
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
    MaloIdent - negative Antwort 03003:
      description: Schema negative Antwort auf eine MaloIdent Anfrage via API-Webdienst
      type: object
      properties:
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
            vorgangsreferenznummer:
              type: string
              description: >
                Externe Vorgangsreferenz zur eindeutigen Identifikation der
                ursprünglichen Anfrage (Wert aus transactionId, Schritt1 des UC
                Ermittlung der MaLo-ID der Marktlokation). | Format $UUID
                RFC4122 | Mapping auf [query] referenceID
              examples:
                - f81d4fae-7dec-11d0-a765-00a0c91e6bf6
            idempodenzschluessel:
              type: string
              description: >
                Initiale Vorgangsnummer (Format $UUID RFC4122) zur Angabe des
                Idempodenzschlüssel im Falle eines Retry aus dem Backend |
                Format $UUID RFC4122 | Mapping auf [header] initialTransactionId
              examples:
                - f81d4fae-7dec-11d0-a765-00a0c91e6bf6
            antwortstatusCodeliste:
              type: string
              description: >
                Angabe des Entscheidungsbaums aus dem edi@energy Dokument
                "Entscheidungsbaum-Diagramme und Codelisten für die
                Antwortnachrichten" als Grundlage für den negativen Antwortgrund
                | Format E_\d{4} | Mapping auf decisionTree           
              examples:
                - E_0594
            antwortstatus:
              type: string
              description: >
                Angabe des Antwortgrundes des in decisionTree genannten
                Entscheidungsbaums. | Format A[A-Z\d]{2} | Mapping auf
                responseCode          
              examples:
                - A10
            freitext:
              type: object
              description: >
                Angabe der weiteren Erläuterung zum in responseCode genannten
                Antwortgrundes sofern dies gemäß dem in decisionTree genannten
                Entscheidungsbaums zulässig ist. | Mapping auf reason           
              properties:
                freitext1:
                  type: string
                  examples:
                    - Ich bin ein Freitext.
              required:
                - freitext1
              x-apidog-orders:
                - freitext1
              x-apidog-ignore-properties: []
            absender:
              type: object
              description: >-
                ILN und Rollencodetyp des Netzbetreibers, der auf die MaloIdent
                Anfrage geantwortet hat
              properties:
                rollencodenummer:
                  type: string
                  description: >-
                    ILN des Netzbetreibers, der auf die MaloIdent Anfrage
                    geantwortet hat
                  examples:
                    - '9900936000002'
              required:
                - rollencodenummer
              x-apidog-orders:
                - rollencodenummer
              x-apidog-ignore-properties: []
            empfaenger:
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
            beteiligterMarktpartner:
              type: object
              description: >-
                Identifiziert den korrekten Netzbetreiber falls sich die
                Marktlokation nicht mehr im Netzgebiet des Senders befindet
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
                    - NB
                  examples:
                    - NB
                rollencodenummer:
                  type: string
                  description: Identifiziert den Marktpartner (Marktpartner-ID).
                  examples:
                    - '9980000000029'
                rollencodetyp:
                  type: object
                  properties: {}
                  x-apidog-orders: []
                  x-apidog-ignore-properties: []
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: Enthält den intern vergebenen Prüfidentifikator 03003
          required:
            - vorgangsnummer
            - absender
            - empfaenger
            - pruefidentifikator
          x-apidog-orders:
            - vorgangsnummer
            - nachrichtendatum
            - vorgangsreferenznummer
            - idempodenzschluessel
            - antwortstatusCodeliste
            - antwortstatus
            - freitext
            - absender
            - empfaenger
            - beteiligterMarktpartner
            - pruefidentifikator
          x-apidog-ignore-properties: []
        zusatzdaten:
          type: object
          description: |
            Informationscontainer zur Identifikation des Prozesses
          properties:
            prozessId:
              type: string
              description: >-
                Referenz Id der Anfrage Dokuments / Beleges im Backend. Kann
                genutzt werden um die Antwort zuzuordnen.
              examples:
                - 00505688-E4A2-1EDF-A0C2-C81842E2515E
              x-apidog-mock: '{{$string.uuid}}'
              nullable: true
            targetBusinessKey:
              type: string
              x-apidog-mock: '{{$string.uuid}}'
              description: BusinessKey des initialen Prozesses
              nullable: true
          required:
            - prozessId
            - targetBusinessKey
          x-apidog-orders:
            - prozessId
            - targetBusinessKey
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - zusatzdaten
      x-apidog-orders:
        - transaktionsdaten
        - zusatzdaten
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
