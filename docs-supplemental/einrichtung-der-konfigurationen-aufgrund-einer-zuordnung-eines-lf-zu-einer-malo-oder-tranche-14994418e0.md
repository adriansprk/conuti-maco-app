# Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer MaLo oder Tranche

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
      summary: >-
        Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu
        einer MaLo oder Tranche
      deprecated: false
      description: >-
        Triggert den Versand der Einrichtung der Konfigurationen nach Abschluss
        des Lieferbeginn an den Messstellenbetreiber durch die MACO APP. Die
        Anfrage wird identifiziert durch den Eventnamen
        START_EINRICHTUNG_KONFIG. Zusätzlich ist eine eindeutige ID prozessId
        aus dem Backend mit zu übergeben, mit der die spätere Antwort vom
        Marktpartner wieder an das Backend übergeben werden kann.
      operationId: START_EINRICHTUNG_KONFIG
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BNB%5D%20START_EINRICHTUNG_KONFIG'
            example:
              stammdaten:
                MARKTLOKATION:
                  - boTyp: MARKTLOKATION
                    versionStruktur: '1'
                    marktlokationsId: '50754496000'
                    marktlokationsTyp:
                      - typ: STANDARD_MARKTLOKATION
                    marktrollen:
                      - boTyp: MARKTTEILNEHMER
                        versionStruktur: '1'
                        marktrolle: LF
                        gewerbekennzeichnung: true
                        rollencodenummer: '9903790000002'
                        rollencodetyp: BDEW
                    zaehlwerke:
                      - verwendungszwecke:
                          - marktrolle: NB
                            zweck:
                              - ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR
                          - marktrolle: LF
                            zweck:
                              - ENDKUNDENABRECHNUNG
                        messprodukt: '9991000000044'
                        zaehlzeiten:
                          zaehlzeitDefinition: null
                MESSLOKATION:
                  - boTyp: MESSLOKATION
                    versionStruktur: '1'
                    messlokationsId: DE0009697056900614312080040415111
                    zaehlwerke:
                      - messprodukt: '99910000001516'
                ANFRAGE:
                  - boTyp: ANFRAGE
                    versionStruktur: '1'
                    lokationsId: '50754496000'
                    lokationsTyp: MALO
                    anfragekategorie: EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                    energierichtung: AUSSP
                AUFTRAG:
                  - boTyp: AUFTRAG
                    versionStruktur: '1'
                    ausfuehrungsdatum: '2025-06-30T22:00:00Z'
                    positionsdaten:
                      - positionsnummer: 1
                        lokationsId: '50754496000'
                      - positionsnummer: 2
                        lokationsId: DE0009697056900614312080040415111
                    energierichtung: AUSSP
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
              zusatzdaten:
                prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                eventname: START_EINRICHTUNG_KONFIG
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14994418-run
components:
  schemas:
    '[NB] START_EINRICHTUNG_KONFIG':
      allOf:
        - $ref: '#/components/schemas/PI_17134'
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
                  const: START_EINRICHTUNG_KONFIG
                  default: START_EINRICHTUNG_KONFIG
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
    PI_17134:
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
                      zugeordnet ist. | EDIFACT: SG2.NAD+DP.SG3.RFF+Z59,
                      SG2.NAD+SU.SG3.RFF+Z18, SG2.NAD+SU.SG3.RFF+Z59,
                      SG2.NAD+Z31.SG3.RFF+Z18, SG2.NAD+DEB.SG3.RFF+Z59
                  marktlokationsTyp:
                    type: array
                    items:
                      type: object
                      properties:
                        typ:
                          type: string
                      x-apidog-orders:
                        - typ
                      x-apidog-ignore-properties: []
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: string
                              title: Zaehlzeitdefinition
                              description: 'EDIFACT: SG29.LIN++Z54.SG30.CCI+[Z39|Z41]'
                          x-apidog-orders:
                            - zaehlzeitDefinition
                          x-apidog-ignore-properties: []
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG29.LIN++Z54.SG30.CCI+ZA8.CAV,
                                  SG29.LIN++Z54.SG30.CCI+ZA7.CAV,
                                  SG29.LIN++Z54.SG30.CCI+ZA9.CAV
                                enum:
                                  - NB
                                  - LF
                                  - MSB
                                  - MSBA
                                  - GMSB
                                  - MDL
                                  - DL
                                  - BKV
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
                              zweck:
                                type: array
                                items:
                                  type: string
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT: SG29.LIN++Z54.SG30.CCI+ZA8.CAV,
                                    SG29.LIN++Z54.SG30.CCI+ZA7.CAV,
                                    SG29.LIN++Z54.SG30.CCI+ZA9.CAV
                            x-apidog-orders:
                              - marktrolle
                              - zweck
                            x-apidog-ignore-properties: []
                        messprodukt:
                          type: string
                          description: 'messprodukt | EDIFACT: SG29.LIN++Z54.PIA+5'
                      x-apidog-orders:
                        - zaehlzeiten
                        - verwendungszwecke
                        - messprodukt
                      x-apidog-ignore-properties: []
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT: SG2.NAD+SU,
                            SG2.NAD+Z31, SG2.NAD+DEB
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT: SG2.NAD+SU, SG2.NAD+Z31, SG2.NAD+DEB
                          enum:
                            - NB
                            - LF
                            - MSB
                            - MSBA
                            - GMSB
                            - MDL
                            - DL
                            - BKV
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
                            SG2.NAD+SU, SG2.NAD+Z31, SG2.NAD+DEB
                        rollencodetyp:
                          type: string
                      x-apidog-orders:
                        - weiterverpflichtet
                        - marktrolle
                        - rollencodenummer
                        - rollencodetyp
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - marktlokationsId
                  - marktlokationsTyp
                  - zaehlwerke
                  - marktrollen
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

                      z.B. DE 47108151234567 | EDIFACT:
                      SG29.LIN++Z19.SG34.RFF+Z19
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: string
                              title: Zaehlzeitdefinition
                              description: 'EDIFACT: SG29.LIN++Z19.SG30.CCI+[Z39|Z41]'
                          x-apidog-orders:
                            - zaehlzeitDefinition
                          x-apidog-ignore-properties: []
                        messprodukt:
                          type: string
                          description: 'messprodukt | EDIFACT: SG29.LIN++Z19.PIA+5'
                      x-apidog-orders:
                        - zaehlzeiten
                        - messprodukt
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - messlokationsId
                  - zaehlwerke
                x-apidog-ignore-properties: []
            ANFRAGE:
              type: array
              items:
                type: object
                properties:
                  anfragetyp:
                    type: string
                    title: Anfragetyp
                    description: 'Anfragetyp | EDIFACT: IMD+[Z66|Z67]'
                    enum:
                      - KAUF
                      - NUTZUNGSUEBERLASSUNG
                      - ABRECHNUNGSBRENNWERT_UND_ZUSTANDSZAHL
                      - LASTGANGDATEN
                      - ZAEHLERSTAENDE
                      - WERTEERMITTLUNG
                      - ENERGIEMENGE_EINZELWERT
                      - INNERHALB_DER_ARBEITSZEIT
                      - AUCH_AUSSERHALB_DER_ARBEITSZEIT
                      - WECHSEL_SAEMTLICHER_EINRICHTUNGEN
                      - TEILWEISER_WECHSEL
                      - AENDERUNG_ZAEHLZEITDEFINITION
                      - ABBESTELLUNG_ZAEHLZEITEN
                      - ABBESTELLUNG_MESSPRODUKT
                      - ANGEBOT_AUF_BASIS_PREISBLATT
                      - INDIVIDUELLES_ANGEBOT
                      - AENDERUNG_KONFIGURATION
                      - KANN_NICHT_ANGEBOTEN_WERDEN
                      - NEUKONFIGURATION
                      - BEENDIGUNG_KONFIGURATION
                      - AKTIVIERUNG_KONFIGURATION
                  lokationsId:
                    type: string
                    description: >-
                      Referenz auf die Lokation / LOC | EDIFACT:
                      SG2.NAD+DP.LOC+172
                  lokationsTyp:
                    type: string
                  energierichtung:
                    type: string
                    title: Energierichtung
                    description: >-
                      Spezifiziert die Energierichtung einer Markt- und/oder
                      Messlokation | EDIFACT: IMD+Z14
                    enum:
                      - AUSSP
                      - EINSP
                  anfragekategorie:
                    type: string
                x-apidog-orders:
                  - anfragetyp
                  - lokationsId
                  - lokationsTyp
                  - energierichtung
                  - anfragekategorie
                required:
                  - lokationsId
                  - lokationsTyp
                  - energierichtung
                  - anfragekategorie
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  tranchenId:
                    type: string
                    description: >-
                      tranchenId | EDIFACT: SG2.NAD+DP.SG3.RFF+Z20,
                      SG2.NAD+SU.SG3.RFF+Z20, SG29.LIN++Z16.SG34.RFF+Z20
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: string
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT: SG29.LIN++Z16.SG30.CCI+ZA8.CAV,
                                    SG29.LIN++Z16.SG30.CCI+ZA7.CAV,
                                    SG29.LIN++Z16.SG30.CCI+ZA9.CAV
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG29.LIN++Z16.SG30.CCI+ZA8.CAV,
                                  SG29.LIN++Z16.SG30.CCI+ZA7.CAV,
                                  SG29.LIN++Z16.SG30.CCI+ZA9.CAV
                                enum:
                                  - NB
                                  - LF
                                  - MSB
                                  - MSBA
                                  - GMSB
                                  - MDL
                                  - DL
                                  - BKV
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
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                        messprodukt:
                          type: string
                          description: 'messprodukt | EDIFACT: SG29.LIN++Z16.PIA+5'
                      x-apidog-orders:
                        - verwendungszwecke
                        - messprodukt
                      x-apidog-ignore-properties: []
                  aufteilungsmenge:
                    type: object
                    properties:
                      wert:
                        type: number
                        title: Schwellwert
                        description: 'EDIFACT: SG29.LIN++Z16.QTY+11'
                    x-apidog-orders:
                      - wert
                    x-apidog-ignore-properties: []
                  bildungTranchengroesse:
                    type: string
                    title: BildungTranchengroesse
                    description: >-
                      BildungTranchengroesse | EDIFACT:
                      SG29.LIN++Z16.SG30.CCI+Z37
                    enum:
                      - PROZENTUAL
                      - AUFTEILUNGSFAKTOR
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
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - tranchenId
                  - zaehlwerke
                  - aufteilungsmenge
                  - bildungTranchengroesse
                  - marktrollen
                x-apidog-ignore-properties: []
            AUFTRAG:
              type: array
              items:
                type: object
                properties:
                  positionsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        anfragegrund:
                          type: string
                          title: Anfragegrund
                          description: 'Anfragegrund | EDIFACT: SG29.LIN++Z16.IMD+[Z64|Z65]'
                          enum:
                            - ABGRENZUNG_VON_ENERGIEMENGEN
                            - ABGRENZUNG
                            - WECHSELEREIGNIS
                            - ZWISCHENABLESUNG
                            - DIREKTER_VERTRAG_MSB_AN
                            - DIREKTER_VERTRAG_MSB_ANN
                            - AENDERUNG_IM_LOKATIONSBUENDEL
                            - NEUKONFIGURATION
                            - KONFIGURATION_UNVERAENDERT
                        positionsnummer:
                          type: integer
                          description: >-
                            Positionsnummer / LIN | EDIFACT: SG29.LIN++Z54,
                            SG29.LIN++Z16, SG29.LIN++Z19
                        lokationsId:
                          type: string
                      x-apidog-orders:
                        - anfragegrund
                        - positionsnummer
                        - lokationsId
                      required:
                        - positionsnummer
                        - lokationsId
                      x-apidog-ignore-properties: []
                  ausfuehrungsdatum:
                    type: string
                    description: >-
                      Ausführungsdatum/-zeit / DTM+203 DTM+469 | EDIFACT:
                      DTM+203
                    format: date-time
                x-apidog-orders:
                  - positionsdaten
                  - ausfuehrungsdatum
                required:
                  - positionsdaten
                  - ausfuehrungsdatum
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - MESSLOKATION
            - ANFRAGE
            - TRANCHE
            - AUFTRAG
          required:
            - ANFRAGE
            - AUFTRAG
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
                        SG2.NAD+MS.SG5.CTA+IC
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG5.CTA+IC.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG5.CTA+IC.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG5.CTA+IC.COM+[EM|FX|TE|AJ|AL]'
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
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
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
            sparte:
              type: string
          x-apidog-orders:
            - absender
            - nachrichtendatum
            - empfaenger
            - sparte
          required:
            - absender
            - empfaenger
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
