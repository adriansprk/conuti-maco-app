# Übermittlung von Zählerständen vom NB

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
      summary: Übermittlung von Zählerständen vom NB
      deprecated: false
      description: Übermittlung von Zählerständen vom NB
      operationId: Übermittlung von Zählerständen vom NB
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/START_ERHEBUNG_MESSWERTE'
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
      x-apidog-folder: Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-28679013-run
components:
  schemas:
    START_ERHEBUNG_MESSWERTE:
      type: object
      properties:
        '0':
          type: object
          properties: {}
        '1':
          type: object
          properties:
            Zusatzdaten:
              type: object
              properties:
                prozessId:
                  type: string
                  description: >-
                    Id des Dokuments / Beleges im Backend. Wird genutzt um die
                    Antwort zuzuordnen.
                  x-apidog-mock: '{{$string.uuid}}'
              x-apidog-orders:
                - prozessId
              required:
                - prozessId
              x-apidog-ignore-properties: []
            eventname:
              type: string
              description: Name des Events
          x-apidog-orders:
            - Zusatzdaten
            - eventname
          required:
            - Zusatzdaten
            - eventname
          x-apidog-ignore-properties: []
      x-apidog-orders:
        - '0'
        - '1'
      required:
        - '0'
        - '1'
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
