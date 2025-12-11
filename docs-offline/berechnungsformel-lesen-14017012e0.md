# Berechnungsformel lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getCalculationFormulaBasic:
    get:
      summary: Berechnungsformel lesen
      deprecated: false
      description: >-
        Lesen des Berechnunungsformel einer Lokation (Parameter1) vom Typ
        (Parameter2 - default MALO) zum Stichtag (Parameter3)
      operationId: LESEN_BRECHNUNGSFORMEL_BASIS
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: LokationsId
          required: true
          example: '{{marktlokationsId}}'
          schema:
            type: string
            default: '74018657187'
            examples:
              - '74018657187'
        - name: parameter2
          in: query
          description: LokationsTyp
          required: true
          example: MALO
          schema:
            type: string
            default: MALO
            enum:
              - MALO
              - MELO
              - NELO
              - TECHNISCHE_RESSOURCE
              - STEUERBARE_RESOURCE
              - TRANCHE
            examples:
              - MALO
        - name: parameter3
          in: query
          description: Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt
          required: true
          example: '{{gueltigVon}}'
          schema:
            type: string
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            examples:
              - '2024-06-28T12:18:00Z'
        - name: parameter4
          in: query
          description: 'Datum (Gültig bis) '
          required: false
          example: '{{gueltigBis}}'
          schema:
            type: string
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            format: date-time
        - name: command
          in: query
          description: >-
            Entspricht der operationId dieser Schnittstelle. Diese Operation Id
            entspricht dem Command im Camunda Konnektor Prozess. Wenn das
            Backend einen generischen Endpunkt bereitstellt, kann dieses Command
            gentutzt werden um zu definieren welche Operation ausgeführt werden
            soll.
          required: false
          example: SAP_LESEN_BRECHNUNGSFORMEL_BASIS
          schema:
            type: string
      responses:
        '200':
          description: 'Erfolgreiches Lesen der Berechnunungsformel '
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Berechnungsformel'
              example:
                boTyp: BERECHNUNGSFORMEL
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
          headers: {}
          x-apidog-name: OK
        '400':
          description: Fehlerhafte Anfrage | Bad Request
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apidog-orders: []
                x-apidog-ignore-properties: []
          headers: {}
          x-apidog-name: Bad Request
        '422':
          description: Nicht verarbeitbare Anfrage
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apidog-orders: []
                x-apidog-ignore-properties: []
          headers: {}
          x-apidog-name: Parameter Error
      security:
        - bearer: []
      x-apidog-folder: Schnittstellen/BO4E Lesen (Backend)
      x-apidog-status: developing
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017012-run
components:
  schemas:
    Berechnungsformel:
      title: Berechnungsformel
      type: object
      properties:
        boTyp:
          $ref: '#/components/schemas/BOTyp'
          default: BERECHNUNGSFORMEL
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        beginndatum:
          type: string
          format: date-time
          description: Der inklusive Zeitpunkt ab dem die Berechnungsformel gültig ist
        notwendigkeit:
          $ref: '#/components/schemas/BerechnungsformelNotwendigkeit'
          description: |-
            Status der Berechnungsformel
            STS Z23
            PI 25001
        lieferrichtung: &ref_2
          $ref: '#/components/schemas/Energierichtung'
          description: Lieferrichtung der Marktlokation
        rechenschrittId:
          type: integer
          description: >-
            Referenz auf einen Rechenschritt - Rechenschrittidentifikator in
            einer Berechnungsformel, der das Ergebnis der Energiemenge ergibt.

            RFF Z23

            PI 25001
        rechenschritt: &ref_0
          $ref: '#/components/schemas/Rechenschritt'
          description: |-
            Bestandteil des Rechenschritts 
            SEQ Z37
            PI 25001
        rechenschritte:
          type: array
          items: *ref_0
          description: >-
            Eine Berechnungsformel enthält, falls sie notwendig ist, einen oder
            mehrere Berechnungschritte, die hier rekursiv abgebildet werden.
        verwendungszweck:
          type: array
          items:
            $ref: '#/components/schemas/Verwendungszweck'
          description: Verwendungszweck der Werte
        gueltigkeitszeitraum:
          $ref: '#/components/schemas/Zeitraum'
          description: Gültigkeitszeitraum der Werte
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - beginndatum
        - notwendigkeit
        - lieferrichtung
        - rechenschrittId
        - rechenschritt
        - rechenschritte
        - verwendungszweck
        - gueltigkeitszeitraum
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zeitraum:
      title: Zeitraum
      type: object
      properties:
        zeiteinheit: &ref_1
          $ref: '#/components/schemas/Zeiteinheit'
          description: nicht in Benutzung
        dauer:
          type: integer
          description: Zeitspanne, Wert
        startdatum:
          type: string
          format: date-time
          description: |-
            Datum aus 
            DTM Z25 Verwendung der Daten ab 
            DTM 163 Verarbeitung, Beginndatum/-zeit
            DTM 155 Rechnungsperiode, Beginndatum
            DTM Z42 vorläufiger Abrechnungszeitraum Beginn
        enddatum:
          type: string
          format: date-time
          description: |-
            Datum aus 
            DTM Z26 Verwendung der Daten bis 
            DTM164 Verarbeitung, Endedatum/-zeit
            DTM 156 Rechnungsperiode, Endedatum
            DTM Z43 vorläufiger Abrechnungszeitraum Ende
        einheit: *ref_1
        ableseZeitraum:
          type: string
          description: |-
            Turnusablesung des NB
            DTM 752
            PI 44113 44140 44142 44043 44168 44169 44060 
        abrechnungsZeitraum:
          type: string
          description: |-
            Termin, zu dem die Netznutzungsabrechnung des NB erfolgt
            DTM Z21
            PI 44112 44139 44142 44002 44013 44014 44035
        zeitraumText:
          type: string
          description: ZeitraumText
        zeitraumId:
          type: integer
          description: |-
            Referenz auf Zeitraum-ID
            RFF Z46
            PI 25001
      x-apidog-orders:
        - zeiteinheit
        - dauer
        - startdatum
        - enddatum
        - einheit
        - ableseZeitraum
        - abrechnungsZeitraum
        - zeitraumText
        - zeitraumId
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zeiteinheit:
      type: string
      title: Zeiteinheit
      description: Zeiteinheit
      enum:
        - SEKUNDE
        - MINUTE
        - STUNDE
        - VIERTEL_STUNDE
        - TAG
        - WOCHE
        - MONAT
        - QUARTAL
        - HALBJAHR
        - JAHR
      x-apidog-enum:
        - value: SEKUNDE
          name: ''
          description: ''
        - value: MINUTE
          name: ''
          description: ''
        - value: STUNDE
          name: ''
          description: ''
        - value: VIERTEL_STUNDE
          name: ''
          description: ''
        - value: TAG
          name: Tag
          description: '804'
        - value: WOCHE
          name: Woche
          description: '803'
        - value: MONAT
          name: Monat
          description: '802'
        - value: QUARTAL
          name: ''
          description: ''
        - value: HALBJAHR
          name: ''
          description: ''
        - value: JAHR
          name: ''
          description: ''
      x-apidog-folder: ''
    Verwendungszweck:
      title: Verwendungszweck
      type: object
      properties:
        marktrolle:
          $ref: '#/components/schemas/Marktrolle'
          description: >-
            Identifizierung der Marktrolle

            CCI ZA8

            PI 55639 55644 55659 55664 55043 55168 55169 55649 55654 55684 55685
            55686 55687 55660 55665 55662 55667 

            ORDERS PI 17121 17134
        zweck:
          type: array
          items:
            $ref: '#/components/schemas/VerwendungszweckValue'
          description: >-
            Verwendungszweck der Werte

            CAV Z47

            PI 55639 55644 55659 55664 55043 55168 55169 55649 55654 55640 55645
            55660 55665 55650 55655 

            PI 55684 55685 55686 55687 55662 55667 

            ORDERS

            PI 17121 17134
      x-apidog-orders:
        - marktrolle
        - zweck
      description: .
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    VerwendungszweckValue:
      type: string
      title: VerwendungszweckValue
      description: VerwendungszweckValue
      enum:
        - NETZNUTZUNGSABRECHNUNG
        - BILANZKREISABRECHNUNG
        - MEHRMINDERMENGENABRECHNUNG
        - ENDKUNDENABRECHNUNG
        - UEBERMITTLUNG_AN_DAS_HKNR
        - BLINDARBEITSABRECHNUNG
        - ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS
        - BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG
        - ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR
      x-apidog-enum:
        - value: NETZNUTZUNGSABRECHNUNG
          name: Netznutzungsabrechnung
          description: Z84
        - value: BILANZKREISABRECHNUNG
          name: Bilanzkreisabrechnung
          description: Z85
        - value: MEHRMINDERMENGENABRECHNUNG
          name: Mehrmindermengenabrechnung
          description: Z86
        - value: ENDKUNDENABRECHNUNG
          name: Endkundenabrechnung
          description: Z47
        - value: UEBERMITTLUNG_AN_DAS_HKNR
          name: Übermitlung an das HKNR
          description: Z92
        - value: BLINDARBEITSABRECHNUNG
          name: ''
          description: ''
        - value: ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS
          name: Zur Ermitlung der Ausgeglichenheit von Bilanzkreisen
          description: ZB5
        - value: BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG
          name: Blindarbeitabrechnung / Betriebsführung
          description: ZD1
        - value: ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR
          name: Es liegt kein Verwendungszweck vor
          description: ZE1
      x-apidog-folder: ''
    Marktrolle:
      type: string
      title: Marktrolle
      description: Diese Rollen kann ein Marktteilnehmer einnehmen
      enum:
        - NB
        - LF
        - MSB
        - MSBA
        - GMSB
        - MDL
        - DL
        - BKV
        - BKO
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
      x-apidog-enum:
        - value: NB
          name: Netzbetreiber
          description: Z88
        - value: LF
          name: Lieferant
          description: Z89
        - value: MSB
          name: Messstellenbetreiber
          description: Z91
        - value: MSBA
          name: Messstellenbetreiber Alt
          description: ZB4
        - value: GMSB
          name: Grundzuständiger Messstellenbetreiber
          description: ZF0
        - value: MDL
          name: ''
          description: ''
        - value: DL
          name: ''
          description: ''
        - value: BKV
          name: ''
          description: ''
        - value: BKO
          name: ''
          description: ''
        - value: UENB
          name: Übertragungsnetzbetreiber
          description: Z90
        - value: KUNDE-SELBST-NN
          name: ''
          description: ''
        - value: MGV
          name: ''
          description: ''
        - value: EIV
          name: ''
          description: ''
        - value: RB
          name: ''
          description: ''
        - value: KUNDE
          name: ''
          description: ''
        - value: INTERESSENT
          name: ''
          description: ''
        - value: KN
          name: ''
          description: ''
        - value: UBA
          name: ''
          description: ''
        - value: BIKO
          name: ''
          description: ''
        - value: ESA
          name: ''
          description: ''
      x-apidog-folder: ''
    Rechenschritt:
      title: Rechenschritt
      type: object
      properties:
        rechenschrittBestandteilId:
          type: integer
          description: Rechenschrittidentifikator
        referenzRechenschrittId:
          type: integer
          description: Referenz Rechenschritt Id
        operation:
          $ref: '#/components/schemas/ArithmetischeOperation'
          description: |-
            Mathematischer Operator - Operation
            CAV Z69
            PI 25001 
        verlustfaktorTrafo:
          type: number
          format: float
          description: |-
            Verlustfaktor Trafo, ist immer multiplikativ anzuwenden
            CAV Z28
            PI 25001
        verlustfaktorLeitung:
          type: number
          format: float
          description: >-
            Verlustfaktor Leitung,  Leitungen/Kabeln verursachten Verluste,
            werden mit diesem Faktor berücksichtigt

            CAV Z28

            PI 25001
        aufteilungsfaktorEnergiemenge:
          type: number
          format: float
          description: |-
            Aufteilungsfaktor Energiemenge
            CAV ZH6
            PI 25001
        messlokationsId:
          type: string
          description: |-
            Referenz auf die ID einer Messlokation
            RFF Z19
            PI 25001 
        energieflussrichtung: *ref_2
      x-apidog-orders:
        - rechenschrittBestandteilId
        - referenzRechenschrittId
        - operation
        - verlustfaktorTrafo
        - verlustfaktorLeitung
        - aufteilungsfaktorEnergiemenge
        - messlokationsId
        - energieflussrichtung
      description: .
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    ArithmetischeOperation:
      type: string
      title: ArithmetischeOperation
      description: Mit dieser Aufzählung können arithmetische Operationen festgelegt werden
      enum:
        - ADDITION
        - SUBTRAKTION
        - DIVISION
        - DIVIDEND
        - MULTIPLIKATION
        - POSITIVWERT
      x-apidog-enum:
        - value: ADDITION
          name: Addition
          description: Z69
        - value: SUBTRAKTION
          name: Subtraktion
          description: Z70
        - value: DIVISION
          name: Divisor
          description: Z80
        - value: DIVIDEND
          name: Dividend
          description: Z81
        - value: MULTIPLIKATION
          name: Faktor
          description: Z82
        - value: POSITIVWERT
          name: Positivwert
          description: Z83
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
    BerechnungsformelNotwendigkeit:
      type: string
      title: BerechnungsformelNotwendigkeit
      description: BerechnungsformelNotwendigkeit
      enum:
        - BERECHNUNGSFORMEL_NOTWENDIG
        - BERECHNUNGSFORMEL_MUSS_ANGEFRAGT_WERDEN
        - BERECHNUNGSFORMEL_TRIVIAL
        - BERECHNUNGSFORMEL_NICHT_NOTWENDIG
      x-apidog-enum:
        - value: BERECHNUNGSFORMEL_NOTWENDIG
          name: Berechnungsformel angefügt
          description: Z33
        - value: BERECHNUNGSFORMEL_MUSS_ANGEFRAGT_WERDEN
          name: Berechnungsformel muss beim Absender angefragt werden
          description: Z34
        - value: BERECHNUNGSFORMEL_TRIVIAL
          name: Berechnungsformel besitzt keine Rechenoperation
          description: Z40
        - value: BERECHNUNGSFORMEL_NICHT_NOTWENDIG
          name: Berechnungsformel nicht erforderlich
          description: Z41
      x-apidog-folder: ''
    BOTyp:
      title: BOTyp
      type: string
      description: Typ des BO
      enum:
        - ANSPRECHPARTNER
        - AVIS
        - ENERGIEMENGE
        - GESCHAEFTSOBJEKT
        - GESCHAEFTSPARTNER
        - MARKTLOKATION
        - MARKTTEILNEHMER
        - MESSLOKATION
        - ZAEHLER
        - KOSTEN
        - TARIF
        - PREISBLATT
        - PREISBLATTNETZNUTZUNG
        - PREISBLATTMESSUNG
        - PREISBLATTUMLAGEN
        - PREISBLATTDIENSTLEISTUNG
        - PREISBLATTKONZESSIONSABGABE
        - ZEITREIHE
        - LASTGANG
        - HANDELSUNSTIMMIGKEIT
        - ANFRAGE
        - AUFTRAG
        - STATUSMITTEILUNG
        - BERECHNUNGSFORMEL
        - RECHNUNG
        - BILANZIERUNG
        - NETZNUTZUNGSVERTRAG
        - MESSSTELLENBETRIEBSVERTRAG
        - ENERGIELIEFERVERTRAG
        - SPERRAUFTRAG
        - ANGEBOT
        - TRANCHE
        - KOMMUNIKATIONSDATEN
        - ZAEHLZEITDEFINITION
        - SCHALTZEITDEFINITION
        - LEISTUNGSKURVENDEFINITION
        - NETZLOKATION
        - STEUERBARE_RESSOURCE
        - TECHNISCHE_RESSOURCE
        - AD_HOC_STEUERKANAL
        - LOKATIONSBUENDEL
        - WERTE_NACH_TYP2
        - REKLAMATION
        - STATUSBERICHT
        - VERTRAG
        - BILANZKREIS
        - VERWENDUNGSZEITRAUM
        - TARIFINFO
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
