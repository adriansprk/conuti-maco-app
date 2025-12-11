# Energieliefervertrag lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getEnerySupplyContractBasic:
    get:
      summary: Energieliefervertrag lesen
      deprecated: false
      description: >-
        Lesen des Energieliefervertrages einer Lokation (Parameter1) vom Typ
        (Parameter2 - default MALO) zum Stichtag (Parameter3)
      operationId: LESEN_ENERGIELIEFERVERTRAG_BASIS
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
          description: 'Datum (Gültig bis) '
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
          example: SAP_LESEN_ENERGIELIEFERVERTRAG_BASIS
          schema:
            type: string
      responses:
        '200':
          description: Erfolgreiches Lesen des Energieliefervertrages
          content:
            application/json:
              schema:
                type: object
                properties:
                  boTyp: &ref_2
                    $ref: '#/components/schemas/BOTyp'
                    default: VERTRAG
                  versionStruktur:
                    type: string
                    default: '1'
                  sparte: &ref_11
                    $ref: '#/components/schemas/Sparte'
                    description: 'Unterscheidungsmöglichkeiten für die Sparte. '
                  vertragsart:
                    type: string
                    description: >-
                      Hier ist festgelegt, um welche Art von Vertrag es sich
                      handelt. Z.B. Netznutzungvertrag
                  vertragsnummer:
                    type: string
                    description: >-
                      Eine im Verwendungskontext eindeutige Nummer für den
                      Vertrag
                  beschreibung:
                    type: string
                    description: >-
                      Freitext zur Beschreibung der Konditionen, z.B.
                      "Standardkonditionen Gas"
                  lokationsId:
                    type: string
                    description: >-
                      Referenz auf die ID der Marktlokation / Messlokation

                      RFF Z18 Kunde des LF

                      PI 55043 55168 55169

                      RFF Z46 Malo

                      55616 55622 55628 55634 55109 55137 55110 55136 55643
                      55648 55663 55669 55653 55658

                      RFF Z19

                      PI 55040 55043 55168 55169  
                  lokationsTyp: &ref_12
                    $ref: '#/components/schemas/Lokationstyp'
                    description: |-
                      Referenz auf die ID der Messlokation
                      RFF Z19
                  vertragsstatus: &ref_13
                    $ref: '#/components/schemas/Vertragstatus'
                    description: nicht in Benutzung
                  vertragsbeginn:
                    type: string
                    format: date-time
                    description: >-
                      Gibt an, wann der Vertrag oder die Zuordnung beginnt.

                      DTM 92

                      PI 55001 55002 55077 55078 55600 55602 55601 55603 55013
                      55014 55607 55608 55004 55005 55051 55052 55238 55239
                      55235 55237
                  vertragsende:
                    type: string
                    format: date-time
                    description: >-
                      Gibt das Ende der Netznutzung oder einer Zuordnung an. 

                      DTM 93

                      PI 55016 55017 55001 55002 55600 55602 55013 55014 55607
                      55608 55010 55011 55004 55005 55007 55008 55039 55040
                      55051 55052 55240 55241 55242 55243 55236 55237
                  gemeinderabatt:
                    type: integer
                    description: >-
                      Gemeinderabatt - Angabe zum Preisnachlass der
                      Netznutzungsentgelte

                      QTY Z16

                      PI 44112 44139 44142 44001 44002 44013 44014 44035
                  vertragskonditionen: &ref_14
                    $ref: '#/components/schemas/Vertragskonditionen'
                    description: Festlegungen zu Laufzeiten und Kündigungsfristen.
                  korrespondenzpartner: &ref_0
                    $ref: '#/components/schemas/Geschaeftspartner'
                    description: |-
                      Korrespondenzanschrift des Kunden des Lieferanten
                      NAD Z04
                      PI 44109 44112 44113 44137 44138 44001 44002 44013 44014 
                  abrechnungUeberNna:
                    type: boolean
                    description: >-
                      Abrechnung des Messstellenbetriebs über NNE - ob die
                      Abrechnung der Entgelte für Messstellenbetrieb über die 

                      Netznutzungsabrechnung erfolgt - wird mit JA oder NEIN
                      beantwortet

                      RFF Z05

                      PI 55620 55626 
                  datenqualitaet: &ref_15
                    $ref: '#/components/schemas/Datenqualitaet'
                    description: |-
                      Referenzierung auf eine ID einer Marktlokation aus LOC+Z16
                      RFF Z50
                      PI 55218 55640 55650 55660 55043 55168 55169 
                      RFF Z51 Z52
                      PI 55220 55645 55655 55665
                  gueltigkeitszeitraum: &ref_3
                    $ref: '#/components/schemas/Zeitraum'
                    description: Referenz auf die Zeitraum-ID
                  vertragspartner1:
                    type: array
                    items: *ref_0
                    description: >-
                      Der "erstgenannte" Vertragspartner. In der Regel der
                      Aussteller des Vertrags. Beispiel: "Vertrag zwischen

                      Vertagspartner 1 ..." Siehe BO Geschaeftspartner
                  vertragspartner2:
                    type: array
                    items: *ref_0
                    description: >-
                      Der "zweitgenannte" Vertragspartner. In der Regel der
                      Empfänger des Vertrags. Beispiel "Vertrag zwischen

                      Vertagspartner 1 und Vertragspartner 2". Siehe BO
                      Geschaeftspartner

                      IFTSTA Name und Anschrift Kunde des LF 

                      NAD Z09

                      PI 21045
                  enFG:
                    type: array
                    items: &ref_16
                      $ref: '#/components/schemas/EnFG'
                    description: enFG
                x-apidog-orders:
                  - 01JM7ZPH5C82BRAZXCGYEWZYZB
                required:
                  - boTyp
                  - versionStruktur
                x-apidog-refs:
                  01JM7ZPH5C82BRAZXCGYEWZYZB:
                    $ref: '#/components/schemas/Vertrag'
                x-apidog-ignore-properties:
                  - boTyp
                  - versionStruktur
                  - sparte
                  - vertragsart
                  - vertragsnummer
                  - beschreibung
                  - lokationsId
                  - lokationsTyp
                  - vertragsstatus
                  - vertragsbeginn
                  - vertragsende
                  - gemeinderabatt
                  - vertragskonditionen
                  - korrespondenzpartner
                  - abrechnungUeberNna
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - vertragspartner1
                  - vertragspartner2
                  - enFG
              example:
                stammdaten:
                  ENERGIELIEFERVERTRAG:
                    - boTyp: VERTRAG
                      versionStruktur: '1'
                      gueltigkeitszeitraum:
                        zeitraumId: null
                        startdatum: null
                        enddatum: null
                      datenqualitaet: null
                      vertragsnummer: '12345'
                      beschreibung: XYZ
                      vertragsart: ENERGIELIEFERVERTRAG
                      vertragstatus: GEKUENDIGT
                      sparte: STROM
                      vertragsbeginn: '0001-01-01T00:00:00Z'
                      vertragsende: '9999-12-31T23:59:59Z'
                      vertragspartner2:
                        - boTyp: GESCHAEFTSPARTNER
                          versionStruktur: '1'
                          gewerbekennzeichnung: false
                          anrede: Herr
                          name1: Haiko
                          name2: Fisch
                          name3: null
                          geschaeftspartnerrolle:
                            - KUNDE
                          partneradresse:
                            postleitzahl: '65189'
                            ort: Wiesbaden
                            strasse: Korallenweg
                            hausnummer: '10'
                            postfach: null
                            adresszusatz: null
                            coErgaenzung: null
                            landescode: DE
                            ortsteil: Riff
                          externeReferenzen:
                            - exRefName: Kundennummer beim Altlieferanten
                              exRefWert: NummerLFA123456_Z01
                      vertragskonditionen:
                        kuendigungsfrist:
                          zeitraumText: null
                        kuendigungstermin: '2025-07-31T23:00:00Z'
                        abrechnungsintervall: null
                      korrespondenzpartner:
                        boTyp: GESCHAEFTSPARTNER
                        versionStruktur: '1'
                        anrede: Herr
                        name1: Hai
                        name2: Fisch
                        name3: null
                        gewerbekennzeichnung: false
                        partneradresse:
                          postleitzahl: '65189'
                          ort: Wiesbaden
                          strasse: Körallenweg
                          hausnummer: '10'
                          postfach: null
                          adresszusatz: null
                          coErgaenzung: null
                          landescode: DE
                          ortsteil: Riff
                      lokationsId: '50754496000'
                      lokationsTyp: MALO
                      enFG:
                        - grundlageVerringerungUmlagen: KEINE_ANGABE
                          grund:
                            - null
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017014-run
components:
  schemas:
    EnFG:
      title: EnFG
      type: object
      properties:
        grundlageVerringerungUmlagen:
          $ref: '#/components/schemas/GrundlageVerringerungUmlagen'
          description: |-
            Grundlage zur Verringerung der Umlagen nach EnFG
            CCI Z61 
            PI 55001 55014 55109 55137 
        grund:
          type: array
          items:
            $ref: '#/components/schemas/GrundlageVerringerungUmlagenGrund'
          description: |-
            Grund der Privilegierung nach EnFG
            CAV ZU5
            PI 55001 55014 55109 55137 
      x-apidog-orders:
        - grundlageVerringerungUmlagen
        - grund
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    GrundlageVerringerungUmlagenGrund:
      type: string
      title: GrundlageVerringerungUmlagenGrund
      description: GrundlageVerringerungUmlagenGrund
      enum:
        - ENFG_STROMSPEICHER_UND_VERLUSTENERGIE
        - ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
        - ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN
        - ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF
        - ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN
        - ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN
        - ENFG_SCHIENENBAHNEN
        - ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR
        - ENFG_LANDSTROMANLAGEN
      x-apidog-enum:
        - value: ENFG_STROMSPEICHER_UND_VERLUSTENERGIE
          name: § 21 EnFG Stromspeicher und Verlustenergie
          description: ZU5
        - value: ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
          name: § 22 EnFG elektrisch angetriebene Wärmepumpen
          description: ZU6
        - value: ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN
          name: § 23 EnFG Umlageerhebung bei Anlagen zur Verstromung von Kuppelgasen
          description: ZU7
        - value: ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF
          name: § 24 EnFG Herstellung von Grünen Wasserstof
          description: ZU8
        - value: ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN
          name: §§ 30 - 35 EnFG stromkostenintensive Unternehmen
          description: ZU9
        - value: >-
            ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN
          name: >-
            § 36 EnFG Herstellung von Wasserstoff in stromkostenintensiven
            Unternehmen
          description: ZV0
        - value: ENFG_SCHIENENBAHNEN
          name: § 37 EnFG Schienenbahnen
          description: ZV1
        - value: ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR
          name: § 38 EnFG elektrische betriebene Bussen im Linienverkehr
          description: ZV2
        - value: ENFG_LANDSTROMANLAGEN
          name: § 39 EnFG Landstromanlagen
          description: ZV3
      x-apidog-folder: ''
    GrundlageVerringerungUmlagen:
      type: string
      title: GrundlageVerringerungUmlagen
      description: Grundlage zur Verringerung der Umlagen nach EnFG
      enum:
        - ERFUELLT_VORAUSSETZUNG_NACH_ENFG
        - ERFUELLT_NICHT_VORAUSSETZUNG_NACH_ENFG
        - KEINE_ANGABE
      x-apidog-enum:
        - value: ERFUELLT_VORAUSSETZUNG_NACH_ENFG
          name: Kunde erfüllt die Voraussetzung nach EnFG
          description: ZF9
        - value: ERFUELLT_NICHT_VORAUSSETZUNG_NACH_ENFG
          name: Kunde erfüllt nicht die Voraussetzung nach EnFG
          description: ZG0
        - value: KEINE_ANGABE
          name: >-
            Keine Angabe, da Marktlokation die Voraussetzung zur Verringerung
            der Umlagen nach EnFG nicht erfüllt
          description: ZG1
      x-apidog-folder: ''
    Zeitraum:
      title: Zeitraum
      type: object
      properties:
        zeiteinheit: &ref_1
          $ref: '#/components/schemas/Zeiteinheit'
          description: nicht in Benutzung
        dauer: &ref_4
          type: integer
          description: Zeitspanne, Wert
        startdatum: &ref_5
          type: string
          format: date-time
          description: |-
            Datum aus 
            DTM Z25 Verwendung der Daten ab 
            DTM 163 Verarbeitung, Beginndatum/-zeit
            DTM 155 Rechnungsperiode, Beginndatum
            DTM Z42 vorläufiger Abrechnungszeitraum Beginn
        enddatum: &ref_6
          type: string
          format: date-time
          description: |-
            Datum aus 
            DTM Z26 Verwendung der Daten bis 
            DTM164 Verarbeitung, Endedatum/-zeit
            DTM 156 Rechnungsperiode, Endedatum
            DTM Z43 vorläufiger Abrechnungszeitraum Ende
        einheit: *ref_1
        ableseZeitraum: &ref_7
          type: string
          description: |-
            Turnusablesung des NB
            DTM 752
            PI 44113 44140 44142 44043 44168 44169 44060 
        abrechnungsZeitraum: &ref_8
          type: string
          description: |-
            Termin, zu dem die Netznutzungsabrechnung des NB erfolgt
            DTM Z21
            PI 44112 44139 44142 44002 44013 44014 44035
        zeitraumText: &ref_9
          type: string
          description: ZeitraumText
        zeitraumId: &ref_10
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
    Geschaeftspartner:
      title: Geschaeftspartner
      type: object
      properties:
        boTyp: *ref_2
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        anrede:
          type: string
          description: |-
            Die Anrede für den GePa, Z.B. Herr.
            Z04 Korrespondenzanschrift des Kunden des Lieferanten
            PI 55001 55600 55601 55013 55014 55043 55168 55169
        name1:
          type: string
          description: >-
            Erster Teil des Namens. Hier kann der Firmenname oder bei
            Privatpersonen beispielsweise der Nachname dargestellt werden.
            Beispiele: Yellow Strom GmbH oder Hagen
        name2:
          type: string
          description: >-
            Zweiter Teil des Namens. Hier kann der eine Erweiterung zum
            Firmennamen oder bei Privatpersonen beispielsweise der Vorname
            dargestellt werden. Beispiele: Bereich Süd oder Nina
        name3:
          type: string
          description: >-
            Dritter Teil des Namens. Hier können weitere Ergänzungen zum
            Firmennamen oder bei Privatpersonen Zusätze zum  Namen dargestellt
            werden. Beispiele: und Afrika oder Sängerin
        name4:
          type: string
          description: Name 4
        umsatzsteuerId:
          type: string
          description: 'Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825'
        glaeubigerId:
          type: string
          description: >-
            Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird- Z.B. DE
            47116789
        emailAdresse:
          type: string
          description: email Adresse
        website:
          type: string
          description: 'Internetseite des Marktpartners. Beispiel: www.mp-energie.de'
        gewerbekennzeichnung:
          type: boolean
          description: >-
            Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
            (gewerbeKennzeichnung = true)

            oder eine Privatperson handelt. (gewerbeKennzeichnung = false)

            Z01 Struktur von Personennamen

            Z02 Struktur der Firmenbezeichnung
        hrnummer:
          type: string
          description: Handelsregisternummer des Geschäftspartners
        amtsgericht:
          type: string
          description: >-
            Amtsgericht bzw Handelsregistergericht, das die
            Handelsregisternummer herausgegeben hat
        partneradresse:
          $ref: '#/components/schemas/Adresse'
          description: Adresse des Geschäftspartners, an der sich der Hauptsitz befindet.
        externeKundenummerLieferant:
          type: string
          description: externeKundenummerLieferant
        externeReferenzen:
          type: array
          items:
            $ref: '#/components/schemas/ExterneReferenz'
          description: >-
            Hier können IDs anderer Systeme hinterlegt werden (z.B. eine
            SAP-GP-Nummer) (Details siehe ExterneReferenz)
        geschaeftspartnerrolle:
          type: array
          items:
            $ref: '#/components/schemas/Geschaeftspartnerrolle'
          description: |-
            Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde).
            NAD Z09 ORDERS
            PI 17101 17003
            NAD Kunde des Messstellenbetreibers ORDERS
            PI 17126
        kontaktweg:
          type: array
          items:
            $ref: '#/components/schemas/Kontaktart'
          description: Bevorzugter Kontaktweg des Geschäftspartners.
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - anrede
        - name1
        - name2
        - name3
        - name4
        - umsatzsteuerId
        - glaeubigerId
        - emailAdresse
        - website
        - gewerbekennzeichnung
        - hrnummer
        - amtsgericht
        - partneradresse
        - externeKundenummerLieferant
        - externeReferenzen
        - geschaeftspartnerrolle
        - kontaktweg
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Geschaeftspartner.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Kontaktart:
      title: Kontaktart
      type: string
      enum:
        - ANSCHREIBEN
        - TELEFONAT
        - FAX
        - E_MAIL
        - SMS
      description: >-
        Gibt an, auf welchem Weg die Person oder der Geschäftspartner
        kontaktiert werden kann
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
    ExterneReferenz:
      title: ExterneReferenz
      type: object
      properties:
        exRefName:
          type: string
          enum:
            - Kundennummer beim Lieferanten
            - Kundennummer beim Altlieferanten
          description: >-
            Bezeichnung der externen Referenz, Kundennummer beim Lieferanten,
            bezieht sich auf das vorangegangene NAD Segment

            RFF AVC

            PI 55109 55137 

            RFF AVC Kundennummer beim Lieferanten ORDERS

            PI 17101
        exRefWert:
          type: string
          description: >-
            Kundennummer beim Altieferanten - Angabe von Referenzen für
            Rückmeldungen und Anfragen

            PI 55109 55137 

            ORDERS PI 17101
      x-apidog-orders:
        - exRefName
        - exRefWert
      x-apidog-ignore-properties: []
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
    Vertragskonditionen:
      title: Vertragskonditionen
      type: object
      properties:
        netznutzungszahler:
          $ref: '#/components/schemas/Netznutzungszahler'
          description: >-
            Hier wird festgelegt, wer die Netznutzung der verbrauchenden Malo
            bezahlt. 

            CAV Z73

            PI 55218 55220 
        netznutzungsvertrag:
          $ref: '#/components/schemas/Netznutzungsvertrag'
          description: >-
            Angaben zum Netznutzungsvertrag, ist die Beziehung der
            Vertragsparteien zur verbrauchenden Malo. 

            CAV Z74

            PI 55218 55220 
        netznutzungsabrechnung: *ref_3
        beinhaltetSingulaerGenutzteBetriebsmittel:
          type: boolean
          description: >-
            Singulär genutzte Betriebsmittel in der Netznutzungsabrechnung Hier
            wird angegeben, ob in der  Netznutzungsabrechnung der verbrauchenden
            Marktlokation singulär genutzte Betriebsmittel abgerechnet werden.
        netznutzungsabrechnungsgrundlage:
          $ref: '#/components/schemas/Netznutzungsabrechnungsgrundlage'
          description: >-
            Grundlage für Lieferscheinprüfung, kann der Lieferant die erhaltenen
            Mengen zur Lieferscheinprüftung nutzen Z12 oder existiert eine
            Vereinbarung das ermittelte Werte nicht zu den Werten der
            Netznutzungsabrechnung passen Z13.

            CAV ZA7

            PI 55218 55220  
        netznutzungsabrechnungsvariante:
          $ref: '#/components/schemas/Netznutzungsabrechnungsvariante'
          description: |-
            Netznutzungsabrechnungsvariante einer verbrauchenden Marktlokation
            CAV ZB1
            PI 44112 44139 44142 44002 44013 44014 44035
        haushaltskunde:
          type: boolean
          description: >-
            Gruppenzuordnung, kennzeichnet ob es sich um einen Haushaltskunden
            handelt oder nicht.

            Z15 Haushaltskunde gem. EnWG

            Z18 Kein Haushaltskunde gem. EnWG

            CCI Z15

            PI 55001 55600 55013 55014 55109 55137 
        abrechnungUeberNna:
          type: boolean
          description: Abrechnung über Nna
        gemeinderabatt:
          $ref: '#/components/schemas/Gemeinderabatt'
          description: nicht in Benutzung
        startAbrechnungsjahr:
          type: string
          format: date-time
          description: >-
            Start des Abrechnungsjahrs bei Marktlokationen mit
            Jahresleistungspreis - Rechnungsperiode, Beginndatum

            DTM 155

            PI 44112 44139 44142 44002 44013 44014 44035
        naechstenetznutzungsabrechnung:
          type: string
          description: >-
            Nächste Netznutzungsabrechnung - Mitteilung an den LF, in welchem
            Jahr die nächste Netznutzungabrechnung stattfindet.

            DTM Z09

            PI 55218 55220
        abrechnungsintervall:
          type: integer
          description: |-
            Abrechnungsintervall des LF in Monaten
            DTM Z20
            PI 44109 44137 44138 44001 44002 44014 
        netznutzungsabrechnungIntervall:
          type: integer
          description: >-
            Netznutzungsabrechnungs- bzw. Einspeisevergütungsintervall des NB,
            hier ist die Anzahl der Monate anzugeben, bis zur nächsten
            Netznutzungsabrechnung. 

            DTM Z22

            PI 55218 55220
        geplanteTurnusablesung: *ref_3
        beauftragungMsb:
          $ref: '#/components/schemas/BeauftragungMsb'
          description: >-
            Gibt an, ob ein Vertrag zwischen Anschlussnutzer und MSB vorliegt
            und ob die Vertragsbeendigung mit dem vorherigen Vertragspartner vor
            der Anmeldung beendet wurde. 

            AGR Z04

            PI 55042 
        kuendigungsfrist:
          description: >-
            Innerhalb dieser Frist kann der Vertrag gekündigt werden. Details
            Zeitraum

            DTM Z01

            PI 55018 55041 
          type: object
          x-apidog-refs:
            01JZJGTT5J8V4M00254JDKDZP2: *ref_3
          x-apidog-orders:
            - 01JZJGTT5J8V4M00254JDKDZP2
          properties:
            zeiteinheit: *ref_1
            dauer: *ref_4
            startdatum: *ref_5
            enddatum: *ref_6
            einheit: *ref_1
            ableseZeitraum: *ref_7
            abrechnungsZeitraum: *ref_8
            zeitraumText: *ref_9
            zeitraumId: *ref_10
          x-apidog-ignore-properties:
            - zeiteinheit
            - dauer
            - startdatum
            - enddatum
            - einheit
            - ableseZeitraum
            - abrechnungsZeitraum
            - zeitraumText
            - zeitraumId
        vertragslaufzeit: *ref_3
        kuendigungstermin:
          type: string
          description: |-
            Übermittlung bestimmtes Kündigungsdatum
            DTM Z10
            PI 55018 55041
        abschlagszyklus: *ref_3
        anzahl_abschlaege:
          type: number
          format: float
          description: Anzahl der vereinbarten Abschläge pro Jahr, z.B. 12
        beschreibung:
          type: string
          description: >-
            Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen
            Gas"
        vertragsverlaengerung: *ref_3
      x-apidog-orders:
        - netznutzungszahler
        - netznutzungsvertrag
        - netznutzungsabrechnung
        - beinhaltetSingulaerGenutzteBetriebsmittel
        - netznutzungsabrechnungsgrundlage
        - netznutzungsabrechnungsvariante
        - haushaltskunde
        - abrechnungUeberNna
        - gemeinderabatt
        - startAbrechnungsjahr
        - naechstenetznutzungsabrechnung
        - abrechnungsintervall
        - netznutzungsabrechnungIntervall
        - geplanteTurnusablesung
        - beauftragungMsb
        - kuendigungsfrist
        - vertragslaufzeit
        - kuendigungstermin
        - abschlagszyklus
        - anzahl_abschlaege
        - beschreibung
        - vertragsverlaengerung
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    BeauftragungMsb:
      type: string
      title: BeauftragungMsb
      description: Beauftragung oder Beendigung liegt vor
      enum:
        - VERTRAG_AN_MSB
        - VERTRAGSBEENDIGUNG_MSB
      x-apidog-enum:
        - value: VERTRAG_AN_MSB
          name: Vertrag zwischen AN und MSB
          description: Z04
        - value: VERTRAGSBEENDIGUNG_MSB
          name: Vertragsbeendigung liegt vor
          description: Z06
      x-apidog-folder: ''
    Gemeinderabatt:
      title: Gemeinderabatt
      type: object
      properties:
        wert:
          type: number
          format: float
          description: |-
            Angabe des Gemeinderabatts
            MOA Z01
            PI 31002 31004 31010
        einheit:
          type: string
          description: Einheit
        typ:
          type: string
          description: Typ
        bemessungsgrundlage:
          type: number
          format: float
          description: Bemessungsgrundlage des Gemeinderabatts- Geldbetrag
      x-apidog-orders:
        - wert
        - einheit
        - typ
        - bemessungsgrundlage
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Netznutzungsabrechnungsvariante:
      type: string
      title: Netznutzungsabrechnungsvariante
      description: Netznutzungsabrechnungsvariante
      enum:
        - ARBEITSPREIS_GRUNDPREIS
        - ARBEITSPREIS_LEISTUNGSPREIS
      x-apidog-enum:
        - value: ARBEITSPREIS_GRUNDPREIS
          name: Arbeitspreis/Grundpreis
          description: Z14
        - value: ARBEITSPREIS_LEISTUNGSPREIS
          name: Arbeitspreis/Leistungspreis
          description: Z15
      x-apidog-folder: ''
    Netznutzungsabrechnungsgrundlage:
      type: string
      title: Netznutzungsabrechnungsgrundlage
      description: Netznutzungsabrechnungsgrundlage
      enum:
        - LIEFERSCHEIN
        - ABWEICHENDE_GRUNDLAGE
      x-apidog-enum:
        - value: LIEFERSCHEIN
          name: In der Marktkommunikation ausgetauschte Daten
          description: Z12
        - value: ABWEICHENDE_GRUNDLAGE
          name: Abweichend vertraglich mit Anschlussnutzer vereinbarte Grundlage
          description: Z13
      x-apidog-folder: ''
    Netznutzungsvertrag:
      type: string
      title: Netznutzungsvertrag
      description: Netznutzungsvertrag
      enum:
        - KUNDEN_NB
        - LIEFERANTEN_NB
      x-apidog-enum:
        - value: KUNDEN_NB
          name: Direkter Vertrag zwischen Kunden und NB
          description: Z08
        - value: LIEFERANTEN_NB
          name: Vertrag zwischen Lieferanten und NB
          description: Z09
      x-apidog-folder: ''
    Netznutzungszahler:
      type: string
      title: Netznutzungszahler
      description: Netznutzungszahler
      enum:
        - KUNDE
        - LIEFERANT
      x-apidog-enum:
        - value: KUNDE
          name: Kunde
          description: Z10
        - value: LIEFERANT
          name: Lieferant
          description: Z11
      x-apidog-folder: ''
    Vertragstatus:
      title: Vertragstatus
      type: string
      enum:
        - IN_ARBEIT
        - UEBERMITTELT
        - ANGENOMMEN
        - AKTIV
        - ABGELEHNT
        - WIDERRUFEN
        - STORNIERT
        - GEKUENDIGT
        - BEENDET
      description: Vertragstatus
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
    Vertrag:
      title: Vertrag
      type: object
      properties:
        boTyp: *ref_2
        versionStruktur:
          type: string
          default: '1'
        sparte: *ref_11
        vertragsart:
          type: string
          description: >-
            Hier ist festgelegt, um welche Art von Vertrag es sich handelt. Z.B.
            Netznutzungvertrag
        vertragsnummer:
          type: string
          description: Eine im Verwendungskontext eindeutige Nummer für den Vertrag
        beschreibung:
          type: string
          description: >-
            Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen
            Gas"
        lokationsId:
          type: string
          description: >-
            Referenz auf die ID der Marktlokation / Messlokation

            RFF Z18 Kunde des LF

            PI 55043 55168 55169

            RFF Z46 Malo

            55616 55622 55628 55634 55109 55137 55110 55136 55643 55648 55663
            55669 55653 55658

            RFF Z19

            PI 55040 55043 55168 55169  
        lokationsTyp: *ref_12
        vertragsstatus: *ref_13
        vertragsbeginn:
          type: string
          format: date-time
          description: >-
            Gibt an, wann der Vertrag oder die Zuordnung beginnt.

            DTM 92

            PI 55001 55002 55077 55078 55600 55602 55601 55603 55013 55014 55607
            55608 55004 55005 55051 55052 55238 55239 55235 55237
        vertragsende:
          type: string
          format: date-time
          description: >-
            Gibt das Ende der Netznutzung oder einer Zuordnung an. 

            DTM 93

            PI 55016 55017 55001 55002 55600 55602 55013 55014 55607 55608 55010
            55011 55004 55005 55007 55008 55039 55040 55051 55052 55240 55241
            55242 55243 55236 55237
        gemeinderabatt:
          type: integer
          description: |-
            Gemeinderabatt - Angabe zum Preisnachlass der Netznutzungsentgelte
            QTY Z16
            PI 44112 44139 44142 44001 44002 44013 44014 44035
        vertragskonditionen: *ref_14
        korrespondenzpartner: *ref_0
        abrechnungUeberNna:
          type: boolean
          description: >-
            Abrechnung des Messstellenbetriebs über NNE - ob die Abrechnung der
            Entgelte für Messstellenbetrieb über die 

            Netznutzungsabrechnung erfolgt - wird mit JA oder NEIN beantwortet

            RFF Z05

            PI 55620 55626 
        datenqualitaet: *ref_15
        gueltigkeitszeitraum: *ref_3
        vertragspartner1:
          type: array
          items: *ref_0
          description: >-
            Der "erstgenannte" Vertragspartner. In der Regel der Aussteller des
            Vertrags. Beispiel: "Vertrag zwischen

            Vertagspartner 1 ..." Siehe BO Geschaeftspartner
        vertragspartner2:
          type: array
          items: *ref_0
          description: >-
            Der "zweitgenannte" Vertragspartner. In der Regel der Empfänger des
            Vertrags. Beispiel "Vertrag zwischen

            Vertagspartner 1 und Vertragspartner 2". Siehe BO Geschaeftspartner

            IFTSTA Name und Anschrift Kunde des LF 

            NAD Z09

            PI 21045
        enFG:
          type: array
          items: *ref_16
          description: enFG
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - sparte
        - vertragsart
        - vertragsnummer
        - beschreibung
        - lokationsId
        - lokationsTyp
        - vertragsstatus
        - vertragsbeginn
        - vertragsende
        - gemeinderabatt
        - vertragskonditionen
        - korrespondenzpartner
        - abrechnungUeberNna
        - datenqualitaet
        - gueltigkeitszeitraum
        - vertragspartner1
        - vertragspartner2
        - enFG
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Vertrag.json
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
