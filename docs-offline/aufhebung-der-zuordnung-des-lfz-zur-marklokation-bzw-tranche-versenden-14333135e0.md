# Aufhebung der Zuordnung des LFZ zur Marklokation bzw. Tranche versenden

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
      summary: Aufhebung der Zuordnung des LFZ zur Marklokation bzw. Tranche versenden
      deprecated: false
      description: >-
        Triggert den Versand von Aufhebung der Zuordnung des LFZ zur
        Marklokation bzw. Tranche an Marktpartner durch die MACO APP. Die
        Anfrage wird identifiziert durch den Eventnamen AUFH_ZUK_ZUORDNUNG.
        Zusätzlich ist eine eindeutige ID prozessId aus dem Backend mit zu
        übergeben, mit der die spätere Antwort vom Marktpartner wieder an das
        Backend übergeben werden kann.
      operationId: START_AUFH_ZUK_ZUORDNUNG
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BNB%5D%20START_AUFH_ZUK_ZUORDNUNG'
            example:
              stammdaten:
                MARKTLOKATION:
                  - boTyp: MARKTLOKATION
                    versionStruktur: '1'
                    marktlokationsId: '57685676748'
                    sparte: STROM
                    energierichtung: AUSSP
                    marktlokationsTyp:
                      - typ: STANDARD_MARKTLOKATION
              transaktionsdaten:
                transaktionsgrund: ZG5
                transaktionsgrundergaenzung: ZW4
                sparte: STROM
                absender:
                  rollencodenummer: '9904000000005'
                  rollencodetyp: BDEW
                empfaenger:
                  rollencodenummer: '9900936000002'
                  rollencodetyp: BDEW
                beteiligterMarktpartner:
                  boTyp: MARKTTEILNEHMER
                  versionStruktur: '1'
                  geschaeftspartnerrolle: LIEFERANT
                  rollencodenummer: '9900936000002'
                  rollencodetyp: BDEW
                kategorie: E02
                vertragsbeginn: '2025-10-31T23:00:00Z'
                vertragsende: '2025-10-31T23:00:00Z'
              zusatzdaten:
                prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                eventname: START_AUFH_ZUK_ZUORDNUNG
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14333135-run
components:
  schemas:
    '[NB] START_AUFH_ZUK_ZUORDNUNG':
      allOf:
        - $ref: '#/components/schemas/PI_55038'
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
                  const: START_AUFH_ZUK_ZUORDNUNG
                  default: START_AUFH_ZUK_ZUORDNUNG
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
    PI_55038:
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
                  beteiligterMarktpartner:
                    type: object
                    properties:
                      rollencodetyp:
                        type: string
                      rollencodenummer:
                        type: string
                      marktrolle:
                        type: string
                    x-apidog-orders:
                      - rollencodetyp
                      - rollencodenummer
                      - marktrolle
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - marktlokationsId
                  - beteiligterMarktpartner
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                  beteiligterMarktpartner:
                    type: object
                    properties:
                      rollencodetyp:
                        type: string
                      rollencodenummer:
                        type: string
                      marktrolle:
                        type: string
                    x-apidog-orders:
                      - rollencodetyp
                      - rollencodenummer
                      - marktrolle
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - tranchenId
                  - beteiligterMarktpartner
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - TRANCHE
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
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
                - marktrolle
              required:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
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
