# Leistungskurvendefinition lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getDefinitionPerformance:
    get:
      summary: Leistungskurvendefinition lesen
      deprecated: false
      description: >-
        Lesen einer Leistungskurvendefinition anhand des
        Konfigurationsprodukt-Code (Parameter1) zum Zeitpunkt (Parameter3) |
        Reading a perfomance definition using konfigurationproduct-code
        (Parameter1) at the time (Parameter2)
      operationId: LESEN_DEFINITION_LST_KURVEN
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: Leistungskurvendefinition
          required: true
          example: '9991000000721'
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
            Erfolgreiches Lesen der Leistungskurvendefinition| Successful
            reading of the performance definition
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Leistungskurvendefinition'
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-34262535-run
components:
  schemas:
    Leistungskurvendefinition:
      title: Leistungskurvendefinition
      type: object
      properties:
        boTyp:
          $ref: '#/components/schemas/BOTyp'
          default: LEISTUNGSKURVENDEFINITION
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

            PI 25007

            DTM Z34

            PI 25009
        endedatum:
          type: string
          format: date-time
          description: |-
            Gültigkeitsende der ausgerollten Definition
            DTM Z35
            PI 25009
        version:
          type: string
          format: date-time
          description: >-
            neue Versionsangabe bei inhaltlichen Änderungen mit
            Fertigstellungsdatum/-zeit

            DTM 293

            PI 25007 25009
        code:
          type: string
          description: |-
            Leistungskurvendefinition
            LOC Z09 
            PI 25009
        notwendigkeit:
          $ref: '#/components/schemas/DefinitionenNotwendigkeit'
          description: >-
            Status der Nutzung von Definitionen, wird vom Marktpartner
            angegeben, ob er Definitionen verwendet

            STS Z36

            PI 25007
        leistungskurven:
          type: array
          items:
            $ref: '#/components/schemas/Leistungskurve'
          description: Zugeordnete Leistungskurvendefinition
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
        - leistungskurven
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Leistungskurvendefinition.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Leistungskurve:
      title: Leistungskurve
      type: object
      properties:
        code:
          type: string
          description: |-
            Code der Leistungskurvendefinition
            CCI Z53
            PI 17130 17122 17128
            UTILTS 
            PI 25007
            REQOTE 
            PI 35004
            QUOTES
            PI 15004
        aenderungszeitpunkt:
          type: string
          format: date-time
          description: |-
            Leistungskurvenänderungszeitpunkt
            DTM Z45
            PI 25009
        haeufigkeit:
          $ref: '#/components/schemas/HaeufigkeitLeistungskurve'
          description: >-
            Häufigkeit der Übermittlung, Angabe ob die Leistungskurvendefinition
            jahrlich oder einmalig übermittelt wird

            CAV ZE0

            PI 25007
        uebermittelbarkeit:
          $ref: '#/components/schemas/UebermittelbarkeitLeistungskurve'
          description: |-
            Übermittelbarkeit der ausgerollten Definition
            CAV ZD5
            PI 25007
        schwellwert:
          $ref: '#/components/schemas/Schwellwert'
          description: Schwellwert der Leistungskurvendefinition
        konfigurationsprodukt:
          type: string
          description: |-
            Konfigurationsprodukt - Produkt-Code
            Erforderliches Produkt Leistungskurvendefinitionen
            PIA 5
            PI 17130 17128 
            REQOTE 
            PI 35004
            QUOTES 
            PI 15004
      x-apidog-orders:
        - code
        - aenderungszeitpunkt
        - haeufigkeit
        - uebermittelbarkeit
        - schwellwert
        - konfigurationsprodukt
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Schwellwert:
      title: Schwellwert
      type: object
      properties:
        obererSchwellwert:
          type: number
          format: float
          description: |-
            oberer Schwellwert
            QTY Z40 , Mengenangabe in Prozent
            PI 25009
            REQOTE Wertbereitstellung
            PI 35003 35004 
            QUOTES 
            PI 15004
        untererSchwellwert:
          type: number
          format: float
          description: |-
            unterer Schwellwert
            REQOTE Wertbereitstellung
            PI 35003 35004 
            QUOTES 
            PI 15004
        konfigurationsprodukt:
          type: string
          description: |-
            Messprodukt-Position-Code
            CCI Z60
            PI 35003 35004 
      x-apidog-orders:
        - obererSchwellwert
        - untererSchwellwert
        - konfigurationsprodukt
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    UebermittelbarkeitLeistungskurve:
      type: string
      title: UebermittelbarkeitLeistungskurve
      description: UebermittelbarkeitLeistungskurve
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
    HaeufigkeitLeistungskurve:
      type: string
      title: HaeufigkeitLeistungskurve
      description: HaeufigkeitLeistungskurve
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
