# Netzlokation lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getGridLocationBasic:
    get:
      summary: Netzlokation lesen
      deprecated: false
      description: >-
        Lesen einer NeLo mittels LokationsId (Parameter1) vom Typ (Parameter2 -
        default MALO) zum Stichtag (Parameter3)
      operationId: LESEN_NETZLOKATION_BASIS
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: 'LokationsId '
          required: true
          example: '{{netzlokationsId}}'
          schema:
            type: string
            default: '74018657187'
            examples:
              - '74018657187'
        - name: parameter2
          in: query
          description: LokationsTyp
          required: true
          example: NELO
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
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            type: string
            examples:
              - '2024-06-28T12:18:00Z'
        - name: parameter4
          in: query
          description: 'Datum (Gültig bis) '
          required: true
          example: '{{gueltigBis}}'
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
          example: SAP_LESEN_NETZLOKATION_BASIS
          schema:
            type: string
      responses:
        '200':
          description: >-
            Erfolgreiches Lesen der Netzlokation | Successful reading of the
            network location
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Netzlokation'
              example:
                - boTyp: NETZLOKATION
                  versionStruktur: '1'
                  netzlokationsId: E1688110018
                  sparte: STROM
                  gueltigkeitszeitraum:
                    zeitraumId: 1
                    startdatum: '2024-10-20T22:00:00Z'
                    enddatum: '2024-12-24T23:00:00Z'
                  datenqualitaet: IM_SYSTEM_VORHANDENE_DATEN
                  abrechnungsdaten:
                    - zahlerBlindarbeitLf: true
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017026-run
components:
  schemas:
    Netzlokation:
      title: Netzlokation
      type: object
      properties:
        boTyp: &ref_6
          $ref: '#/components/schemas/BOTyp'
          default: NETZLOKATION
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        netzlokationsId:
          type: string
          description: >-
            Angabe der ID der Netzlokation, dient der eindeutigen Identifikation
            einer Netzkokation.

            LOC Z18

            RFF Z32 Referenzierung auf eine ID einer Netzlokation LOC+Z18

            PI 55002 55078 55602 55603 55013 55607 55615 55621 55627 55633 55225
            55227 55175 55180 55173 55177 55690 55230 55232 55639 55644 55649
            55654 55659 55664 55035 55095 55060 55043 55168 55169 55052

            IFTSTA LOC 172

            PI 21025 21027 21033

            QOUTES LOC 172

            PI 15003 15004

            INVOIC LOC 172 

            PI 31009 31004 31011
        sparte:
          $ref: '#/components/schemas/Sparte'
          description: Gas oder Strom
        netzanschlussleistung:
          type: string
          description: Netzanschlussleistungsmenge der Netzlokation
        grundzustaendigerMSBCodeNr:
          type: string
          description: >-
            Codenummer des grundzuständigen Messstellenbetreibers, der für diese
            Netzlokation zuständig ist.
        steuerkanal:
          type: boolean
          description: >-
            Angabe, ob ein Steuerkanal oder kein Steuerkanal der Netzlokation
            zugeordnet ist und somit die Netzlokation gesteuert werden kann.

            CCI Z49

            PI 55639 55644 55649 55654 55659 55664 55035 55095 55060 55043 55168
            55169
        lokationszuordnung:
          $ref: '#/components/schemas/Lokationszuordnung'
          description: nicht in Benutzung
        produktdatenRelevanteRolle: &ref_5
          $ref: '#/components/schemas/Marktrolle'
          description: |-
            Produkt-Daten für Marktrolle relevant
            CCI ZA7
        auftraggebenderMarktpartner: &ref_0
          $ref: '#/components/schemas/Marktteilnehmer'
          description: 'Auftraggebender Marktpartner, Zugeordneter Marktpartner '
        konfigurationsprodukt:
          type: string
          description: |-
            Konfigurationsprodukt 9991000000721 Leistungskurvendefinition Z12 
            PIA 5
            PI 55639 55644 55649 55654 55659 55664 55043 55168 55169
        keinKonfigurationsprodukt:
          type: boolean
          description: |-
            Kein Produkt zugeordnet ZF6
            CCI 11
            PI 55639 55644 55649 55654 55659 55664 55043 55168 55169
        leistungskurvendefinition:
          type: string
          description: |-
            Code "ABC" der Zugeordnete Leistungskurvendefinition für das Objekt
            CCI Z53
            PI 55639 55644 55649 55654 55659 55664 55043 55168 55169
        marktrollen:
          type: array
          items: *ref_0
          description: |-
            Zugeordnete Marktpartner
            CCI ZB3
        zaehlwerke:
          type: array
          items:
            $ref: '#/components/schemas/Zaehlwerk'
          description: >-
            OBIS-Kennzahl der Netzlokation, Produktidentifikation beim Austausch
            von Daten zu Energiemengen
        abrechnungsdaten:
          type: array
          items:
            $ref: '#/components/schemas/Netznutzungsabrechnungsdaten'
          description: Abrechnungsdaten der Netzlokation
        datenqualitaet:
          $ref: '#/components/schemas/Datenqualitaet'
          description: >-
            Daten der Netzlokation, alle Eigenschaften zur Netzlokation werden
            übermittelt

            SEQ Z51 Eigenschaften Netzlokation

            PI 55615 55627 55639 55649 55659 55043 55168 55169

            SEQ ZA9 Erwartete Daten der Netzlokation

            PI 55621 55633 55644 55654 55664

            SEQ ZB0 Im System vorhandene Daten der Netzlokation

            PI 55621 55633 55644 55654 55664

            SEQ ZD7 Informative Daten der Netzlokation

            PI 55002 55078 55602 55603 55013 55607 55690 55035 55095 55060

            SEQ Z71 Austausch der Abrechungsinformationen

            PI 55225 55230

            SEQ ZD8 Informative Abrechnungsdaten der Netzlokation

            SEQ ZH1 Erwartete Abrechnungsdaten der Netzlokation

            PI 55227 55232 

            SEQ ZH2 Im System vorhandene Abrechnungsdaten der Netzlokation

            PI 55227 55232 

            SEQ Z57 OBIS-Daten der Netzlokation

            PI 55639 55649 55659 55043 55168 55169 

            SEQ ZA7 Erwartete OBIS-Daten der Netzlokation

            PI 55644 55654 55664 

            SEQ ZA8 Im System vorhandene OBIS-Daten der Netzlokation

            PI 55644 55654 55664 

            SEQ ZD9 Informative OBIS-Daten der Netzlokation

            PI 55060

            SEQ Z60 Produkt-Daten der Netzlokation

            PI 55639 55649 55659 55043 55168 55169

            SEQ ZE0 Informative Produkt-Daten der Netzlokation

            PI 55035 55095 55060

            SEQ ZG8 Erwartete Produkt-Daten der NeLo

            PI 55644 55654 55664 

            SEQ ZG9 Im System vorhandene Produkt-Daten der NeLo

            PI 55644 55654 55664
        gueltigkeitszeitraum:
          $ref: '#/components/schemas/Zeitraum'
          description: Referenz auf Zeitraum-ID
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - netzlokationsId
        - sparte
        - netzanschlussleistung
        - grundzustaendigerMSBCodeNr
        - steuerkanal
        - lokationszuordnung
        - produktdatenRelevanteRolle
        - auftraggebenderMarktpartner
        - konfigurationsprodukt
        - keinKonfigurationsprodukt
        - leistungskurvendefinition
        - marktrollen
        - zaehlwerke
        - abrechnungsdaten
        - datenqualitaet
        - gueltigkeitszeitraum
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Netzlokation.json
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
    Netznutzungsabrechnungsdaten:
      title: Netznutzungsabrechnungsdaten
      type: object
      properties:
        artikelId:
          type: string
          description: |-
            Artikel-ID Produkt-/Leistungsnummer
            PIA Z02
            55218 55220 55225 55227 55557 55559 55035 
        artikelIdTyp:
          $ref: '#/components/schemas/ArtikelIdTyp'
          description: |-
            Gruppenartikel-ID / Artikel-ID
            PI 55218 55220 55225 55227 55557 55559 55035 
        anzahl:
          type: integer
          description: >-
            Anzahl in der NNA abzurechenden Positionen der Gruppenartikel-ID /
            Artikel-ID angeben. Z. B. wenn in der

            NNA mehrere Zähler oder Wandlersätze abgerechnet werden müssen.

            QTY Z38

            PI 55218 55220 55557 55559 55035 
        gemeinderabatt:
          type: number
          format: float
          description: >-
            Gemeinderabatt, Angabe zum Preisnachlass der Netznutzungsentgelte
            für den Eigenverbrauch in Prozent. Kein Preisnachlass wird mit 0
            Prozent übermittelt.

            QTY Z16

            PI 55218 55220 55035 
        zuschlag:
          type: number
          format: float
          description: |-
            Zuschlag, Aufschlag auf den Preis
            QTY Z34
            PI 55218 55220 55035 
        abschlag:
          type: number
          format: float
          description: |-
            Abschlag, Rabatt auf einen Preis
            QTY Z35
            PI 55218 55220 55035 
        singulaereBetriebsmittel:
          $ref: '#/components/schemas/Menge'
          description: |-
            Singulär genutzten Betriebsmitel
            QTY Z33 
            PI 55218 55220 55035 
        preisSingulaereBetriebsmittel:
          $ref: '#/components/schemas/Preis'
          description: |-
            Preisangabe für Singulär genutzte Betriebsmitel, je Menge pro Tag.
            CCI Z44
            PI 55218 55220 55035 
        abrechnungBlindarbeit:
          type: boolean
          description: >-
            NB teilt nur mit, ob an der Netzlokation eine Abrechnung der
            Blindarbeit stattfindet ZD9 oder keine Abrechnung ZE0 stattfindet.

            CCI Z45

            PI 55225 55227 
        zahlerBlindarbeit:
          $ref: '#/components/schemas/ZahlerBlindarbeit'
          description: |-
            NB teilt mit, wer der Zahler der Blindarbeit ist.
            CAV ZE4
            PI 55225 55227 
        zahlerBlindarbeitLf:
          type: boolean
          description: >-
            Zahlung der Blindarbeit durch den Lieferanten ZE1 oder die Zahlung
            erfolgt nicht durch den Lieferanten ZE2

            CCI Z46

            PI 55230 55232 
        differenzDaten:
          type: boolean
          description: Differenz Daten
        zaehlzeiten: &ref_4
          $ref: '#/components/schemas/Zaehlzeitregister'
          description: |-
            Zugeordnetes Zählzeitregister 
            CCI Z38
      x-apidog-orders:
        - artikelId
        - artikelIdTyp
        - anzahl
        - gemeinderabatt
        - zuschlag
        - abschlag
        - singulaereBetriebsmittel
        - preisSingulaereBetriebsmittel
        - abrechnungBlindarbeit
        - zahlerBlindarbeit
        - zahlerBlindarbeitLf
        - differenzDaten
        - zaehlzeiten
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
        schwachlastfaehig: &ref_3
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
    ZahlerBlindarbeit:
      type: string
      title: ZahlerBlindarbeit
      description: ZahlerBlindarbeit
      enum:
        - ANSCHLUSSNUTZER
        - LIEFERANT
        - NICHT_FESTGELEGT
      x-apidog-enum:
        - value: ANSCHLUSSNUTZER
          name: Anschlussnutzer
          description: Z36
        - value: LIEFERANT
          name: Lieferant
          description: Z37
        - value: NICHT_FESTGELEGT
          name: Zahler der Blindarbeit noch nicht festgelegt
          description: Z38
      x-apidog-folder: ''
    Preis:
      title: Preis
      type: object
      properties:
        wert:
          type: number
          format: float
          description: |-
            Wert Geldbetrag
            QUOTES CAL Berechnungspreis
            PI 15001 15002 15003
        einheit:
          $ref: '#/components/schemas/Waehrungseinheit'
          description: |-
            Referenzwährung EUR
            CUX 2 
            PI 19116 
        bezugswert: &ref_2
          $ref: '#/components/schemas/Mengeneinheit'
          description: |-
            Maßeinheit
            QUOTES PI 15001 15002 15003
            INVOIC
        status:
          $ref: '#/components/schemas/Preisstatus'
          description: nicht in Benutzung
      x-apidog-orders:
        - wert
        - einheit
        - bezugswert
        - status
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Preisstatus:
      title: Preisstatus
      type: string
      enum:
        - VORLAEUFIG
        - ENDGUELTIG
      description: Preisstatus
      x-apidog-folder: ''
    Mengeneinheit:
      type: string
      title: Mengeneinheit
      description: >-
        Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden
        können
      enum:
        - W
        - WH
        - KW
        - KWH
        - KVARH
        - MW
        - MWH
        - STUECK
        - KUBIKMETER
        - STUNDE
        - TAG
        - MONAT
        - JAHR
        - PROZENT
        - ANZAHL
        - VAR
        - KVAR
        - VARH
        - KWHK
        - Z16
        - KWT
      x-apidog-enum:
        - value: W
          name: ''
          description: ''
        - value: WH
          name: ''
          description: ''
        - value: KW
          name: ''
          description: ''
        - value: KWH
          name: Kilowattstunde
          description: KWH
        - value: KVARH
          name: ''
          description: ''
        - value: MW
          name: ''
          description: ''
        - value: MWH
          name: ''
          description: ''
        - value: STUECK
          name: Stück
          description: H87
        - value: KUBIKMETER
          name: ''
          description: ''
        - value: STUNDE
          name: ''
          description: ''
        - value: TAG
          name: Tag
          description: ZD8
        - value: MONAT
          name: Monat
          description: MON
        - value: JAHR
          name: Jahr
          description: ANN
        - value: PROZENT
          name: Prozent
          description: P1
        - value: ANZAHL
          name: ''
          description: ''
        - value: VAR
          name: ''
          description: ''
        - value: KVAR
          name: ''
          description: ''
        - value: VARH
          name: ''
          description: ''
        - value: KWHK
          name: ''
          description: ''
        - value: Z16
          name: kWh/K (Kilowatt-Stunde/Kelvin)
          description: Z16
        - value: KWT
          name: Kilowatt
          description: ''
      x-apidog-folder: ''
    Waehrungseinheit:
      title: Waehrungseinheit
      type: string
      enum:
        - EUR
        - CT
      description: Waehrungseinheit
      x-apidog-folder: ''
    Menge:
      title: Menge
      type: object
      properties:
        wert:
          type: number
          format: float
          description: Wert Mengenangabe
        einheit: *ref_2
      x-apidog-orders:
        - wert
        - einheit
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    ArtikelIdTyp:
      type: string
      title: ArtikelIdTyp
      description: >-
        Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene
        Artikel, die im Strommarkt die BDEW-Artikelnummer ablösen
      enum:
        - ARTIKELID
        - GRUPPENARTIKELID
      x-apidog-enum:
        - value: ARTIKELID
          name: Artikel-ID
          description: Z09
        - value: GRUPPENARTIKELID
          name: Gruppenartikel-ID
          description: Z10
      x-apidog-folder: ''
    Zaehlwerk:
      title: Zaehlwerk
      type: object
      properties:
        zaehlwerkId:
          type: string
          description: >-
            Identifikation des Zählwerks (Registers) innerhalb des Zählers.
            Oftmals eine laufende Nummer hinter der

            Zählernummer. Z.B. 47110815_1
        bezeichnung:
          type: string
          description: >-
            Bezeichnung des Zählwerks auf dem Gerät, dient zur Identifizierung
            und Beschreibung der lokalen Kennzeichnung auf dem Gerät (z. B. HT
            oder NT)

            CCI Z63

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55168 55169
        richtung:
          $ref: '#/components/schemas/Energierichtung'
          description: >-
            Die Energierichtung, Einspeisung oder Ausspeisung. Details
            Energierichtung
        obisKennzahl:
          type: string
          description: >-
            Produktidentifikation bei Austausch von Daten der Energiemengen
            werden gewährleistet durch OBIS Kennzahlen.

            PIA 5 OBIS-Kennzahl der Netzlokation

            PI 55639 55644 55649 55654 55659 55664 55060 55043 55168 55169

            PIA 5 OBIS-Kennzahl der Marktlokation

            PI 55684 55685 55640 55645 55650 55655 55660 55665 55553 55555 55035
            55095 55060 55043 55168 55169 55239 55074 55075 55076 55195 55196 

            RFF Z10 Referenz auf die OBIS-Kennzahl der Marktlokation

            PI 55616 55622 

            PIA 5 OBIS-Daten der Marktlokation der beteiligten Marktrolle

            PI 55196

            PIA 5 OBIS-Kennzahl der Tranche

            PI 55686 55687 55642 55647 55652 55657 55662 55667 55095 55074 55075
            55076 55195 55196

            PIA 5 OBIS-Kennzahl der Zähleinrichtung /Smartmeter-Gateway

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55035 55095 55060
            55043 55168 55169 55074 55075 55076
        wandlerfaktor:
          type: number
          format: float
          description: >-
            Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um
            zum eigentlichen Verbrauch im Zeitraum zu

            kommen.
        einheit: *ref_2
        schwachlastfaehig: *ref_3
        verbrauchsart:
          type: array
          items:
            $ref: '#/components/schemas/Verbrauchsart'
          description: >-
            Angabe für welchen Verwendungszweck die Stromentnahme an der
            OBIS-Kennzahl der Marktlokation erfolgt. Definiert den
            Verwendungszweck des Stroms: 

            CAV Z64

            PI 55616 55622 55035 
        unterbrechbarkeit:
          $ref: '#/components/schemas/Unterbrechbarkeit'
          description: >-
            Unterbrechbarkeit Marktlokation, Angabe, ob eine Unterbrechung der
            Verbrauchseinrichtung durch den Netzbetreiber möglich ist.

            CAV Z62

            PI 55616 55622 55035
        waermenutzung:
          $ref: '#/components/schemas/Waermenutzung'
          description: >-
            Wärmenutzung Marktlokation, im Falle der Wärmenutzung wird eine
            genauere Angabe über die Wärmenutzung definiert.

            CAV Z56

            PI 55616 55622 55617 55623 55629 55635 55035 55060 55043 55168 55169
        konzessionsabgabe:
          $ref: '#/components/schemas/Konzessionsabgabe'
          description: |-
            Konzessionsabgabedaten
            CCI Z08
            PI 44112 44139 44142 44001 44002 44013 44014 44035
        steuerbefreit:
          type: boolean
          description: Steuerbefreit
        vorkommastelle:
          type: integer
          description: >-
            Angabe der Vorkommastelle des Zählwerks

            CAV Wert

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55043 55168 55169
            55074 55075 55076
        nachkommastelle:
          type: integer
          description: >-
            Angabe der Nachkommastelle des Zählwerks

            CAV Wert

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55043 55168 55169
            55074 55075 55076
        abrechnungsrelevant:
          type: boolean
          description: Abrechnungsrelevant
        anzahlAblesungen:
          type: integer
          description: Anzahl Ablesungen
        zaehlzeiten: *ref_4
        konfiguration:
          type: string
          description: >-
            Angabe der Konfigurations-ID

            RFF AGK

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55035 55095 55060
            55043 55168 55169 55074 55075 55076
        messprodukt:
          type: string
          description: |-
            Erforderliches Messprodukt Z11 der Malo/ Tranche/ Melo
            PIA 5
            PI 55043 55168 55169 
            Messprodukt der Tranche
            PI 55060 55043 55168 55169 
            Messprodukt der Messlokation
            PI 55060 55043 55168 55169
            Erforderliches Produkt der Marktlokation ORDERS 
            PI 17123 17121 17134
            Erforderliches Produkt der Tranche ORDERS 
            PI 17121 17134 
            Erforderliches Produkt der Messlokation ORDERS 
            PI 17121 17118 17003 17134 17135
            Erforderliches Produkt der Netzlokation ORDERS
            PI 17121 17003
        wertegranularitaet:
          $ref: '#/components/schemas/Wertegranularitaet'
          description: >-
            Mit der Wertegranularität wird angegeben in welchem Intervall Werte
            der im PIA+5 genannten OBIS-Kennzahl im Markt

            bereitgestellt werden. ZD9 Jährlich ZE8 Halbjährlich ZE9
            Quartalsweise ZB7 Monatlich

            CCI ZE4

            PI 55640 55645 55650 55655 55660 55665 55643 55648 55653 55658 55663
            55669 55553 55555 55035 55095 55060 55043 55168 55169 55074 55075
            55076
        notwendigkeitZweiteMessung:
          $ref: '#/components/schemas/NotwendigkeitZweiteMessung'
          description: >-
            Weitere Beschreibung erforderliches Messprodukt, Notwendigkeit einer
            zweiten Messung vorhanden oder nicht vorhanden. Der Wert dient dem
            MSB zur Ermittlung, Plausibilisierung oder auch Ersatzwertbildung an
            der Melo. 

            CAV ZC9

            PI 55060 55043 55168 55169

            ORDERS PI 17121 17118
        werteuebermittlungVerwendungszweck:
          $ref: '#/components/schemas/WerteuebermittlungVerwendungszweck'
          description: >-
            Werteübermitlung an den NB aufgrund weiterem Verwendungszweck
            vorhanden oder nicht vorhanden. Das wird benötigt, da noch nicht
            alle Berechnungsformeln für Abrechnungszwecke ausgetauscht werden
            können.  

            CCI Z88

            PI 55060 55043 55168 55169

            ORDERS PI 17121 17118
        artEMobilitaet:
          $ref: '#/components/schemas/ArtEmobilitaet'
          description: >-
            Art der E-Mobilität, im Falle der E-Mobilität wird eine genauere
            Angabe über die Art definitiert. 

            CAV Z87

            PI 55616 55622 55617 55623 55629 55635 55035 55060 55043 55168 55169
        konfigurationsprodukt:
          type: string
          description: Konfigurationsprodukt
        keinKonfigurationsprodukt:
          type: boolean
          description: Kein Konfigurationsprodukt
        leistungskurvendefinition:
          type: string
          description: Leistungskurvendefinition
        verwendungszwecke:
          type: array
          items:
            $ref: '#/components/schemas/Verwendungszweck'
          description: Verwendungungszweck der Werte Marktlokation, Tranche
      x-apidog-orders:
        - zaehlwerkId
        - bezeichnung
        - richtung
        - obisKennzahl
        - wandlerfaktor
        - einheit
        - schwachlastfaehig
        - verbrauchsart
        - unterbrechbarkeit
        - waermenutzung
        - konzessionsabgabe
        - steuerbefreit
        - vorkommastelle
        - nachkommastelle
        - abrechnungsrelevant
        - anzahlAblesungen
        - zaehlzeiten
        - konfiguration
        - messprodukt
        - wertegranularitaet
        - notwendigkeitZweiteMessung
        - werteuebermittlungVerwendungszweck
        - artEMobilitaet
        - konfigurationsprodukt
        - keinKonfigurationsprodukt
        - leistungskurvendefinition
        - verwendungszwecke
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Verwendungszweck:
      title: Verwendungszweck
      type: object
      properties:
        marktrolle: *ref_5
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
    ArtEmobilitaet:
      type: string
      title: ArtEmobilitaet
      description: ArtEmobilitaet
      enum:
        - WB
        - LS
        - LP
      x-apidog-enum:
        - value: WB
          name: Wallbox
          description: ZE6
        - value: LS
          name: E-Mobilitätsladesäule
          description: Z87
        - value: LP
          name: Ladepark
          description: ZE7
      x-apidog-folder: ''
    WerteuebermittlungVerwendungszweck:
      type: string
      title: WerteuebermittlungVerwendungszweck
      description: Werteübermitlung an den NB aufgrund weiterem Verwendungszweck
      enum:
        - VORHANDEN
        - NICHT_VORHANDEN
      x-apidog-enum:
        - value: VORHANDEN
          name: vorhanden
          description: Z06
        - value: NICHT_VORHANDEN
          name: nicht vorhanden
          description: Z07
      x-apidog-folder: ''
    NotwendigkeitZweiteMessung:
      type: string
      title: NotwendigkeitZweiteMessung
      description: NotwendigkeitZweiteMessung
      enum:
        - VORHANDEN
        - NICHT_VORHANDEN
      x-apidog-enum:
        - value: VORHANDEN
          name: vorhanden
          description: Z06
        - value: NICHT_VORHANDEN
          name: nicht vorhanden
          description: Z07
      x-apidog-folder: ''
    Wertegranularitaet:
      type: string
      title: Wertegranularitaet
      description: Wertegranularitaet
      enum:
        - JAEHRLICH
        - HALBJAEHRLICH
        - QUARTALSWEISE
        - MONATLICH
      x-apidog-enum:
        - value: JAEHRLICH
          name: Jährlich
          description: ZD9
        - value: HALBJAEHRLICH
          name: Halbjährlich
          description: ZE8
        - value: QUARTALSWEISE
          name: Quartalsweise
          description: ZE9
        - value: MONATLICH
          name: Monatlich
          description: ZB7
      x-apidog-folder: ''
    Konzessionsabgabe:
      title: Konzessionsabgabe
      type: object
      properties:
        satz:
          $ref: '#/components/schemas/AbgabeArt'
          description: |-
            Gruppen der KAV
            CAV KAS
        kosten:
          type: number
          format: float
          description: Konzessionsabgabe in Euro/kWh
        kategorie:
          type: string
          description: >-
            Gebührenkategorie der Konzessionsabgabe - Übermittlung von
            zusätzlichen Informationen
      x-apidog-orders:
        - satz
        - kosten
        - kategorie
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    AbgabeArt:
      type: string
      title: AbgabeArt
      description: Art der Konzessionsabgabe
      enum:
        - KAS
        - SA
        - SAS
        - TA
        - TAS
        - TK
        - TKS
        - TS
        - TSS
      x-apidog-enum:
        - value: KAS
          name: >-
            für alle konzessionsvertraglichen Sonderregelungen, die nicht in die
            Systematik der KAV eingegliedert sind
          description: KAS
        - value: SA
          name: >-
            Sondervertragskunden < 1 kV nach § 2 (7) und > 1 kV, Preis nach § 2
            (3) (für Strom 0,11 ct/ kWh und für Gas 0,03 ct/kWh)
          description: SA
        - value: SAS
          name: >-
            Kennzeichnung, dass ein abweichender Preis für Sondervertragskunden
            vorliegt
          description: SAS
        - value: TA
          name: >-
            Tarifkunden, für Strom § 2. (2) 1b HT bzw. ET (hohe KA) und für Gas
            § 2 (2) 2b
          description: TA
        - value: TAS
          name: Kennzeichnung, dass ein abweichender Preis für Tarifkunden vorliegt
          description: TAS
        - value: TK
          name: >-
            für Gas nach KAV § 2 (2) 2a bei ausschließlicher Nutzung zum Kochen
            und Warmwassererzeugung
          description: TK
        - value: TKS
          name: >-
            Kennzeichnung, wenn nach KAV § 2 (2) 2a ein anderer Preis zu
            verwenden ist
          description: TKS
        - value: TS
          name: ''
          description: ''
        - value: TSS
          name: ''
          description: ''
      x-apidog-folder: ''
    Waermenutzung:
      type: string
      title: Waermenutzung
      description: Waermenutzung
      enum:
        - SPEICHERHEIZUNG
        - WAERMEPUMPE
        - DIREKTHEIZUNG
        - WAERMEPUMPE_WAERME_KAELTE
        - WAERMEPUMPE_KAELTE
        - WAERMEPUMPE_WAERME
      x-apidog-enum:
        - value: SPEICHERHEIZUNG
          name: Speicherheizung
          description: Z56
        - value: WAERMEPUMPE
          name: Wärmepumpe (unspezifiziert)
          description: Z57
        - value: DIREKTHEIZUNG
          name: Direktheizung
          description: Z61
        - value: WAERMEPUMPE_WAERME_KAELTE
          name: Wärmepumpe (Wärme und Kälte)
          description: ZV5
        - value: WAERMEPUMPE_KAELTE
          name: Wärmepumpe (Kälte)
          description: ZV6
        - value: WAERMEPUMPE_WAERME
          name: Wärmepumpe (Wärme)
          description: ZV7
      x-apidog-folder: ''
    Unterbrechbarkeit:
      type: string
      title: Unterbrechbarkeit
      description: Unterbrechbarkeit
      enum:
        - UV
        - NUV
      x-apidog-enum:
        - value: UV
          name: unterbrechbare Verbrauchseinrichtung
          description: Z62
        - value: NUV
          name: nicht-unterbrechbare Verbrauchseinrichtung
          description: Z63
      x-apidog-folder: ''
    Verbrauchsart:
      type: string
      title: Verbrauchsart
      description: Verbrauchsart
      enum:
        - KL
        - W
        - EMOB
        - SB
        - SW
        - WK
      x-apidog-enum:
        - value: KL
          name: Kraft/Licht
          description: Z64
        - value: W
          name: ''
          description: ''
        - value: EMOB
          name: E-Mobilität
          description: ZE5
        - value: SB
          name: Straßenbeleuchtung
          description: ZA8
        - value: SW
          name: Steuerung Wärmeabgabe
          description: ZB3
        - value: WK
          name: Wärme/Kälte
          description: Z65
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
    Marktteilnehmer:
      title: Marktteilnehmer
      type: object
      properties:
        boTyp: *ref_6
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        geschaeftspartnerrolle:
          $ref: '#/components/schemas/Geschaeftspartnerrolle'
          description: Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde).
        anrede:
          type: string
          description: Anrede
        name1:
          type: string
          description: 'Erster Teil des Namens - Name des Unternehmens '
        name2:
          type: string
          description: Zweiter Teil des Namens
        name3:
          type: string
          description: Dritter Teil des Namens
        name4:
          type: string
          description: Vierter Teil des Namens
        partneradresse:
          $ref: '#/components/schemas/Adresse'
          description: Anschrift des Unternehmens
        gewerbekennzeichnung:
          type: boolean
          description: >-
            Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
            (gewerbeKennzeichnung = true) oder eine Privatperson handelt.
            (gewerbeKennzeichnung = false)
        externeKundenummerLieferant:
          type: string
          description: externe Kundenummer Lieferant
        marktrolle: *ref_5
        rollencodenummer:
          type: string
          description: |-
            Gibt die Codenummer der Marktrolle an - MP ID
            ORDERS NAD Z31 Übertragungsnetzbetreiber 
            PI 17134
            ORDERS NAD DEB Messstellenbetreiber
            PI 17003 17134 17135
            IFTSTA NAD DEB Messstellenbetreiber 
            PI 21007 21015 21018
        rollencodetyp:
          $ref: '#/components/schemas/Rollencodetyp'
          description: >-
            Gibt den Typ des Codes an - Verantwortliche Stelle für die
            Codepflege

            9 GS1

            293 DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)

            332 DE, DVGW Service & Consult GmbH 
        umsatzsteuerId:
          type: string
          description: |-
            Umsatzsteuernummer
            RFF VA
            PI 37000 37001 37002 37005 37004 37003 37006
        steuernummer:
          type: string
          description: |-
            Steuernummer
            RFF FC
            PI 37000 37001 37002 37005 37004 37003 37006
        ansprechpartner:
          $ref: '#/components/schemas/Ansprechpartner'
          description: |-
            Ansprechpartner innerhalb des im vorangegangenen NAD-Segment
            CTA IC 
        makoadresse:
          type: string
          description: >-
            Die 1:1-Kommunikationsadresse des Marktteilnehmers. Diese wird in
            der Marktkommunikation verwendet.
        downloadlinkZertifikat:
          type: string
          description: Downloadlink Zertifikat
        amtsgericht:
          type: string
          description: |-
            Amtsgericht - Angabe des Gerichtes
            FTX Z15
            PI 37000 37001 37002 37005 37004 37003 37006
        hrnummer:
          type: string
          description: Handelsregister-Nummer
        website:
          type: string
          description: |-
            Internetseite (URL) 
            FTX Z13
            PI 37000 37001 37002 37005 37004 37003 37006
        faxnummer:
          type: string
          description: |-
            Faxnummer des Unternehmens
            RFF Z25
            PI 37000 37001 37002 37005 37004 37003 37006
        kommunikationsrolle:
          $ref: '#/components/schemas/Kommunikationsrolle'
          description: Ansprechpartner für den Themenbereich
        weiterverpflichtet:
          type: boolean
          description: >-
            Art der Leistungserbringung

            Z19 Auf vertraglicher Grundlage gegenüber Anschlussnutzer /
            Anschlussnehmer

            Z20 In der Ausübung der Weiterverpflichtung durch den gMSB

            PI 55002 55078 55602 55603 55013 55616 55622 55628 55634 55690 55035
            55095 55060 55043 55168 55169
        kommunikationsparameter:
          $ref: '#/components/schemas/Kommunikationsparameter'
          description: nicht in Benutzung
        messstellenbetreiberEigenschaft:
          $ref: '#/components/schemas/MSBEigenschaft'
          description: >-
            Eigenschaft des Messstellenbetreiber an der Lokation

            CAV Z39

            PI 55002 55078 55602 55603 55013 55616 55622 55628 55634 55690 55035
            55095 55060 55043 55168 55169
        bankverbindung:
          type: array
          items:
            $ref: '#/components/schemas/Bankverbindung'
          description: |-
            Bankverbindung
            FII BK
            PI 37000 37001 37002 37005 37004 37003 37006
        erreichbarkeit:
          type: array
          items:
            $ref: '#/components/schemas/Erreichbarkeit'
          description: |-
            Erreichbarkeit des Unternehmens  an Werktagen
            CCI Z40
            PI 37000 37001 37002 37005 37004 37003 37006
        ipAdresse:
          type: string
          description: |-
            IP-Adresse des Absenders
            FTX Z27
        ipRange:
          $ref: '#/components/schemas/IpRange'
          description: |-
            IP-Range des Absenders
            FTX Z28
        zuordnungVon:
          type: string
          format: date-time
          description: Startdatum der Zuordnung des Marktteilnehmers
        zuordnungBis:
          type: string
          format: date-time
          description: Enddatum der Zuordnung des Marktteilnehmers
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - geschaeftspartnerrolle
        - anrede
        - name1
        - name2
        - name3
        - name4
        - partneradresse
        - gewerbekennzeichnung
        - externeKundenummerLieferant
        - marktrolle
        - rollencodenummer
        - rollencodetyp
        - umsatzsteuerId
        - steuernummer
        - ansprechpartner
        - makoadresse
        - downloadlinkZertifikat
        - amtsgericht
        - hrnummer
        - website
        - faxnummer
        - kommunikationsrolle
        - weiterverpflichtet
        - kommunikationsparameter
        - messstellenbetreiberEigenschaft
        - bankverbindung
        - erreichbarkeit
        - ipAdresse
        - ipRange
        - zuordnungVon
        - zuordnungBis
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Marktteilnehmer.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    IpRange:
      title: IpRange
      type: object
      properties:
        untereGrenze:
          type: string
          description: untere Grenze der IP-Range des Absenders
        obereGrenze:
          type: string
          description: obere Grenze der IP-Range des Absenders
      x-apidog-orders:
        - untereGrenze
        - obereGrenze
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Erreichbarkeit:
      title: Erreichbarkeit
      type: object
      properties:
        verfuegbarkeit:
          $ref: '#/components/schemas/Verfuegbarkeit'
          description: |-
            Erreichbarkeit des Unternehmens an den Werktagen
            DTM Z36
            PI 37000 37001 37002 37005 37004 37003 37006
        zeit:
          type: string
          description: |-
            Zeit der Erreichbarkeit
            501 HHMMHHMM
      x-apidog-orders:
        - verfuegbarkeit
        - zeit
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Verfuegbarkeit:
      type: string
      title: Verfuegbarkeit
      description: Verfuegbarkeit
      enum:
        - MONTAG
        - DIENSTAG
        - MITTWOCH
        - DONNERSTAG
        - FREITAG
        - PAUSE
      x-apidog-enum:
        - value: MONTAG
          name: Verfügbarkeit Montag
          description: Z36
        - value: DIENSTAG
          name: Verfügbarkeit Dienstag
          description: Z37
        - value: MITTWOCH
          name: Verfügbarkeit Mittwoch
          description: Z38
        - value: DONNERSTAG
          name: Verfügbarkeit Donnerstag
          description: Z39
        - value: FREITAG
          name: Verfügbarkeit Freitag
          description: Z40
        - value: PAUSE
          name: Mittagspause (= Ausschluss der Verfügbarkeit)
          description: Z41
      x-apidog-folder: ''
    Bankverbindung:
      title: Bankverbindung
      type: object
      properties:
        verwendungszweck:
          $ref: '#/components/schemas/BankverbindungVerwendungszweck'
          description: nicht in Benutzung
        iban:
          type: string
          description: IBAN
        kontoinhaber:
          type: string
          description: Der Kontoinhaber
        bic:
          type: string
          description: BIC Code
        kreditinstitut:
          type: string
          description: Name des Kreditinstitut
      x-apidog-orders:
        - verwendungszweck
        - iban
        - kontoinhaber
        - bic
        - kreditinstitut
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    BankverbindungVerwendungszweck:
      title: BankverbindungVerwendungszweck
      type: string
      enum:
        - BV_ZAHLUNG_NNA
        - BV_ZAHLUNG_MMMA
        - BV_ZAHLUNG_MSB_ABRECHNNUNG
        - BV_ZAHLUNG_ENT_SPERREN_ABRECHNUNG
        - BV_SONSTIGE
      description: BankverbindungVerwendungszweck
      x-apidog-folder: ''
    MSBEigenschaft:
      type: string
      title: MSBEigenschaft
      description: MSBEigenschaft
      enum:
        - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
        - WETTBEWERBLICHER_MESSSTELLENBETREIBER
        - AUFFANGMESSSTELLENBETREIBER
      x-apidog-enum:
        - value: GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
          name: Grundzuständiger Messstellenbetreiber
          description: Z39
        - value: WETTBEWERBLICHER_MESSSTELLENBETREIBER
          name: Wetbewerblicher Messstellenbetreiber
          description: Z40
        - value: AUFFANGMESSSTELLENBETREIBER
          name: Auffangmessstellenbetreiber
          description: Z41
      x-apidog-folder: ''
    Kommunikationsparameter:
      title: Kommunikationsparameter
      type: object
      properties:
        zieladresse:
          $ref: '#/components/schemas/Zieladresse'
          description: nicht in Benutzung
        zertifikatsAussteller:
          $ref: '#/components/schemas/ZertifikatsAussteller'
          description: nicht in Benutzung
        zertifikatsNutzer:
          $ref: '#/components/schemas/ZertifikatsNutzer'
          description: nicht in Benutzung
      x-apidog-orders:
        - zieladresse
        - zertifikatsAussteller
        - zertifikatsNutzer
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    ZertifikatsNutzer:
      title: ZertifikatsNutzer
      type: object
      properties:
        zertifikatsNutzer1:
          type: string
          description: Zertifikatsnutzer 1
        zertifikatsNutzer2:
          type: string
          description: Zertifikatsnutzer 2
        zertifikatsNutzer3:
          type: string
          description: Zertifikatsnutzer 3
        zertifikatsNutzer4:
          type: string
          description: Zertifikatsnutzer 4
        zertifikatsNutzer5:
          type: string
          description: Zertifikatsnutzer 5
      x-apidog-orders:
        - zertifikatsNutzer1
        - zertifikatsNutzer2
        - zertifikatsNutzer3
        - zertifikatsNutzer4
        - zertifikatsNutzer5
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    ZertifikatsAussteller:
      title: ZertifikatsAussteller
      type: object
      properties:
        zertifikatsAussteller1:
          type: string
          description: Zertifikats Aussteller 1
        zertifikatsAussteller2:
          type: string
          description: Zertifikats Aussteller 2
        zertifikatsAussteller3:
          type: string
          description: Zertifikats Aussteller 3
        zertifikatsAussteller4:
          type: string
          description: Zertifikats Aussteller 4
        zertifikatsAussteller5:
          type: string
          description: Zertifikats Aussteller 5
      x-apidog-orders:
        - zertifikatsAussteller1
        - zertifikatsAussteller2
        - zertifikatsAussteller3
        - zertifikatsAussteller4
        - zertifikatsAussteller5
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zieladresse:
      title: Zieladresse
      type: object
      properties:
        zieladresse1:
          type: string
          description: Zieladresse URI IPv4 für die Bereitstellung der Werte
        zieladresse2:
          type: string
          description: Zieladresse URI IPv6 für die Bereitstellung der Werte
        zieladresse3:
          type: string
          description: Zieladresse 3
        zieladresse4:
          type: string
          description: Zieladresse 4
        zieladresse5:
          type: string
          description: Zieladresse 5
      x-apidog-orders:
        - zieladresse1
        - zieladresse2
        - zieladresse3
        - zieladresse4
        - zieladresse5
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Kommunikationsrolle:
      type: string
      title: Kommunikationsrolle
      description: Kommunikationsrolle
      enum:
        - DATENAUSTAUSCH
        - RAHMENVERTRAEGE
        - KUENDIGUNGSPROZESSE
        - WECHSELPROZESSE
        - STAMMDATENPROZESSE
        - EINSPEISEPROZESSE
        - ABRECHNUNGSPROZESSE
        - MMMA_PROZESSE
        - BEWEGUNGSDATEN
        - ENT_SPERR_PROZESSE
        - BILANZIERUNGSPROZESSE
        - NETZANSCHLUSS_ANLAGEN
      x-apidog-enum:
        - value: DATENAUSTAUSCH
          name: Ansprechpartner Übertragungsweg / Datenaustausch
          description: Z10
        - value: RAHMENVERTRAEGE
          name: Ansprechpartner Rahmenverträge
          description: Z11
        - value: KUENDIGUNGSPROZESSE
          name: Ansprechpartner Kündigungsprozesse
          description: Z12
        - value: WECHSELPROZESSE
          name: Ansprechpartner Wechselprozesse
          description: Z13
        - value: STAMMDATENPROZESSE
          name: Ansprechpartner Stammdatenprozesse
          description: Z14
        - value: EINSPEISEPROZESSE
          name: Ansprechpartner Einspeiseprozesse
          description: Z16
        - value: ABRECHNUNGSPROZESSE
          name: Ansprechpartner Abrechnungsprozesse
          description: Z17
        - value: MMMA_PROZESSE
          name: Ansprechpartner MMMA-Prozesse
          description: Z18
        - value: BEWEGUNGSDATEN
          name: Ansprechpartner Bewegungsdaten
          description: Z19
        - value: ENT_SPERR_PROZESSE
          name: Ansprechpartner Sperr-/Entsperrprozesse
          description: Z20
        - value: BILANZIERUNGSPROZESSE
          name: Ansprechpartner Bilanzierungsprozesse / Bilanzkreismanagement
          description: Z21
        - value: NETZANSCHLUSS_ANLAGEN
          name: >-
            Ansprechpartner technischer Netzanschluss für Neuanlagen und
            Anlagenumbau
          description: Z33
      x-apidog-folder: ''
    Ansprechpartner:
      title: Ansprechpartner
      type: object
      properties:
        boTyp: *ref_6
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        nachname:
          type: string
          description: Nachname (Familienname) des Ansprechpartners
        eMailAdresse:
          type: string
          description: E-Mail Adresse
        rufnummern:
          type: array
          items:
            $ref: '#/components/schemas/Rufnummer'
          description: >-
            Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar
            ist.
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - nachname
        - eMailAdresse
        - rufnummern
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Ansprechpartner.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Rufnummer:
      title: Rufnummer
      type: object
      properties:
        nummerntyp:
          $ref: '#/components/schemas/Rufnummernart'
          description: |-
            Art des Kommunikationsmittels
            COM
        rufnummer:
          type: string
          description: Rufnummer
      x-apidog-orders:
        - nummerntyp
        - rufnummer
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Rufnummernart:
      type: string
      title: Rufnummernart
      description: Rufnummernart
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
      x-apidog-enum:
        - value: RUF_ZENTRALE
          name: weiteres Telefon
          description: AJ
        - value: FAX_ZENTRALE
          name: ''
          description: ''
        - value: SAMMELRUF
          name: ''
          description: ''
        - value: SAMMELFAX
          name: ''
          description: ''
        - value: ABTEILUNGRUF
          name: ''
          description: ''
        - value: ABTEILUNGFAX
          name: ''
          description: ''
        - value: RUF_DURCHWAHL
          name: Telefon
          description: TE
        - value: FAX_DURCHWAHL
          name: Telefax
          description: FX
        - value: MOBIL_NUMMER
          name: Handy
          description: AL
      x-apidog-folder: ''
    Rollencodetyp:
      type: string
      title: Rollencodetyp
      description: Rollencodetyp
      enum:
        - BDEW
        - GS1
        - GLN
        - DVGW
      x-apidog-enum:
        - value: BDEW
          name: DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)
          description: '293'
        - value: GS1
          name: GS1
          description: '9'
        - value: GLN
          name: ''
          description: ''
        - value: DVGW
          name: DE, DVGW Service & Consult GmbH
          description: '332'
      x-apidog-folder: ''
    Adresse:
      title: Adresse
      type: object
      properties:
        postleitzahl:
          type: string
          description: Postleitzahl
        ort:
          type: string
          description: Ort
        strasse:
          type: string
          description: Strasse
        hausnummer:
          type: string
          description: Hausnummer und Ergänzung
        postfach:
          type: string
          description: Postfach
        adresszusatz:
          type: string
          description: Adresszusatz
        coErgaenzung:
          type: string
          description: coErgaenzung
        landescode:
          $ref: '#/components/schemas/Landescode'
          description: Landescode
        ortsteil:
          type: string
          description: Ortsteil
        zusatzInformation:
          $ref: '#/components/schemas/AdresszusatzInformation'
          description: Zusatzinformation zur Identifizierung, Zeile für Name und Anschrift
      x-apidog-orders:
        - postleitzahl
        - ort
        - strasse
        - hausnummer
        - postfach
        - adresszusatz
        - coErgaenzung
        - landescode
        - ortsteil
        - zusatzInformation
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    AdresszusatzInformation:
      title: AdresszusatzInformation
      type: object
      properties:
        zusatz1:
          type: string
          description: Adresszusatz 1
        zusatz2:
          type: string
          description: Adresszusatz 2
        zusatz3:
          type: string
          description: Adresszusatz 3
        zusatz4:
          type: string
          description: Adresszusatz 4
        zusatz5:
          type: string
          description: Adresszusatz 5
      x-apidog-orders:
        - zusatz1
        - zusatz2
        - zusatz3
        - zusatz4
        - zusatz5
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Landescode:
      title: Landescode
      type: string
      enum:
        - AC
        - AD
        - AE
        - AF
        - AG
        - AI
        - AL
        - AM
        - AN
        - AO
        - AQ
        - AR
        - AS
        - AT
        - AU
        - AW
        - AX
        - AZ
        - BA
        - BB
        - BD
        - BE
        - BF
        - BG
        - BH
        - BI
        - BJ
        - BL
        - BM
        - BN
        - BO
        - BQ
        - BR
        - BS
        - BT
        - BU
        - BV
        - BW
        - BY
        - BZ
        - CA
        - CC
        - CD
        - CF
        - CG
        - CH
        - CI
        - CK
        - CL
        - CM
        - CN
        - CO
        - CP
        - CR
        - CS
        - CU
        - CV
        - CW
        - CX
        - CY
        - CZ
        - DE
        - DG
        - DJ
        - DK
        - DM
        - DO
        - DZ
        - EA
        - EC
        - EE
        - EG
        - EH
        - ER
        - ES
        - ET
        - EU
        - FI
        - FJ
        - FK
        - FM
        - FO
        - FR
        - FX
        - GA
        - GB
        - GD
        - GE
        - GF
        - GG
        - GH
        - GI
        - GL
        - GM
        - GN
        - GP
        - GQ
        - GR
        - GS
        - GT
        - GU
        - GW
        - GY
        - HK
        - HM
        - HN
        - HR
        - HT
        - HU
        - IC
        - ID
        - IE
        - IL
        - IM
        - IN
        - IO
        - IQ
        - IR
        - IS
        - IT
        - JE
        - JM
        - JO
        - JP
        - KE
        - KG
        - KH
        - KI
        - KM
        - KN
        - KP
        - KR
        - KW
        - KY
        - KZ
        - LA
        - LB
        - LC
        - LI
        - LK
        - LR
        - LS
        - LT
        - LU
        - LV
        - LY
        - MA
        - MC
        - MD
        - ME
        - MF
        - MG
        - MH
        - MK
        - ML
        - MM
        - MN
        - MO
        - MP
        - MQ
        - MR
        - MS
        - MT
        - MU
        - MV
        - MW
        - MX
        - MY
        - MZ
        - NA
        - NC
        - NE
        - NF
        - NG
        - NI
        - NL
        - 'NO'
        - NP
        - NR
        - NT
        - NU
        - NZ
        - OM
        - PA
        - PE
        - PF
        - PG
        - PH
        - PK
        - PL
        - PM
        - PN
        - PR
        - PS
        - PT
        - PW
        - PY
        - QA
        - RE
        - RO
        - RS
        - RU
        - RW
        - SA
        - SB
        - SC
        - SD
        - SE
        - SF
        - SG
        - SH
        - SI
        - SJ
        - SK
        - SL
        - SM
        - SN
        - SO
        - SR
        - SS
        - ST
        - SU
        - SV
        - SX
        - SY
        - SZ
        - TA
        - TC
        - TD
        - TF
        - TG
        - TJ
        - TK
        - TL
        - TM
        - TN
        - TO
        - TP
        - TR
        - TT
        - TV
        - TW
        - TZ
        - UA
        - UG
        - UK
        - UM
        - US
        - UY
        - UZ
        - VA
        - VC
        - VE
        - VG
        - VI
        - VN
        - VU
        - WF
        - WS
        - XK
        - YE
        - YT
        - YU
        - ZA
        - ZM
        - ZR
        - ZW
      description: Der ISO-Landescode als Enumeration
      x-apidog-folder: ''
    Geschaeftspartnerrolle:
      type: string
      title: Geschaeftspartnerrolle
      description: Geschaeftspartnerrolle
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
      x-apidog-enum:
        - value: KUNDE
          name: ''
          description: ''
        - value: LIEFERANT
          name: ''
          description: ''
        - value: DIENSTLEISTER
          name: ''
          description: ''
        - value: INTERESSENT
          name: ''
          description: ''
        - value: MARKTPARTNER
          name: ''
          description: ''
        - value: EIGENTUEMER
          name: ''
          description: ''
        - value: HAUSVERWALTER
          name: ''
          description: ''
        - value: KORRESPONDENZEMPFAENGER
          name: ''
          description: ''
        - value: ABLESEKARTENEMPFAENGER
          name: ''
          description: ''
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
    Lokationszuordnung:
      title: Lokationszuordnung
      type: string
      enum:
        - UNVERAENDERT
        - BEGINNT
        - ENDET
      description: Lokationszuordnung
      x-apidog-folder: ''
    Sparte:
      type: string
      title: Sparte
      description: Division
      enum:
        - STROM
        - GAS
        - FERNWAERME
        - NAHWAERME
        - WASSER
        - ABWASSER
      x-apidog-enum:
        - value: STROM
          name: Sparte Strom
          description: Represents electricity as the utility division
        - value: GAS
          name: Sparte Gas
          description: Represents natural gas as the utility division
        - value: FERNWAERME
          name: Sparte Fernwärme
          description: Represents district heating as the utility division
        - value: NAHWAERME
          name: Sparte Nahwärme
          description: Represents local heating as the utility division
        - value: WASSER
          name: Sparte Wasser
          description: Represents water supply as the utility division
        - value: ABWASSER
          name: Sparte Abwasser
          description: Represents wastewater services as the utility division
      examples:
        - STROM
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
