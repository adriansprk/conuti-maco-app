# Übermittlung der Berechnungsformel

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
      summary: Übermittlung der Berechnungsformel
      deprecated: false
      description: >-
        Triggert den Versand der Berechnungsformel nach Abschluss des
        Lieferbeginn an den Lieferant oder als Einzelevent an den
        Messstellenbetreiber durch die MACO APP. Die Anfrage wird identifiziert
        durch den Eventnamen START_BERECHNUNGSFORMEL. Zusätzlich ist eine
        eindeutige ID prozessId aus dem Backend mit zu übergeben, mit der die
        spätere Antwort vom Marktpartner wieder an das Backend übergeben werden
        kann.
      operationId: START_BERECHNUNGSFORMEL
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BNB%5D%20START_BERECHNUNGSFORMEL'
            examples:
              '1':
                value:
                  stammdaten:
                    VERWENDUNGSZEITRAUM:
                      - boTyp: VERWENDUNGSZEITRAUM
                        versionStruktur: '1'
                        zeitraumId: 1
                        datenqualitaet: GUELTIGE_DATEN
                        verwendungAb: '2025-02-28T23:00:00Z'
                    BERECHNUNGSFORMEL:
                      - boTyp: BERECHNUNGSFORMEL
                        versionStruktur: '1'
                        gueltigkeitszeitraum:
                          zeitraumId: 1
                          startdatum: '2025-02-28T23:00:00Z'
                        notwendigkeit: BERECHNUNGSFORMEL_NICHT_NOTWENDIG
                  transaktionsdaten:
                    sparte: STROM
                    absender:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      marktrolle: NB
                      gewerbekennzeichnung: true
                      rollencodenummer: '9900683000008'
                      rollencodetyp: BDEW
                    empfaenger:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      marktrolle: LF
                      gewerbekennzeichnung: true
                      rollencodenummer: '9979052000006'
                      rollencodetyp: BDEW
                    lokationsId: '50754496000'
                    lokationsTyp: MALO
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_BERECHNUNGSFORMEL
                summary: 25001 Marktlokation / Z41
              '2':
                value:
                  stammdaten:
                    VERWENDUNGSZEITRAUM:
                      - boTyp: VERWENDUNGSZEITRAUM
                        versionStruktur: '1'
                        zeitraumId: 1
                        datenqualitaet: GUELTIGE_DATEN
                        verwendungAb: '2025-02-28T23:00:00Z'
                    BERECHNUNGSFORMEL:
                      - boTyp: BERECHNUNGSFORMEL
                        versionStruktur: '1'
                        gueltigkeitszeitraum:
                          zeitraumId: 1
                          startdatum: '2025-02-28T23:00:00Z'
                        notwendigkeit: BERECHNUNGSFORMEL_TRIVIAL
                  transaktionsdaten:
                    sparte: STROM
                    absender:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      marktrolle: NB
                      gewerbekennzeichnung: true
                      rollencodenummer: '9900683000008'
                      rollencodetyp: BDEW
                    empfaenger:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      marktrolle: LF
                      gewerbekennzeichnung: true
                      rollencodenummer: '9979052000006'
                      rollencodetyp: BDEW
                    lokationsId: E1688117482
                    lokationsTyp: NELO
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_BERECHNUNGSFORMEL
                summary: 25001 Netzlokation / Z40
              '3':
                value:
                  stammdaten:
                    VERWENDUNGSZEITRAUM:
                      - boTyp: VERWENDUNGSZEITRAUM
                        versionStruktur: '1'
                        zeitraumId: 1
                        datenqualitaet: GUELTIGE_DATEN
                        verwendungAb: '2025-02-28T23:00:00Z'
                    BERECHNUNGSFORMEL:
                      - boTyp: BERECHNUNGSFORMEL
                        versionStruktur: '1'
                        gueltigkeitszeitraum:
                          zeitraumId: 1
                          startdatum: '2025-02-28T23:00:00Z'
                        notwendigkeit: BERECHNUNGSFORMEL_MUSS_ANGEFRAGT_WERDEN
                  transaktionsdaten:
                    sparte: STROM
                    absender:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      marktrolle: NB
                      gewerbekennzeichnung: true
                      rollencodenummer: '9900683000008'
                      rollencodetyp: BDEW
                      ansprechpartner:
                        boTyp: ANSPRECHPARTNER
                        versionStruktur: '1'
                        nachname: Max Mustermannn
                        eMailAdresse: m.mustermann@email.de
                    empfaenger:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      marktrolle: LF
                      gewerbekennzeichnung: true
                      rollencodenummer: '9979052000006'
                      rollencodetyp: BDEW
                    lokationsId: '50754496000'
                    lokationsTyp: MALO
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_BERECHNUNGSFORMEL
                summary: 25001 Marktlokation / Z34
              '4':
                value:
                  stammdaten:
                    VERWENDUNGSZEITRAUM:
                      - boTyp: VERWENDUNGSZEITRAUM
                        versionStruktur: '1'
                        zeitraumId: 1
                        datenqualitaet: GUELTIGE_DATEN
                        verwendungAb: '2025-02-28T23:00:00Z'
                    BERECHNUNGSFORMEL:
                      - boTyp: BERECHNUNGSFORMEL
                        versionStruktur: '1'
                        gueltigkeitszeitraum:
                          zeitraumId: 1
                          startdatum: '2025-02-28T23:00:00Z'
                        notwendigkeit: BERECHNUNGSFORMEL_NOTWENDIG
                        rechenschrittId: 1
                        rechenschritte:
                          - rechenschrittBestandteilId: 1
                            operation: ADDITION
                            messlokationsId: DE0009697056900614312080040415222
                            energieflussrichtung: AUSSP
                          - rechenschrittBestandteilId: 1
                            operation: ADDITION
                            messlokationsId: DE0009697056900614312080040415333
                            energieflussrichtung: AUSSP
                  transaktionsdaten:
                    sparte: STROM
                    absender:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      marktrolle: NB
                      gewerbekennzeichnung: true
                      rollencodenummer: '9900683000008'
                      rollencodetyp: BDEW
                    empfaenger:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      marktrolle: LF
                      gewerbekennzeichnung: true
                      rollencodenummer: '9979052000006'
                      rollencodetyp: BDEW
                    lokationsId: '52754496222'
                    lokationsTyp: MALO
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_BERECHNUNGSFORMEL
                summary: 25001 Marktlokation / Z33 / Addition 2 Messlokationen
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-15090201-run
components:
  schemas:
    '[NB] START_BERECHNUNGSFORMEL':
      allOf:
        - $ref: '#/components/schemas/PI_25001'
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
                  const: START_BERECHNUNGSFORMEL
                  default: START_BERECHNUNGSFORMEL
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
    PI_25001:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            BERECHNUNGSFORMEL:
              type: array
              items:
                type: object
                properties:
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                      startdatum:
                        type: string
                        format: date-time
                      enddatum:
                        type: string
                        format: date-time
                    x-apidog-orders:
                      - zeitraumId
                      - startdatum
                      - enddatum
                    required:
                      - zeitraumId
                      - startdatum
                    x-apidog-ignore-properties: []
                  notwendigkeit:
                    type: string
                  rechenschrittId:
                    type: integer
                  rechenschritte:
                    type: array
                    items:
                      type: object
                      properties:
                        rechenschrittBestandteilId:
                          type: integer
                        referenzRechenschrittId:
                          type: integer
                        operation:
                          type: string
                        verlustfaktorTrafo:
                          type: integer
                        verlustfaktorLeitung:
                          type: integer
                        messlokationsId:
                          type: string
                        energieflussrichtung:
                          type: string
                        aufteilungsfaktorEnergiemenge:
                          type: string
                      x-apidog-orders:
                        - rechenschrittBestandteilId
                        - referenzRechenschrittId
                        - operation
                        - verlustfaktorTrafo
                        - verlustfaktorLeitung
                        - messlokationsId
                        - energieflussrichtung
                        - aufteilungsfaktorEnergiemenge
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - gueltigkeitszeitraum
                  - notwendigkeit
                  - rechenschrittId
                  - rechenschritte
                required:
                  - gueltigkeitszeitraum
                  - notwendigkeit
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG5.IDE+24.SG6.RFF+[Z49|Z53]'
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG5.IDE+24.SG6.RFF+[Z49|Z53]'
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
                      SG5.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG5.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                x-apidog-orders:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                  - verwendungBis
                required:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - BERECHNUNGSFORMEL
            - VERWENDUNGSZEITRAUM
          required:
            - BERECHNUNGSFORMEL
            - VERWENDUNGSZEITRAUM
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
                marktrolle:
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
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA+IC
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA+IC.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA+IC.COM+[EM|FX|TE|AJ|AL]'
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
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA+IC.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
                - ansprechpartner
                - rufnummern
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            lokationsId:
              type: string
              description: 'Referenz auf die Lokation / LOC | EDIFACT: SG5.IDE+24.LOC+172'
            lokationsTyp:
              type: string
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle:
                  type: string
                rollencodenummer:
                  type: string
                rollencodetyp:
                  type: string
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
          x-apidog-orders:
            - absender
            - lokationsId
            - lokationsTyp
            - empfaenger
          required:
            - absender
            - lokationsId
            - lokationsTyp
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
