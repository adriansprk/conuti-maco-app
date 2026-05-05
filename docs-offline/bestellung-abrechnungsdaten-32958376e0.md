# Bestellung Abrechnungsdaten

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /inbound:
    post:
      summary: Bestellung Abrechnungsdaten
      deprecated: false
      description: Prozess zur Bestellung einer Änderung von Abrechnungsdaten
      operationId: START_BESTELLUNG_ABRECHNUNGSDATEN
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht LF
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              x-apidog-refs: {}
              properties:
                Marktlokation:
                  type: object
                  properties:
                    boTyp: &ref_0
                      $ref: '#/components/schemas/BOTyp'
                      default: MARKTLOKATION
                      description: MARKTLOKATION
                    versionStruktur:
                      type: string
                      default: '1'
                      description: versionStruktur
                      x-apidog-mock: '1'
                      title: Structure version
                    marktlokationsId:
                      type: string
                      description: >-
                        Angabe der ID der Marktlokation, für die die Stammdaten
                        gelten.

                        LOC Z16

                        PI 55016 55001 55002 55077 55078 55600 55602 55604 55601
                        55603 55605 55013 55607 55010 55004 55007 55036 55037
                        55038 55611 55218 55220 55613 55614 55126 55156 55674
                        55675 55672 55673 55688 55689 55616 55622 55628 55634
                        55691 55692 55175 55180 55173 55177 55690 55109 55137
                        55110 55136 55684 55685 55640 55645 55650 55655 55660
                        55665 55557 55559 55670 55671 55035 55095 55060 55039
                        55042 55043 55168 55169 55052 55238 55239 55240 55241
                        55242 55243 55074 55075 55076 55065 55066 55195 55196
                        55223 55224 55201 55202

                        Ruhende Malo Zuordnung geringfügiger Verbräuche gem §
                        10c EEG Anwendung findet Anwendung, nimmt nicht selbst
                        an der Bilanzierung teil. 

                        LOC Z22

                        PI 55001 55002 55010 55004 55007 55175 55180 55173 55177
                        55690 55035 55060 55043 55168 

                        RFF Z18

                        PI 55196 55043 55168 55169 

                        ORDERS 

                        RFF Z18 

                        PI 17002 17003 17135

                        RFF Z59 Marktlokation Kundenanlage

                        PI 17134 17135 

                        REQOTE LOC 172

                        PI 35001 35002 35003 35004 

                        IFTSTA LOC 172

                        PI 21032 21033 21039 21040 21045

                        QUOTES LOC 172

                        PI 15002 15003 15004

                        RFF Z18

                        PI 15002

                        INVOIC LOC 172 

                        PI 31001 31002 31009 31004 31005 31006 31011
                      x-apidog-mock: '{{$string.numeric(length=10)}}'
                      title: >-
                        ID of the market location to which the master data
                        applies
                    sparte:
                      description: Strom oder Gas
                      title: Utility division
                      $ref: '#/components/schemas/Sparte'
                    erforderlichesProduktpaket:
                      type: array
                      items:
                        $ref: '#/components/schemas/Produktpaket'
                      description: |-
                        Bestandteil eines Produktpakets,  Produktpaket-ID
                        SEQ Z79
                        PI 55001 55077 55600 55601 55014 55608 
                      title: Component of a product package; product package ID
                  x-apidog-orders:
                    - boTyp
                    - versionStruktur
                    - marktlokationsId
                    - sparte
                    - erforderlichesProduktpaket
                  x-apidog-refs: {}
                  required:
                    - boTyp
                    - versionStruktur
                  x-apidog-ignore-properties: []
                Anfrage:
                  type: object
                  properties:
                    boTyp: *ref_0
                    versionStruktur:
                      type: string
                      x-apidog-mock: '1'
                      description: versionStruktur
                    lokationsTyp:
                      type: string
                      x-apidog-mock: '{{$string.numeric(length=10)}}'
                      description: >
                        Angabe der ID der Marktlokation, für die die Stammdaten
                        gelten.
                    anfragekategorie:
                      type: string
                      description: BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                  x-apidog-orders:
                    - boTyp
                    - versionStruktur
                    - lokationsTyp
                    - anfragekategorie
                  required:
                    - boTyp
                    - versionStruktur
                    - lokationsTyp
                    - anfragekategorie
                  x-apidog-ignore-properties: []
                Auftrag:
                  type: object
                  properties:
                    boTyp: *ref_0
                    versionStruktur:
                      type: string
                      x-apidog-mock: '1'
                      description: versionStruktur
                    ausfuehrungsdatum:
                      type: string
                    positionsdaten:
                      type: array
                      items:
                        type: string
                  x-apidog-orders:
                    - boTyp
                    - versionStruktur
                    - ausfuehrungsdatum
                    - positionsdaten
                  required:
                    - boTyp
                    - versionStruktur
                    - ausfuehrungsdatum
                    - positionsdaten
                  x-apidog-ignore-properties: []
                Transaktionsdaten:
                  type: object
                  properties:
                    absender:
                      type: array
                      items:
                        type: object
                        properties:
                          boTyp: *ref_0
                          versionStruktur:
                            type: string
                            default: '1'
                            description: versionStruktur
                          gewerbekennzeichnung:
                            type: boolean
                            description: >-
                              Kennzeichnung ob es sich um einen
                              Gewerbe/Unternehmen (gewerbeKennzeichnung = true)
                              oder eine Privatperson handelt.
                              (gewerbeKennzeichnung = false)
                          marktrolle:
                            $ref: '#/components/schemas/Marktrolle'
                            description: >-
                              Gibt im Klartext die Bezeichnung der Marktrolle
                              an.

                              CAV Z91 

                              PI 55002 55078 55602 55603 55013 55607 55613 55674
                              55615 55621 55627 55633 55688 55689 55616 55622
                              55628 55634 55618 55624 55630 55636 55620 55626
                              55632 55638 55690 55670 55035 55095 55060 55194
                              55043 55168 55169 55239 

                              CAV Z88 

                              PI 55639 55644 55649 55654 55659 55664 55043 55168
                              55169

                              CAV Z89

                              PI 55613 55614 55674 55675 55690 55670 55671 55060
                              55043 55169 55074 55075 55076 55195 55196

                              CAV Z90

                              PI 55043 55168 55169 55195 55196 

                              CAV ZF0

                              PI 55002 55078 55602 55603 55013 55607 55620 55626
                              55632 55638 55035 55095 55060 55194 55043 55168
                              55169

                              CAV ZB4

                              PI 55043 55168 55169
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
                              Gibt den Typ des Codes an - Verantwortliche Stelle
                              für die Codepflege

                              9 GS1

                              293 DE, BDEW (Bundesverband der Energie- und
                              Wasserwirtschaft e.V.)

                              332 DE, DVGW Service & Consult GmbH 
                          ansprechpartner:
                            $ref: '#/components/schemas/Ansprechpartner'
                            description: >-
                              Ansprechpartner innerhalb des im vorangegangenen
                              NAD-Segment

                              CTA IC 
                        x-apidog-refs: {}
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                          - gewerbekennzeichnung
                          - marktrolle
                          - rollencodenummer
                          - rollencodetyp
                          - ansprechpartner
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                    abtretungserklaerung:
                      type: array
                      items:
                        $ref: '#/components/schemas/Abtretungserklaerung'
                  x-apidog-orders:
                    - absender
                    - abtretungserklaerung
                  required:
                    - absender
                    - abtretungserklaerung
                  x-apidog-ignore-properties: []
                zusatzdaten:
                  type: object
                  properties:
                    prozessId:
                      type: string
                    eventname:
                      type: string
                      description: START_BESTELLUNG_ABRECHNUNGSDATEN
                  x-apidog-orders:
                    - prozessId
                    - eventname
                  required:
                    - prozessId
                    - eventname
                  x-apidog-ignore-properties: []
              required:
                - Marktlokation
                - Anfrage
                - Auftrag
                - Transaktionsdaten
                - zusatzdaten
              x-apidog-orders:
                - Marktlokation
                - Anfrage
                - Auftrag
                - Transaktionsdaten
                - zusatzdaten
              x-apidog-ignore-properties: []
            example: |-
              {
                "stammdaten": {
                  "MARKTLOKATION": [
                    {
                      "boTyp": "MARKTLOKATION",
                      "versionStruktur": "1",
                      "marktlokationsId": "44153874533",
                      "marktlokationsTyp": [
                        {
                          "typ": "STANDARD_MARKTLOKATION"
                        }
                      ],
                      "sparte": "STROM",
                      "erforderlichesProduktpaket": [
                        {
                          "produkt": [
                            {
                              "produktCode": "9991000002545",
                              "codeProdukteigenschaft": "9991000002719"
                            }
                          ]
                        }
                      ]
                    }
                  ],
                  "ANFRAGE": [
                    {
                      "boTyp": "ANFRAGE",
                      "versionStruktur": "1",
                      "lokationsId": "44153874533",
                      "lokationsTyp": "MALO",
                      "anfragekategorie": "BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN"
                    }
                  ],
                  "AUFTRAG": [
                    {
                      "boTyp": "AUFTRAG",
                      "versionStruktur": "1",
                      "startdatum": "2024-09-22T22:00:00Z",
                      "positionsdaten": [
                        {
                          "positionsnummer": 1
                        }
                      ]
                    }
                  ]
                },
                "transaktionsdaten": {
                  "sparte": "STROM",
                  "pruefidentifikator": "17133",
                  "absender": {
                    "boTyp": "MARKTTEILNEHMER",
                    "versionStruktur": "1",
                    "gewerbekennzeichnung": true,
                    "rollencodenummer": "9903111000003",
                    "rollencodetyp": "BDEW",
                    "ansprechpartner": {
                      "boTyp": "ANSPRECHPARTNER",
                      "versionStruktur": "1",
                      "nachname": "Laue",
                      "eMailAdresse": "andre.l@conuti.de"
                    }
                  },
                  "empfaenger": {
                    "boTyp": "MARKTTEILNEHMER",
                    "versionStruktur": "1",
                    "gewerbekennzeichnung": true,
                    "rollencodenummer": "9903111000003",
                    "rollencodetyp": "BDEW"
                  },
                  "kategorie": "Z91",
                  "abtretungserklaerung": {
                    "passwort": "sdfghjkmnbcgfdfgh",
                    "link1": "https://stadt.de"
                  },
                  "zusatzdaten": {
                    "prozessId": "00505688-E4A2-1EDF-A0C2-C81842E2515E",
                    "eventname": "START_BESTELLUNG_ABRECHNUNGSDATEN"
                  }
                }
      responses:
        '201':
          description: Erfolg | Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EVENT_SUCCESS'
          headers: {}
          x-apidog-name: Created
        '400':
          description: Fehler | Fail
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EVENT_FAIL'
          headers: {}
          x-apidog-name: Bad Request
      security:
        - bearer: []
      x-apidog-folder: Schnittstellen/Trigger (MACO APP)/Einzelansicht LF
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-32958376-run
components:
  schemas:
    Abtretungserklaerung:
      title: Abtretungserklaerung
      type: object
      properties:
        passwort:
          type: string
          description: Passwort zum Abruf
        link1:
          type: string
          description: Link Zeile 1
        link2:
          type: string
          description: Link Zeile 2
        link3:
          type: string
          description: Link Zeile 3
        link4:
          type: string
          description: Link Zeile 4
        link5:
          type: string
          description: Link Zeile 5
      x-apidog-orders:
        - passwort
        - link1
        - link2
        - link3
        - link4
        - link5
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Ansprechpartner:
      title: Ansprechpartner
      type: object
      properties:
        boTyp: *ref_0
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
    Produktpaket:
      title: Produktpaket
      type: object
      properties:
        produktpaketId:
          type: integer
          description: >-
            Produkt-Code, Produkt-Codes sind in der Codeliste der
            Konfigurationen beschrieben

            PIA 5

            PI 55001 55077 55600 55601 55014 55608 

            Priorisierung erforderliches Produktpaket

            SEQ ZH0

            PI 55001 55077 55600 55601 55014 55608 
        produkt:
          type: array
          items:
            $ref: '#/components/schemas/Produkt'
          description: |-
            Produkt
            PIA Z11
            PI 55001 55077 55600 55601 55014 55608 
        umsetzungsgradvorgabe:
          $ref: '#/components/schemas/Umsetzungsgradvorgabe'
          description: >-
            Umsetzungsgradvorgabe des Produktpakets wird unterteilt in Z01
            Produktpaket ist vollumfänglich umzusetzen oder Z02 Produktpaket
            kann in Teilen umgesetzt werden zum Zuordnungsbeginn

            CCI Z65

            PI 55001 55077 55600 55601 55014 55608
        priorisierung:
          $ref: '#/components/schemas/Priorisierung'
          description: |-
            Priorisierung erforderliches Produktpaket
            CAV Z75 
      x-apidog-orders:
        - produktpaketId
        - produkt
        - umsetzungsgradvorgabe
        - priorisierung
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Priorisierung:
      type: string
      title: Priorisierung
      description: Priorisierung
      enum:
        - PRIORITAET1
        - PRIORITAET2
        - PRIORITAET3
        - PRIORITAET4
        - PRIORITAET5
      x-apidog-enum:
        - value: PRIORITAET1
          name: 1. Priorität
          description: Z75
        - value: PRIORITAET2
          name: 2. Priorität
          description: Z76
        - value: PRIORITAET3
          name: 3. Priorität
          description: Z77
        - value: PRIORITAET4
          name: 4. Priorität
          description: Z78
        - value: PRIORITAET5
          name: 5. Priorität
          description: Z79
      x-apidog-folder: ''
    Umsetzungsgradvorgabe:
      type: string
      title: Umsetzungsgradvorgabe
      description: Umsetzungsgradvorgabe
      enum:
        - ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
        - ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR
      x-apidog-enum:
        - value: ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
          name: Produktpaket ist vollumfänglich umzusetzen
          description: Z01
        - value: ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR
          name: Produktpaket kann in Teilen umgesetzt werden
          description: Z02
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
    EVENT_SUCCESS:
      type: object
      description: Erfolgsmeldung auf Prozessdaten API Aufruf
      properties:
        businessKey:
          description: Einzigartige Kennung des Geschäftsprozesses
          format: uuid
          type: string
          x-apidog-mock: '{{$string.uuid}}'
        message:
          description: Nachricht mit Details zum ausgelösten Even
          type: string
          examples:
            - >-
              received event XXXXXXXXXXXX with id at 2024-08-08T12:58:22Z and
              started process with businessKey
              4c7170ed-3518-41ee-8582-39ab65b00107
          x-apidog-mock: >-
            received event with id EVENT_NAME at {{$date.isoTimestamp}} and
            started process with businessKey {{$string.uuid}}
      required:
        - businessKey
        - message
      x-apidog-orders:
        - businessKey
        - message
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    EVENT_FAIL:
      type: object
      description: 'Fehlermeldung auf Prozessdaten API Aufruf '
      properties:
        errorCode:
          type: string
          description: Error identifier
          examples:
            - '400'
        message:
          type: string
          description: Technische Meldung
          examples:
            - Validation Failed
      x-apidog-orders:
        - errorCode
        - message
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
