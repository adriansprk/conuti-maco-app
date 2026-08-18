# Lokationsbündel lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getLocationBundleBasic:
    get:
      summary: Lokationsbündel lesen
      deprecated: false
      description: >-
        Lesen eines Lokationsbündels mittels LokationsId (Parameter1) zum
        Zeitpunkt (parameter3) 
      operationId: LESEN_LOKATIONSBUENDEL_BASIS
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: LokationsId
          required: true
          schema:
            type: string
            default: '74018657187'
            examples:
              - '74018657187'
        - name: parameter2
          in: query
          description: 'LokationsTyp '
          required: true
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
          schema:
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            type: string
            examples:
              - '2024-06-28T12:18:00Z'
        - name: parameter4
          in: query
          description: Datum (Gültig bis)
          required: true
          schema:
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            type: string
            examples:
              - '2024-06-28T12:18:00Z'
        - name: command
          in: query
          description: >-
            Entspricht der operationId dieser Schnittstelle. Diese Operation Id
            entspricht dem Command im Camunda Konnektor Prozess. Wenn das
            Backend einen generischen Endpunkt bereitstellt, kann dieses Command
            gentutzt werden um zu definieren welche Operation ausgeführt werden
            soll.
          required: false
          example: SAP_LESEN_LOKATIONSBUENDEL_BASIS
          schema:
            type: string
      responses:
        '200':
          description: >-
            Erfolgreiches Lesen des Lokationsbündels | Successful reading of the
            location bundle
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Lokationsbuendel'
              example:
                boTyp: LOKATIONSBUENDEL
                versionStruktur: '1'
                gueltigkeitszeitraum:
                  zeitraumId: null
                  startdatum: null
                  enddatum: null
                datenqualitaet: null
                lokationsbuendelstrukturId: '56143614'
                lokationsbuendelNummer: 1
                standardisierteLokationsbuendelstruktur: true
                zuordnungObjectcode:
                  - referenzLokationsTyp: MALO
                    referenzLokationsId: '50754496001'
                    objectcode:
                      - objectcode: '1463515'
                        lokationsbuendelNummer: 1
                    vorgelagerteLokationTyp: NELO
                    vorgelagerteLokationId: '12754496001'
                    referenzMarktlokationTechnischeRessource:
                      - Marktlokation1
                      - Marktlokation2
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017019-run
components:
  schemas:
    Lokationsbuendel:
      title: Lokationsbuendel
      type: object
      properties:
        boTyp:
          $ref: '#/components/schemas/BOTyp'
          default: LOKATIONSBUENDEL
          description: .
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        lokationsbuendelstrukturId:
          type: string
          description: ID der Lokationsbündelstruktur
        lokationsbuendelNummer:
          type: integer
          description: Fortlaufende Nummer eines Lokationsbündels
        standardisierteLokationsbuendelstruktur:
          type: boolean
          description: >
            Gibt an, ob sich die Struktur mittels eines
            Lokationsbündelstrukturcodes beschreiben lässt  (Z31) oder ob es
            keinen passenden Lokationsbündelstrukturcode gibt (Z39).

            RFF Z31 Z39

            55175 55180 55173 55177 55690 55035 55095 55060 55043 55168 55169 
        datenqualitaet:
          $ref: '#/components/schemas/Datenqualitaet'
          description: >-
            Referenz auf die Lokationsbündelstruktur. Lokationsbündelstrukturen,
            welche sich hinter einer Netzlokation befinden.

            SEQ Z78  Referenz auf die Lokationsbündelstruktur

            PI 55175 55173 55690 55043 55168 55169

            SEQ ZC7 Erwartete Referenz auf die Lokationsbündelstruktur

            PI 55180 55177

            SEQ ZC8 Im System vorhandene Referenz auf die
            Lokationsbündelstruktur

            PI 55180 55177

            SEQ ZD5 Informative Referenz auf die Lokationsbündelstruktur

            PI 55035 55095 55060

            SEQ Z58 Zuordnung Lokation zum Objektcode des Lokationsbündels 

            PI 55175 55173 55690 55043 55168 55169

            SEQ ZC9 Erwartete Zuordnung Lokation zum Objektcode des
            Lokationsbündels

            PI 55180 55177 

            SEQ ZD0 Im System vorhandene Zuordnung Lokation zum Objektcode des
            Lokationsbündels

            PI 55180 55177

            SEQ ZD6 Informative Zuordnung Lokation zum Objektcode des
            Lokationsbündels

            PI 55035 55095 55060 
        gueltigkeitszeitraum:
          $ref: '#/components/schemas/Zeitraum'
          description: Referenz auf Zeitraum-ID
        zuordnungObjectcode:
          type: array
          items:
            $ref: '#/components/schemas/ZuordnungObjectcode'
          description: Zuordnung Objectcode
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - lokationsbuendelstrukturId
        - lokationsbuendelNummer
        - standardisierteLokationsbuendelstruktur
        - datenqualitaet
        - gueltigkeitszeitraum
        - zuordnungObjectcode
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Lokationsbuendel.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    ZuordnungObjectcode:
      title: ZuordnungObjectcode
      type: object
      properties:
        referenzLokationsTyp: &ref_0
          $ref: '#/components/schemas/Lokationstyp'
          description: >-
            Referenz auf die ID der Netzlokation, Marktlokation, Messlokation,
            Technischen Ressource

            RFF Z18
        referenzLokationsId:
          type: string
          description: ID einer Lokation
        vorgelagerteLokationTyp: *ref_0
        vorgelagerteLokationId:
          type: string
          description: ID einer Lokation
        objectcode:
          type: array
          items:
            $ref: '#/components/schemas/Objectcode'
          description: >-
            Objektcode der Lokation in der Lokationsbündelstruktur. Zur
            Referenzierung auf den Objektcode der (im Vorgang genannten)
            Lokationsbündelstruktur.

            RFF Z33
        referenzMarktlokationTechnischeRessource:
          type: array
          items:
            type: string
          description: >-
            Referenz auf die der Technischen Ressource zugeordneten
            Marktlokation

            RFF Z16

            PI 55035 55095 55060 55043 55168 55169
      x-apidog-orders:
        - referenzLokationsTyp
        - referenzLokationsId
        - vorgelagerteLokationTyp
        - vorgelagerteLokationId
        - objectcode
        - referenzMarktlokationTechnischeRessource
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Objectcode:
      title: Objectcode
      type: object
      properties:
        objectcode:
          type: string
          description: Objectcode
        lokationsbuendelNummer:
          type: integer
          description: Fortlaufende Nummer eines Lokationsbündels
      x-apidog-orders:
        - objectcode
        - lokationsbuendelNummer
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Lokationstyp:
      type: string
      title: Lokationstyp
      description: Gibt an, ob es sich um eine Markt- oder Messlokation handelt
      enum:
        - MALO
        - MELO
        - NELO
        - TECHNISCHE_RESSOURCE
      x-apidog-enum:
        - value: MALO
          name: Marktlokation
          description: Z18
        - value: MELO
          name: Messlokation
          description: Z19
        - value: NELO
          name: Netzlokation
          description: Z32
        - value: TECHNISCHE_RESSOURCE
          name: Technische Ressource
          description: Z37
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
