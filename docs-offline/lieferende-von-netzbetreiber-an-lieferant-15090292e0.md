# Lieferende von Netzbetreiber an Lieferant

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
      summary: Lieferende von Netzbetreiber an Lieferant
      deprecated: false
      description: >-
        Triggert den Versand des Lieferende von Netzbetreiber an Lieferant z.B.
        für die Umsetzungen von Stilllegungen durch die MACO APP. Die Anfrage
        wird identifiziert durch den Eventnamen START_LIEFERENDE. Zusätzlich ist
        eine eindeutige ID prozessId aus dem Backend mit zu übergeben, mit der
        die spätere Antwort vom Marktpartner wieder an das Backend übergeben
        werden kann.
      operationId: START_LIEFERENDE
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BNB%5D%20START_LIEFERENDE'
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
                        marktlokationsTyp:
                          - typ: STANDARD_MARKTLOKATION
                  transaktionsdaten:
                    transaktionsgrund: Z33
                    transaktionsgrundergaenzung: ZW4
                    sparte: STROM
                    absender:
                      rollencodenummer: '9904000000005'
                      rollencodetyp: BDEW
                    empfaenger:
                      rollencodenummer: '9900936000002'
                      rollencodetyp: BDEW
                    kategorie: E02
                    vertragsende: '2025-10-31T23:00:00Z'
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_LIEFERENDE
                summary: 55007 / Z33 / Verbrauchende Marktlokation
              '2':
                value:
                  stammdaten:
                    TRANCHE:
                      - boTyp: TRANCHE
                        versionStruktur: '1'
                        tranchenId: '50754497111'
                        sparte: STROM
                    NETZNUTZUNGSVERTRAG:
                      - boTyp: VERTRAG
                        versionStruktur: '1'
                        vertragsart: NETZNUTZUNGSVERTRAG
                        sparte: STROM
                        vertragsende: '2025-10-31T23:00:00Z'
                  transaktionsdaten:
                    sparte: STROM
                    transaktionsgrund: ZT0
                    transaktionsgrundergaenzung: ZW5
                    pruefidentifikator: '55007'
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
                      rollencodenummer: '9903526000002'
                      rollencodetyp: BDEW
                    kategorie: E02
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_LIEFERENDE
                summary: 55007 / ZT0 / Tranche
              '3':
                value:
                  stammdaten:
                    MARKTLOKATION:
                      - boTyp: MARKTLOKATION
                        versionStruktur: '1'
                        marktlokationsId: '50754496000'
                        marktlokationsTyp:
                          - typ: RUHENDE_MARKTLOKATION
                        sparte: STROM
                    NETZNUTZUNGSVERTRAG:
                      - boTyp: VERTRAG
                        versionStruktur: '1'
                        vertragsart: NETZNUTZUNGSVERTRAG
                        sparte: STROM
                        vertragsende: '2025-10-31T23:00:00Z'
                  transaktionsdaten:
                    sparte: STROM
                    transaktionsgrund: ZQ7
                    transaktionsgrundergaenzung: ZAP
                    pruefidentifikator: '55007'
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
                    kategorie: E02
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_LIEFERENDE
                summary: 55007 / ZQ7 / ruhende Marktlokation
              '4':
                value:
                  stammdaten:
                    MARKTLOKATION:
                      - boTyp: MARKTLOKATION
                        versionStruktur: '1'
                        marktlokationsId: '50754496000'
                        sparte: STROM
                    NETZNUTZUNGSVERTRAG:
                      - boTyp: VERTRAG
                        versionStruktur: '1'
                        vertragsart: NETZNUTZUNGSVERTRAG
                        sparte: STROM
                        vertragsende: '2025-10-31T23:00:00Z'
                  transaktionsdaten:
                    sparte: STROM
                    transaktionsgrund: ZT0
                    transaktionsgrundergaenzung: ZW3
                    pruefidentifikator: '55007'
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
                      rollencodenummer: '9903526000002'
                      rollencodetyp: BDEW
                    kategorie: E02
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_LIEFERENDE
                summary: 55007 / ZT0 / Erzeugende Marktlokation
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-15090292-run
components:
  schemas:
    '[NB] START_LIEFERENDE':
      allOf:
        - $ref: '#/components/schemas/PI_55007'
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
                  const: START_LIEFERENDE
                  default: START_LIEFERENDE
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
    PI_55007:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
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
                    description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
                    format: date-time
                x-apidog-orders:
                  - vertragsart
                  - vertragsende
                required:
                  - vertragsart
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16,
                      SG4.IDE+24.SG5.LOC+Z22
                  marktlokationsTyp:
                    type: array
                    items:
                      type: object
                      properties:
                        typ:
                          type: string
                          title: AbschlagTyp
                          description: >-
                            AbschlagTyp | EDIFACT: SG4.IDE+24.SG5.LOC+Z16,
                            SG4.IDE+24.SG5.LOC+Z22
                          enum:
                            - GEMEINDERABATT_KAV
                            - ANPASSUNG_P19_STROM_NEV
                      x-apidog-orders:
                        - typ
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - marktlokationsId
                  - marktlokationsTyp
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
            - NETZNUTZUNGSVERTRAG
            - MARKTLOKATION
            - TRANCHE
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            vertragsende:
              type: string
              description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
              format: date-time
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E02|Z90]'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
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
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
                - ansprechpartner
                - rufnummern
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
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
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
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
            - kategorie
            - absender
            - empfaenger
            - anfragereferenznummer
            - transaktionsgrundergaenzung
            - transaktionsgrund
            - sparte
          required:
            - kategorie
            - absender
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
