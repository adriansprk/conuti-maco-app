# Schaltzeitdefinition lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getDefinitionSwitch:
    get:
      summary: Schaltzeitdefinition lesen
      deprecated: false
      description: >-
        Lesen einer Schaltzeitdefinition anhand des Konfigurationsprodukt-Code
        (Parameter1) zum Zeitpunkt (Parameter3) | Reading a switchtime
        definition using konfigurationproduct-code (Parameter1) at the time
        (Parameter2)
      operationId: LESEN_DEFINITION_SCHALTZEIT
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: Schaltzeitdefinition
          required: true
          example: '9991000000713'
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
            Erfolgreiches Lesen der Schaltzeitdefinition | Successful reading of
            the switchtime definition
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Schaltzeitdefinition'
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-34260808-run
components:
  schemas:
    Schaltzeitdefinition:
      title: Schaltzeitdefinition
      type: object
      properties:
        boTyp:
          $ref: '#/components/schemas/BOTyp'
          default: SCHALTZEITDEFINITION
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        beginndatum:
          type: string
          format: date-time
          description: >
            Gültigkeit, Beginndatum - Angabe, zu welchem Zeitpunkt die
            Definition ihre Gültigkeit erlangt

            DTM 157

            PI 25006

            DTM Z34 

            PI 25008
        endedatum:
          type: string
          format: date-time
          description: |-
            Gültigkeitsende der ausgerollten Definition
            DTM Z35
            PI 25008
        version:
          type: string
          format: date-time
          description: >-
            neue Versionsangabe bei inhaltlichen Änderungen mit
            Fertigstellungsdatum/-zeit

            DTM 293

            PI 25006 25008
        code:
          type: string
          description: |-
            Schaltzeitdefinition
            LOC Z09
            PI 25008
        notwendigkeit:
          $ref: '#/components/schemas/DefinitionenNotwendigkeit'
          description: >-
            Status der Nutzung von Definitionen, wird vom Marktpartner
            angegeben, ob er Definitionen verwendet

            STS Z36

            PI 25006
        schaltzeiten:
          type: array
          items:
            $ref: '#/components/schemas/Schaltzeit'
          description: Zugeordnete Schaltzeitdefinition
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - beginndatum
        - endedatum
        - version
        - code
        - notwendigkeit
        - schaltzeiten
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Schaltzeitdefinition.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Schaltzeit:
      title: Schaltzeit
      type: object
      properties:
        code:
          type: string
          description: |-
            Code der Schaltzeitdefinition
            CCI Z52
            PI 17130 17122 17128
            UTILTS 
            PI 25006
            REQOTE 
            PI 35004
            QUOTES 
            PI 15004
        aenderungszeitpunkt:
          type: string
          format: date-time
          description: |-
            Schaltzeitänderungszeitpunkt
            DTM Z44
            PI 25008
        haeufigkeit:
          $ref: '#/components/schemas/HaeufigkeitSchaltzeit'
          description: >-
            Häufigkeit der Übermittlung, Angabe ob die Schaltzeitdefinition
            jahrlich oder einmalig übermittelt wird

            CAV ZE0

            PI 25006
        uebermittelbarkeit:
          $ref: '#/components/schemas/UebermittelbarkeitSchaltzeit'
          description: |-
            Übermittelbarkeit der ausgerollten Definition
            CAV ZD5
            PI 25004
        schalthandlung:
          $ref: '#/components/schemas/Schalthandlung'
          description: |-
            Schalthandlung an der Lokation
            CCI Z58
            PI 25008
        konfigurationsprodukt:
          type: string
          description: |-
            Produktidentifikation -  Codeliste der Konfigurationen 
            Erforderliches Produkt Schaltzeitdefinitionen
            PIA 5
            PI 17130 17128
            REQOTE PI 35004
            QUOTES PI 15004
      x-apidog-orders:
        - code
        - aenderungszeitpunkt
        - haeufigkeit
        - uebermittelbarkeit
        - schalthandlung
        - konfigurationsprodukt
      description: .
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Schalthandlung:
      type: string
      title: Schalthandlung
      description: Schalthandlung
      enum:
        - LEISTUNG_AN
        - LEISTUNG_AUS
      x-apidog-enum:
        - value: LEISTUNG_AN
          name: Leistung an der Lokation an
          description: ZF4
        - value: LEISTUNG_AUS
          name: Leistung an der Lokation aus
          description: ZF5
      x-apidog-folder: ''
    UebermittelbarkeitSchaltzeit:
      type: string
      title: UebermittelbarkeitSchaltzeit
      description: UebermittelbarkeitSchaltzeit
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
    HaeufigkeitSchaltzeit:
      type: string
      title: HaeufigkeitSchaltzeit
      description: HaeufigkeitSchaltzeit
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
