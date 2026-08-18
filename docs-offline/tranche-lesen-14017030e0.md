# Tranche lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getTrancheBasic:
    get:
      summary: Tranche lesen
      deprecated: false
      description: >-
        Lesen einer Tranche mittels LokationsId (Parameter1) zum Zeitpunkt
        (Parameter2) | Reading a tranche using location ID (Parameter1) at the
        time (Parameter2)
      operationId: LESEN_TRANCHE_BASIS
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
          description: Erfolgreiches Lesen der Tranche | Successful reading of the tranche
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Tranche'
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017030-run
components:
  schemas:
    Tranche:
      title: Tranche
      type: object
      properties:
        boTyp: &ref_9
          $ref: '#/components/schemas/BOTyp'
          default: TRANCHE
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        tranchenId:
          type: string
          description: >-
            Angabe der ID der Tranche,  für die die Stammdaten gelten. Die ID
            dient der eindeutigen Identifikation einer Tranche und wird
            spätestens bei der Bestätigung vom NB mitgeliefert - erzeugende
            Anlagen

            LOC Z21

            PI 55016 55077 55078 55607 55010 55004 55007 55036 55037 55038 55674
            55675 55672 55673 55619 55625 55690 55686 55687 55642 55647 55652
            55657 55662 55667 55670 55671 55095 55060 55043 55168 55169 55052
            55074 55075 55076 55065 55066 55195 55196 55223 55224 55201 55202 

            RFF Z20

            PI 55690 55670 55671 55095 55060 55095 55043 55168 55169 55074 55075
            55076 55065 55066 55195 55196 55201 55202 

            ORDERS RFF Z20 

            PI 17121 17134 17135 

            QOUTES LOC 172 

            PI 15003
        sparte:
          $ref: '#/components/schemas/Sparte'
          description: Sparte der Tranche
        energierichtung: &ref_4
          $ref: '#/components/schemas/Energierichtung'
          description: nicht in Benutzung
        bilanzierungsmethode:
          $ref: '#/components/schemas/Bilanzierungsmethode'
          description: nicht in Benutzung
        verbrauchsart:
          type: array
          items: &ref_6
            $ref: '#/components/schemas/Verbrauchsart'
          description: nicht in Benutzung
        unterbrechbar:
          type: boolean
          description: unterbrechbar
        netzebene:
          $ref: '#/components/schemas/Netzebene'
          description: nicht in Benutzung
        netzbetreiberCodeNr:
          type: string
          description: Netzbetreiber CodeNr
        gebietTyp:
          $ref: '#/components/schemas/Gebiettyp'
          description: nicht in Benutzung
        netzgebietNr:
          type: string
          description: Netzgebiet Nummer
        bilanzierungsgebiet:
          type: string
          description: Bilanzierungsgebiet
        grundversorgerCodeNr:
          type: string
          description: Grundversorger CodeNr
        gasqualitaet:
          $ref: '#/components/schemas/Gasqualitaet'
          description: nicht in Benutzung
        endkunde:
          $ref: '#/components/schemas/Geschaeftspartner'
          description: nicht in Benutzung
        lokationsadresse: &ref_10
          $ref: '#/components/schemas/Adresse'
          description: nicht in Benutzung
        katasterinformation:
          $ref: '#/components/schemas/Katasteradresse'
          description: nicht in Benutzung
        regelzone:
          type: string
          description: Regelzone
        marktgebiet:
          type: string
          description: Marktgebiet
        zeitreihentyp:
          $ref: '#/components/schemas/Zeitreihentyp'
          description: nicht in Benutzung
        messtechnischeEinordnung:
          $ref: '#/components/schemas/MesstechnischeEinordnung'
          description: nicht in Benutzung
        sperrstatus:
          $ref: '#/components/schemas/Sperrstatus'
          description: nicht in Benutzung
        referenzMarktlokationsId:
          type: string
          description: |-
            Referenz auf die zugeordnete Marktlokation der Tranche
            RFF Z16
            PI 55690 55060 55168 55169
        versorgungsart:
          $ref: '#/components/schemas/Versorgungsart'
          description: nicht in Benutzung
        fernsteuerbarkeit:
          $ref: '#/components/schemas/Fernsteuerbarkeit'
          description: nicht in Benutzung
        verguetungEmpfaenger:
          $ref: '#/components/schemas/VerguetungEmpfaenger'
          description: |-
            Empfänger der Vergütung
            CAV Z10
            PI 55619 55625  
        foerderungsLand:
          type: string
          description: Förderung Land
        statusErzeugendeMalo:
          $ref: '#/components/schemas/StatusErzeugendeMarktlokation'
          description: nicht in Benutzung
        referenzTranche:
          type: string
          description: Referenz Tranche
        aufteilungsmenge: &ref_2
          $ref: '#/components/schemas/Menge'
          description: >-
            Prozentualer Anteil der Tranche an der erzeugenden Marktlokation.
            Angabe erfolgt in Prozent. 

            QTY 11

            PI 55078 55603 55607 55060 55043 55168 55169 55074 55075 55076

            ORDERS QTY 11

            PI 17134
        bilanzkreis:
          type: string
          description: >-
            Bilanzkreis einer Tranche

            CCI Z19

            PI 55674 55675 55672 55673 55670 55671 55074 55075 55076 55195
            55196  
        bildungTranchengroesse:
          $ref: '#/components/schemas/BildungTranchengroesse'
          description: |-
            Basis zur Bildung der Tranchengröße 
            CCI Z37
            PI 55078 55607 55060 55043 55168 55169 55074 55075 55076 
            ORDERS 
            PI 17134
        zukuenftigerMeldepunkt:
          type: boolean
          description: Zukuenftiger Meldepunkt
        lokationszuordnung:
          $ref: '#/components/schemas/Lokationszuordnung'
          description: nicht in Benutzung
        beteiligterMarktpartner: &ref_0
          $ref: '#/components/schemas/Marktteilnehmer'
          description: >-
            Beteiligter Marktpartner MP-ID 

            NAD VY 

            PI 55003 55080 55604 55605 55010 55036 55691 55692 55075 55076 55067
            55071 55072 
        marktrollen:
          type: array
          items: *ref_0
          description: |-
            Zugeordnete Marktpartner zu einer Tranche
            CCI ZB3
        zaehlwerke:
          type: array
          items:
            $ref: '#/components/schemas/Zaehlwerk'
          description: Zählwerke
        zaehlwerkeBeteiligteMarktrolle:
          type: array
          items: &ref_8
            $ref: '#/components/schemas/Marktrolle'
          description: Zählwerke Beteiligte Marktrolle
        verbrauchsmenge:
          type: array
          items:
            $ref: '#/components/schemas/Verbrauch'
          description: Verbrauchsmenge
        zugehoerigeMesslokationen:
          type: array
          items:
            $ref: '#/components/schemas/Messlokationszuordnung'
          description: Zugehoerige Messlokationen
        netznutzungsabrechnungsdaten:
          type: array
          items:
            $ref: '#/components/schemas/Netznutzungsabrechnungsdaten'
          description: Netznutzungsabrechnungsdaten
        energieherkunft:
          type: array
          items:
            $ref: '#/components/schemas/Energieherkunft'
          description: Energieherkunft
        datenqualitaet:
          $ref: '#/components/schemas/Datenqualitaet'
          description: |-
            Leitet Segmentengruppe ein
            SEQ Z15 Daten der Tranche
            SEQ Z94 Erwartete Daten der Tranche
            SEQ Z95 Im System vorhandene Daten der Tranche
            SEQ ZE7 Informative Daten der Tranche
            SEQ Z16 Erforderliches Produkt der Tranche
            SEQ ZE8 Informative Erforderliches Produkt der Tranche
            SEQ Z17 OBIS-Daten der Tranche
            SEQ Z99 Erwartete OBIS-Daten der Tranche
            SEQ ZA0 Im System vorhandene OBIS-Daten der Tranche
            SEQ ZE9 Informative OBIS-Daten der Tranche
        gueltigkeitszeitraum:
          $ref: '#/components/schemas/Zeitraum'
          description: Referenz auf Zeitraum-ID
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - tranchenId
        - sparte
        - energierichtung
        - bilanzierungsmethode
        - verbrauchsart
        - unterbrechbar
        - netzebene
        - netzbetreiberCodeNr
        - gebietTyp
        - netzgebietNr
        - bilanzierungsgebiet
        - grundversorgerCodeNr
        - gasqualitaet
        - endkunde
        - lokationsadresse
        - katasterinformation
        - regelzone
        - marktgebiet
        - zeitreihentyp
        - messtechnischeEinordnung
        - sperrstatus
        - referenzMarktlokationsId
        - versorgungsart
        - fernsteuerbarkeit
        - verguetungEmpfaenger
        - foerderungsLand
        - statusErzeugendeMalo
        - referenzTranche
        - aufteilungsmenge
        - bilanzkreis
        - bildungTranchengroesse
        - zukuenftigerMeldepunkt
        - lokationszuordnung
        - beteiligterMarktpartner
        - marktrollen
        - zaehlwerke
        - zaehlwerkeBeteiligteMarktrolle
        - verbrauchsmenge
        - zugehoerigeMesslokationen
        - netznutzungsabrechnungsdaten
        - energieherkunft
        - datenqualitaet
        - gueltigkeitszeitraum
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Tranche.json
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
    Energieherkunft:
      title: Energieherkunft
      type: object
      properties:
        erzeugungsart:
          $ref: '#/components/schemas/Erzeugungsart'
          description: >-
            Art der Erzeugung,  dient zur genaueren Wertspezifizierung des
            Merkmals im vorangegangen CCI Segment Z34 Art der erzeugenden
            Marktlokation.

            PI 55607 55616 55622 55628 55634 55095 55060 55043 55168 55169 55074
            55075 55076
        anteilProzent:
          type: number
          format: float
          description: Prozentualer Anteil der Erzeugung
      x-apidog-orders:
        - erzeugungsart
        - anteilProzent
      description: .
      x-apidog-ignore-properties: []
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
        singulaereBetriebsmittel: *ref_2
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
        zaehlzeiten: &ref_7
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
        schwachlastfaehig: &ref_5
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
        bezugswert: &ref_3
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
    Messlokationszuordnung:
      title: Messlokationszuordnung
      type: object
      properties:
        messlokationsId:
          type: string
          description: MesslokationsId
        arithmetik:
          $ref: '#/components/schemas/ArithmetischeOperation'
          description: nicht in Benutzung
        gueltigSeit:
          type: string
          format: date-time
          description: Zuordnung gültig ab
        gueltigBis:
          type: string
          format: date-time
          description: Zuordnung gültig bis
      x-apidog-orders:
        - messlokationsId
        - arithmetik
        - gueltigSeit
        - gueltigBis
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
    Verbrauch:
      title: Verbrauch
      type: object
      properties:
        startdatum:
          type: string
          format: date-time
          description: >-
            Beginn Messperiode

            DTM 163

            PI 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010 13012
            13003 13023 13005 13026 13020 13022 13021 13007 13014 13027 
        enddatum:
          type: string
          format: date-time
          description: >-
            Ende Messperiode

            DTM 164

            PI 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010 13012
            13003 13023 13005 13026 13020 13022 13021 13007 13014 13027 
        wertermittlungsverfahren:
          $ref: '#/components/schemas/Wertermittlungsverfahren'
          description: Messwert oder Prognosewert - bezieht sich auf die Statusangabe
        messwertstatus:
          $ref: '#/components/schemas/Messwertstatus'
          description: >-
            Statusangaben

            PI 13017 13019 13016 13015 13002 13009 13018 13025 13008 13003 13022
            13021 13007 13027 13010 13011 13012 13003 13023 13005 13026 13020
            13013 13014 13028 
        obiskennzahl:
          type: string
          description: >-
            Produktidentifikation unter Verwendung des OBIS-Kennzeichens

            PIA 5

            SRW OBIS-Kennzahl

            PI 13017 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010
            13011 13012 13003 13005 13007 13027

            Z02 BDEW OBIS-ähnliche Kennzahl

            PI 13016 13011 13013 13014

            Z08 Medium

            PI 13023 13026 13020 13022 13021 
        wert:
          type: number
          format: float
          description: |-
            Energiemenge, Mengenangabe MSCONS
            QTY 136 Erreichte Menge in dem Zeitintervall
            PI 21045
        einheit: *ref_3
        type:
          $ref: '#/components/schemas/Verbrauchsmengetyp'
          description: nicht in Benutzung
        tarifstufe:
          $ref: '#/components/schemas/Tarifstufe'
          description: nicht in Benutzung
        nutzungszeitpunkt:
          type: string
          format: date-time
          description: |-
            Nutzungszeitpunkt - eindeutige Zählerstandszuordnung
            DTM 7
            PI 13017 13002 13027 
        ausfuehrungszeitpunkt:
          type: string
          format: date-time
          description: |-
            Ausführungs- / Änderungszeitpunkt - Konstruktionsänderungsdatum
            DTM 60
            PI 13017 13002
        position:
          type: integer
          description: >-
            Positionsdaten -  zeigt den Beginn eines Positionsteils, Hochzählung

            LIN 1

            PI 13017 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010
            13011 13012 13003 13023 13005 13026 13020 13022 13021 13007 13013
            13014 13027
        ablesedatum:
          type: string
          format: date-time
          description: |-
            Ablesedatum
            DTM 9
            PI 13017 13002 
        leistungsperiode:
          type: string
          description: |-
            Leistungsperiode
            DTM 306
            PI 13016 13015 13013
        statuszusatzinformationen:
          type: array
          items:
            $ref: '#/components/schemas/StatusZusatzInformation'
          description: Plausibilisierungshinweis
      x-apidog-orders:
        - startdatum
        - enddatum
        - wertermittlungsverfahren
        - messwertstatus
        - obiskennzahl
        - wert
        - einheit
        - type
        - tarifstufe
        - nutzungszeitpunkt
        - ausfuehrungszeitpunkt
        - position
        - ablesedatum
        - leistungsperiode
        - statuszusatzinformationen
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    StatusZusatzInformation:
      title: StatusZusatzInformation
      type: object
      properties:
        art:
          $ref: '#/components/schemas/StatusArt'
          description: |-
            Z33 Plausibilisierungshinweis
            STS Z33
        status:
          $ref: '#/components/schemas/Status'
          description: |-
            Statusanlaß
            STS Z34
            PI 13017 13019 13016 13002 13009 13018 13025 13008 13002 13007
      x-apidog-orders:
        - art
        - status
      description: .
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Status:
      type: string
      title: Status
      description: Status
      enum:
        - KUNDENSELBSTABLESUNG
        - LEERSTAND
        - REALER_ZAEHLERUEBERLAUF_GEPRUEFT
        - PLAUSIBEL_WG_KONTROLLABLESUNG
        - PLAUSIBEL_WG_KUNDENHINWEIS
        - AUSTAUSCH_DES_ERSATZWERTES
        - RECHENWERT
        - BASIS_MME
        - VERGLEICHSMESSUNG_GEEICHT
        - VERGLEICHSMESSUNG_NICHT_GEEICHT
        - MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN
        - MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN
        - INTERPOLATION
        - HALTEWERT
        - BILANZIERUNG_NETZABSCHNITT
        - HISTORISCHE_MESSWERTE
        - STATISTISCHE_METHODE
        - AUFTEILUNG
        - VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS
        - UMGANGS_UND_KORREKTURMENGEN
        - ANGABEN_MESSLOKATION
        - KEIN_ZUGANG
        - KOMMUNIKATIONSSTOERUNG
        - NETZAUSFALL
        - SPANNUNGSAUSFALL
        - STATUS_GERAETEWECHSEL
        - KALIBRIERUNG
        - GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN
        - MESSEINRICHTUNG_GESTOERT_DEFEKT
        - UNSICHERHEIT_MESSUNG
        - BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK
        - MENGENUMWERTUNG_VOLLSTAENDIG
        - UHRZEIT_GESTELLT_SYNCHRONISATION
        - MESSWERT_UNPLAUSIBEL
        - FALSCHER_WANDLERFAKTOR
        - FEHLERHAFTE_ABLESUNG
        - AENDERUNG_DER_BERECHNUNG
        - UMBAU_DER_MESSLOKATION
        - DATENBEARBEITUNGSFEHLER
        - BRENNWERTKORREKTUR
        - Z_ZAHL_KORREKTUR
        - STOERUNG_DEFEKT_MESSEINRICHTUNG
        - AENDERUNG_TARIFSCHALTZEITEN
        - TARIFSCHALTGERAET_DEFEKT
        - IMPULSWERTIGKEIT_NICHT_AUSREICHEND
        - ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL
        - ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL
        - WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET
        - GESTOERTE_WERTE
        - WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN
        - KONSISTENZ_UND_SYNCHRONPRUEFUNG
        - GRUND_ANGABEN_MESSLOKATION
        - >-
          ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR
        - UMSTELLUNG_GASQUALITAET
        - >-
          ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
        - >-
          ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
        - >-
          ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
        - >-
          ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
        - GESCHEITERT
        - AUSGEBAUT
      x-apidog-enum:
        - value: KUNDENSELBSTABLESUNG
          name: Kundenselbstablesung
          description: Z83
        - value: LEERSTAND
          name: Leerstand
          description: Z84
        - value: REALER_ZAEHLERUEBERLAUF_GEPRUEFT
          name: Realer Zählerüberlauf geprüf
          description: Z85
        - value: PLAUSIBEL_WG_KONTROLLABLESUNG
          name: Plausibel wg. Kontrollablesung
          description: Z86
        - value: PLAUSIBEL_WG_KUNDENHINWEIS
          name: Plausibel wg. Kundenhinweis
          description: Z87
        - value: AUSTAUSCH_DES_ERSATZWERTES
          name: Austausch des Ersatzwertes
          description: ZC3
        - value: RECHENWERT
          name: Rechenwert
          description: ZR5
        - value: BASIS_MME
          name: Wert auf Basis der modernen Messeinrichtung
          description: ZS2
        - value: VERGLEICHSMESSUNG_GEEICHT
          name: Vergleichsmessung (geeicht)
          description: Z88
        - value: VERGLEICHSMESSUNG_NICHT_GEEICHT
          name: Vergleichsmessung (nicht geeicht)
          description: Z89
        - value: MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN
          name: Messwertnachbildung aus geeichten Werten
          description: Z90
        - value: MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN
          name: Messwertnachbildung aus nicht geeichten Werten
          description: Z91
        - value: INTERPOLATION
          name: Interpolation
          description: Z92
        - value: HALTEWERT
          name: Haltewert
          description: Z93
        - value: BILANZIERUNG_NETZABSCHNITT
          name: Bilanzierung Netzabschnit
          description: Z94
        - value: HISTORISCHE_MESSWERTE
          name: Historische Messwerte
          description: Z95
        - value: STATISTISCHE_METHODE
          name: Statistische Methode
          description: ZJ2
        - value: AUFTEILUNG
          name: Aufteilung
          description: ZQ8
        - value: VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS
          name: Verwendung von Werten des Störmengenzählwerks
          description: ZQ9
        - value: UMGANGS_UND_KORREKTURMENGEN
          name: Umgangs- und Korrekturmengen
          description: ZR0
        - value: ANGABEN_MESSLOKATION
          name: Ersatzwertbildungsverfahren gemäß Angaben auf Ebene der Messlokation
          description: ZS0
        - value: KEIN_ZUGANG
          name: kein Zugang
          description: Z74
        - value: KOMMUNIKATIONSSTOERUNG
          name: Kommunikationsstörung
          description: Z75
        - value: NETZAUSFALL
          name: Netzausfall
          description: Z76
        - value: SPANNUNGSAUSFALL
          name: Spannungsausfall
          description: Z77
        - value: STATUS_GERAETEWECHSEL
          name: Gerätewechsel
          description: Z78
        - value: KALIBRIERUNG
          name: Kalibrierung
          description: Z79
        - value: GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN
          name: Gerät arbeitet außerhalb der Betriebsbedingungen
          description: Z80
        - value: MESSEINRICHTUNG_GESTOERT_DEFEKT
          name: Messeinrichtung gestört/defekt
          description: Z81
        - value: UNSICHERHEIT_MESSUNG
          name: Unsicherheit Messung
          description: Z82
        - value: BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK
          name: Berücksichtigung Störmengenzählwerk
          description: Z98
        - value: MENGENUMWERTUNG_VOLLSTAENDIG
          name: Mengenumwertung unvollständig
          description: Z99
        - value: UHRZEIT_GESTELLT_SYNCHRONISATION
          name: Uhrzeit gestellt /Synchronisation
          description: ZA0
        - value: MESSWERT_UNPLAUSIBEL
          name: Messwert unplausibel
          description: ZA1
        - value: FALSCHER_WANDLERFAKTOR
          name: Falscher Wandlerfaktor
          description: ZA3
        - value: FEHLERHAFTE_ABLESUNG
          name: Fehlerhafte Ablesung
          description: ZA4
        - value: AENDERUNG_DER_BERECHNUNG
          name: Änderung der Berechnung
          description: ZA5
        - value: UMBAU_DER_MESSLOKATION
          name: Umbau der Messlokation
          description: ZA6
        - value: DATENBEARBEITUNGSFEHLER
          name: Datenbearbeitungsfehler
          description: ZA7
        - value: BRENNWERTKORREKTUR
          name: Brennwertkorrektur
          description: ZA8
        - value: Z_ZAHL_KORREKTUR
          name: Z-Zahl-Korrektur
          description: ZA9
        - value: STOERUNG_DEFEKT_MESSEINRICHTUNG
          name: Störung / Defekt Messeinrichtung
          description: ZB0
        - value: AENDERUNG_TARIFSCHALTZEITEN
          name: Änderung Tarifschaltzeiten
          description: ZB9
        - value: TARIFSCHALTGERAET_DEFEKT
          name: Tarifschaltgerät defekt
          description: ZC2
        - value: IMPULSWERTIGKEIT_NICHT_AUSREICHEND
          name: Impulswertigkeit nicht ausreichend
          description: ZC4
        - value: ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL
          name: Energiemenge in ungemessenem Zeitintervall
          description: ZJ8
        - value: ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL
          name: Energiemenge aus dem ungepairten Zeitintervall
          description: ZJ9
        - value: WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET
          name: Wartungsarbeiten an geeichtem Messgerät
          description: ZR1
        - value: GESTOERTE_WERTE
          name: gestörte Werte
          description: ZR2
        - value: WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN
          name: Wartungsarbeiten an eichrechtskonformen Messgeräten
          description: ZR3
        - value: KONSISTENZ_UND_SYNCHRONPRUEFUNG
          name: Konsistenz- und Synchronprüfung
          description: ZR4
        - value: GRUND_ANGABEN_MESSLOKATION
          name: Grund der Ersatzwertbildung gemäß Angaben auf Ebene der Messlokation
          description: ZS9
        - value: >-
            ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR
          name: >-
            Anforderung in die Vergangenheit, zum angeforderten Zeitpunkt liegt
            kein Wert vor
          description: ZT8
        - value: UMSTELLUNG_GASQUALITAET
          name: Umstellung Gasqualität
          description: ZG3
        - value: >-
            ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
          name: >-
            Zählerstand zum Beginn der angegebenen Energiemenge vorhanden und
            kommuniziert
          description: Z36
        - value: >-
            ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
          name: >-
            Zählerstand zum Ende der angegebenen Energiemenge vorhanden und
            kommuniziert
          description: Z37
        - value: >-
            ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
          name: >-
            Zählerstand zum Beginn der angegebenen Energiemenge nicht vorhanden
            da Mengenabgrenzung
          description: Z38
        - value: >-
            ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
          name: >-
            Zählerstand zum Ende der angegebenen Energiemenge nicht vorhanden da
            Mengenabgrenzung
          description: Z39
        - value: GESCHEITERT
          name: ''
          description: ''
        - value: AUSGEBAUT
          name: ''
          description: ''
      x-apidog-folder: ''
    StatusArt:
      type: string
      title: StatusArt
      description: StatusArt
      enum:
        - PLAUSIBILISIERUNGSHINWEIS
        - ERSATZWERTBILDUNGSVERFAHREN
        - KORREKTURGRUND
        - GRUND_ERSATZWERTBILDUNGSVERFAHREN
        - GASQUALITAET
        - MESSKLASSIFIZIERUNG
      x-apidog-enum:
        - value: PLAUSIBILISIERUNGSHINWEIS
          name: Plausibilisierungshinweis
          description: Z33
        - value: ERSATZWERTBILDUNGSVERFAHREN
          name: Ersatzwertbildungsverfahren
          description: Z32
        - value: KORREKTURGRUND
          name: Korrekturgrund
          description: Z34
        - value: GRUND_ERSATZWERTBILDUNGSVERFAHREN
          name: Grund der Ersatzwertbildung
          description: Z40
        - value: GASQUALITAET
          name: Gasqualität
          description: Z31
        - value: MESSKLASSIFIZIERUNG
          name: Messklassifizierung
          description: '10'
      x-apidog-folder: ''
    Tarifstufe:
      type: string
      title: Tarifstufe
      description: Tarifstufe
      enum:
        - TARIFSTUFE_0
        - TARIFSTUFE_1
        - TARIFSTUFE_2
        - TARIFSTUFE_3
        - TARIFSTUFE_4
        - TARIFSTUFE_5
        - TARIFSTUFE_6
        - TARIFSTUFE_7
        - TARIFSTUFE_8
        - TARIFSTUFE_9
      x-apidog-enum:
        - value: TARIFSTUFE_0
          name: Tarifstufe 0
          description: Z20
        - value: TARIFSTUFE_1
          name: Tarifstufe 1
          description: Z21
        - value: TARIFSTUFE_2
          name: Tarifstufe 2
          description: Z22
        - value: TARIFSTUFE_3
          name: Tarifstufe 3
          description: Z23
        - value: TARIFSTUFE_4
          name: Tarifstufe 4
          description: Z24
        - value: TARIFSTUFE_5
          name: Tarifstufe 5
          description: Z25
        - value: TARIFSTUFE_6
          name: Tarifstufe 6
          description: Z26
        - value: TARIFSTUFE_7
          name: Tarifstufe 7
          description: Z27
        - value: TARIFSTUFE_8
          name: Tarifstufe 8
          description: Z28
        - value: TARIFSTUFE_9
          name: Tarifstufe 9
          description: Z29
      x-apidog-folder: ''
    Verbrauchsmengetyp:
      title: Verbrauchsmengetyp
      type: string
      enum:
        - ARBEITLEISTUNGTAGESPARAMETERABHMALO
        - VERANSCHLAGTEJAHRESMENGE
        - TUMKUNDENWERT
      description: Verbrauchsmengetyp
      x-apidog-folder: ''
    Messwertstatus:
      type: string
      title: Messwertstatus
      description: Der Status eines Zählerstandes
      enum:
        - ABGELESEN
        - ERSATZWERT
        - VORSCHLAGSWERT
        - NICHT_VERWENDBAR
        - PROGNOSEWERT
        - ENERGIEMENGESUMMIERT
        - VOLAEUFIGERWERT
        - FEHLT
        - ANGABE_FUER_LIEFERSCHEIN
        - GRUNDLAGE_POG_ERMITTLUNG
      x-apidog-enum:
        - value: ABGELESEN
          name: Wahrer Wert
          description: '220'
        - value: ERSATZWERT
          name: Ersatzwert
          description: '67'
        - value: VORSCHLAGSWERT
          name: Vorschlagswert
          description: '201'
        - value: NICHT_VERWENDBAR
          name: Nicht verwendbarer Wert
          description: '20'
        - value: PROGNOSEWERT
          name: Prognosewert
          description: '187'
        - value: ENERGIEMENGESUMMIERT
          name: Energiemenge summiert (Summenwert, Bilanzsumme)
          description: '79'
        - value: VOLAEUFIGERWERT
          name: Vorläufiger Wert
          description: Z18
        - value: FEHLT
          name: Fehlender Wert
          description: Z30
        - value: ANGABE_FUER_LIEFERSCHEIN
          name: Angabe für Lieferschein
          description: Z31
        - value: GRUNDLAGE_POG_ERMITTLUNG
          name: Grundlage POG-Ermittlung
          description: Z47
      x-apidog-folder: ''
    Wertermittlungsverfahren:
      title: Wertermittlungsverfahren
      type: string
      enum:
        - PROGNOSE
        - MESSUNG
      description: Wertermittlungsverfahren
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
        richtung: *ref_4
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
        einheit: *ref_3
        schwachlastfaehig: *ref_5
        verbrauchsart:
          type: array
          items: *ref_6
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
        zaehlzeiten: *ref_7
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
        marktrolle: *ref_8
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
    Marktteilnehmer:
      title: Marktteilnehmer
      type: object
      properties:
        boTyp: *ref_9
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        geschaeftspartnerrolle: &ref_11
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
        partneradresse: *ref_10
        gewerbekennzeichnung:
          type: boolean
          description: >-
            Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
            (gewerbeKennzeichnung = true) oder eine Privatperson handelt.
            (gewerbeKennzeichnung = false)
        externeKundenummerLieferant:
          type: string
          description: externe Kundenummer Lieferant
        marktrolle: *ref_8
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
        boTyp: *ref_9
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
    Lokationszuordnung:
      title: Lokationszuordnung
      type: string
      enum:
        - UNVERAENDERT
        - BEGINNT
        - ENDET
      description: Lokationszuordnung
      x-apidog-folder: ''
    BildungTranchengroesse:
      type: string
      title: BildungTranchengroesse
      description: Basis zur Bildung der Tranchengröße
      enum:
        - PROZENTUAL
        - AUFTEILUNGSFAKTOR
      x-apidog-enum:
        - value: PROZENTUAL
          name: Prozentual
          description: ZD1
        - value: AUFTEILUNGSFAKTOR
          name: >-
            Aufteilungsfaktor auf Basis von Referenzenträger/installierter
            Leistung
          description: ZD2
      x-apidog-folder: ''
    Menge:
      title: Menge
      type: object
      properties:
        wert:
          type: number
          format: float
          description: Wert Mengenangabe
        einheit: *ref_3
      x-apidog-orders:
        - wert
        - einheit
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    StatusErzeugendeMarktlokation:
      type: string
      title: StatusErzeugendeMarktlokation
      description: StatusErzeugendeMarktlokation
      enum:
        - EINSPEISEVERGUETUNG_PARAGRAPH_37
        - GEFOERDERTE_DIREKTVERMARKTUNG
        - SONSTIGE_DIREKTVERMARKTUNG
        - VERMARKTUNG_OHNE_GESETZL_VERGUETUNG
        - KWKG_VERGUETUNG
        - EINSPEISEVERGUETUNG_PARAGRAPH_38_AUSFALLVERGUETUNG
      x-apidog-enum:
        - value: EINSPEISEVERGUETUNG_PARAGRAPH_37
          name: 'EEG-Veräußerungsform: Ausfallvergütung'
          description: Z90
        - value: GEFOERDERTE_DIREKTVERMARKTUNG
          name: 'EEG-Veräußerungsform: Marktprämie'
          description: Z91
        - value: SONSTIGE_DIREKTVERMARKTUNG
          name: ''
          description: ''
        - value: VERMARKTUNG_OHNE_GESETZL_VERGUETUNG
          name: Veräußerungsform ohne gesetzliche Vergütung
          description: Z92
        - value: KWKG_VERGUETUNG
          name: KWKG-Vergütung
          description: Z94
        - value: EINSPEISEVERGUETUNG_PARAGRAPH_38_AUSFALLVERGUETUNG
          name: ''
          description: ''
      x-apidog-folder: ''
    VerguetungEmpfaenger:
      type: string
      title: VerguetungEmpfaenger
      description: Empfänger der Vergütung zur Einspeisung
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
    Fernsteuerbarkeit:
      type: string
      title: Fernsteuerbarkeit
      description: Fernsteuerbarkeit
      enum:
        - TECHNISCH_NICHT_FERNSTEUERBAR
        - TECHNISCH_FERNSTEUERBAR
        - DURCH_LF_FERNSTEUERBAR
      x-apidog-enum:
        - value: TECHNISCH_NICHT_FERNSTEUERBAR
          name: Marktlokation ist technisch nicht fernsteuerbar
          description: Z96
        - value: TECHNISCH_FERNSTEUERBAR
          name: Marktlokation ist technisch fernsteuerbar
          description: Z97
        - value: DURCH_LF_FERNSTEUERBAR
          name: Marktlokation ist durch den Lieferanten fernsteuerbar
          description: Z98
      x-apidog-folder: ''
    Versorgungsart:
      type: string
      title: Versorgungsart
      description: Versorgungsart
      enum:
        - ERSATZVERSORGUNG
        - GRUNDVERSORGUNG
        - ERSATZBELIEFERUNG
      x-apidog-enum:
        - value: ERSATZVERSORGUNG
          name: Ersatzversorgung
          description: ZC9
        - value: GRUNDVERSORGUNG
          name: Grundversorgung
          description: ZD0
        - value: ERSATZBELIEFERUNG
          name: Ersatzbelieferung
          description: ZE3
      x-apidog-folder: ''
    Sperrstatus:
      type: string
      title: Sperrstatus
      description: Sperrstatus
      enum:
        - ENTSPERRT
        - GESPERRT
      x-apidog-enum:
        - value: ENTSPERRT
          name: Marktlokation im Regelbetrieb
          description: ZD3
        - value: GESPERRT
          name: Marktlokation gesperrt
          description: ZB9
      x-apidog-folder: ''
    MesstechnischeEinordnung:
      type: string
      title: MesstechnischeEinordnung
      description: MesstechnischeEinordnung
      enum:
        - IMS
        - KME_MME
        - KEINE_MESSUNG
      x-apidog-enum:
        - value: IMS
          name: iMS
          description: Z52
        - value: KME_MME
          name: kME / mME
          description: Z53
        - value: KEINE_MESSUNG
          name: keine Messung
          description: Z68
      x-apidog-folder: ''
    Zeitreihentyp:
      title: Zeitreihentyp
      type: string
      enum:
        - EGS
        - LGS
        - NZR
        - SES
        - SLS
        - TES
        - TLS
        - SLS_TLS
        - SES_TES
      description: Zeitreihentyp
      x-apidog-folder: ''
    Katasteradresse:
      title: Katasteradresse
      type: object
      properties:
        gemarkung_flur:
          type: string
          description: Gemarkung Flur
        flurstueck:
          type: string
          description: Flurstück Name
        flurstueckNummer:
          type: string
          description: Flurstück Nummer
      x-apidog-orders:
        - gemarkung_flur
        - flurstueck
        - flurstueckNummer
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
    Geschaeftspartner:
      title: Geschaeftspartner
      type: object
      properties:
        boTyp: *ref_9
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
        partneradresse: *ref_10
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
          items: *ref_11
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
    Gasqualitaet:
      type: string
      title: Gasqualitaet
      description: Unterscheidung für hoch- und niedrig-kalorisches Gas.
      enum:
        - H_GAS
        - L_GAS
      x-apidog-enum:
        - value: H_GAS
          name: H-Gas
          description: Y04
        - value: L_GAS
          name: L-Gas
          description: Y05
      x-apidog-folder: ''
    Gebiettyp:
      title: Gebiettyp
      type: string
      enum:
        - REGELZONE
        - MARKTGEBIET
        - BILANZIERUNGSGEBIET
        - VERTEILNETZ
        - TRANSPORTNETZ
        - REGIONALNETZ
        - AREALNETZ
        - GRUNDVERSORGUNGSGEBIET
        - VERSORGUNGSGEBIET
      description: Gebiettyp
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
    Bilanzierungsmethode:
      title: Bilanzierungsmethode
      type: string
      enum:
        - RLM
        - SLP
        - TLP_GEMEINSAM
        - TLP_GETRENNT
        - PAUSCHAL
        - IMS
      description: >-
        Mit dieser Aufzählung kann zwischen den Bilanzierungsmethoden bzw.
        -grundlagen unterschieden werden.
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
