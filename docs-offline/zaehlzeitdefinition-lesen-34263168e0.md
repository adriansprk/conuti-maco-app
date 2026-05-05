# Zaehlzeitdefinition lesen 

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getDefinitionCounting:
    get:
      summary: 'Zaehlzeitdefinition lesen '
      deprecated: false
      description: >-
        Lesen einer Zaehlzeitdefinition anhand des Codes (Parameter1) zum
        Zeitpunkt (Parameter3) | Reading a perfomance definition using code
        (Parameter1) at the time (Parameter2)
      operationId: LESEN_DEFINITION_ZAEHLZEIT
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: 'Zaehlzeitdefinition '
          required: true
          example: ABC
          schema:
            type: string
            default: '74018657187'
            examples:
              - '74018657187'
        - name: parameter2
          in: query
          description: LokationsTyp | Location type
          required: false
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
          description: Datum (Gültig ab) | Date (Valid from)
          required: true
          schema:
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            type: string
            examples:
              - '2024-06-28T12:18:00Z'
        - name: parameter4
          in: query
          description: Datum (Gültig bis) | Date (Valid until)
          required: false
          schema:
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            type: string
            examples:
              - '2024-06-28T12:18:00Z'
      responses:
        '200':
          description: >-
            Erfolgreiches Lesen der Zaehlzeitdefinition | Successful reading of
            the counting definition
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Zaehlzeitdefinition'
                description: Liste der Zähler
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
      security:
        - bearer: []
      x-apidog-folder: Schnittstellen/BO4E Lesen (Backend)
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-34263168-run
components:
  schemas:
    Zaehlzeitdefinition:
      title: Zaehlzeitdefinition
      type: object
      properties:
        boTyp:
          $ref: '#/components/schemas/BOTyp'
          default: ZAEHLZEITDEFINITION
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        beginndatum:
          type: string
          format: date-time
          description: >-
            Gültigkeit, Beginndatum - Angabe, zu welchem Zeitpunkt die
            Definition ihre Gültigkeit erlangt

            DTM 157

            PI 25004

            DTM Z34

            PI 25005

            PI 
        endedatum:
          type: string
          format: date-time
          description: |-
            Gültigkeitsende der ausgerollten Definition
            DTM Z35
            PI 25005
        version:
          type: string
          format: date-time
          description: Version der Zählzeitdefinition als Datum
        notwendigkeit:
          $ref: '#/components/schemas/DefinitionenNotwendigkeit'
          description: >-
            Status der Nutzung von Definitionen, wird vom Marktpartner
            angegeben, ob er Definitionen verwendet

            STS Z36

            PI 25004
        versionsangabe:
          type: string
          description: >-
            neue Versionsangabe bei inhaltlichen Änderungen mit
            Fertigstellungsdatum/-zeit

            DTM 293

            PI 25004 25005
        code:
          type: string
          description: |-
            Zählzeitdefinition
            LOC Z09
            PI 25005 
        zaehlzeiten:
          type: array
          items:
            $ref: '#/components/schemas/Zaehlzeit'
          description: >-
            Eigenschaften der Zählzeitdefinition und einer ausgerollten
            Zählzeitdefinition

            Z42 Zählzeitdefinition

            Z43 Ausgerollte Zählzeitdefinition

            SEQ Z42

            PI 25004

            SEQ Z43

            PI 25005
        zaehlzeitregister:
          type: array
          items:
            $ref: '#/components/schemas/Zaehlzeitregister'
          description: Liste der Zählzeitregister
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - beginndatum
        - endedatum
        - version
        - notwendigkeit
        - versionsangabe
        - code
        - zaehlzeiten
        - zaehlzeitregister
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Zaehlzeitdefinition.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zaehlzeitregister:
      title: Zaehlzeitregister
      type: object
      properties:
        register:
          type: string
          description: >-
            Code des Zählzeitregisters

            CCI Z38 

            PI 55218 55220 55640 55645 55650 55655 55660 55665 55643 55648 55653
            55658 55663 55669 55553 55555 55035 55060 55043 55168 55169 

            UTILTS CCI Z38

            PI 25004
        zaehlzeitDefinition:
          type: string
          description: >-
            Code der Zählzeitdefinition

            CCI Z39

            PI 55218 55220 55035 55640 55645 55650 55655 55660 55665 55643 55648
            55653 55658 55663 55669 55553 55555 55060 55043 55168 55169

            CCI Z41 Keine Zählzeit für Messprodukt erforderlich

            PI 55060 55043 55168 55169

            Z39 Code der Zählzeitdefinition ORDERS

            Z41 Keine Zählzeit für Messprodukt erforderlich ORDERS

            CCI Z39

            PI 17123 17121 17118 17134 17135

            UTILTS RFF Z27

            PI 25004
        schwachlastfaehig:
          $ref: '#/components/schemas/Schwachlastfaehig'
          description: >-
            Schwachlastfähigkeit des Registers, hier wird übermittelt ob eine
            Schwachlast-Fähigkeit für die Konzessionsabgabe benötigt wird.

            Z59 Nicht-Schwachlast fähig

            Z60 Schwachlast fähig

            CCI Z10

            PI 25004
      x-apidog-orders:
        - register
        - zaehlzeitDefinition
        - schwachlastfaehig
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Schwachlastfaehig:
      type: string
      title: Schwachlastfaehig
      description: Schwachlastfaehig
      enum:
        - SCHWACHLASTFAEHIG
        - NICHT_SCHWACHLASTFAEHIG
      x-apidog-enum:
        - value: SCHWACHLASTFAEHIG
          name: Schwachlast fähig
          description: Z60
        - value: NICHT_SCHWACHLASTFAEHIG
          name: Nicht-Schwachlast fähig
          description: Z59
      x-apidog-folder: ''
    Zaehlzeit:
      title: Zaehlzeit
      type: object
      properties:
        code:
          type: string
          description: |-
            Code der Zählzeitdefinition
            CCI Z39 
            PI 17122
            UTILTS 
            PI 25004
        haeufigkeit:
          $ref: '#/components/schemas/HaeufigkeitZaehlzeit'
          description: >-
            Häufigkeit der Übermittlung, ob die Zählzeitdefinition jährlich oder
            nur einmalig zu übermitteln ist

            CAV ZE0

            PI 25004
        uebermittelbarkeit:
          $ref: '#/components/schemas/UebermittelbarkeitZaehlzeit'
          description: |-
            Übermittelbarkeit der ausgerollten Definition
            CAV ZD5
            PI 25004
        ermittlungLeistungsmaximum:
          $ref: '#/components/schemas/ErmittlungLeistungsmaximum'
          description: >-
            Ermittlung des Leistungsmaximums bei atypischer Netznutzung, ob
            Netzbetreiber bei Ermittlung Hochlastzeitfenster nutzt

            CAV ZD4

            PI 25004
        istBestellbar:
          type: boolean
          description: |-
            Bestellbarkeit der Zählzeitdefinition
            Z27 Zählzeitdefinition ist bestellbar
            Z28 Zählzeitdefinition ist nicht bestellbar
            CAV ZD7
            PI 25004
        typ:
          $ref: '#/components/schemas/ZaehlzeitdefinitionTyp'
          description: |-
            Zählzeitdefinitionstyp
            CAV ZD3
            PI 25004
        beschreibungTyp:
          type: string
          description: Beschreibung Zählzeitdefinitionstyp im Textform
        aenderungszeitpunkt:
          type: string
          format: date-time
          description: >-
            Zählzeitänderungszeitpunkt, Wechsel auf ein neues aktives
            Zählzeitregister

            DTM Z33

            PI 25005 
        register:
          type: string
          description: |-
            Zählendes Register
            RFF Z28
            PI 25005
      x-apidog-orders:
        - code
        - haeufigkeit
        - uebermittelbarkeit
        - ermittlungLeistungsmaximum
        - istBestellbar
        - typ
        - beschreibungTyp
        - aenderungszeitpunkt
        - register
      description: .
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    ZaehlzeitdefinitionTyp:
      type: string
      title: ZaehlzeitdefinitionTyp
      description: ZaehlzeitdefinitionTyp
      enum:
        - WAERMEPUMPE
        - NACHTSPEICHERHEIZUNG
        - SCHWACHLASTZEITFENSTER
        - SONSTIGE
        - HOCHLASTZEITFENSTER
      x-apidog-enum:
        - value: WAERMEPUMPE
          name: Wärmepumpe
          description: Z29
        - value: NACHTSPEICHERHEIZUNG
          name: Nachtspeicherheizung
          description: Z30
        - value: SCHWACHLASTZEITFENSTER
          name: Schwachlastzeitfenster
          description: Z31
        - value: SONSTIGE
          name: sonstiger Zählzeitdefinitionstyp
          description: Z32
        - value: HOCHLASTZEITFENSTER
          name: Hochlastzeitfenster
          description: Z35
      x-apidog-folder: ''
    ErmittlungLeistungsmaximum:
      type: string
      title: ErmittlungLeistungsmaximum
      description: ErmittlungLeistungsmaximum
      enum:
        - VERWENDUNG_HOCHLASTFENSTER
        - KEINE_VERWENDUNG_HOCHLASTFENSTER
      x-apidog-enum:
        - value: VERWENDUNG_HOCHLASTFENSTER
          name: Verwendung des Hochlastzeitfensters
          description: Z25
        - value: KEINE_VERWENDUNG_HOCHLASTFENSTER
          name: keine Verwendung des Hochlastzeitfensters
          description: Z26
      x-apidog-folder: ''
    UebermittelbarkeitZaehlzeit:
      type: string
      title: UebermittelbarkeitZaehlzeit
      description: UebermittelbarkeitZaehlzeit
      enum:
        - ELEKTRONISCH
        - NICHT_ELEKTRONISCH
      x-apidog-enum:
        - value: ELEKTRONISCH
          name: elektronisch übermittelbar
          description: Z23
        - value: NICHT_ELEKTRONISCH
          name: elektronisch nicht übermittelbar
          description: Z24
      x-apidog-folder: ''
    HaeufigkeitZaehlzeit:
      type: string
      title: HaeufigkeitZaehlzeit
      description: HaeufigkeitZaehlzeit
      enum:
        - EINMALIG
        - JAEHRLICH
      x-apidog-enum:
        - value: EINMALIG
          name: einmalig zu übermittelnde ausgerollte Definition
          description: Z33
        - value: JAEHRLICH
          name: jährlich zu übermittelnde ausgerollte Definition
          description: Z34
      x-apidog-folder: ''
    DefinitionenNotwendigkeit:
      type: string
      title: DefinitionenNotwendigkeit
      description: DefinitionenNotwendigkeit
      enum:
        - ZAEHLZEITDEFINITIONEN_WERDEN_VERWENDET
        - ZAEHLZEITDEFINITIONEN_WERDEN_NICHT_VERWENDET
        - DEFINITIONEN_WERDEN_VERWENDET
        - DEFINITIONEN_WERDEN_NICHT_VERWENDET
      x-apidog-enum:
        - value: ZAEHLZEITDEFINITIONEN_WERDEN_VERWENDET
          name: ''
          description: ''
        - value: ZAEHLZEITDEFINITIONEN_WERDEN_NICHT_VERWENDET
          name: ''
          description: ''
        - value: DEFINITIONEN_WERDEN_VERWENDET
          name: Definitionen werden verwendet
          description: Z45
        - value: DEFINITIONEN_WERDEN_NICHT_VERWENDET
          name: Definitionen werden nicht verwendet
          description: Z46
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
