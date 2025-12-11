# Preisblatt lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getPriceSheetBasic:
    get:
      summary: Preisblatt lesen
      deprecated: false
      description: Lesen eines Preisblatts anhand processDate / gueltigAb
      operationId: LESEN_PREISBLATT_BASIS
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: 'LokationsId '
          required: false
          example: ''
          schema:
            type: string
            default: '74018657187'
            examples:
              - '74018657187'
        - name: parameter2
          in: query
          description: LokationsTyp
          required: false
          example: ''
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
          required: false
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
          example: SAP_LESEN_PREISBLATT_BASIS
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
                $ref: '#/components/schemas/Preisblatt'
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-24422191-run
components:
  schemas:
    Preisblatt:
      title: Preisblatt
      type: object
      properties:
        boTyp:
          $ref: '#/components/schemas/BOTyp'
          default: PREISBLATT
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        bezeichnung:
          type: string
          description: Bezeichnung des Auf-/Abschlags
        gueltigkeit: &ref_1
          $ref: '#/components/schemas/Zeitraum'
          description: |-
            Der Zeitraum für den der Preis festgelegt ist. Gültigkeitsbeginn
            DTM 157
            PI 27002 27003
        preisstatus:
          $ref: '#/components/schemas/Preisstatus'
          description: Gibt den Status des veröffentlichten Preises an
        sparte:
          $ref: '#/components/schemas/Sparte'
          description: Strom oder Gas
        bilanzierungsdatum:
          type: string
          format: date-time
          description: |-
            Bilanzierungsdatum
            DTM 492
            PI 27001
        regelzone:
          type: string
          description: |-
            Regelzone
            LOC 231
            PI 27001 
        leistungstyp: &ref_0
          $ref: '#/components/schemas/Leistungstyp'
          description: >-
            Standardisierte Bezeichnung für die abgerechnete
            Leistungserbringung. Details Leistungstyp
        nichtGenutzt:
          type: boolean
          description: nicht Genutzt
        preispositionen:
          type: array
          items:
            $ref: '#/components/schemas/Preisposition'
          description: >-
            Die einzelnen Positionen, die mit dem Preisblatt abgerechnet werden
            können. Z.B. Arbeitspreis, Grundpreis etc.

            Code des Preisschlüsselstamms

            PIA 1

            PI 27002
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - bezeichnung
        - gueltigkeit
        - preisstatus
        - sparte
        - bilanzierungsdatum
        - regelzone
        - leistungstyp
        - nichtGenutzt
        - preispositionen
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Preisblatt.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Preisposition:
      title: Preisposition
      type: object
      properties:
        berechnungsmethode:
          $ref: '#/components/schemas/Kalkulationsmethode'
          description: >-
            Das Modell, das der Preisbildung zugrunde liegt. Details
            Kalkulationsmethode
        leistungstyp: *ref_0
        leistungsbezeichnung:
          type: string
          description: >-
            Bezeichnung für die in der Position abgebildete Leistungserbringung.

            Z15 POG bei verbrauchender Marktlokation > 100.000 kWh/a mit iMS

            Z16 POG bei verbrauchender Marktlokation ]50.000 kWh/a; 100.000
            kWh/a] mit iMS

            Z17 POG bei verbrauchender Marktlokation ]20.000 kWh/a; 50.000
            kWh/a] mit iMS

            Z18 POG bei verbrauchender Marktlokation ]10.000 kWh/a; 20.000
            kWh/a] mit iMS

            Z19 POG bei verbrauchender Marktlokation mit unterbrechbaren
            Verbrauchseinrichtung nach § 14a EnWG mit iMS

            Z20 POG bei verbrauchender Marktlokation ]6.000 kWh/a; 10.000 kWh/a]
            mit iMS

            Z21 POG bei erzeugender Marktlokation ]7 kW; 15kW] mit iMS

            Z22 POG bei erzeugender Marktlokation ]15 kW; 30 kW] mit iMS

            Z23 POG bei erzeugender Marktlokation ]30 kW; 100 kW] mit iMS

            Z24 POG bei erzeugender Marktlokation > 100 kW mit iMS

            Z25 POG bei Marktlokation mit mME

            Z28 POG bei verbrauchender Marktlokation ]4.000 kWh/a; 6.000 kWh/a]
            mit iMS

            Z29 POG bei verbrauchender Marktlokation ]3.000 kWh/a; 4.000 kWh/a]
            mit iMS

            Z30 POG bei verbrauchender Marktlokation ]2.000 kWh/a; 3.000 kWh/a]
            mit iMS

            Z31 POG bei verbrauchender Marktlokation [0 kWh/a; 2.000 kWh/a] mit
            iMS

            Z32 POG bei optionaler Ausstattung mit iMS von Neuanlagen von
            erzeugender Marktlokation

            Z41 Zusatzleistung

            IMD C

            PI 27002
        preiseinheit: &ref_2
          $ref: '#/components/schemas/Waehrungseinheit'
          description: |-
            Währungsangaben für die gesamte Preisliste
            CUX 2 EUR
            PI 27001 27002 27003
        bezugsgroesse:
          $ref: '#/components/schemas/Mengeneinheit'
          description: >-
            Hier wird festgelegt, auf welche Bezugsgröße sich der Preis bezieht,
            z.B. kWh oder Stück. Details

            Mengeneinheit
        zeitbasis: &ref_3
          $ref: '#/components/schemas/Zeiteinheit'
          description: >-
            Die Zeit(dauer) auf die sich der Preis bezieht. Z.B. ein Jahr für
            einen Leistungspreis der in €/kW/Jahr

            ausgegeben wird.
        tarifzeit:
          $ref: '#/components/schemas/Tarifzeit'
          description: Festlegung, für welche Tarifzeit der Preis hier festgelegt ist.
        bdewArtikelnummer:
          $ref: '#/components/schemas/BDEWArtikelnummer'
          description: |-
            Artikelnummer des BDEW  
            Z01 Artikelnummer
            PI 27001 27002 27003
        zonungsgroesse:
          $ref: '#/components/schemas/Bemessungsgroesse'
          description: >-
            Mit der Menge der hier angegebenen Größe wird die Staffelung/Zonung
            durchgeführt. Z.B. Vollbenutzungsstunden.
        preisschluesselstamm:
          type: string
          description: Preisschlüsselstamm
        positionsnummer:
          type: integer
          description: |-
            Fortlaufende Nummer für die Preisposition
            LIN 
            PI 27001 27002 27003
        messebene:
          $ref: '#/components/schemas/Netzebene'
          description: |-
            Spannungsebene der Primärwicklung des Wandlers
            CAV E06
            PI 27002
        beschreibung:
          type: string
          description: Produkt-/Leistungsbeschreibung, wenn IMD+X vorhanden
        verarbeitungszeitraum: *ref_1
        artikelId:
          type: string
          description: |-
            Artikel-ID des BDEW 
            Z09 Artikel-ID
            PI 27001 27002 27003
        zu_abschlaege:
          type: array
          items:
            $ref: '#/components/schemas/PositionsAufAbschlag'
          description: Zuschläge oder Abschläge auf die Position.
        preisstaffeln:
          type: array
          items:
            $ref: '#/components/schemas/Preisstaffel'
          description: |-
            Preisangaben Nettopreis für die aktuelle Position
            PRI CAL
            PI 27001 27002 27003
      x-apidog-orders:
        - berechnungsmethode
        - leistungstyp
        - leistungsbezeichnung
        - preiseinheit
        - bezugsgroesse
        - zeitbasis
        - tarifzeit
        - bdewArtikelnummer
        - zonungsgroesse
        - preisschluesselstamm
        - positionsnummer
        - messebene
        - beschreibung
        - verarbeitungszeitraum
        - artikelId
        - zu_abschlaege
        - preisstaffeln
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Preisstaffel:
      title: Preisstaffel
      type: object
      properties:
        einheitspreis:
          type: number
          format: float
          description: |-
            Berechnungspreis
            PRI CAL
            PI 
        staffelgrenzeVon:
          type: number
          format: float
          description: |-
            Zonengrenzen von
            RGN 10
        staffelgrenzeBis:
          type: number
          format: float
          description: |-
            Zonengrenzen bis
            RGN 10
        sigmoidparameter:
          $ref: '#/components/schemas/Sigmoidparameter'
          description: nicht in Benutzung
      x-apidog-orders:
        - einheitspreis
        - staffelgrenzeVon
        - staffelgrenzeBis
        - sigmoidparameter
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Sigmoidparameter:
      title: Sigmoidparameter
      type: object
      properties:
        A:
          type: number
          format: float
          description: A
        B:
          type: number
          format: float
          description: B
        C:
          type: number
          format: float
          description: C
        D:
          type: number
          format: float
          description: D
      x-apidog-orders:
        - A
        - B
        - C
        - D
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PositionsAufAbschlag:
      title: PositionsAufAbschlag
      type: object
      properties:
        bezeichnung:
          type: string
          description: Bezeichnung
        beschreibung:
          type: string
          description: Beschreibung
        aufAbschlagstyp:
          $ref: '#/components/schemas/AufAbschlagstyp'
          description: nicht in Benutzung
        aufAbschlagswert:
          type: number
          format: float
          description: auf Abschlagswert
        aufAbschlagswaehrung: *ref_2
      x-apidog-orders:
        - bezeichnung
        - beschreibung
        - aufAbschlagstyp
        - aufAbschlagswert
        - aufAbschlagswaehrung
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    AufAbschlagstyp:
      title: AufAbschlagstyp
      type: string
      enum:
        - RELATIV
        - ABSOLUT
      description: >-
        Festlegung, ob der Auf- oder Abschlag mit relativen oder absoluten
        Werten erfolgt
      x-apidog-folder: ''
    Netzebene:
      type: string
      title: Netzebene
      description: Netzebene
      enum:
        - NSP
        - MSP
        - HSP
        - HSS
        - MSP_NSP_UMSP
        - HSP_MSP_UMSP
        - HSS_HSP_UMSP
        - HD
        - MD
        - ND
      x-apidog-enum:
        - value: NSP
          name: Niederspannung
          description: E06
        - value: MSP
          name: Mittelspannung
          description: E05
        - value: HSP
          name: Hochspannung
          description: E04
        - value: HSS
          name: Höchstspannung
          description: E03
        - value: MSP_NSP_UMSP
          name: MS/NS Umspannung
          description: E09
        - value: HSP_MSP_UMSP
          name: HS/MS Umspannung
          description: E08
        - value: HSS_HSP_UMSP
          name: Hös/HS Umspannung
          description: E07
        - value: HD
          name: Hochdruck
          description: Y01
        - value: MD
          name: Mitteldruck
          description: Y02
        - value: ND
          name: Niederdruck
          description: Y03
      x-apidog-folder: ''
    Bemessungsgroesse:
      title: Bemessungsgroesse
      type: string
      enum:
        - WIRKARBEIT_EL
        - LEISTUNG_EL
        - BLINDARBEIT_KAP
        - BLINDARBEIT_IND
        - BLINDLEISTUNG_KAP
        - BLINDLEISTUNG_IND
        - WIRKARBEIT_TH
        - LEISTUNG_TH
        - VOLUMEN
        - VOLUMENSTROM
        - BENUTZUNGSDAUER
        - ANZAHL
      description: >-
        Zur Abbildung von Messgrössen und zur Verwendung in
        energiewirtschaftlichen Berechnungen.
      x-apidog-folder: ''
    BDEWArtikelnummer:
      type: string
      title: BDEWArtikelnummer
      description: BDEW Artikelnummer
      enum:
        - LEISTUNG
        - LEISTUNG_PAUSCHAL
        - GRUNDPREIS
        - REGELENERGIE_ARBEIT
        - REGELENERGIE_LEISTUNG
        - NOTSTROMLIEFERUNG_ARBEIT
        - NOTSTROMLIEFERUNG_LEISTUNG
        - RESERVENETZKAPAZITAET
        - RESERVELEISTUNG
        - ZUSAETZLICHE_ABLESUNG
        - PRUEFGEBUEHREN_AUSSERPLANMAESSIG
        - WIRKARBEIT
        - SINGULAER_GENUTZTE_BETRIEBSMITTEL
        - ABGABE_KWKG
        - ABSCHLAG
        - KONZESSIONSABGABE
        - ENTGELT_FERNAUSLESUNG
        - UNTERMESSUNG
        - BLINDMEHRARBEIT
        - ENTGELT_ABRECHNUNG
        - SPERRKOSTEN
        - ENTSPERRKOSTEN
        - MAHNKOSTEN
        - MEHR_MINDERMENGEN
        - INKASSOKOSTEN
        - BLINDMEHRLEISTUNG
        - ENTGELT_MESSUNG_ABLESUNG
        - ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK
        - AUSGLEICHSENERGIE
        - AUSGLEICHSENERGIE_UNTERDECKUNG
        - ZAEHLEINRICHTUNG
        - WANDLER_MENGENUMWERTER
        - KOMMUNIKATIONSEINRICHTUNG
        - TECHNISCHE_STEUEREINRICHTUNG
        - PARAGRAF_19_STROM_NEV_UMLAGE
        - BEFESTIGUNGSEINRICHTUNG
        - OFFSHORE_HAFTUNGSUMLAGE
        - FIXE_ARBEITSENTGELTKOMPONENTE
        - FIXE_LEISTUNGSENTGELTKOMPONENTE
        - UMLAGE_ABSCHALTBARE_LASTEN
        - MEHRMENGE
        - MINDERMENGE
        - ENERGIESTEUER
        - SMARTMETER_GATEWAY
        - STEUERBOX
        - MSB_INKL_MESSUNG
        - ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_1_MSBG
        - ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_2_MSBG
        - ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_3_MSBG
        - ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_4_MSBG
        - ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_5_MSBG
        - ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_3_MSBG
        - ENTGELT_KAPAZITAETEN
      x-apidog-enum:
        - value: LEISTUNG
          name: Leistung
          description: 9990001 00005 3
        - value: LEISTUNG_PAUSCHAL
          name: Leistung pauschal
          description: 9990001 00007 9
        - value: GRUNDPREIS
          name: Grundpreis
          description: 9990001 00008 7
        - value: REGELENERGIE_ARBEIT
          name: ''
          description: ''
        - value: REGELENERGIE_LEISTUNG
          name: ''
          description: ''
        - value: NOTSTROMLIEFERUNG_ARBEIT
          name: ''
          description: ''
        - value: NOTSTROMLIEFERUNG_LEISTUNG
          name: ''
          description: ''
        - value: RESERVENETZKAPAZITAET
          name: Reservenetzkapazität
          description: 9990001 00016 0
        - value: RESERVELEISTUNG
          name: Reserveleistung
          description: 9990001 00017 8
        - value: ZUSAETZLICHE_ABLESUNG
          name: Zusätzliche Ablesung
          description: '9990001 00018 6 '
        - value: PRUEFGEBUEHREN_AUSSERPLANMAESSIG
          name: ''
          description: ''
        - value: WIRKARBEIT
          name: Wirkarbeit
          description: 9990001 00026 9
        - value: SINGULAER_GENUTZTE_BETRIEBSMITTEL
          name: singulär genutzte Betriebsmittel (z. B. Trafomiete, Leitungen)
          description: 9990001 00028 5
        - value: ABGABE_KWKG
          name: Abgabe KWKG
          description: 9990001 00033 4
        - value: ABSCHLAG
          name: Abschlag
          description: 9990001 00037 6
        - value: KONZESSIONSABGABE
          name: Konzessionsabgabe
          description: 9990001 00041 7
        - value: ENTGELT_FERNAUSLESUNG
          name: Entgelt für Fernauslesung
          description: 9990001 00043 3
        - value: UNTERMESSUNG
          name: Untermessung
          description: '9990001 00047 5 '
        - value: BLINDMEHRARBEIT
          name: Blindmehrarbeit
          description: 9990001 00050 8
        - value: ENTGELT_ABRECHNUNG
          name: Entgelt für Abrechnung
          description: 9990001 00053 2
        - value: SPERRKOSTEN
          name: ''
          description: ''
        - value: ENTSPERRKOSTEN
          name: ''
          description: ''
        - value: MAHNKOSTEN
          name: ''
          description: ''
        - value: MEHR_MINDERMENGEN
          name: ''
          description: ''
        - value: INKASSOKOSTEN
          name: ''
          description: ''
        - value: BLINDMEHRLEISTUNG
          name: ''
          description: ''
        - value: ENTGELT_MESSUNG_ABLESUNG
          name: Entgelt für Messung und Ablesung
          description: 9990001 00061 5
        - value: ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK
          name: Entgelt für Einbau, Betrieb und Wartung der Messtechnik
          description: '9990001 00062 3 '
        - value: AUSGLEICHSENERGIE
          name: Ausgleichsenergie Überdeckung
          description: 9990001 00063 1
        - value: AUSGLEICHSENERGIE_UNTERDECKUNG
          name: Ausgleichsenergie Unterdeckung
          description: 9990001 00080 5
        - value: ZAEHLEINRICHTUNG
          name: Zähleinrichtung
          description: 9990001 00064 9
        - value: WANDLER_MENGENUMWERTER
          name: Wandler/Mengenumwerter
          description: 9990001 00065 7
        - value: KOMMUNIKATIONSEINRICHTUNG
          name: Kommunikationseinrichtung
          description: 9990001 00066 5
        - value: TECHNISCHE_STEUEREINRICHTUNG
          name: 'Technische Steuereinrichtung '
          description: '9990001 00067 3 '
        - value: PARAGRAF_19_STROM_NEV_UMLAGE
          name: § 19 StromNEV Umlage
          description: 9990001 00068 1
        - value: BEFESTIGUNGSEINRICHTUNG
          name: Befestigungseinrichtung (z. B. Zählertafel)
          description: 9990001 00069 9
        - value: OFFSHORE_HAFTUNGSUMLAGE
          name: Offshore-Netzumlage
          description: '9990001 00070 6 '
        - value: FIXE_ARBEITSENTGELTKOMPONENTE
          name: Fixe Arbeitsentgeltkomponente
          description: 9990001 00071 4
        - value: FIXE_LEISTUNGSENTGELTKOMPONENTE
          name: Fixe Leistungsentgeltkomponente
          description: 9990001 00072 2
        - value: UMLAGE_ABSCHALTBARE_LASTEN
          name: 'Umlage abschaltbare Lasten '
          description: 9990001 00073 0
        - value: MEHRMENGE
          name: Mehrmenge
          description: 9990001 00074 8
        - value: MINDERMENGE
          name: Mindermenge
          description: 9990001 00075 6
        - value: ENERGIESTEUER
          name: Energiesteuer
          description: 9990001 00076 4
        - value: SMARTMETER_GATEWAY
          name: Smartmeter-Gateway
          description: 9990001 00077 2
        - value: STEUERBOX
          name: Steuerbox
          description: 9990001 00078 0
        - value: MSB_INKL_MESSUNG
          name: Entgelt für Messstellenbetrieb
          description: 9990001 00079 8
        - value: ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_1_MSBG
          name: Zusatzdienstleistung nach § 35 Abs. 2 Nr. 1 MsbG
          description: 9990001 00081 3
        - value: ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_2_MSBG
          name: Zusatzdienstleistung nach § 35 Abs. 2 Nr. 2 MsbG
          description: 9990001 00082 1
        - value: ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_3_MSBG
          name: Zusatzdienstleistung nach § 35 Abs. 2 Nr. 3 MsbG
          description: 9990001 00083 9
        - value: ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_4_MSBG
          name: Zusatzdienstleistung nach § 35 Abs. 2 Nr. 4 MsbG
          description: 9990001 00084 7
        - value: ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_2_5_MSBG
          name: Zusatzdienstleistung nach § 35 Abs. 2 Nr. 5 MsbG
          description: 9990001 00085 5
        - value: ZUSATZDIENSTLEISTUNG_PARAGRAPH_35_3_MSBG
          name: Zusatzdienstleistung nach § 35 Abs. 3 MsbG
          description: 9990001 00086 3
        - value: ENTGELT_KAPAZITAETEN
          name: 'Entgelt für Kapazitäten '
          description: 9990001 00087 1
      x-apidog-folder: ''
    Tarifzeit:
      title: Tarifzeit
      type: string
      enum:
        - TZ_STANDARD
        - TZ_HT
        - TZ_NT
      description: Tarifzeit
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
    Kalkulationsmethode:
      title: Kalkulationsmethode
      type: string
      enum:
        - KEINE
        - STAFFELN
        - ZONEN
        - VORZONEN_GP
        - SIGMOID
        - BLINDARBEIT_GT_50_PROZENT
        - BLINDARBEIT_GT_40_PROZENT
        - AP_GP_ZONEN
        - LP_INSTALL_LEISTUNG
        - AP_TRANSPORT_ODER_VERTEILNETZ
        - AP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID
        - LP_JAHRESVERBRAUCH
        - LP_TRANSPORT_ODER_VERTEILNETZ
        - LP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID
        - FUNKTIONEN
        - VERBRAUCH_UEBER_SLP_GRENZE_FUNKTIONSBEZOGEN_WEITERE_BERECHNUNG_ALS_LGK
      description: Auflistung der verschiedenen Berechnungsmethoden für ein Preisblatt
      x-apidog-folder: ''
    Leistungstyp:
      title: Leistungstyp
      type: string
      enum:
        - ARBEITSPREIS_WIRKARBEIT
        - LEISTUNGSPREIS_WIRKLEISTUNG
        - ARBEITSPREIS_BLINDARBEIT_IND
        - ARBEITSPREIS_BLINDARBEIT_KAP
        - GRUNDPREIS
        - MEHRMINDERMENGE
        - MESSSTELLENBETRIEB
        - MESSDIENSTLEISTUNG
        - MESSDIENSTLEISTUNG_INKL_MESSUNG
        - ABRECHNUNG
        - KONZESSIONS_ABGABE
        - KWK_UMLAGE
        - OFFSHORE_UMLAGE
        - ABLAV_UMLAGE
        - REGELENERGIE_UMLAGE
        - BILANZIERUNG_UMLAGE
        - AUSLESUNG_ZUSAETZLICH
        - ABLESUNG_ZUSAETZLICH
        - ABRECHNUNG_ZUSAETZLICH
        - SPERRUNG
        - ENTSPERRUNG
        - MAHNKOSTEN
        - INKASSOKOSTEN
      description: Leistungstyp
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
    Preisstatus:
      title: Preisstatus
      type: string
      enum:
        - VORLAEUFIG
        - ENDGUELTIG
      description: Preisstatus
      x-apidog-folder: ''
    Zeitraum:
      title: Zeitraum
      type: object
      properties:
        zeiteinheit: *ref_3
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
        einheit: *ref_3
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
