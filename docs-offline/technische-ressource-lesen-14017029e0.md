# Technische Ressource lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getTechnicalResourceBasic:
    get:
      summary: Technische Ressource lesen
      deprecated: false
      description: >-
        Lesen einer technischen Ressource mittels LokationsId (Parameter1) zum
        Zeitpunkt (Parameter2) | Reading a technical resource using location ID
        (Parameter1) at the time (Parameter2)
      operationId: LESEN_TECHNISCHE_RESSOURCE_BASIS
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: LokationsId | Location ID
          required: true
          schema:
            type: string
            default: '74018657187'
            examples:
              - '74018657187'
        - name: parameter2
          in: query
          description: LokationsTyp | Location type
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
          required: true
          schema:
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            type: string
            examples:
              - '2024-06-28T12:18:00Z'
      responses:
        '200':
          description: >-
            Erfolgreiches Lesen der technischen Ressource | Successful reading
            of the technical resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TechnischeRessource'
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017029-run
components:
  schemas:
    TechnischeRessource:
      title: TechnischeRessource
      type: object
      properties:
        boTyp:
          $ref: '#/components/schemas/BOTyp'
          default: TECHNISCHE_RESSOURCE
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        ressourcenId:
          type: string
          description: >-
            ID der Technischen Ressource, dient der eindeutigen Identifikation
            einer Technischen Ressource

            LOC Z20

            PI 55002 55078 55600 55602 55601 55603 55013 55607 55617 55623 55629
            55635 55175 55180 55173 55177 55690 55035 55095 55060 55043 

            RFF Z37

            PI 55035 55095 55060 55043 55168 55169 

            RFF Z37 

            PI 17003
        sparte:
          $ref: '#/components/schemas/Sparte'
          description: nicht in Benutzung
        lokationszuordnung:
          $ref: '#/components/schemas/Lokationszuordnung'
          description: nicht in Benutzung
        referenzMesslokation:
          type: string
          description: >-
            Referenzierung auf eine ID einer vorgelagerten Messlokation, zur
            Ermittlung von Energiemengen bei mehreren Melos.

            RFF Z34

            PI 55043 55168 55169
        referenzMarktlokation:
          type: string
          description: >-
            Referenzierung auf eine ID der zugeordneten Marktlokationen zu einer
            Technischen Ressource

            RFF Z16

            PI 55175 55180 55173 55177 55690 55035 55095 55060 55043 55168
            55169 
        referenzNetzlokation:
          type: string
          description: |-
            Referenzierung auf eine ID der zugeordneten Netzlokation.
            RFF Z32
            PI 55617 55623 55629 55635 55035 55095 55060 55043 55168 55169
        referenzSteuerbareRessource:
          type: string
          description: >-
            Referenzierung auf eine ID der Steuerbaren Ressource, damit wird
            beschrieben über welche SR die TR gesteuert wird. 

            RFF Z38

            PI 55617 55623 55629 55635 55035 55095 55060 55043 55168 55169
        nennleistung:
          $ref: '#/components/schemas/Nennleistung'
          description: >-
            Nennleistung der Technischen Ressource, bei verbrauchenden Anlagen
            ist es was die TR aufnehmen kann und bei speichernden Anlagen ist es
            was die TR zum Befüllen des Speichers aufnehmen kann. 
        speicherkapazitaet:
          type: number
          format: float
          description: >-
            Speicherkapazität, die von der TR gespeichert werden kann. Angabe in
            kWh. 

            QTY Z42

            PI 55617 55623 55629 55635 55035 55095 55060 55043 55168 55169
        verbrauchsart:
          type: array
          items:
            $ref: '#/components/schemas/Verbrauchsart'
          description: |-
            Verbrauchsart der Technischen Ressource
            CAV Z64
            PI 55617 55623 55629 55635 55035 55060 55043 55168 55169
        waermenutzung:
          $ref: '#/components/schemas/Waermenutzung'
          description: >-
            im Falle der Wärmenutzung wird hier die genauere Angabe über die
            Wärmenutzung definiert. 

            CAV Z56

            PI 55617 55623 55629 55635 55035 55060 55043 55168 55169
        artEMobilitaet:
          $ref: '#/components/schemas/ArtEmobilitaet'
          description: |-
            Definiert die genauere Art der E-Mobilität.
            CAV ZE6
            PI 55617 55623 55629 55635 55035 55060 55043 55168 55169
        erzeugungsart:
          $ref: '#/components/schemas/Erzeugungsart'
          description: |-
            Art der Erzeugung der Energie
            CAV ZF5
            PI 55617 55623 55629 55635 55095 55060 55043 55168 55169
        speicherart:
          $ref: '#/components/schemas/Speicherart'
          description: |-
            Speicherart
            CAV ZF7
            PI 55617 55623 55629 55635 55035 55095 55060 55043 55168 55169
        enwg:
          type: boolean
          description: |-
            Kategorie der verbrauchenden Technischen Ressource
            ZG8 Technischen Ressource fällt unter § 14a EnWG
            ZG9 Technischen Ressource fällt nicht unter § 14a EnWG
            CAV ZG8
            PI 55617 55623 55629 55635 55035 55060 55043 55168 55169
        inbetriebsetzungsdatum:
          $ref: '#/components/schemas/Inbetriebsetzung'
          description: >-
            Inbetriebsetzungsdatum der verbrauchenden Technischen Ressource nach
            § 14a EnWG

            CAV ZH0

            PI 55617 55623 55035
        einordnung:
          $ref: '#/components/schemas/RessourceWechselmoeglichkeit'
          description: >-
            Einordnung der verbrauchenden Technischen Ressource nach § 14a EnWG
            mit Inbetriebsetzung vor 2024

            CAV ZH2

            PI 55617 55623 55035 
        weitereEinrichtung:
          type: boolean
          description: >-
            Information zu weiteren technischen Einrichtungen. Diese Geräte
            wurden nicht in der Marktkommunikation ausgetauscht. 

            ZH7 Weitere technische Einrichtungen vorhanden

            ZH8 Keine weitere technische Einrichtung vorhanden

            CAV ZH7

            PI 55617 55623 55629 55635 55035 55060 55043 55168 55169
        art:
          $ref: '#/components/schemas/TechnischeRessourceArt'
          description: |-
            Art und Nutzung der Technischen Ressource
            CCI Z17
            PI 55617 55623 55629 55635 55035 55095 55060 55043 55168 55169
        datenqualitaet:
          $ref: '#/components/schemas/Datenqualitaet'
          description: |
            Leitet Segmentengruppe ein
            SEQ Z52 Daten der Technischen Ressource
            SEQ ZF0 Informative Daten der Technischen Ressource
            SEQ ZG4 Erwartete Daten der Technischen Ressource
            SEQ ZG5 Im System vorhandene Daten der Technischen Ressource
        gueltigkeitszeitraum:
          $ref: '#/components/schemas/Zeitraum'
          description: Referenz auf Zeitraum-ID
        erforderlicheProdukte:
          type: array
          items:
            $ref: '#/components/schemas/Produkt'
          description: erforderliche Produkte
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - ressourcenId
        - sparte
        - lokationszuordnung
        - referenzMesslokation
        - referenzMarktlokation
        - referenzNetzlokation
        - referenzSteuerbareRessource
        - nennleistung
        - speicherkapazitaet
        - verbrauchsart
        - waermenutzung
        - artEMobilitaet
        - erzeugungsart
        - speicherart
        - enwg
        - inbetriebsetzungsdatum
        - einordnung
        - weitereEinrichtung
        - art
        - datenqualitaet
        - gueltigkeitszeitraum
        - erforderlicheProdukte
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/TechnischeRessource.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Produkt:
      title: Produkt
      type: object
      properties:
        produktCode:
          type: string
          description: |-
            Produkt-Code
            Erforderliches Produkt Abrechnungsdaten ORDERS
            PIA 5
            PI 17133
        codeProdukteigenschaft:
          type: string
          description: |-
            Code der Produkteigenschaft
            CAV ZH9
            PI 55001 55077 55600 55601 55014 55608 
        wertedetails:
          type: string
          description: >-
            Wertedetails zum Produkt, Wertedetails zum Produkt sind in der
            Codeliste der Konfigurationen beschrieben

            CAV ZV4

            PI 55001 55077 55600 55601 55014 55608 
      x-apidog-orders:
        - produktCode
        - codeProdukteigenschaft
        - wertedetails
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zeitraum:
      title: Zeitraum
      type: object
      properties:
        zeiteinheit: &ref_0
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
        einheit: *ref_0
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
    TechnischeRessourceArt:
      type: string
      title: TechnischeRessourceArt
      description: Art und Nutzung der Technischen Ressource
      enum:
        - STROMERZEUGUNG
        - STROMVERBRAUCH
        - SPEICHER
      x-apidog-enum:
        - value: STROMERZEUGUNG
          name: Stromerzeugungsart
          description: Z50
        - value: STROMVERBRAUCH
          name: Stromverbrauchsart
          description: Z17
        - value: SPEICHER
          name: Speicher
          description: Z56
      x-apidog-folder: ''
    RessourceWechselmoeglichkeit:
      type: string
      title: RessourceWechselmoeglichkeit
      description: Einordnung der verbrauchenden Technischen Ressource nach § 14a EnWG
      enum:
        - WECHSELMOEGLICHKEIT_EINMALIG_NOCH_MOEGLICH
        - WECHSELMOEGLICHKEIT_NICHT_MOEGLICH
        - BEFRISTET_OHNE_WECHSELMOEGLICHKEIT
        - WECHSEL_WURDE_DURCHGEFUEHRT
      x-apidog-enum:
        - value: WECHSELMOEGLICHKEIT_EINMALIG_NOCH_MOEGLICH
          name: >-
            Wechselmöglichkeit in das § 14a EnWGModell gem. Festlegung
            BK6-22-300 einmalig noch möglich
          description: ZH2
        - value: WECHSELMOEGLICHKEIT_NICHT_MOEGLICH
          name: >-
            Wechselmöglichkeit in das § 14a EnWGModell gem. Festlegung
            BK6-22-300 nicht möglich
          description: ZH3
        - value: BEFRISTET_OHNE_WECHSELMOEGLICHKEIT
          name: >-
            Befristet im alten § 14a EnWG-Modell bis 2028 ohne
            Wechselmöglichkeit
          description: ZH4
        - value: WECHSEL_WURDE_DURCHGEFUEHRT
          name: >-
            Wechsel in das § 14a EnWG-Modell gem. Festlegung BK6-22-300 wurde
            durchgeführt
          description: ZH5
      x-apidog-folder: ''
    Inbetriebsetzung:
      type: string
      title: Inbetriebsetzung
      description: Inbetriebsetzung
      enum:
        - INBETRIEBSETZUNG_NACH_2023
        - INBETRIEBSETZUN_VOR_2024
      x-apidog-enum:
        - value: INBETRIEBSETZUNG_NACH_2023
          name: Inbetriebsetzung der TR nach 2023
          description: ZH0
        - value: INBETRIEBSETZUN_VOR_2024
          name: Inbetriebsetzung der TR vor 2024
          description: ZH1
      x-apidog-folder: ''
    Speicherart:
      type: string
      title: Speicherart
      description: Speicherart
      enum:
        - WASSERSTOFFSPEICHER
        - PUMPSPEICHER
        - BATTERIESPEICHER
        - SONSTIGE_SPEICHERART
      x-apidog-enum:
        - value: WASSERSTOFFSPEICHER
          name: Wasserstoffspeicher
          description: ZF7
        - value: PUMPSPEICHER
          name: Pumpspeicher
          description: ZF8
        - value: BATTERIESPEICHER
          name: Bateriespeicher
          description: ZF9
        - value: SONSTIGE_SPEICHERART
          name: Sonstige Speicherart
          description: ZG6
      x-apidog-folder: ''
    Erzeugungsart:
      type: string
      title: Erzeugungsart
      description: Auflistung der Erzeugungsarten von Energie.
      enum:
        - EEG
        - KWK
        - EEG_DV
        - KWK_DV
        - WIND
        - SOLAR
        - KERNKRAFT
        - WASSER
        - GEOTHERMIE
        - BIOMASSE
        - KOHLE
        - GAS
        - SONSTIGE
        - SONSTIGE_EEG
        - SONSTIGE_ERZEUGUNGSART
      x-apidog-enum:
        - value: EEG
          name: EEG-Marktlokation ohne DV-Pflicht
          description: Z33
        - value: KWK
          name: KWKG-Marktlokation ohne DV-Pflicht
          description: Z34
        - value: EEG_DV
          name: EEG-Marktlokation mit DV-Pflicht
          description: Z37
        - value: KWK_DV
          name: KWKG-Marktlokation mit DV-Pflicht
          description: Z46
        - value: WIND
          name: Wind
          description: ZF6
        - value: SOLAR
          name: Solar
          description: ZF5
        - value: KERNKRAFT
          name: ''
          description: ''
        - value: WASSER
          name: Wasser
          description: ZG1
        - value: GEOTHERMIE
          name: ''
          description: ''
        - value: BIOMASSE
          name: ''
          description: ''
        - value: KOHLE
          name: ''
          description: ''
        - value: GAS
          name: Gas
          description: ZG0
        - value: SONSTIGE
          name: sonstige Marktlokation
          description: Z35
        - value: SONSTIGE_EEG
          name: ''
          description: ''
        - value: SONSTIGE_ERZEUGUNGSART
          name: Sonstige Erzeugungsart
          description: ZG5
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
    Nennleistung:
      title: Nennleistung
      type: object
      properties:
        aufnahme:
          type: number
          format: float
          description: |-
            Aufnahme der Nennleistung
            QTY Z43 
            PI 55617 55623 55629 55635 55035 55095 55060 55043 55168 55169
        abgabe:
          type: number
          format: float
          description: |-
            Abgabe der Nennleistung
            QTY Z44 
            PI 55617 55623 55629 55635 55035 55095 55060 55043 55168 55169
      x-apidog-orders:
        - aufnahme
        - abgabe
      x-apidog-ignore-properties: []
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
