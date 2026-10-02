# Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche

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
        Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw.
        Tranche
      deprecated: false
      description: >-
        Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw.
        Tranche
      operationId: START_ABMELDEANFRAGE
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BNB%5D%20START_ABMELDEANFRAGE'
            examples: {}
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14992646-run
components:
  schemas:
    '[NB] START_ABMELDEANFRAGE':
      allOf:
        - $ref: '#/components/schemas/PI_55010'
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
                  const: START_ABMELDEANFRAGE
                  default: START_ABMELDEANFRAGE
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
    PI_55010:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            ENERGIELIEFERVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen

                            beispielsweise der Nachname dargestellt werden.
                            Beispiele: Yellow Strom GmbH

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z09
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z09
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                          enum:
                            - KUNDE
                            - LIEFERANT
                            - DIENSTLEISTER
                            - INTERESSENT
                            - MARKTPARTNER
                            - EIGENTUEMER
                            - HAUSVERWALTER
                            - KORRESPONDENZEMPFAENGER
                            - ABLESEKARTENEMPFAENGER
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z09'
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                      x-apidog-orders:
                        - name1
                        - name3
                        - anrede
                        - geschaeftspartnerrolle
                        - name4
                        - name2
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragspartner2
                x-apidog-ignore-properties: []
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsende:
                    type: string
                    description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
                    format: date-time
                x-apidog-orders:
                  - vertragsende
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
            - ENERGIELIEFERVERTRAG
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
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E02'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E02'
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            annahmedatum:
              type: string
              description: >-
                Annahmedatum eines Dokument / DTM+154 | EDIFACT:
                SG4.IDE+24.DTM+154
              format: date-time
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
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
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - vertragsende
            - dokumentennummer
            - kategorie
            - absender
            - annahmedatum
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
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
