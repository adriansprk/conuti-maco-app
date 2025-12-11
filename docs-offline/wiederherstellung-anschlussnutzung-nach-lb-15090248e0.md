# Wiederherstellung Anschlussnutzung nach LB

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
      summary: Wiederherstellung Anschlussnutzung nach LB
      deprecated: false
      description: >-
        Triggert den Versand der Wiederherstellung der Anschlussnutzung bei
        Lieferbeginn an den Messstellenbetreiber durch die MACO APP. Die Anfrage
        wird identifiziert durch den Eventnamen START_WIEDERHERST_LB. Zusätzlich
        ist eine eindeutige ID prozessId aus dem Backend mit zu übergeben, mit
        der die spätere Antwort vom Marktpartner wieder an das Backend übergeben
        werden kann.
      operationId: START_WIEDERHERST_LB
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BNB%5D%20START_WIEDERHERST_LB'
            example:
              stammdaten:
                MARKTLOKATION:
                  - boTyp: MARKTLOKATION
                    versionStruktur: '1'
                    marktlokationsId: '50754496000'
                    marktlokationsTyp:
                      - typ: STANDARD_MARKTLOKATION
                    sparte: STROM
                STATUSMITTEILUNG:
                  - boTyp: STATUSMITTEILUNG
                    versionStruktur: '1'
                    statusObjekt: ENTSPERREN
                    auftragsstatus: ERFOLGREICH
                    positionsdaten:
                      - positionsnummer: 1
              transaktionsdaten:
                sparte: STROM
                absender:
                  boTyp: MARKTTEILNEHMER
                  versionStruktur: '1'
                  gewerbekennzeichnung: true
                  rollencodenummer: '9903526000002'
                  rollencodetyp: BDEW
                empfaenger:
                  boTyp: MARKTTEILNEHMER
                  versionStruktur: '1'
                  gewerbekennzeichnung: true
                  rollencodenummer: '9900683000008'
                  rollencodetyp: BDEW
                fertigstellungsdatum: '2025-06-30T12:00:00Z'
                antwortstatus: A01
                antwortstatusCodeliste: E_0487
              zusatzdaten:
                prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                eventname: START_WIEDERHERST_LB
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-15090248-run
components:
  schemas:
    '[NB] START_WIEDERHERST_LB':
      allOf:
        - oneOf:
            - $ref: '#/components/schemas/PI_21039'
            - $ref: '#/components/schemas/PI_21040'
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
                  const: START_WIEDERHERST_LB
                  default: START_WIEDERHERST_LB
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
    PI_21040:
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
                x-apidog-orders:
                  - marktlokationsId
                required:
                  - marktlokationsId
                x-apidog-ignore-properties: []
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
                      required:
                        - positionsnummer
                      x-apidog-ignore-properties: []
                  statusObjekt:
                    type: string
                x-apidog-orders:
                  - auftragsstatus
                  - positionsdaten
                  - statusObjekt
                required:
                  - auftragsstatus
                  - positionsdaten
                  - statusObjekt
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - STATUSMITTEILUNG
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
                marktrolle:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG1.NAD+MS'
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
                    boTyp:
                      type: string
                    versionStruktur:
                      type: string
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG1.NAD+MS.SG2.CTA+IC
                    eMailAdresse:
                      type: string
                    rufnummern:
                      type: array
                      items:
                        type: object
                        properties:
                          nummerntyp:
                            type: string
                          rufnummer:
                            type: string
                        x-apidog-orders:
                          - nummerntyp
                          - rufnummer
                        required:
                          - nummerntyp
                          - rufnummer
                        x-apidog-ignore-properties: []
                  x-apidog-orders:
                    - boTyp
                    - versionStruktur
                    - nachname
                    - eMailAdresse
                    - rufnummern
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
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
            fertigstellungsdatum:
              type: string
              format: date-time
          x-apidog-orders:
            - absender
            - empfaenger
            - fertigstellungsdatum
          required:
            - absender
            - empfaenger
            - fertigstellungsdatum
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_21039:
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
                x-apidog-orders:
                  - marktlokationsId
                required:
                  - marktlokationsId
                x-apidog-ignore-properties: []
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
                      required:
                        - positionsnummer
                      x-apidog-ignore-properties: []
                  statusObjekt:
                    type: string
                x-apidog-orders:
                  - auftragsstatus
                  - positionsdaten
                  - statusObjekt
                required:
                  - auftragsstatus
                  - positionsdaten
                  - statusObjekt
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - STATUSMITTEILUNG
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
                marktrolle:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG1.NAD+MS'
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
                    boTyp:
                      type: string
                    versionStruktur:
                      type: string
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG1.NAD+MS.SG2.CTA+IC
                    eMailAdresse:
                      type: string
                    rufnummern:
                      type: array
                      items:
                        type: object
                        properties:
                          nummerntyp:
                            type: string
                          rufnummer:
                            type: string
                        x-apidog-orders:
                          - nummerntyp
                          - rufnummer
                        required:
                          - nummerntyp
                          - rufnummer
                        x-apidog-ignore-properties: []
                  x-apidog-orders:
                    - boTyp
                    - versionStruktur
                    - nachname
                    - eMailAdresse
                    - rufnummern
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
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
            fertigstellungsdatum:
              type: string
              format: date-time
          x-apidog-orders:
            - absender
            - empfaenger
            - fertigstellungsdatum
          required:
            - absender
            - empfaenger
            - fertigstellungsdatum
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
