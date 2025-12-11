# Verwendungszeitraum einer Marktlokation ermitteln

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getMarketlokationAllocationPeriod:
    get:
      summary: Verwendungszeitraum einer Marktlokation ermitteln
      deprecated: true
      description: >-
        ** OBSOLET: Wird neu definiert**

        Lesen Verwendungszeitraum einer Marktlokation mittels LokationsId
        (Parameter1) 
      operationId: LESEN_MARKTLOKATION_VERWENDUNGSZEITRAUM
      tags:
        - Schnittstellen/Obsolet
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: 'LokationsId '
          required: true
          schema:
            type: string
            default: '74018657187'
            examples:
              - '74018657187'
      responses:
        '200':
          description: >-
            Erfolgreiches Lesen den Marktlokationen | Successful reading of the
            market locations
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Verwendungszeitraum'
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
      x-apidog-folder: Schnittstellen/Obsolet
      x-apidog-status: obsolete
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017021-run
components:
  schemas:
    Verwendungszeitraum:
      title: Verwendungszeitraum
      type: object
      properties:
        boTyp:
          $ref: '#/components/schemas/BOTyp'
          default: VERWENDUNGSZEITRAUM
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        verwendungAb:
          type: string
          format: date-time
          description: |-
            Verwendung der Daten ab
            DTM Z25
            PI 25001
        verwendungBis:
          type: string
          format: date-time
          description: |-
            Verwendung der Daten bis
            DTM Z36
            PI 25001
        zeitraumId:
          type: integer
          description: Zeitraum-ID, Nummer des Zeitraums
        datenqualitaet:
          $ref: '#/components/schemas/Datenqualitaet'
          description: >-
            Verwendungszeitraum der Daten, beginnend mit dem ältesten Zeitraum
            eines Vorgangs. Hier wird angegeben, in welchem Zeitraum Daten
            vorhanden sind oder nicht vorhanden sind. 

            Kombinationen: 

            RFF Z47 Z54

            PI 55220 55614 55156 55675 55673 55621 55633 55689 55622 55634 55692
            55625 55623 55635 55624 55636 55626 55638 55227 55180 55177 55137
            55136 55232 55685 55687 55644 55654 55664 55645 55655 55665 55647
            55657 55667 55646 55656 55666 55648 55658 55669 55559 55555 55671 

            RFF Z48 Z55

            PI 55220 55614 55156 55675 55673 55621 55633 55689 55622 55634 55692
            55625 55623 55635 55624 55636 55626 55638 55227 55180 55177 55137
            55136 55232 55685 55687 55644 55654 55664 55645 55655 55665 55647
            55657 55667 55646 55656 55666 55648 55658 55669 55559 55555 55671 

            RFF Z49 Z53

            PI 55218 55613 55126 55674 55672 55615 55627 55688 55616 55628 55691
            55619 55617 55629 55618 55630 55620 55632 55225 55175 55173 55690
            55109 55110 55230 55684 55686 55639 55649 55659 55640 55650 55660
            55642 55652 55662 55641 55651 55661 55643 55653 55663 55557 55553
            55670 

            UTILTS RFF Z49 Z53

            PI 25001  
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - verwendungAb
        - verwendungBis
        - zeitraumId
        - datenqualitaet
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Verwendungszeitraum.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Datenqualitaet:
      type: string
      title: Datenqualitaet
      description: Datenqualitaet
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
      x-apidog-enum:
        - value: ERWARTETE_DATEN
          name: ''
          description: abhängig vom BO
        - value: IM_SYSTEM_VORHANDENE_DATEN
          name: ''
          description: abhängig vom BO
        - value: INFORMATIVE_DATEN
          name: ''
          description: abhängig vom BO
        - value: GUELTIGE_DATEN
          name: ''
          description: abhängig vom BO
        - value: KEINE_DATEN
          name: ''
          description: abhängig vom BO
        - value: IM_SYSTEM_KEINE_DATEN_VORHANDEN
          name: ''
          description: abhängig vom BO
        - value: KEINE_DATEN_ERWARTET
          name: ''
          description: abhängig vom BO
        - value: DIFFERENZ_DATEN
          name: ''
          description: abhängig vom BO
        - value: DIFFERENZ_ERWARTETE_DATEN
          name: ''
          description: abhängig vom BO
        - value: DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN
          name: ''
          description: abhängig vom BO
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
