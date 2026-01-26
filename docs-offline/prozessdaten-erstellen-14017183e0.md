# Prozessdaten erstellen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /createProcessData:
    post:
      summary: Prozessdaten erstellen
      deprecated: false
      description: Verbuchung von Daten aus Marktprozesen im Backend
      operationId: ERSTELLEN_PROZESSDATEN
      tags:
        - Schnittstellen/Prozessdaten LF (Backend)
        - PROZESSDATEN
      parameters:
        - name: command
          in: query
          description: >-
            Entspricht der operationId dieser Schnittstelle. Diese Operation Id
            entspricht dem Command im Camunda Konnektor Prozess. Wenn das
            Backend einen generischen Endpunkt bereitstellt, kann dieses Command
            gentutzt werden um zu definieren welche Operation ausgeführt werden
            soll.
          required: false
          schema:
            type: string
            default: ERSTELLEN_PROZESSDATEN
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Prozessdaten%20erstellen%20LF'
            example:
              stammdaten:
                BILANZIERUNG:
                  - bilanzkreis: Test2312312
                    boTyp: BILANZIERUNG
                    jahresverbrauchsprognose:
                      einheit: KWH
                      wert: 2000
                    lastprofile:
                      - bezeichnung: H00
                        einspeisung: false
                        herausgeber: NB
                        profilart: ART_STANDARDLASTPROFIL
                        verfahren: SYNTHETISCH
                    versionStruktur: '1'
                ENERGIELIEFERVERTRAG:
                  - boTyp: VERTRAG
                    enFG:
                      - grundlageVerringerungUmlagen: KEINE_ANGABE
                    korrespondenzpartner:
                      boTyp: GESCHAEFTSPARTNER
                      gewerbekennzeichnung: false
                      name1: Test2312312
                      partneradresse:
                        landescode: DE
                        ort: Dummyort
                        postleitzahl: '00000'
                        strasse: Dummystrasse
                      versionStruktur: '1'
                    sparte: STROM
                    versionStruktur: '1'
                    vertragsart: ENERGIELIEFERVERTRAG
                    vertragspartner2:
                      - anrede: Dr.
                        boTyp: GESCHAEFTSPARTNER
                        geschaeftspartnerrolle:
                          - KUNDE
                        gewerbekennzeichnung: false
                        name1: Mustermann
                        name2: Max
                        versionStruktur: '1'
                MARKTLOKATION:
                  - boTyp: MARKTLOKATION
                    energierichtung: AUSSP
                    marktlokationsId: '50074561192'
                    sparte: STROM
                    versionStruktur: '1'
                MESSLOKATION:
                  - ablesekartenempfaenger:
                      boTyp: GESCHAEFTSPARTNER
                      geschaeftspartnerrolle:
                        - ABLESEKARTENEMPFAENGER
                      gewerbekennzeichnung: true
                      name1: Test2312312
                      partneradresse:
                        landescode: DE
                        ort: Dummyort
                        postleitzahl: '11111'
                        strasse: Dummyweg
                      versionStruktur: '1'
                    boTyp: MESSLOKATION
                    sparte: STROM
                    versionStruktur: '1'
                NETZNUTZUNGSVERTRAG:
                  - boTyp: VERTRAG
                    gemeinderabatt: 0
                    sparte: STROM
                    versionStruktur: '1'
                    vertragsart: NETZNUTZUNGSVERTRAG
                    vertragsbeginn: '2024-12-31T23:00:00Z'
                    vertragskonditionen:
                      haushaltskunde: true
                      netznutzungsvertrag: LIEFERANTEN_NB
                      netznutzungszahler: LIEFERANT
              transaktionsdaten:
                absender:
                  ansprechpartner:
                    boTyp: ANSPRECHPARTNER
                    eMailAdresse: max@mustermann.de
                    nachname: Max Mustermann
                    rufnummern:
                      - nummerntyp: RUF_ZENTRALE
                        rufnummer: '+12345678902'
                      - nummerntyp: FAX_DURCHWAHL
                        rufnummer: '+12345678910'
                      - nummerntyp: RUF_DURCHWAHL
                        rufnummer: '+12345678901'
                      - nummerntyp: MOBIL_NUMMER
                        rufnummer: '+12345678903'
                    versionStruktur: '1'
                  boTyp: MARKTTEILNEHMER
                  rollencodenummer: '9903790000002'
                  rollencodetyp: BDEW
                  versionStruktur: '1'
                bilanzkreis:
                  - bezeichnung: Test2312312
                datenaustauschreferenz: '114622'
                dokumentennummer: 933588BGM
                empfaenger:
                  boTyp: MARKTTEILNEHMER
                  rollencodenummer: '9900321000005'
                  rollencodetyp: BDEW
                  versionStruktur: '1'
                identifikationslogik: Z12
                kategorie: E01
                nachrichtendatum: '2024-04-01T10:57:00Z'
                nachrichtenreferenznummer: S933588
                pruefidentifikator: '55001'
                sparte: STROM
                transaktionsgrund: E03
                vorgangsnummer: ABC488710359
              zusatzdaten: {}
      responses:
        '200':
          description: Erfolgreiche Verbuchung von Daten aus Marktprozesen im Backend
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apidog-orders: []
                x-apidog-ignore-properties: []
          headers: {}
          x-apidog-name: OK
        '422':
          description: Fehlerhafte Anfrage
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apidog-orders: []
                x-apidog-ignore-properties: []
          headers: {}
          x-apidog-name: Parameter Error
      security:
        - bearer: []
      x-apidog-folder: Schnittstellen/Prozessdaten LF (Backend)
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017183-run
components:
  schemas:
    Prozessdaten erstellen LF:
      allOf:
        - anyOf:
            - $ref: '#/components/schemas/PI_55691'
            - $ref: '#/components/schemas/PI_55007'
            - $ref: '#/components/schemas/PI_55010'
            - $ref: '#/components/schemas/PI_55013'
            - $ref: '#/components/schemas/PI_55016'
            - $ref: '#/components/schemas/PI_55037'
            - $ref: '#/components/schemas/PI_55038'
            - $ref: '#/components/schemas/PI_55126'
            - $ref: '#/components/schemas/PI_55175'
            - $ref: '#/components/schemas/PI_55218'
            - $ref: '#/components/schemas/PI_55225'
            - $ref: '#/components/schemas/PI_55553'
            - $ref: '#/components/schemas/PI_55615'
            - $ref: '#/components/schemas/PI_55616'
            - $ref: '#/components/schemas/PI_55617'
            - $ref: '#/components/schemas/PI_55618'
            - $ref: '#/components/schemas/PI_55619'
            - $ref: '#/components/schemas/PI_55620'
            - $ref: '#/components/schemas/PI_55649'
            - $ref: '#/components/schemas/PI_55650'
            - $ref: '#/components/schemas/PI_55651'
            - $ref: '#/components/schemas/PI_55652'
            - $ref: '#/components/schemas/PI_55672'
            - $ref: '#/components/schemas/PI_15004'
            - $ref: '#/components/schemas/PI_19132'
            - $ref: '#/components/schemas/PI_55607'
            - $ref: '#/components/schemas/PI_21033'
            - $ref: '#/components/schemas/PI_19124'
            - $ref: '#/components/schemas/PI_21043'
            - $ref: '#/components/schemas/PI_55022'
            - $ref: '#/components/schemas/44010_Abmeldungsanfrage'
        - $ref: '#/components/schemas/ZUSATZDATEN%20(%20SST%20erstellen)'
      x-apidog-folder: ''
    ZUSATZDATEN ( SST erstellen):
      type: object
      properties:
        zusatzdaten:
          type: object
          properties:
            prozessId:
              type: string
              description: >-
                Id des Dokuments / Beleges im Backend. Wird genutzt um die
                Antwort zuzuordnen.
              x-apidog-mock: '{{$string.uuid}}'
              nullable: true
            businessKey:
              type: string
              description: Id des Prozesses, welcher aktuell den Aufruf durchführt
              x-apidog-mock: '{{$string.uuid}}'
              nullable: true
            targetBusinessKey:
              type: string
              description: Id des initial referenzierenden Prozesses
              x-apidog-mock: '{{$string.uuid}}'
              nullable: true
          x-apidog-orders:
            - prozessId
            - businessKey
            - targetBusinessKey
          required:
            - businessKey
          x-apidog-ignore-properties: []
      x-apidog-orders:
        - zusatzdaten
      required:
        - zusatzdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    44010_Abmeldungsanfrage:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            absender:
              type: object
              properties:
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: |-
                        Nachname (Familienname) des Ansprechpartners | 
                        <TipInfo>SG2.NAD+MS.SG3.CTA</TipInfo>
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | 

                        <TipInfo>SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]</TipInfo>
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: |-
                    Gibt die Codenummer der Marktrolle an - MP ID
                    NAD Z31 Übertragungsnetzbetreiber ORDERS
                    PI 17134
                    NAD DEB Messstellenbetreiber ORDERS
                    PI 17003 17134 17135
                    NAD DEB Messstellenbetreiber IFTSTA 
                    PI 21007 21015 21018 | 
                    <TipInfo>SG2.NAD+MS, SG2.NAD+MR</TipInfo>
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: >-

                          <TipInfo>SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]</TipInfo>
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: >-

                          <TipInfo>SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]</TipInfo>
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
                            name: ''
                            description: ''
                          - value: FAX_DURCHWAHL
                            name: Telefax
                            description: FX
                          - value: MOBIL_NUMMER
                            name: Handy
                            description: AL
                        x-apidog-folder: Bo4e/ENUM
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: |-
                    Rollencodetyp | 
                    <TipInfo>SG2.NAD+MS, SG2.NAD+MR</TipInfo>
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                  x-apidog-enum:
                    - value: BDEW
                      name: >-
                        DE, BDEW (Bundesverband der Energie- und
                        Wasserwirtschaft e.V.)
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
                  x-apidog-folder: Bo4e/ENUM
              x-apidog-orders:
                - ansprechpartner
                - rollencodenummer
                - rufnummern
                - rollencodetyp
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | 

                <TipInfo>SG4.IDE+24.SG6.RFF+Z13</TipInfo>
            vertragsende:
              type: string
              description: >-
                Gibt das Ende der Netznutzung oder einer Zuordnung an. 

                DTM 93

                PI 55016 55017 55001 55002 55600 55602 55013 55014 55607 55608
                55010 55011 55004 55005 55007 55008 55039 55040 55051 55052
                55240 55241 55242 55243 55236 55237 | 

                <TipInfo>SG4.IDE+24.DTM+93</TipInfo>
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: |-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | 
                <TipInfo>UNH</TipInfo>
            dokumentennummer:
              type: string
              description: |-
                EDIFact Referenz aus dem BGM Segment / BGM | 
                <TipInfo>BGM+E02</TipInfo>
            kategorie:
              type: string
              title: Anfragekategorie
              description: |-
                Anfragekategorie | 
                <TipInfo>BGM+E02</TipInfo>
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
              x-apidog-folder: Bo4e/ENUM
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | 

                <TipInfo>SG4.IDE+24.STS+7</TipInfo>
            nachrichtendatum:
              type: string
              description: |-
                Erstellungdatum der EDIFact / DTM+137 | 
                <TipInfo>DTM+137</TipInfo>
              format: date-time
            beteiligterMarktpartner:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: |-
                    Rollencodetyp | 
                    <TipInfo>SG4.IDE+24.SG12.NAD+VY</TipInfo>
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                  x-apidog-enum:
                    - value: BDEW
                      name: >-
                        DE, BDEW (Bundesverband der Energie- und
                        Wasserwirtschaft e.V.)
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
                  x-apidog-folder: Bo4e/ENUM
                rollencodenummer:
                  type: string
                  description: |-
                    Gibt die Codenummer der Marktrolle an - MP ID
                    NAD Z31 Übertragungsnetzbetreiber ORDERS
                    PI 17134
                    NAD DEB Messstellenbetreiber ORDERS
                    PI 17003 17134 17135
                    NAD DEB Messstellenbetreiber IFTSTA 
                    PI 21007 21015 21018 | 
                    <TipInfo>SG4.IDE+24.SG12.NAD+VY</TipInfo>
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC
                | 

                <TipInfo>SG4.IDE+24</TipInfo>
          x-apidog-orders:
            - absender
            - pruefidentifikator
            - vertragsende
            - nachrichtenreferenznummer
            - dokumentennummer
            - kategorie
            - transaktionsgrund
            - nachrichtendatum
            - beteiligterMarktpartner
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            ENERGIELIEFERVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        ortsteil:
                          type: string
                          description: |-
                            Ortsteil | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        strasse:
                          type: string
                          description: |-
                            Strasse | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        hausnummer:
                          type: string
                          description: |-
                            Hausnummer und Ergänzung | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        postfach:
                          type: string
                          description: |-
                            Postfach | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        postleitzahl:
                          type: string
                          description: |-
                            Postleitzahl | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr.

                            Z04 Korrespondenzanschrift des Kunden des
                            Lieferanten

                            PI 55001 55600 55601 55013 55014 55043 55168 55169
                            | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        name4:
                          type: string
                          description: |-
                            Name 4 | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder bei Privatpersonen
                            Zusätze zum  Namen dargestellt werden. Beispiele:
                            und Afrika oder Sängerin | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder bei Privatpersonen
                            beispielsweise der Vorname dargestellt werden.
                            Beispiele: Bereich Süd oder Nina | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        ort:
                          type: object
                          title: Sort
                          description: |-

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                          x-apidog-orders: []
                          properties: {}
                          x-apidog-ignore-properties: []
                        landescode:
                          type: string
                          title: Landescode
                          description: |-
                            Der ISO-Landescode als Enumeration | 
                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
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
                          x-apidog-folder: Bo4e/ENUM
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen beispielsweise der Nachname
                            dargestellt werden. Beispiele: Yellow Strom GmbH
                            oder Hagen | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                        gewerbekennzeichnung:
                          type: boolean
                          description: >-
                            Kennzeichnung ob es sich um einen
                            Gewerbe/Unternehmen (gewerbeKennzeichnung = true)

                            oder eine Privatperson handelt.
                            (gewerbeKennzeichnung = false)

                            Z01 Struktur von Personennamen

                            Z02 Struktur der Firmenbezeichnung | 

                            <TipInfo>SG4.IDE+24.SG12.NAD+Z09</TipInfo>
                      x-apidog-orders:
                        - ortsteil
                        - strasse
                        - hausnummer
                        - postfach
                        - postleitzahl
                        - anrede
                        - name4
                        - name3
                        - name2
                        - ort
                        - landescode
                        - name1
                        - gewerbekennzeichnung
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragspartner2
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | 

                      <TipInfo>SG4.IDE+24.SG5.LOC+172</TipInfo>
                x-apidog-orders:
                  - marktlokationsId
                x-apidog-ignore-properties: []
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsende:
                    type: string
                    description: >-
                      Gibt das Ende der Netznutzung oder einer Zuordnung an. 

                      DTM 93

                      PI 55016 55017 55001 55002 55600 55602 55013 55014 55607
                      55608 55010 55011 55004 55005 55007 55008 55039 55040
                      55051 55052 55240 55241 55242 55243 55236 55237 | 

                      <TipInfo>SG4.IDE+24.DTM+93</TipInfo>
                    format: date-time
                x-apidog-orders:
                  - vertragsende
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - ENERGIELIEFERVERTRAG
            - MARKTLOKATION
            - NETZNUTZUNGSVERTRAG
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 44010 - Abmeldungsanfrage [NB an LF] UTILMD AHB Gas
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55022:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E01|E02|E35]
            freitext:
              type: object
              properties:
                freitext2:
                  type: string
                  description: 'Freitext Zeile 2 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext4:
                  type: string
                  description: 'Freitext Zeile 4 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext1:
                  type: string
                  description: 'Freitext Zeile 1 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext5:
                  type: string
                  description: 'Freitext Zeile 5 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext3:
                  type: string
                  description: 'Freitext Zeile 3 | EDIFACT: SG4.IDE+24.FTX+ACB'
              x-apidog-orders:
                - freitext2
                - freitext4
                - freitext1
                - freitext5
                - freitext3
              x-apidog-ignore-properties: []
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E01|E02|E35]'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            vorgangsreferenznummer:
              type: string
              description: >-
                Referenznummer des Vorgangs der Anmeldung nach WiM / ORDERS
                RFF+Z41 / IFTSTA RFF+ACW | EDIFACT: SG4.IDE+24.SG6.RFF+ACW
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - freitext
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - vorgangsreferenznummer
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
      description: >-
        55022 - Beteiligte wie bei Ursprungsnachricht an Beteiligte wie bei
        Ursprungsnachricht - Anfrage nach Stornierung
      x-apidog-orders:
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_21043:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            kategorie:
              type: string
              description: Bestellkategorie - EDIFACT BGM+Z73
            dokumentennummer:
              type: string
              description: 'Dokumentennummer - EDIFACT BGM '
            nachrichtendatum:
              type: string
              description: Nachrichtendatum - EDIFACT DTM+137
              format: date-time
            empfaenger:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: 'MP-ID - EDIFACT SG1. NAD+MR+MP-ID '
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: >-
                    Rollencodetyp Sparte Strom- EDIFACT SG1. NAD+MR+MP-ID: 9 /
                    293
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                  x-apidog-enum:
                    - value: BDEW
                      name: >-
                        DE, BDEW (Bundesverband der Energie- und
                        Wasserwirtschaft e.V.)
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
                  x-apidog-folder: Bo4e/ENUM
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
              description: MP-ID - EDIFACT SG1. NAD+MR+MP-ID
              x-apidog-ignore-properties: []
            absender:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: MP-ID  - EDIFACT SG1. NAD+MS+MP-ID
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: >-
                    Rollencodetyp Sparte Strom- EDIFACT SG1. NAD+MS+MP-ID: 9 /
                    293
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                  x-apidog-enum:
                    - value: BDEW
                      name: >-
                        DE, BDEW (Bundesverband der Energie- und
                        Wasserwirtschaft e.V.)
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
                  x-apidog-folder: Bo4e/ENUM
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: Kontakt - EDIFACT SG2. CTA+IC+Kontaktname
                    eMailAdresse:
                      type: string
                      description: Elektronische Post - EDIFACT SG2. COM+Adresse:EM
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  description: Ansprechpartner - EDIFACT SG2. CTA+IC
                  required:
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rufnummern:
                  type: object
                  properties:
                    rufnummer:
                      type: string
                      description: Rufnummer
                    nummerntyp:
                      type: string
                      description: 'Rufnummerntyp - EDIFACT SG2. COM+Rufnummer: FX TE AJ AL'
                  x-apidog-orders:
                    - rufnummer
                    - nummerntyp
                  required:
                    - rufnummer
                    - nummerntyp
                  description: Rufnummern - EDIFACT SG2. COM+Rufnummer
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
                - ansprechpartner
                - rufnummern
              description: Absender - EDIFACT SG1. NAD+MS
              required:
                - rufnummern
              x-apidog-ignore-properties: []
            antwortstatus:
              type: string
              description: Code des Prüfschritts - EDIFACT SG15. STS+Z21+Z13+CODE
            antwortstatusCodeliste:
              type: string
              description: EBD - EDIFACT SG15. STS+Z21+Z13+CODE:EBD
            pruefidentifikator:
              type: string
              description: Prüfidentifikator - EDIFACT SG15. RFF+Z13
            anfrageReferenz:
              type: string
              description: >-
                Referenz auf die Bestellung aus ORDERS BGM - EDIFACT SG15.
                RFF+AGI 
            sendungsposition:
              type: integer
              description: Sendungsposition - EDIFACT SG15. GID+1
          x-apidog-orders:
            - kategorie
            - dokumentennummer
            - nachrichtendatum
            - empfaenger
            - absender
            - antwortstatus
            - antwortstatusCodeliste
            - pruefidentifikator
            - anfrageReferenz
            - sendungsposition
          description: Transaktionsdaten
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            STATUSMITTEILUNG:
              type: array
              items:
                type: object
                properties:
                  positionsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        positionsnummer:
                          type: integer
                          description: Vorgangsnummer - EDIFACT CNI+1 bis n
                        statusVeraenderungsZeitpunkt:
                          type: string
                          description: Statusveränderungszeitpunkt - EDIFACT SG15. DTM+334
                          format: date-time
                        allgemeineInformationen:
                          type: object
                          properties:
                            info1:
                              type: string
                              description: Freier Text - EDIFACT SG25 FTX+ACB+++Info1
                            info2:
                              type: string
                              description: Freier Text - EDIFACT SG25 FTX+ACB+++Info1:info2
                            info3:
                              type: string
                              description: >-
                                Freier Text - EDIFACT SG25
                                FTX+ACB+++Info1:info2:info3
                            info4:
                              type: string
                              description: >-
                                Freier Text - EDIFACT SG25
                                FTX+ACB+++Info1:info2:info3:info4
                            info5:
                              type: string
                              description: >-
                                Freier Text - EDIFACT SG25
                                FTX+ACB+++Info1:info2:info3:info4:info5
                          x-apidog-orders:
                            - info1
                            - info2
                            - info3
                            - info4
                            - info5
                          description: Zusätzliche Informationen - EDIFACT SG25 FTX+ACB
                          x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - positionsnummer
                        - statusVeraenderungsZeitpunkt
                        - allgemeineInformationen
                      required:
                        - positionsnummer
                      x-apidog-ignore-properties: []
                    description: Positionsdaten
                x-apidog-orders:
                  - positionsdaten
                x-apidog-ignore-properties: []
              description: BO Statusmitteilung
            statusObjekt:
              type: string
              description: Status STATUSBESTELLUNG - EDIFACT SG15. STS+Z21
            auftragsstatus:
              type: string
              description: Status Bestellung - EDIFACT SG15. STS+Z21+Z13,Z14,Z32,Z43,Z44
          x-apidog-orders:
            - STATUSMITTEILUNG
            - statusObjekt
            - auftragsstatus
          description: 'Stammdaten '
          required:
            - statusObjekt
            - auftragsstatus
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 21043 - Bestellungsantwort/ - mitteilung MSB an LF, MSB, NB | NB an LF
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_19124:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'Dokumentennummer - EDIFACT BGM '
            kategorie:
              type: string
              description: Änderungskategorie - EDIFACT BGM Z56
            nachrichtendatum:
              type: string
              description: Nachrichtendatum - EDIFACT DTM+137
              format: date-time
            auftragsReferenz:
              type: string
              description: Referenz Nachrichtennummer Einkauf - EDIFACT SG1.RFF+ON
            pruefidentifikator:
              type: string
              description: Prüfidentifikator - EDIFACT SG1. RFF+Z13
            antwortstatus:
              type: string
              description: Code des Prüfschritts - EDIFACT SG2. ATJ+CODE
            antwortstatusCodeliste:
              type: string
              description: Codeliste - EDIFACT SG2. ATJ+CODE+EBD
            freitext:
              type: string
              title: Freitext
              description: Allgemeine Information - EDIFACT SG2. FTX+AAP
            absender:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: MP-ID  - EDIFACT SG3. NAD+MS+MP-ID
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: >-
                    Rollencodetyp Sparte Strom- EDIFACT SG3. NAD+MS+MP-ID: 9 /
                    293
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                  x-apidog-enum:
                    - value: BDEW
                      name: >-
                        DE, BDEW (Bundesverband der Energie- und
                        Wasserwirtschaft e.V.)
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
                  x-apidog-folder: Bo4e/ENUM
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: Kontakt - EDIFACT SG6. CTA+IC+Kontaktname
                    eMailAdresse:
                      type: string
                      description: Elektronische Post - EDIFACT SG6. COM+Adresse:EM
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  description: Ansprechpartner - EDIFACT SG6. CTA+IC
                  x-apidog-ignore-properties: []
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: Rufnummer
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: >-
                          Rufnummerntyp - EDIFACT SG6. COM+Rufnummer: FX TE AJ
                          AL
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
                            name: ''
                            description: ''
                          - value: FAX_DURCHWAHL
                            name: Telefax
                            description: FX
                          - value: MOBIL_NUMMER
                            name: Handy
                            description: AL
                        x-apidog-folder: Bo4e/ENUM
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                  description: Rufnummern - EDIFACT SG6. COM+Rufnummer
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
                - ansprechpartner
                - rufnummern
              description: Absender - EDIFACT SG3. NAD+MS
              required:
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: MP-ID - EDIFACT SG3. NAD+MR+MP-ID
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: >-
                    Rollencodetyp Sparte Strom- EDIFACT SG3. NAD+MR+MP-ID: 9 /
                    293
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                  x-apidog-enum:
                    - value: BDEW
                      name: >-
                        DE, BDEW (Bundesverband der Energie- und
                        Wasserwirtschaft e.V.)
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
                  x-apidog-folder: Bo4e/ENUM
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
              description: MP-ID - EDIFACT SG3. NAD+MR+MP-ID
              required:
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - nachrichtendatum
            - auftragsReferenz
            - pruefidentifikator
            - antwortstatus
            - antwortstatusCodeliste
            - freitext
            - absender
            - empfaenger
          description: Transaktionsdaten
          required:
            - dokumentennummer
            - kategorie
            - nachrichtendatum
            - auftragsReferenz
            - pruefidentifikator
            - antwortstatus
            - antwortstatusCodeliste
            - absender
            - empfaenger
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            ANFRAGE:
              type: object
              properties:
                anfragekategorie:
                  type: string
                  description: Änderungskategorie - EDIFACT BGM Z56
              x-apidog-orders:
                - anfragekategorie
              required:
                - anfragekategorie
              description: BO Anfrage
              x-apidog-ignore-properties: []
          x-apidog-orders:
            - ANFRAGE
          description: Stammdaten
          required:
            - ANFRAGE
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 19124 - Mitteilung zur Änderung einer Zählzeitdefinition NB, MSB an LF
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_21033:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            kategorie:
              type: string
              description: Anfragekategorie - EDIFACT BGM+Z09
            dokumentennummer:
              type: string
              description: 'Dokumentennummer - EDIFACT BGM '
            nachrichtendatum:
              type: string
              description: Nachrichtendatum - EDIFACT DTM+137
              format: date-time
            empfaenger:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: 'MP-ID - EDIFACT SG1. NAD+MR+MP-ID '
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: >-
                    Rollencodetyp Sparte Strom- EDIFACT SG1. NAD+MR+MP-ID: 9 /
                    293
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                  x-apidog-enum:
                    - value: BDEW
                      name: >-
                        DE, BDEW (Bundesverband der Energie- und
                        Wasserwirtschaft e.V.)
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
                  x-apidog-folder: Bo4e/ENUM
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
              description: MP-ID - EDIFACT SG1. NAD+MR+MP-ID
              x-apidog-ignore-properties: []
            absender:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: MP-ID  - EDIFACT SG1. NAD+MS+MP-ID
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: >-
                    Rollencodetyp Sparte Strom- EDIFACT SG1. NAD+MS+MP-ID: 9 /
                    293
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                  x-apidog-enum:
                    - value: BDEW
                      name: >-
                        DE, BDEW (Bundesverband der Energie- und
                        Wasserwirtschaft e.V.)
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
                  x-apidog-folder: Bo4e/ENUM
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: Kontakt - EDIFACT SG2. CTA+IC+Kontaktname
                    eMailAdresse:
                      type: string
                      description: Elektronische Post - EDIFACT SG2. COM+Adresse:EM
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  required:
                    - eMailAdresse
                  description: Kontakt - EDIFACT SG2. CTA+IC+Kontaktname
                  x-apidog-ignore-properties: []
                rufnummern:
                  type: object
                  properties:
                    rufnummer:
                      type: string
                      description: Rufnummer
                    nummerntyp:
                      type: string
                      description: 'Rufnummerntyp - EDIFACT SG2. COM+Rufnummer: FX TE AJ AL'
                  x-apidog-orders:
                    - rufnummer
                    - nummerntyp
                  required:
                    - rufnummer
                    - nummerntyp
                  description: Rufnummern - EDIFACT SG2. COM+Rufnummer
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
                - ansprechpartner
                - rufnummern
              description: Absender - EDIFACT SG1. NAD+MS
              required:
                - rufnummern
              x-apidog-ignore-properties: []
            antwortstatus:
              type: string
              description: Code des Prüfschritts - EDIFACT SG15. STS+Z20+Z32+CODE
            antwortstatusCodeliste:
              type: string
              description: EBD - EDIFACT SG15. STS+Z20+Z32+CODE:EBD
            pruefidentifikator:
              type: string
              description: Prüfidentifikator - EDIFACT SG15. RFF+Z13
            anfragereferenznummer:
              type: string
              description: 'Nummer der Anfrage- EDIFACT RFF+AAV '
            startdatum:
              type: string
              description: Frühester Zeitpunkt - EDIFACT DTM+469
              format: date-time
            sendungsposition:
              type: integer
              description: Sendungsposition - EDIFACT GID+1
          x-apidog-orders:
            - kategorie
            - dokumentennummer
            - nachrichtendatum
            - empfaenger
            - absender
            - antwortstatus
            - antwortstatusCodeliste
            - pruefidentifikator
            - anfragereferenznummer
            - startdatum
            - sendungsposition
          description: Transaktionsdaten
          required:
            - kategorie
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            STATUSMITTEILUNG:
              type: array
              items:
                type: object
                properties:
                  positionsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        positionsnummer:
                          type: integer
                          description: Vorgangsnummer - EDIFACT CNI+1 bis n
                        allgemeineInformationen:
                          type: object
                          properties:
                            info1:
                              type: string
                              description: Freier Text - EDIFACT SG25 FTX+ACB+++Info1
                            info3:
                              type: string
                              description: Freier Text - EDIFACT SG25 FTX+ACB+++Info1:info2
                            info4:
                              type: string
                              description: >-
                                Freier Text - EDIFACT SG25
                                FTX+ACB+++Info1:info2:info3
                            info2:
                              type: string
                              description: >-
                                Freier Text - EDIFACT SG25
                                FTX+ACB+++Info1:info2:info3:info4
                            info5:
                              type: string
                              description: >-
                                Freier Text - EDIFACT SG25
                                FTX+ACB+++Info1:info2:info3:info4:info5
                          x-apidog-orders:
                            - info1
                            - info3
                            - info4
                            - info2
                            - info5
                          description: Zusätzliche Informationen - EDIFACT SG25 FTX+ACB
                          x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - positionsnummer
                        - allgemeineInformationen
                      required:
                        - positionsnummer
                      x-apidog-ignore-properties: []
                    description: Positionsdaten
                  statusObjekt:
                    type: string
                    description: Status ANGEBOTANFRAGE - EDIFACT SG15. STS+Z20
                  auftragsstatus:
                    type: string
                    title: Auftragsstatus
                    description: Auftragsstatus ABGELEHNT - EDIFACT SG15. STS+Z20+Z32
                    enum:
                      - GESCHEITERT
                      - ERFOLGREICH
                      - LIEFERUNG_GEPLANT
                      - GEPLANT
                      - ZUGESTIMMT
                      - WIDERSPROCHEN
                      - STOERUNGSFREI
                      - GESTOERT
                      - FESTGESTELLTE_STOERUNG
                      - VERMUTETE_STOERUNG
                      - ABGELEHNT
                      - BEENDET
                      - ANTWORT_DRITTER
                      - BESTAETIGT
                      - UMGESETZT
                      - ENFG_STROMSPEICHER_UND_VERLUSTENERGIE
                      - ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
                      - >-
                        ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN
                      - ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF
                      - ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN
                      - >-
                        ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN
                      - ENFG_SCHIENENBAHNEN
                      - ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR
                      - ENFG_LANDSTROMANLAGEN
                      - AENDERUNG_DER_DATEN
                      - KEINE_AENDERUNG_DER_DATEN
                    x-apidog-enum:
                      - value: GESCHEITERT
                        name: ''
                        description: ''
                      - value: ERFOLGREICH
                        name: ''
                        description: ''
                      - value: LIEFERUNG_GEPLANT
                        name: ''
                        description: ''
                      - value: GEPLANT
                        name: ''
                        description: ''
                      - value: ZUGESTIMMT
                        name: ''
                        description: ''
                      - value: WIDERSPROCHEN
                        name: ''
                        description: ''
                      - value: STOERUNGSFREI
                        name: störungsfrei
                        description: Z09
                      - value: GESTOERT
                        name: gestört
                        description: Z10
                      - value: FESTGESTELLTE_STOERUNG
                        name: festgestellte Störung
                        description: Z11
                      - value: VERMUTETE_STOERUNG
                        name: vermutete Störung
                        description: Z12
                      - value: ABGELEHNT
                        name: ''
                        description: ''
                      - value: BEENDET
                        name: ''
                        description: ''
                      - value: ANTWORT_DRITTER
                        name: ''
                        description: ''
                      - value: BESTAETIGT
                        name: ''
                        description: ''
                      - value: UMGESETZT
                        name: ''
                        description: ''
                      - value: ENFG_STROMSPEICHER_UND_VERLUSTENERGIE
                        name: ''
                        description: ''
                      - value: ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
                        name: ''
                        description: ''
                      - value: >-
                          ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN
                        name: ''
                        description: ''
                      - value: ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF
                        name: ''
                        description: ''
                      - value: ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN
                        name: ''
                        description: ''
                      - value: >-
                          ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN
                        name: ''
                        description: ''
                      - value: ENFG_SCHIENENBAHNEN
                        name: ''
                        description: ''
                      - value: ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR
                        name: ''
                        description: ''
                      - value: ENFG_LANDSTROMANLAGEN
                        name: ''
                        description: ''
                      - value: AENDERUNG_DER_DATEN
                        name: ''
                        description: ''
                      - value: KEINE_AENDERUNG_DER_DATEN
                        name: ''
                        description: ''
                    x-apidog-folder: Bo4e/ENUM
                x-apidog-orders:
                  - positionsdaten
                  - statusObjekt
                  - auftragsstatus
                required:
                  - statusObjekt
                x-apidog-ignore-properties: []
              description: BO Statusmitteilung
            MESSLOKATION:
              type: array
              items:
                type: object
                properties:
                  messlokationsId:
                    type: string
                    description: ID der Messlokation - EDIFACT SG14. LOC+172
                x-apidog-orders:
                  - messlokationsId
                x-apidog-ignore-properties: []
              description: BO Messlokation
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: ID der Marktlokation - EDIFACT SG14. LOC+172
                x-apidog-orders:
                  - marktlokationsId
                x-apidog-ignore-properties: []
              description: BO Marktlokation
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  netzlokationsId:
                    type: string
                    description: ID der Netzlokation - EDIFACT SG14. LOC+172
                x-apidog-orders:
                  - netzlokationsId
                x-apidog-ignore-properties: []
              description: BO Netzlokation
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: ID der Steuerbaren Ressource - EDIFACT SG14. LOC+172
                x-apidog-orders:
                  - ressourcenId
                x-apidog-ignore-properties: []
              description: BO Steuerbare Ressource
          x-apidog-orders:
            - STATUSMITTEILUNG
            - MESSLOKATION
            - MARKTLOKATION
            - NETZLOKATION
            - STEUERBARE_RESSOURCE
          description: 'Stammdaten '
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 21033 - Ablehnung der Anfrage MSB an ESA, LF, NB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55607:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            MESSLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+ZF0
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+ZF0
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
                      x-apidog-orders:
                        - rollencodenummer
                        - weiterverpflichtet
                        - messstellenbetreiberEigenschaft
                        - marktrolle
                      x-apidog-ignore-properties: []
                  messlokationsId:
                    type: string
                    description: >-
                      Die Messlokations-Identifikation. Das ist die frühere
                      Zählpunktbezeichnung,

                      z.B. DE 47108151234567 | EDIFACT: SG4.IDE+24.SG5.LOC+Z17,
                      SG4.IDE+24.SG8.SEQ+ZF3.RFF+Z19
                x-apidog-orders:
                  - marktrollen
                  - messlokationsId
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
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
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
                      x-apidog-orders:
                        - rollencodenummer
                        - marktrolle
                        - messstellenbetreiberEigenschaft
                        - weiterverpflichtet
                      x-apidog-ignore-properties: []
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  energieherkunft:
                    type: array
                    items:
                      type: object
                      properties:
                        erzeugungsart:
                          type: string
                          title: Erzeugungsart
                          description: >-
                            Auflistung der Erzeugungsarten von Energie. |
                            EDIFACT: SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++Z34.CAV
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
                      x-apidog-orders:
                        - erzeugungsart
                      x-apidog-ignore-properties: []
                  statusErzeugendeMalo:
                    type: string
                    title: StatusErzeugendeMarktlokation
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+Z22'
                    enum:
                      - EINSPEISEVERGUETUNG_PARAGRAPH_37
                      - GEFOERDERTE_DIREKTVERMARKTUNG
                      - SONSTIGE_DIREKTVERMARKTUNG
                      - VERMARKTUNG_OHNE_GESETZL_VERGUETUNG
                      - KWKG_VERGUETUNG
                      - EINSPEISEVERGUETUNG_PARAGRAPH_38_AUSFALLVERGUETUNG
                x-apidog-orders:
                  - marktrollen
                  - marktlokationsId
                  - energieherkunft
                  - statusErzeugendeMalo
                x-apidog-ignore-properties: []
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsende:
                    type: string
                    description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
                    format: date-time
                  vertragsbeginn:
                    type: string
                    description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
                    format: date-time
                x-apidog-orders:
                  - vertragsende
                  - vertragsbeginn
                x-apidog-ignore-properties: []
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZD7.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZD7.SG10.CCI+++ZB3.CAV+Z91
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
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZD7.SG10.CCI+++ZB3.CAV+Z91
                      x-apidog-orders:
                        - messstellenbetreiberEigenschaft
                        - marktrolle
                        - rollencodenummer
                      x-apidog-ignore-properties: []
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18,
                      SG4.IDE+24.SG8.SEQ+ZD7.RFF+Z32
                x-apidog-orders:
                  - marktrollen
                  - netzlokationsId
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  bildungTranchengroesse:
                    type: string
                    title: BildungTranchengroesse
                    description: >-
                      BildungTranchengroesse | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z15.SG10.CCI+Z37
                    enum:
                      - PROZENTUAL
                      - AUFTEILUNGSFAKTOR
                  aufteilungsmenge:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z15.SG9.QTY+11'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z15.SG9.QTY+11
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
                    x-apidog-orders:
                      - wert
                      - einheit
                    x-apidog-ignore-properties: []
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                x-apidog-orders:
                  - bildungTranchengroesse
                  - aufteilungsmenge
                  - tranchenId
                x-apidog-ignore-properties: []
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF1.SG10.CCI+++ZB3.CAV+Z91
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
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF1.SG10.CCI+++ZB3.CAV+Z91
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF1.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                      x-apidog-orders:
                        - marktrolle
                        - rollencodenummer
                        - messstellenbetreiberEigenschaft
                      x-apidog-ignore-properties: []
                  ressourcenId:
                    type: string
                    description: >-
                      ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19,
                      SG4.IDE+24.SG8.SEQ+ZF1.RFF+Z38
                x-apidog-orders:
                  - marktrollen
                  - ressourcenId
                x-apidog-ignore-properties: []
            TECHNISCHE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z20'
                x-apidog-orders:
                  - ressourcenId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MESSLOKATION
            - MARKTLOKATION
            - NETZNUTZUNGSVERTRAG
            - NETZLOKATION
            - TRANCHE
            - STEUERBARE_RESSOURCE
            - TECHNISCHE_RESSOURCE
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E01|Z89]
            vertragsende:
              type: string
              description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
              format: date-time
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E01|Z89]'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzungBefristeteAnmeldung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund bei befristeten An-/Abmeldungen
                / UTILMD STS+7++E01+ZW4+### | EDIFACT: SG4.IDE+24.STS+7
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            vertragsbeginn:
              type: string
              description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
              format: date-time
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - vertragsende
            - kategorie
            - absender
            - transaktionsgrundergaenzungBefristeteAnmeldung
            - nachrichtendatum
            - nachrichtenreferenznummer
            - vertragsbeginn
            - empfaenger
            - anfragereferenznummer
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55607 - NB an LFN - Zuordnung des LFN zur Tranche aufgrund fehlender
        Antwort
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_19132:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'Dokumentennummer - EDIFACT BGM '
            kategorie:
              type: string
              description: Bestellkategorie - EDIFACT BGM Z73 / Z74
            nachrichtendatum:
              type: string
              format: date-time
              description: Nachrichtendatum - EDIFACT DTM+137
            auftragsReferenz:
              type: string
              description: Referenz Nachrichtennummer Einkauf - EDIFACT SG1.RFF+ON
            pruefidentifikator:
              type: string
              description: Prüfidentifikator - EDIFACT SG1. RFF+Z13
            antwortstatus:
              type: string
              description: Code des Prüfschritts - EDIFACT SG2. ATJ+CODE
            antwortstatusCodeliste:
              type: string
              description: Codeliste - EDIFACT SG2. ATJ+CODE+EBD
            freitext:
              type: string
              description: Allgemeine Information - EDIFACT SG2. FTX+AAP
            absender:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: MP-ID  - EDIFACT SG3. NAD+MS+MP-ID
                rollencodetyp:
                  type: string
                  description: >-
                    Rollencodetyp Sparte Strom- EDIFACT SG3. NAD+MS+MP-ID: 9 /
                    293
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: Kontakt - EDIFACT SG6. CTA+IC+Kontaktname
                    eMailAdresse:
                      type: string
                      description: Elektronische Post - EDIFACT SG6. COM+Adresse:EM
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  description: Ansprechpartner - EDIFACT SG6. CTA+IC
                  x-apidog-ignore-properties: []
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: string
                        description: Rufnummer
                      nummertyp:
                        type: object
                        properties:
                          rufnummertyp:
                            type: string
                        x-apidog-orders:
                          - rufnummertyp
                        required:
                          - rufnummertyp
                        description: >-
                          Rufnummerntyp - EDIFACT SG6. COM+Rufnummer: FX TE AJ
                          AL
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - rufnummer
                      - nummertyp
                    required:
                      - rufnummer
                      - nummertyp
                    x-apidog-ignore-properties: []
                  description: Rufnummern - EDIFACT SG6. COM+Rufnummer
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
                - ansprechpartner
                - rufnummern
              description: Absender - EDIFACT SG3. NAD+MS
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: MP-ID - EDIFACT SG3. NAD+MR+MP-ID
                rollencodetyp:
                  type: string
                  description: >-
                    Rollencodetyp Sparte Strom- EDIFACT SG3. NAD+MR+MP-ID: 9 /
                    293
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
              description: Empfänger - EDIFACT SG3. NAD+MR
              x-apidog-ignore-properties: []
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - nachrichtendatum
            - auftragsReferenz
            - pruefidentifikator
            - antwortstatus
            - antwortstatusCodeliste
            - freitext
            - absender
            - empfaenger
          required:
            - dokumentennummer
            - kategorie
            - nachrichtendatum
            - auftragsReferenz
            - pruefidentifikator
            - antwortstatus
            - antwortstatusCodeliste
          description: Transaktionsdaten
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            ANFRAGE:
              type: array
              items:
                type: object
                properties:
                  anfragekategorie:
                    type: string
                    description: Bestellkategorie - EDIFACT BGM Z73/ Z74
                x-apidog-orders:
                  - anfragekategorie
                required:
                  - anfragekategorie
                x-apidog-ignore-properties: []
              description: BO Anfrage
          x-apidog-orders:
            - ANFRAGE
          required:
            - ANFRAGE
          description: Stammdaten
          x-apidog-ignore-properties: []
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      description: 19132 - Mitteilung zur Bestellung Konfiguration MSB an NB, LF, MSB
      required:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_15004:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            kategorie:
              type: string
              description: Angebotskategorie EDIFACT BGM+Z74
            dokumentennummer:
              type: string
              description: 'Dokumentennummer EDIFACT BGM '
            nachrichtendatum:
              type: string
              format: date-time
              description: Nachrichtendatum EDIFACT DTM+137
            pruefidentifikator:
              type: string
              description: Prüfidentifikator EDIFACT SG1. RFF+Z13
            absender:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: MP-ID EDIFACT SG11. NAD+MS+MP-ID
                rollencodetyp:
                  type: string
                  description: >-
                    Rollencodetyp Sparte Strom EDIFACT SG11. NAD+MS+MP-ID: 9 /
                    293
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: Kontakt EDIFACT SG14. CTA+IC+Kontaktname
                    eMailAdresse:
                      type: string
                      description: Kommunikationsadresse EDIFACT SG14. COM + eMail EM
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  required:
                    - nachname
                    - eMailAdresse
                  description: Informationskontakt EDIFACT SG14. CTA+IC
                  x-apidog-ignore-properties: []
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      nummertyp:
                        type: string
                        description: >-
                          Rufnummerntyp - EDIFACT SG14. COM+Rufnummer: FX TE AJ
                          AL
                      rufnummer:
                        type: string
                        description: Rufnummer EDIFACT COM+Rufnummer
                    x-apidog-orders:
                      - nummertyp
                      - rufnummer
                    x-apidog-ignore-properties: []
                  description: Rufnummern - EDIFACT SG14. COM + Rufnummer
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
                - ansprechpartner
                - rufnummern
              required:
                - rollencodenummer
                - rollencodetyp
              description: 'Nachrichtenabsender EDIFACT SG11. NAD MS '
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: MP-ID EDIFACT SG11. NAD+MR+MP-ID
                rollencodetyp:
                  type: string
                  description: >-
                    Rollencodetyp Sparte Strom EDIFACT SG11. NAD+MR+MP-ID: 9 /
                    293
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
              required:
                - rollencodenummer
                - rollencodetyp
              description: Nachrichtenempfänger EDIFACT SG11. NAD MR
              x-apidog-ignore-properties: []
          x-apidog-orders:
            - kategorie
            - dokumentennummer
            - nachrichtendatum
            - pruefidentifikator
            - absender
            - empfaenger
          description: Transaktionsdaten
          required:
            - kategorie
            - dokumentennummer
            - nachrichtendatum
            - pruefidentifikator
            - absender
            - empfaenger
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            ANFRAGE:
              type: array
              items:
                type: object
                properties:
                  anfragetyp:
                    type: string
                    description: Leistungsbeschreibung EDIFACT IMD+Z55 / Z64
                x-apidog-orders:
                  - anfragetyp
                required:
                  - anfragetyp
                x-apidog-ignore-properties: []
              description: BO ANFRAGE
            ANGEBOT:
              type: array
              items:
                type: object
                properties:
                  anfragereferenz:
                    type: string
                    description: Nachrichtennummer der Anfrage EDIFACT SG1. RFF+AAV
                  positionsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        positionsbezeichnung:
                          type: string
                          description: fortlaufende Nummer EDIFACT SG27 LIN
                        artikelId:
                          type: array
                          items:
                            type: string
                          description: Artikel-ID EDIFACT SG27. PIA+Z02
                      x-apidog-orders:
                        - positionsbezeichnung
                        - artikelId
                      x-apidog-ignore-properties: []
                    description: Positionsdaten
                x-apidog-orders:
                  - anfragereferenz
                  - positionsdaten
                required:
                  - anfragereferenz
                x-apidog-ignore-properties: []
              description: BO ANGEBOT
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: Marktlokations-ID EDIFACT SG11. LOC+172
                x-apidog-orders:
                  - marktlokationsId
                x-apidog-ignore-properties: []
              description: BO MARKTLOKATION
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  netzlokationsId:
                    type: string
                    description: Netzlokations-ID EDIFACT SG11. LOC+172
                x-apidog-orders:
                  - netzlokationsId
                x-apidog-ignore-properties: []
              description: BO NETZLOKATION
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: SR-ID EDIFACT SG11. LOC+172
                x-apidog-orders:
                  - ressourcenId
                x-apidog-ignore-properties: []
              description: BO STEUERBARE_RESSOURCE
            MESSLOKATION:
              type: array
              items:
                type: object
                properties:
                  messlokationsId:
                    type: string
                    description: Zählpunktbezeichnung EDIFACT SG11. LOC+172
                x-apidog-orders:
                  - messlokationsId
                x-apidog-ignore-properties: []
              description: BO MESSLOKATION
            SCHALTZEITDEFINITION:
              type: array
              items:
                type: object
                properties:
                  schaltzeiten:
                    type: array
                    items:
                      type: object
                      properties:
                        konfigurationsprodukt:
                          type: string
                          description: Produkt-Code EDIFACT SG27. PIA+5
                        code:
                          type: string
                          description: Code der Schaltzeitdefinition EDIFACT SG28. CCI+Z52
                      x-apidog-orders:
                        - konfigurationsprodukt
                        - code
                      x-apidog-ignore-properties: []
                    description: Schaltzeitdefinition EDIFACT SG27 LIN Z64
                x-apidog-orders:
                  - schaltzeiten
                x-apidog-ignore-properties: []
              description: BO SCHALTZEITDEFINITION
            LEISTUNGSKURVENDEFINITION:
              type: array
              items:
                type: object
                properties:
                  leistungskurven:
                    type: array
                    items:
                      type: object
                      properties:
                        konfigurationsprodukt:
                          type: string
                          description: Produkt-Code EDIFACT SG27. PIA+5
                        code:
                          type: string
                          description: >-
                            Code der Leistungskurvendefinition EDIFACT SG28.
                            CCI+Z53
                      x-apidog-orders:
                        - konfigurationsprodukt
                        - code
                      required:
                        - konfigurationsprodukt
                        - code
                      x-apidog-ignore-properties: []
                    description: Leistungskurvendefinitionen EDIFACT SG27 LIN Z65
                x-apidog-orders:
                  - leistungskurven
                x-apidog-ignore-properties: []
              description: BO LEISTUNGSKURVENDEFINITION
            AD_HOC_STEUERKANAL:
              type: array
              items:
                type: object
                properties:
                  konfigurationsprodukt:
                    type: string
                    description: Produkt-Code EDIFACT SG27. PIA+5
                x-apidog-orders:
                  - konfigurationsprodukt
                x-apidog-ignore-properties: []
              description: BO AD_HOC_STEUERKANAL
            WERTE_NACH_TYP2:
              type: array
              items:
                type: object
                properties:
                  messprodukt:
                    type: string
                    description: Produkt-Code EDIFACT SG27. PIA+5
                  konfigurationsprodukt:
                    type: string
                    description: Produkt-Code EDIFACT SG27. PIA+5
                  aenderungsmoeglichkeitKonfiguration:
                    type: string
                    description: >-
                      Änderungsmöglichkeit erforderlich / nicht erforderlich
                      EDIFACT SG28. CCI+Z54++ZF7 / ZF8
                  schwellwerte:
                    type: array
                    items:
                      type: object
                      properties:
                        konfigurationsprodukt:
                          type: string
                          description: >-
                            Messprodukt-Position-Code EDIFACT SG28.
                            CCI+Z60++Messprodukt
                        obererSchwellwert:
                          type: string
                          description: >-
                            oberer Schwellwert EDIFACT SG28.
                            CCI+Z60++Messprodukt:::XXX
                        untererSchwellwert:
                          type: string
                          description: >-
                            unterer Schwellwert EDIFACT SG28.
                            CCI+Z60++Messprodukt:::XXX:YYY
                      x-apidog-orders:
                        - konfigurationsprodukt
                        - obererSchwellwert
                        - untererSchwellwert
                      x-apidog-ignore-properties: []
                    description: Schwellwerte EDIFACT SG28. CCI+Z60
                x-apidog-orders:
                  - messprodukt
                  - konfigurationsprodukt
                  - aenderungsmoeglichkeitKonfiguration
                  - schwellwerte
                x-apidog-ignore-properties: []
              description: BO WERTE_NACH_TYP2
          x-apidog-orders:
            - ANFRAGE
            - ANGEBOT
            - MARKTLOKATION
            - NETZLOKATION
            - STEUERBARE_RESSOURCE
            - MESSLOKATION
            - SCHALTZEITDEFINITION
            - LEISTUNGSKURVENDEFINITION
            - AD_HOC_STEUERKANAL
            - WERTE_NACH_TYP2
          required:
            - ANFRAGE
            - ANGEBOT
          description: Stammdaten
          x-apidog-ignore-properties: []
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      description: 15004 - Angebot einer Konfiguration MSB an NB, LF
      required:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55672:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  lastprofile:
                    type: array
                    items:
                      type: object
                      properties:
                        profilschar:
                          type: string
                          description: >-
                            Profilschar des Profils | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+++Z12.CAV
                        bezeichnung:
                          type: string
                          description: >-
                            Externe Bezeichnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02.CAV,
                            SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+Z05.CAV
                        referenzprofilbezeichnung:
                          type: string
                          description: >-
                            Bezeichnung des Referenzprofils | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z38.SG10.CCI+Z05.CAV
                        tagesparameter:
                          type: object
                          properties:
                            herausgeber:
                              type: string
                              title: Herausgeber
                              description: >-
                                Herausgeber | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+[ZA0|Z99]
                              enum:
                                - NB
                                - BDEW
                                - TUM
                            dienstanbieter:
                              type: string
                              description: >-
                                dienstanbieter | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+[ZA0|Z99]
                            klimazone:
                              type: string
                              description: >-
                                klimazone | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+[ZA0|Z99]
                            temperaturmessstelle:
                              type: string
                              description: >-
                                temperaturmessstelle | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+[ZA0|Z99]
                          x-apidog-orders:
                            - herausgeber
                            - dienstanbieter
                            - klimazone
                            - temperaturmessstelle
                          x-apidog-ignore-properties: []
                        profilart:
                          type: string
                          title: Profilart
                          description: >-
                            Profilart | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02,
                            SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+Z05
                          enum:
                            - ART_STANDARDLASTPROFIL
                            - ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL
                            - ART_LASTPROFIL
                        einspeisung:
                          type: boolean
                          description: >-
                            Kennzeichen Einspeisung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02,
                            SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+Z05
                        verfahren:
                          type: string
                          title: Profilverfahren
                          description: >-
                            Profilverfahren | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02,
                            SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+Z05
                          enum:
                            - SYNTHETISCH
                            - ANALYTISCH
                      x-apidog-orders:
                        - profilschar
                        - bezeichnung
                        - referenzprofilbezeichnung
                        - tagesparameter
                        - profilart
                        - einspeisung
                        - verfahren
                      x-apidog-ignore-properties: []
                  zeitreihentyp:
                    type: string
                    title: Zeitreihentyp
                    description: >-
                      Zeitreihentyp | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+15+Z21.CAV
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
                  temperaturarbeit:
                    type: object
                    properties:
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+[Z10|265]
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
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+[Z10|265]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - einheit
                      - wert
                    x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z21,
                          SG4.IDE+24.SG8.SEQ+Z08, SG4.IDE+24.SG8.SEQ+Z38
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z21,
                      SG4.IDE+24.SG8.SEQ+Z08, SG4.IDE+24.SG8.SEQ+Z38
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
                  prognosegrundlage:
                    type: string
                    title: Prognosegrundlage
                    description: >-
                      Prognosegrundlage | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI
                    enum:
                      - WERTE
                      - PROFILE
                  bilanzkreis:
                    type: object
                    title: Bilanzkreis
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z19'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  detailsPrognosegrundlage:
                    type: array
                    items:
                      type: array
                      description: >-
                        Prognosegrundlage - Besteht der Bedarf ein
                        tagesparameteräbhängiges Lastprofil mit gemeinsamer
                        Messung anzugeben, so ist dies über die 2 -malige
                        Wiederholung des CAV Segments mit der Angabe der Codes
                        E02 und E14 möglich. | EDIFACT:
                        SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI.CAV+[E02|E14]
                      items:
                        type: string
                        title: Profiltyp
                        description: Profiltyp
                        enum:
                          - SLP_SEP
                          - TLP_TEP
                          - TEP
                  aggregationsverantwortung:
                    type: string
                    title: Aggregationsverantwortung
                    description: >-
                      Aggregationsverantwortung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+6
                    enum:
                      - UENB
                      - VNB
                  jahresverbrauchsprognose:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+31'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+31
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
                    x-apidog-orders:
                      - wert
                      - einheit
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - lastprofile
                  - zeitreihentyp
                  - temperaturarbeit
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - prognosegrundlage
                  - bilanzkreis
                  - detailsPrognosegrundlage
                  - aggregationsverantwortung
                  - jahresverbrauchsprognose
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z15'
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
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z15'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  bilanzkreis:
                    type: object
                    title: Bilanzkreis
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z15.SG10.CCI+Z19'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - datenqualitaet
                  - tranchenId
                  - gueltigkeitszeitraum
                  - bilanzkreis
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z90
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z90
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
                      x-apidog-orders:
                        - rollencodenummer
                        - marktrolle
                      x-apidog-ignore-properties: []
                  regelzone:
                    type: string
                    description: >-
                      für EDIFACT mapping | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z18
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01'
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  bilanzierungsgebiet:
                    type: string
                    description: >-
                      Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist -
                      im Falle eines Strom Netzes. | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z20
                x-apidog-orders:
                  - marktrollen
                  - regelzone
                  - marktlokationsId
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - bilanzierungsgebiet
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - BILANZIERUNG
            - TRANCHE
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - transaktionsgrundergaenzung
            - vorgangsnummer
            - pruefidentifikator
            - transaktionsgrund
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55672 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55652:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+Z17.SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+Z17.SG10.CCI+++ZA7.CAV
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
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z17.PIA+5
                      x-apidog-orders:
                        - verwendungszwecke
                        - obisKennzahl
                      x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z17'
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
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z17'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zaehlwerke
                  - datenqualitaet
                  - tranchenId
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - TRANCHE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 55652 - MSB an LF - Änderung vom MSB an LF
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55651:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z61.SG10.CCI+++ZA7'
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z62,
                          SG4.IDE+24.SG8.SEQ+Z61
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  zugeordneteDefinition:
                    type: object
                    properties:
                      schaltzeitdefinition:
                        type: object
                        title: Schaltzeitdefinition
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z61.SG10.CCI+[Z52|Z53]'
                        properties:
                          boTyp:
                            type: string
                            title: BOTyp
                            description: Typ des BO
                            enum:
                              - SCHALTZEITDEFINITION
                          versionStruktur:
                            type: string
                            description: versionStruktur
                            default: '1'
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                      leistungskurvendefinition:
                        type: object
                        title: Leistungskurvendefinition
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z61.SG10.CCI+[Z52|Z53]'
                        properties:
                          boTyp:
                            type: string
                            title: BOTyp
                            description: Typ des BO
                            enum:
                              - LEISTUNGSKURVENDEFINITION
                          versionStruktur:
                            type: string
                            description: versionStruktur
                            default: '1'
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - schaltzeitdefinition
                      - leistungskurvendefinition
                    x-apidog-ignore-properties: []
                  auftraggebenderMarktpartner:
                    type: object
                    properties:
                      rollencodenummer:
                        type: string
                        description: >-
                          Gibt die Codenummer der Marktrolle an. | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z61.SG10.CCI+++ZB3.CAV+[Z88|Z89]
                      marktrolle:
                        type: string
                        title: Marktrolle
                        description: >-
                          Diese Rollen kann ein Marktteilnehmer einnehmen |
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z61.SG10.CCI+++ZB3.CAV+[Z88|Z89]
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
                    x-apidog-orders:
                      - rollencodenummer
                      - marktrolle
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z62,
                      SG4.IDE+24.SG8.SEQ+Z61
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
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z61.PIA+5
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                  steuerkanal:
                    type: object
                    title: AdHocSteuerkanal
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z62.SG10.CCI+Z49.CAV+ZF2'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - AD_HOC_STEUERKANAL
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - produktdatenRelevanteRolle
                  - gueltigkeitszeitraum
                  - zugeordneteDefinition
                  - auftraggebenderMarktpartner
                  - datenqualitaet
                  - konfigurationsprodukt
                  - ressourcenId
                  - steuerkanal
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - STEUERBARE_RESSOURCE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 55651 - MSB an LF - Änderung vom MSB an LF
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55650:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z02.PIA+5
                        wertegranularitaet:
                          type: string
                          title: Wertegranularitaet
                          description: >-
                            Wertegranularitaet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z02.SG10.CCI+++ZE4.CAV+[ZD9|ZE8|ZE9|ZB7]
                          enum:
                            - JAEHRLICH
                            - HALBJAEHRLICH
                            - QUARTALSWEISE
                            - MONATLICH
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z02.SG10.CCI+Z39'
                              properties:
                                boTyp:
                                  type: string
                                  title: BOTyp
                                  description: Typ des BO
                                  enum:
                                    - ZAEHLZEITDEFINITION
                                versionStruktur:
                                  type: string
                                  description: versionStruktur
                                  default: '1'
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                            register:
                              type: object
                              title: Zaehlzeitregister
                              description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z02.SG10.CCI+Z38'
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - zaehlzeitDefinition
                            - register
                          x-apidog-ignore-properties: []
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+Z02.SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+Z02.SG10.CCI+++ZA7.CAV
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
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - obisKennzahl
                        - wertegranularitaet
                        - zaehlzeiten
                        - verwendungszwecke
                      x-apidog-ignore-properties: []
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+Z50,
                      SG4.IDE+24.SG8.SEQ+Z02, SG4.IDE+24.SG8.SEQ+Z59
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+Z50,
                          SG4.IDE+24.SG8.SEQ+Z02, SG4.IDE+24.SG8.SEQ+Z59
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z59.SG10.CCI+++ZA7'
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
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z59.PIA+5,
                      SG4.IDE+24.SG8.SEQ+Z59.SG10.CCI+11
                  leistungskurvendefinition:
                    type: object
                    title: Leistungskurvendefinition
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z59.SG10.CCI+Z53'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - LEISTUNGSKURVENDEFINITION
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zaehlwerke
                  - marktlokationsId
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - produktdatenRelevanteRolle
                  - konfigurationsprodukt
                  - leistungskurvendefinition
                x-apidog-ignore-properties: []
            MESSSTELLENBETRIEBSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragskonditionen:
                    type: object
                    properties:
                      geplanteTurnusablesung:
                        type: object
                        properties:
                          ableseZeitraum:
                            type: string
                            description: >-
                              ableseZeitraum | EDIFACT:
                              SG4.IDE+24.SG6.RFF+Z50.DTM+752
                        x-apidog-orders:
                          - ableseZeitraum
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - geplanteTurnusablesung
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragskonditionen
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - MESSSTELLENBETRIEBSVERTRAG
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 55650 - MSB an LF - Änderung vom MSB an LF
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55649:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  auftraggebenderMarktpartner:
                    type: object
                    properties:
                      marktrolle:
                        type: string
                        title: Marktrolle
                        description: >-
                          Diese Rollen kann ein Marktteilnehmer einnehmen |
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z60.SG10.CCI+++ZB3.CAV+[Z88|Z89]
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
                      rollencodenummer:
                        type: string
                        description: >-
                          Gibt die Codenummer der Marktrolle an. | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z60.SG10.CCI+++ZB3.CAV+[Z88|Z89]
                    x-apidog-orders:
                      - marktrolle
                      - rollencodenummer
                    x-apidog-ignore-properties: []
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z57.PIA+5
                        verwendungszwecke:
                          type: array
                          items:
                            type: object
                            properties:
                              zweck:
                                type: array
                                items:
                                  type: object
                                  title: Verwendungszweck
                                  description: >-
                                    EDIFACT:
                                    SG4.IDE+24.SG8.SEQ+Z57.SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+Z57.SG10.CCI+++ZA7.CAV
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
                            x-apidog-orders:
                              - zweck
                              - marktrolle
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - obisKennzahl
                        - verwendungszwecke
                      x-apidog-ignore-properties: []
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z60.SG10.CCI+++ZA7'
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z51,
                          SG4.IDE+24.SG8.SEQ+Z57, SG4.IDE+24.SG8.SEQ+Z60
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  steuerkanal:
                    type: object
                    title: AdHocSteuerkanal
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z51.SG10.CCI+Z49'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - AD_HOC_STEUERKANAL
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18
                  keinKonfigurationsprodukt:
                    type: boolean
                    description: >-
                      keinKonfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z60.SG10.CCI+11
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z51,
                      SG4.IDE+24.SG8.SEQ+Z57, SG4.IDE+24.SG8.SEQ+Z60
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
                  leistungskurvendefinition:
                    type: object
                    title: Leistungskurvendefinition
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z60.SG10.CCI+Z53'
                    properties:
                      boTyp:
                        type: string
                        title: BOTyp
                        description: Typ des BO
                        enum:
                          - LEISTUNGSKURVENDEFINITION
                      versionStruktur:
                        type: string
                        description: versionStruktur
                        default: '1'
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-orders:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                  konfigurationsprodukt:
                    type: string
                    description: >-
                      konfigurationsprodukt | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z60.PIA+5
                x-apidog-orders:
                  - auftraggebenderMarktpartner
                  - zaehlwerke
                  - produktdatenRelevanteRolle
                  - gueltigkeitszeitraum
                  - steuerkanal
                  - netzlokationsId
                  - keinKonfigurationsprodukt
                  - datenqualitaet
                  - leistungskurvendefinition
                  - konfigurationsprodukt
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 55649 - MSB an LF - Änderung vom MSB an LF
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55620:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            MESSLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z18.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+Z18.SG10.CCI+++ZB3.CAV+ZF0
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z18.SG10.CCI+++ZB3.CAV+Z91
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z18.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z18.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+Z18.SG10.CCI+++ZB3.CAV+ZF0
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
                      x-apidog-orders:
                        - rollencodenummer
                        - weiterverpflichtet
                        - messstellenbetreiberEigenschaft
                        - marktrolle
                      x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z18'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  messlokationsId:
                    type: string
                    description: >-
                      Die Messlokations-Identifikation. Das ist die frühere
                      Zählpunktbezeichnung,

                      z.B. DE 47108151234567 | EDIFACT: SG4.IDE+24.SG5.LOC+Z17
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z18'
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
                x-apidog-orders:
                  - marktrollen
                  - gueltigkeitszeitraum
                  - messlokationsId
                  - datenqualitaet
                x-apidog-ignore-properties: []
            MESSSTELLENBETRIEBSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragskonditionen:
                    type: object
                    properties:
                      abrechnungUeberNna:
                        type: boolean
                        description: >-
                          abrechnungUeberNna | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z18.RFF+Z05
                    x-apidog-orders:
                      - abrechnungUeberNna
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragskonditionen
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MESSLOKATION
            - MESSSTELLENBETRIEBSVERTRAG
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55620 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55619:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z15'
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
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                  verguetungEmpfaenger:
                    type: string
                    title: VerguetungEmpfaenger
                    description: >-
                      VerguetungEmpfaenger | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z15.SG10.CCI+++Z89.CAV
                    enum:
                      - KUNDE
                      - LIEFERANT
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z15'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - datenqualitaet
                  - tranchenId
                  - verguetungEmpfaenger
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - TRANCHE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55619 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55618:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z62'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z62'
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
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z62.SG10.CCI+++ZB3.CAV+Z91
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
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z62.SG10.CCI+++ZB3.CAV+Z91
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z62.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                      x-apidog-orders:
                        - marktrolle
                        - rollencodenummer
                        - messstellenbetreiberEigenschaft
                      x-apidog-ignore-properties: []
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                x-apidog-orders:
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                  - ressourcenId
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - STEUERBARE_RESSOURCE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55618 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55617:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - vorgangsnummer
            - pruefidentifikator
            - transaktionsgrund
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            TECHNISCHE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  einordnung:
                    type: string
                    title: MesstechnischeEinordnung
                    description: >-
                      MesstechnischeEinordnung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+[Z17|Z50|Z56].CAV+[ZH2|ZH3|ZH4|ZH5]
                    enum:
                      - IMS
                      - KME_MME
                      - KEINE_MESSUNG
                  weitereEinrichtung:
                    type: boolean
                    description: >-
                      weitereEinrichtung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+Z63.CAV+[ZH7|ZH8]
                  nennleistung:
                    type: object
                    properties:
                      aufnahme:
                        type: number
                        description: >-
                          Aufnahme der Nennleistung | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z52.SG9.QTY+Z43
                        format: float
                      abgabe:
                        type: object
                        title: Konzessionsabgabe
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z52.SG9.QTY+Z44'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - aufnahme
                      - abgabe
                    x-apidog-ignore-properties: []
                  referenzNetzlokation:
                    type: string
                    description: >-
                      referenzNetzlokation | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.RFF+Z32
                  enwg:
                    type: boolean
                    description: >-
                      enwg | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+[Z17|Z50|Z56].CAV+[ZG8|ZG9]
                  speicherkapazitaet:
                    type: number
                    description: >-
                      Speicherkapazität

                      Beispiel: QTY+Z42:100:KWH' | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG9.QTY+Z42
                    format: float
                  erzeugungsart:
                    type: string
                    title: Erzeugungsart
                    description: >-
                      Auflistung der Erzeugungsarten von Energie. | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+[Z17|Z50|Z56].CAV+[ZF5|ZF6|ZG0|ZG1|ZG5]
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
                  referenzSteuerbareRessource:
                    type: string
                    description: >-
                      referenzSteuerbareRessource | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.RFF+Z38
                  speicherart:
                    type: string
                    title: Speicherart
                    description: >-
                      Speicherart | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+[Z17|Z50|Z56].CAV+[ZF7|ZF8|ZF9|ZG6]
                    enum:
                      - WASSERSTOFFSPEICHER
                      - PUMPSPEICHER
                      - BATTERIESPEICHER
                      - SONSTIGE_SPEICHERART
                  art:
                    type: string
                    title: AbgabeArt
                    description: >-
                      Art der Konzessionsabgabe | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+[Z17|Z50|Z56]
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
                  waermenutzung:
                    type: string
                    title: Waermenutzung
                    description: >-
                      Waermenutzung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+[Z17|Z50|Z56].CAV
                    enum:
                      - SPEICHERHEIZUNG
                      - WAERMEPUMPE
                      - DIREKTHEIZUNG
                      - WAERMEPUMPE_WAERME_KAELTE
                      - WAERMEPUMPE_KAELTE
                      - WAERMEPUMPE_WAERME
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z20'
                  verbrauchsart:
                    type: string
                    title: Verbrauchsart
                    description: >-
                      Verbrauchsart | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+[Z17|Z50|Z56].CAV+[Z64|Z65|ZE5|ZA8]
                    enum:
                      - KL
                      - W
                      - EMOB
                      - SB
                      - SW
                      - WK
                  inbetriebsetzungsdatum:
                    type: string
                    title: Inbetriebsetzung
                    description: >-
                      EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+[Z17|Z50|Z56].CAV+[ZH0|ZH1]
                    enum:
                      - INBETRIEBSETZUNG_NACH_2023
                      - INBETRIEBSETZUN_VOR_2024
                x-apidog-orders:
                  - einordnung
                  - weitereEinrichtung
                  - nennleistung
                  - referenzNetzlokation
                  - enwg
                  - speicherkapazitaet
                  - erzeugungsart
                  - referenzSteuerbareRessource
                  - speicherart
                  - art
                  - waermenutzung
                  - ressourcenId
                  - verbrauchsart
                  - inbetriebsetzungsdatum
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: >-
                      zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53],
                      SG4.IDE+24.SG8.SEQ+Z52
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - TECHNISCHE_RESSOURCE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55617 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55616:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen

                            beispielsweise der Nachname dargestellt werden.
                            Beispiele: Yellow Strom GmbH

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z25
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z25
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z25
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
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z25
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z25'
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z25
                      x-apidog-orders:
                        - name1
                        - anrede
                        - geschaeftspartnerrolle
                        - name3
                        - name4
                        - name2
                      x-apidog-ignore-properties: []
                  korrespondenzpartner:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z26'
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z26'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z26'
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z26
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
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z26'
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z26'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z26
                        x-apidog-orders:
                          - postfach
                          - ortsteil
                          - postleitzahl
                          - landescode
                          - ort
                          - strasse
                          - hausnummer
                        x-apidog-ignore-properties: []
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z26
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z26
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z26'
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z26
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z26
                    x-apidog-orders:
                      - partneradresse
                      - name2
                      - anrede
                      - name4
                      - name3
                      - name1
                    x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG12.NAD+Z25.RFF+Z46,
                          SG4.IDE+24.SG12.NAD+Z26.RFF+Z46
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG12.NAD+Z25,
                      SG4.IDE+24.SG12.NAD+Z26
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
                x-apidog-orders:
                  - vertragspartner2
                  - korrespondenzpartner
                  - gueltigkeitszeitraum
                  - datenqualitaet
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01,
                      SG4.IDE+24.SG8.SEQ+Z44, SG4.IDE+24.SG8.SEQ+Z40,
                      SG4.IDE+24.SG12.NAD+EO, SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58],
                      SG4.IDE+24.SG12.NAD+DP
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
                  hausverwalter:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          ortsteil:
                            type: string
                            description: >-
                              Ortsteil | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
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
                          strasse:
                            type: string
                            description: >-
                              Strasse | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
                          postfach:
                            type: string
                            description: >-
                              Postfach | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
                          postleitzahl:
                            type: string
                            description: >-
                              Postleitzahl | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]'
                        x-apidog-orders:
                          - ortsteil
                          - landescode
                          - strasse
                          - postfach
                          - postleitzahl
                          - hausnummer
                          - ort
                        x-apidog-ignore-properties: []
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]'
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
                      gewerbekennzeichnung:
                        type: boolean
                        description: >-
                          Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
                          (gewerbeKennzeichnung = true)

                          oder eine Privatperson handelt. (gewerbeKennzeichnung
                          = false) | EDIFACT: SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
                    x-apidog-orders:
                      - partneradresse
                      - name1
                      - name4
                      - anrede
                      - gewerbekennzeichnung
                      - name2
                      - name3
                    x-apidog-ignore-properties: []
                  lokationsadresse:
                    type: object
                    properties:
                      landescode:
                        type: string
                        title: Landescode
                        description: >-
                          Der ISO-Landescode als Enumeration | EDIFACT:
                          SG4.IDE+24.SG12.NAD+DP
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
                      zusatzInformation:
                        type: object
                        properties:
                          zusatz4:
                            type: string
                            description: 'Adresszusatz 4 | EDIFACT: SG4.IDE+24.SG12.NAD+DP'
                          zusatz1:
                            type: string
                            description: 'Adresszusatz 1 | EDIFACT: SG4.IDE+24.SG12.NAD+DP'
                          zusatz2:
                            type: string
                            description: 'Adresszusatz 2 | EDIFACT: SG4.IDE+24.SG12.NAD+DP'
                          zusatz5:
                            type: string
                            description: 'Adresszusatz 5 | EDIFACT: SG4.IDE+24.SG12.NAD+DP'
                          zusatz3:
                            type: string
                            description: 'Adresszusatz 3 | EDIFACT: SG4.IDE+24.SG12.NAD+DP'
                        x-apidog-orders:
                          - zusatz4
                          - zusatz1
                          - zusatz2
                          - zusatz5
                          - zusatz3
                        x-apidog-ignore-properties: []
                      ortsteil:
                        type: string
                        description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+DP'
                      postleitzahl:
                        type: string
                        description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+DP'
                      strasse:
                        type: string
                        description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+DP'
                      hausnummer:
                        type: string
                        description: >-
                          Hausnummer und Ergänzung | EDIFACT:
                          SG4.IDE+24.SG12.NAD+DP
                      ort:
                        type: string
                        description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+DP'
                      postfach:
                        type: string
                        description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+DP'
                    x-apidog-orders:
                      - landescode
                      - zusatzInformation
                      - ortsteil
                      - postleitzahl
                      - strasse
                      - hausnummer
                      - ort
                      - postfach
                    x-apidog-ignore-properties: []
                  statusErzeugendeMalo:
                    type: string
                    title: StatusErzeugendeMarktlokation
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z22'
                    enum:
                      - EINSPEISEVERGUETUNG_PARAGRAPH_37
                      - GEFOERDERTE_DIREKTVERMARKTUNG
                      - SONSTIGE_DIREKTVERMARKTUNG
                      - VERMARKTUNG_OHNE_GESETZL_VERGUETUNG
                      - KWKG_VERGUETUNG
                      - EINSPEISEVERGUETUNG_PARAGRAPH_38_AUSFALLVERGUETUNG
                  eigentuemer:
                    type: object
                    properties:
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+EO
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+EO'
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+EO
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+EO
                      partneradresse:
                        type: object
                        properties:
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+EO'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+EO'
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+EO'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+EO'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+EO
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+EO
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
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+EO'
                        x-apidog-orders:
                          - strasse
                          - postfach
                          - ort
                          - postleitzahl
                          - hausnummer
                          - landescode
                          - ortsteil
                        x-apidog-ignore-properties: []
                      gewerbekennzeichnung:
                        type: boolean
                        description: >-
                          Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
                          (gewerbeKennzeichnung = true)

                          oder eine Privatperson handelt. (gewerbeKennzeichnung
                          = false) | EDIFACT: SG4.IDE+24.SG12.NAD+EO
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+EO
                    x-apidog-orders:
                      - name3
                      - name4
                      - name2
                      - name1
                      - partneradresse
                      - gewerbekennzeichnung
                      - anrede
                    x-apidog-ignore-properties: []
                  redispatch:
                    type: boolean
                    description: 'redispatch | EDIFACT: SG4.IDE+24.SG8.SEQ+Z40.PIA+5'
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z91
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z91
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
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z91
                      x-apidog-orders:
                        - messstellenbetreiberEigenschaft
                        - weiterverpflichtet
                        - marktrolle
                        - rollencodenummer
                      x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01,
                          SG4.IDE+24.SG8.SEQ+Z44, SG4.IDE+24.SG8.SEQ+Z40,
                          SG4.IDE+24.SG12.NAD+EO.RFF+Z46,
                          SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58].RFF+Z46,
                          SG4.IDE+24.SG12.NAD+DP.RFF+Z46
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  verguetungEmpfaenger:
                    type: string
                    title: VerguetungEmpfaenger
                    description: >-
                      VerguetungEmpfaenger | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++Z89.CAV
                    enum:
                      - KUNDE
                      - LIEFERANT
                  fernsteuerbarkeit:
                    type: string
                    title: Fernsteuerbarkeit
                    description: >-
                      Fernsteuerbarkeit | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z24
                    enum:
                      - TECHNISCH_NICHT_FERNSTEUERBAR
                      - TECHNISCH_FERNSTEUERBAR
                      - DURCH_LF_FERNSTEUERBAR
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z44.RFF+Z10
                        verbrauchsart:
                          type: string
                          title: Verbrauchsart
                          description: >-
                            Verbrauchsart | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z44.SG10.CCI+Z17.CAV
                          enum:
                            - KL
                            - W
                            - EMOB
                            - SB
                            - SW
                            - WK
                      x-apidog-orders:
                        - obisKennzahl
                        - verbrauchsart
                      x-apidog-ignore-properties: []
                  energieherkunft:
                    type: array
                    items:
                      type: object
                      properties:
                        erzeugungsart:
                          type: string
                          title: Erzeugungsart
                          description: >-
                            Auflistung der Erzeugungsarten von Energie. |
                            EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++Z34.CAV
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
                      x-apidog-orders:
                        - erzeugungsart
                      x-apidog-ignore-properties: []
                  messtechnischeEinordnung:
                    type: string
                    title: MesstechnischeEinordnung
                    description: >-
                      MesstechnischeEinordnung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++Z83.CAV
                    enum:
                      - IMS
                      - KME_MME
                      - KEINE_MESSUNG
                x-apidog-orders:
                  - marktlokationsId
                  - datenqualitaet
                  - hausverwalter
                  - lokationsadresse
                  - statusErzeugendeMalo
                  - eigentuemer
                  - redispatch
                  - marktrollen
                  - gueltigkeitszeitraum
                  - verguetungEmpfaenger
                  - fernsteuerbarkeit
                  - zaehlwerke
                  - energieherkunft
                  - messtechnischeEinordnung
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                x-apidog-orders:
                  - zeitraumId
                  - verwendungBis
                  - verwendungAb
                  - datenqualitaet
                x-apidog-ignore-properties: []
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  wahlrechtPrognosegrundlage:
                    type: string
                    title: WahlrechtPrognosegrundlage
                    description: >-
                      WahlrechtPrognosegrundlage | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++Z84.CAV
                    enum:
                      - DURCH_LF
                      - DURCH_LF_NICHT_GEGEBEN
                      - NICHT_WEGEN_GROSSEN_VERBRAUCHS
                      - NICHT_WEGEN_EIGENVERBRAUCH
                      - NICHT_WEGEN_TAGES_VERBRAUCH
                      - NICHT_WEGEN_ENWG
                x-apidog-orders:
                  - wahlrechtPrognosegrundlage
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZNUTZUNGSVERTRAG
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
            - BILANZIERUNG
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                  x-apidog-orders:
                    - eMailAdresse
                    - nachname
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - empfaenger
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - transaktionsgrund
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - dokumentennummer
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55616 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55615:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z51'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z51.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z51.SG10.CCI+++ZB3.CAV+Z91
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
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z51.SG10.CCI+++ZB3.CAV+Z91
                      x-apidog-orders:
                        - messstellenbetreiberEigenschaft
                        - marktrolle
                        - rollencodenummer
                      x-apidog-ignore-properties: []
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z51'
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
                x-apidog-orders:
                  - gueltigkeitszeitraum
                  - marktrollen
                  - netzlokationsId
                  - datenqualitaet
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55615 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55553:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            AD_HOC_STEUERKANAL:
              type: array
              items:
                type: object
                properties:
                  IPAdresseCLSDevice:
                    type: object
                    properties:
                      IPAdresseCLSDevice1:
                        type: string
                        description: 'IPAdresseCLSDevice1 | EDIFACT: SG4.IDE+24.FTX+Z18'
                      IPAdresseCLSDevice3:
                        type: string
                        description: 'IPAdresseCLSDevice3 | EDIFACT: SG4.IDE+24.FTX+Z18'
                      IPAdresseCLSDevice2:
                        type: string
                        description: 'IPAdresseCLSDevice2 | EDIFACT: SG4.IDE+24.FTX+Z18'
                      IPAdresseCLSDevice5:
                        type: string
                        description: 'IPAdresseCLSDevice5 | EDIFACT: SG4.IDE+24.FTX+Z18'
                      IPAdresseCLSDevice4:
                        type: string
                        description: 'IPAdresseCLSDevice4 | EDIFACT: SG4.IDE+24.FTX+Z18'
                    x-apidog-orders:
                      - IPAdresseCLSDevice1
                      - IPAdresseCLSDevice3
                      - IPAdresseCLSDevice2
                      - IPAdresseCLSDevice5
                      - IPAdresseCLSDevice4
                    x-apidog-ignore-properties: []
                  zieladresse:
                    type: object
                    properties:
                      zieladresse1:
                        type: string
                        description: 'zieladresse1 | EDIFACT: SG4.IDE+24.FTX+Z17'
                      zieladresse5:
                        type: string
                        description: 'zieladresse5 | EDIFACT: SG4.IDE+24.FTX+Z17'
                      zieladresse4:
                        type: string
                        description: 'zieladresse4 | EDIFACT: SG4.IDE+24.FTX+Z17'
                      zieladresse3:
                        type: string
                        description: 'zieladresse3 | EDIFACT: SG4.IDE+24.FTX+Z17'
                      zieladresse2:
                        type: string
                        description: 'zieladresse2 | EDIFACT: SG4.IDE+24.FTX+Z17'
                    x-apidog-orders:
                      - zieladresse1
                      - zieladresse5
                      - zieladresse4
                      - zieladresse3
                      - zieladresse2
                    x-apidog-ignore-properties: []
                  zertifikatsNutzer:
                    type: object
                    properties:
                      zertifikatsNutzer3:
                        type: string
                        description: 'zertifikatsNutzer3 | EDIFACT: SG4.IDE+24.FTX+Z23'
                      zertifikatsNutzer4:
                        type: string
                        description: 'zertifikatsNutzer4 | EDIFACT: SG4.IDE+24.FTX+Z23'
                      zertifikatsNutzer2:
                        type: string
                        description: 'zertifikatsNutzer2 | EDIFACT: SG4.IDE+24.FTX+Z23'
                      zertifikatsNutzer1:
                        type: string
                        description: 'zertifikatsNutzer1 | EDIFACT: SG4.IDE+24.FTX+Z23'
                      zertifikatsNutzer5:
                        type: string
                        description: 'zertifikatsNutzer5 | EDIFACT: SG4.IDE+24.FTX+Z23'
                    x-apidog-orders:
                      - zertifikatsNutzer3
                      - zertifikatsNutzer4
                      - zertifikatsNutzer2
                      - zertifikatsNutzer1
                      - zertifikatsNutzer5
                    x-apidog-ignore-properties: []
                  aussteller:
                    type: object
                    properties:
                      aussteller3:
                        type: string
                        description: 'aussteller3 | EDIFACT: SG4.IDE+24.FTX+Z24'
                      aussteller4:
                        type: string
                        description: 'aussteller4 | EDIFACT: SG4.IDE+24.FTX+Z24'
                      aussteller5:
                        type: string
                        description: 'aussteller5 | EDIFACT: SG4.IDE+24.FTX+Z24'
                      aussteller1:
                        type: string
                        description: 'aussteller1 | EDIFACT: SG4.IDE+24.FTX+Z24'
                      aussteller2:
                        type: string
                        description: 'aussteller2 | EDIFACT: SG4.IDE+24.FTX+Z24'
                    x-apidog-orders:
                      - aussteller3
                      - aussteller4
                      - aussteller5
                      - aussteller1
                      - aussteller2
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - IPAdresseCLSDevice
                  - zieladresse
                  - zertifikatsNutzer
                  - aussteller
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z02.PIA+5
                        wertegranularitaet:
                          type: string
                          title: Wertegranularitaet
                          description: >-
                            Wertegranularitaet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z02.SG10.CCI+++ZE4.CAV+[ZD9|ZE8|ZE9|ZB7]
                          enum:
                            - JAEHRLICH
                            - HALBJAEHRLICH
                            - QUARTALSWEISE
                            - MONATLICH
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z02.SG10.CCI+Z39'
                              properties:
                                boTyp:
                                  type: string
                                  title: BOTyp
                                  description: Typ des BO
                                  enum:
                                    - ZAEHLZEITDEFINITION
                                versionStruktur:
                                  type: string
                                  description: versionStruktur
                                  default: '1'
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                            register:
                              type: object
                              title: Zaehlzeitregister
                              description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z02.SG10.CCI+Z38'
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - zaehlzeitDefinition
                            - register
                          x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - obisKennzahl
                        - wertegranularitaet
                        - zaehlzeiten
                      x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z02'
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z02'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zaehlwerke
                  - datenqualitaet
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            ZAEHLER:
              type: array
              items:
                type: object
                properties:
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z03,
                          SG4.IDE+24.SG8.SEQ+Z20
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  zaehlwerke:
                    type: array
                    items:
                      type: object
                      properties:
                        zaehlzeiten:
                          type: object
                          properties:
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z20.SG10.CCI+Z39'
                              properties:
                                boTyp:
                                  type: string
                                  title: BOTyp
                                  description: Typ des BO
                                  enum:
                                    - ZAEHLZEITDEFINITION
                                versionStruktur:
                                  type: string
                                  description: versionStruktur
                                  default: '1'
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                            register:
                              type: object
                              title: Zaehlzeitregister
                              description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z20.SG10.CCI+Z38'
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - zaehlzeitDefinition
                            - register
                          x-apidog-ignore-properties: []
                        bezeichnung:
                          type: string
                          description: >-
                            Externe Bezeichnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z20.SG10.CCI+++Z63
                        wertegranularitaet:
                          type: string
                          title: Wertegranularitaet
                          description: >-
                            Wertegranularitaet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z20.SG10.CCI+++ZE4.CAV+[ZD9|ZE8|ZE9|ZB7]
                          enum:
                            - JAEHRLICH
                            - HALBJAEHRLICH
                            - QUARTALSWEISE
                            - MONATLICH
                        nachkommastelle:
                          type: integer
                          description: >-
                            nachkommastelle | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z20.SG10.CCI+11++Z33.CAV
                        obisKennzahl:
                          type: string
                          description: >-
                            Die OBIS-Kennzahl für das Zählwerk, die festlegt,
                            welche auf die gemessene Größe mit dem Stand
                            gemeldet wird.

                            Nur Zählwerkstände mit dieser OBIS-Kennzahl werden
                            an diesem Zählwerk registriert. Beispiel:1-0:1.8.1
                            für

                            elektrische Wirkarbeit. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z20.PIA+5
                        vorkommastelle:
                          type: integer
                          description: >-
                            vorkommastelle | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z20.SG10.CCI+11++Z33.CAV
                        konfiguration:
                          type: string
                          title: AenderungsmoeglichkeitKonfiguration
                          description: >-
                            AenderungsmoeglichkeitKonfiguration | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z20.RFF+AGK
                          enum:
                            - ERFORDERLICH
                            - NICHT_ERFORDERLICH
                      x-apidog-orders:
                        - zaehlzeiten
                        - bezeichnung
                        - wertegranularitaet
                        - nachkommastelle
                        - obisKennzahl
                        - vorkommastelle
                        - konfiguration
                      x-apidog-ignore-properties: []
                  geraete:
                    type: array
                    items:
                      type: object
                      properties:
                        geraetetyp:
                          type: string
                          title: Geraetetyp
                          description: >-
                            Auflistung möglicher abzurechnender Gerätetypen |
                            EDIFACT: SG4.IDE+24.SG8.SEQ+Z20.RFF+Z14
                          enum:
                            - WECHSELSTROMZAEHLER
                            - DREHSTROMZAEHLER
                            - ZWEIRICHTUNGSZAEHLER
                            - RLM_ZAEHLER
                            - IMS_ZAEHLER
                            - BALGENGASZAEHLER
                            - MAXIMUMZAEHLER
                            - MULTIPLEXANLAGE
                            - PAUSCHALANLAGE
                            - VERSTAERKERANLAGE
                            - SUMMATIONSGERAET
                            - IMPULSGEBER
                            - EDL_21_ZAEHLERAUFSATZ
                            - VIER_QUADRANTEN_LASTGANGZAEHLER
                            - MENGENUMWERTER
                            - STROMWANDLER
                            - SPANNUNGSWANDLER
                            - DATENLOGGER
                            - KOMMUNIKATIONSANSCHLUSS
                            - MODEM
                            - TELEKOMMUNIKATIONSEINRICHTUNG
                            - KOMMUNIKATIONSEINRICHTUNG
                            - DREHKOLBENGASZAEHLER
                            - TURBINENRADGASZAEHLER
                            - ULTRASCHALLZAEHLER
                            - WIRBELGASZAEHLER
                            - MODERNE_MESSEINRICHTUNG
                            - ELEKTRONISCHER_HAUSHALTSZAEHLER
                            - STEUEREINRICHTUNG
                            - TECHNISCHESTEUEREINRICHTUNG
                            - TARIFSCHALTGERAET
                            - RUNDSTEUEREMPFAENGER
                            - OPTIONALE_ZUS_ZAEHLEINRICHTUNG
                            - MESSWANDLERSATZ_IMS_MME
                            - KOMBIMESSWANDLER_IMS_MME
                            - TARIFSCHALTGERAET_IMS_MME
                            - RUNDSTEUEREMPFAENGER_IMS_MME
                            - TEMPERATUR_KOMPENSATION
                            - HOECHSTBELASTUNGS_ANZEIGER
                            - SONSTIGES_GERAET
                            - SMARTMETERGATEWAY
                            - STEUERBOX
                            - BLOCKSTROMWANDLER
                            - KOMBIMESSWANDLER
                            - MODEM_GSM
                            - ETHERNET_KOM
                            - PLC_COM
                            - MODEM_FESTNETZ
                            - DSL_KOM
                            - LTE_KOM
                            - DICHTEMENGENUMWERTER
                            - TEMPERATURMENGENUMWERTER
                            - ZUSTANDSMENGENUMWERTER
                            - MESSDATENREGISTRIERGERAET
                            - WANDLER
                        geraetenummer:
                          type: string
                          description: >-
                            Die auf dem Geräte aufgedruckte Nummer, die vom MSB
                            vergeben wird. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z20.RFF+Z14
                      x-apidog-orders:
                        - geraetetyp
                        - geraetenummer
                      x-apidog-ignore-properties: []
                  gateway:
                    type: string
                    description: >-
                      Angabe eines SMGW, mit dem der Zaehler parametrisiert ist
                      | EDIFACT: SG4.IDE+24.SG8.SEQ+Z03.RFF+Z14
                  zaehlernummer:
                    type: string
                    description: >-
                      Die Nummer des zu sperrenden Zählers | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z03.SG10.CCI+++E13.CAV+Z30
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z03,
                      SG4.IDE+24.SG8.SEQ+Z20
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
                x-apidog-orders:
                  - gueltigkeitszeitraum
                  - zaehlwerke
                  - geraete
                  - gateway
                  - zaehlernummer
                  - datenqualitaet
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - AD_HOC_STEUERKANAL
            - MARKTLOKATION
            - ZAEHLER
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ipAdresse:
                  type: string
                  description: 'ipAdresse | EDIFACT: SG4.IDE+24.FTX+Z27'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                ipRange:
                  type: object
                  properties:
                    obereGrenze:
                      type: string
                      description: 'obereGrenze | EDIFACT: SG4.IDE+24.FTX+Z28'
                    untereGrenze:
                      type: string
                      description: 'untereGrenze | EDIFACT: SG4.IDE+24.FTX+Z28'
                  x-apidog-orders:
                    - obereGrenze
                    - untereGrenze
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ipAdresse
                - ansprechpartner
                - rollencodetyp
                - ipRange
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            nachrichtenReferenzBestellbestaetigung:
              type: string
              description: >-
                Referenznummer der Nachricht der betroffenen Antwort auf
                Bestellung 'Bestellbestätigung' / ORDERS RFF+Z42 | EDIFACT:
                SG4.IDE+24.SG6.RFF+Z42
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            vorgangsReferenzBestellbestaetigung:
              type: string
              description: >-
                Referenznummer des Vorgangs der betroffenen Antwort auf
                Bestellung 'Bestellbestätigung' / ORDERS RFF+Z43 | EDIFACT:
                SG4.IDE+24.SG6.RFF+Z43
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - nachrichtenReferenzBestellbestaetigung
            - pruefidentifikator
            - vorgangsReferenzBestellbestaetigung
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 55553 - MSB an weiterer MSB - Änderung vom MSB an weiteren MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55225:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  abrechnungsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        artikelId:
                          type: array
                          description: >-
                            ArtikelId gem. BDEW | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z71.PIA+Z02
                          items:
                            type: string
                        zahlerBlindarbeit:
                          type: string
                          title: ZahlerBlindarbeit
                          description: >-
                            ZahlerBlindarbeit | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z71.SG10.CCI+Z45.CAV+ZE4
                          enum:
                            - ANSCHLUSSNUTZER
                            - LIEFERANT
                            - NICHT_FESTGELEGT
                        artikelIdTyp:
                          type: string
                          title: ArtikelIdTyp
                          description: >-
                            Liste von Artikel-IDs, z.B. für standardisierte vom
                            BDEW herausgegebene Artikel, die im Strommarkt die
                            BDEW-Artikelnummer ablösen | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z71.PIA+Z02
                          enum:
                            - ARTIKELID
                            - GRUPPENARTIKELID
                        abrechnungBlindarbeit:
                          type: boolean
                          description: >-
                            abrechnungBlindarbeit | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z71.SG10.CCI+Z45
                      x-apidog-orders:
                        - artikelId
                        - zahlerBlindarbeit
                        - artikelIdTyp
                        - abrechnungBlindarbeit
                      x-apidog-ignore-properties: []
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18
                x-apidog-orders:
                  - abrechnungsdaten
                  - netzlokationsId
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: >-
                      zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53],
                      SG4.IDE+24.SG8.SEQ+Z71
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55225 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55218:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  verbrauchsaufteilung:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++E17.CAV+Z22'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++E17.CAV+Z22
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
                    x-apidog-orders:
                      - wert
                      - einheit
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - verbrauchsaufteilung
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  netznutzungsabrechnungsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        artikelIdTyp:
                          type: string
                          title: ArtikelIdTyp
                          description: >-
                            Liste von Artikel-IDs, z.B. für standardisierte vom
                            BDEW herausgegebene Artikel, die im Strommarkt die
                            BDEW-Artikelnummer ablösen | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z45|Z84].PIA+Z02
                          enum:
                            - ARTIKELID
                            - GRUPPENARTIKELID
                        zaehlzeiten:
                          type: object
                          properties:
                            register:
                              type: object
                              title: Zaehlzeitregister
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[Z45|Z84].SG10.CCI+Z38
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[Z45|Z84].SG10.CCI+Z39
                              properties:
                                boTyp:
                                  type: string
                                  title: BOTyp
                                  description: Typ des BO
                                  enum:
                                    - ZAEHLZEITDEFINITION
                                versionStruktur:
                                  type: string
                                  description: versionStruktur
                                  default: '1'
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - register
                            - zaehlzeitDefinition
                          x-apidog-ignore-properties: []
                        singulaereBetriebsmittel:
                          type: object
                          properties:
                            wert:
                              type: object
                              title: Schwellwert
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[Z45|Z84].SG9.QTY+Z33,
                                SG4.IDE+24.SG8.SEQ+[Z45|Z84].SG10.CCI+Z44+ZD8
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - wert
                          x-apidog-ignore-properties: []
                        artikelId:
                          type: array
                          description: >-
                            ArtikelId gem. BDEW | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z45|Z84].PIA+Z02
                          items:
                            type: string
                        gemeinderabatt:
                          type: object
                          title: Gemeinderabatt
                          description: >-
                            EDIFACT: SG4.IDE+24.SG8.SEQ+[Z45|Z84].SG9.QTY+Z16,
                            SG4.IDE+24.SG8.SEQ+[Z45|Z84].SG9.QTY
                          x-apidog-orders: []
                          properties: {}
                          x-apidog-ignore-properties: []
                        zuschlag:
                          type: object
                          title: Zuschlag
                          description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[Z45|Z84].SG9.QTY'
                          x-apidog-orders: []
                          properties: {}
                          x-apidog-ignore-properties: []
                        abschlag:
                          type: object
                          title: Abschlag
                          description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[Z45|Z84].SG9.QTY'
                          x-apidog-orders: []
                          properties: {}
                          x-apidog-ignore-properties: []
                        anzahl:
                          type: string
                          title: Registeranzahl
                          description: >-
                            Registeranzahl | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z45|Z84].SG9.QTY+Z38
                          enum:
                            - EINTARIF
                            - MEHRTARIF
                            - ZWEITARIF
                      x-apidog-orders:
                        - artikelIdTyp
                        - zaehlzeiten
                        - singulaereBetriebsmittel
                        - artikelId
                        - gemeinderabatt
                        - zuschlag
                        - abschlag
                        - anzahl
                      x-apidog-ignore-properties: []
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z50|Z51|Z52],
                      SG4.IDE+24.SG8.SEQ+[Z45|Z84]
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT:
                          SG4.IDE+24.SG6.RFF+[Z50|Z51|Z52],
                          SG4.IDE+24.SG8.SEQ+[Z45|Z84]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  netzbetreiberCodeNr:
                    type: string
                    description: >-
                      Codenummer des Netzbetreibers, an dessen Netz diese
                      Marktlokation

                      angeschlossen ist. | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[Z45|Z84].SG10.CCI+++ZB3.CAV+Z88
                x-apidog-orders:
                  - netznutzungsabrechnungsdaten
                  - marktlokationsId
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - netzbetreiberCodeNr
                x-apidog-ignore-properties: []
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragskonditionen:
                    type: object
                    properties:
                      naechstenetznutzungsabrechnung:
                        type: string
                        description: >-
                          naechstenetznutzungsabrechnung | EDIFACT:
                          SG4.IDE+24.SG6.RFF+[Z50|Z51|Z52].DTM+Z09
                      netznutzungsvertrag:
                        type: string
                        title: Netznutzungsvertrag
                        description: >-
                          Netznutzungsvertrag | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++Z88.CAV+Z74
                        enum:
                          - KUNDEN_NB
                          - LIEFERANTEN_NB
                      netznutzungsabrechnungIntervall:
                        type: integer
                        description: >-
                          netznutzungsabrechnungIntervall | EDIFACT:
                          SG4.IDE+24.SG6.RFF+[Z50|Z51|Z52].DTM+Z22
                      netznutzungszahler:
                        type: string
                        title: Netznutzungszahler
                        description: >-
                          Netznutzungszahler | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++Z88.CAV+Z73
                        enum:
                          - KUNDE
                          - LIEFERANT
                      netznutzungsabrechnungsgrundlage:
                        type: string
                        title: Netznutzungsabrechnungsgrundlage
                        description: >-
                          Netznutzungsabrechnungsgrundlage | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++Z88.CAV+ZA7
                        enum:
                          - LIEFERSCHEIN
                          - ABWEICHENDE_GRUNDLAGE
                      netznutzungsabrechnung:
                        type: object
                        properties:
                          abrechnungsZeitraum:
                            type: string
                            description: >-
                              abrechnungsZeitraum | EDIFACT:
                              SG4.IDE+24.SG6.RFF+[Z50|Z51|Z52].DTM+Z21
                        x-apidog-orders:
                          - abrechnungsZeitraum
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - naechstenetznutzungsabrechnung
                      - netznutzungsvertrag
                      - netznutzungsabrechnungIntervall
                      - netznutzungszahler
                      - netznutzungsabrechnungsgrundlage
                      - netznutzungsabrechnung
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragskonditionen
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: >-
                      zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53],
                      SG4.IDE+24.SG8.SEQ+Z01
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - BILANZIERUNG
            - MARKTLOKATION
            - NETZNUTZUNGSVERTRAG
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - vorgangsnummer
            - pruefidentifikator
            - transaktionsgrund
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55218 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55175:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - vorgangsnummer
            - pruefidentifikator
            - transaktionsgrund
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16,
                      SG4.IDE+24.SG5.LOC+Z22
                x-apidog-orders:
                  - marktlokationsId
                x-apidog-ignore-properties: []
            LOKATIONSBUENDEL:
              type: array
              items:
                type: object
                properties:
                  lokationsbuendelNummer:
                    type: integer
                    description: >-
                      lokationsbuendelNummer | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z78.RFF+[Z31|Z39]
                  lokationsbuendelstrukturId:
                    type: string
                    description: >-
                      lokationsbuendelstrukturId | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z78.RFF+[Z31|Z39]
                  standardisierteLokationsbuendelstruktur:
                    type: boolean
                    description: >-
                      standardisierteLokationsbuendelstruktur | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z78.RFF+[Z31|Z39]
                x-apidog-orders:
                  - lokationsbuendelNummer
                  - lokationsbuendelstrukturId
                  - standardisierteLokationsbuendelstruktur
                x-apidog-ignore-properties: []
              properties:
                zuordnungObjectcode:
                  type: array
                  items:
                    type: object
                    properties:
                      objectcode:
                        type: array
                        items:
                          type: object
                          properties:
                            lokationsbuendelNummer:
                              type: integer
                              description: >-
                                lokationsbuendelNummer | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z58.RFF+Z33
                            objectcode:
                              type: object
                              title: Objectcode
                              description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z58.RFF+Z33'
                              x-apidog-orders: []
                          x-apidog-orders:
                            - lokationsbuendelNummer
                            - objectcode
                      vorgelagerteLokationId:
                        type: string
                        description: >-
                          vorgelagerteLokationId | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z58.RFF+[Z34|Z35]
                      referenzMarktlokationTechnischeRessource:
                        type: array
                        items:
                          type: array
                          description: >-
                            referenzMarktlokationTechnischeRessource | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z58.RFF+Z16
                          items:
                            type: string
                      referenzLokationsTyp:
                        type: string
                        title: Lokationstyp
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z58.RFF+[Z32|Z18|Z19|Z37]'
                        enum:
                          - MALO
                          - MELO
                          - NELO
                          - TECHNISCHE_RESSOURCE
                      vorgelagerteLokationTyp:
                        type: string
                        title: Lokationstyp
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z58.RFF+[Z34|Z35]'
                        enum:
                          - MALO
                          - MELO
                          - NELO
                          - TECHNISCHE_RESSOURCE
                      referenzLokationsId:
                        type: string
                        description: >-
                          referenzLokationsId | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z58.RFF+[Z32|Z18|Z19|Z37]
                    x-apidog-orders:
                      - objectcode
                      - vorgelagerteLokationId
                      - referenzMarktlokationTechnischeRessource
                      - referenzLokationsTyp
                      - vorgelagerteLokationTyp
                      - referenzLokationsId
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18
                x-apidog-orders:
                  - netzlokationsId
                x-apidog-ignore-properties: []
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                x-apidog-orders:
                  - ressourcenId
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: >-
                      zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53],
                      SG4.IDE+24.SG8.SEQ+Z78, SG4.IDE+24.SG8.SEQ+Z58
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
            MESSLOKATION:
              type: array
              items:
                type: object
                properties:
                  messlokationsId:
                    type: string
                    description: >-
                      Die Messlokations-Identifikation. Das ist die frühere
                      Zählpunktbezeichnung,

                      z.B. DE 47108151234567 | EDIFACT: SG4.IDE+24.SG5.LOC+Z17
                x-apidog-orders:
                  - messlokationsId
                x-apidog-ignore-properties: []
            TECHNISCHE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z20'
                x-apidog-orders:
                  - ressourcenId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - LOKATIONSBUENDEL
            - NETZLOKATION
            - STEUERBARE_RESSOURCE
            - VERWENDUNGSZEITRAUM
            - MESSLOKATION
            - TECHNISCHE_RESSOURCE
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 55175 - NB an LF - Änderung vom NB an LF
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55126:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  lastprofile:
                    type: array
                    items:
                      type: object
                      properties:
                        profilschar:
                          type: string
                          description: >-
                            Profilschar des Profils | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+++Z12.CAV
                        bezeichnung:
                          type: string
                          description: >-
                            Externe Bezeichnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02.CAV,
                            SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+Z03.CAV
                        tagesparameter:
                          type: object
                          properties:
                            herausgeber:
                              type: string
                              title: Herausgeber
                              description: >-
                                Herausgeber | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+[ZA0|Z99]
                              enum:
                                - NB
                                - BDEW
                                - TUM
                            dienstanbieter:
                              type: string
                              description: >-
                                dienstanbieter | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+[ZA0|Z99]
                            klimazone:
                              type: string
                              description: >-
                                klimazone | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+[ZA0|Z99]
                            temperaturmessstelle:
                              type: string
                              description: >-
                                temperaturmessstelle | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+[ZA0|Z99]
                          x-apidog-orders:
                            - herausgeber
                            - dienstanbieter
                            - klimazone
                            - temperaturmessstelle
                          x-apidog-ignore-properties: []
                        profilart:
                          type: string
                          title: Profilart
                          description: >-
                            Profilart | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02,
                            SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+Z03
                          enum:
                            - ART_STANDARDLASTPROFIL
                            - ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL
                            - ART_LASTPROFIL
                        einspeisung:
                          type: boolean
                          description: >-
                            Kennzeichen Einspeisung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02,
                            SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+Z03
                        verfahren:
                          type: string
                          title: Profilverfahren
                          description: >-
                            Profilverfahren | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02,
                            SG4.IDE+24.SG8.SEQ+Z08.SG10.CCI+Z03
                          enum:
                            - SYNTHETISCH
                            - ANALYTISCH
                      x-apidog-orders:
                        - profilschar
                        - bezeichnung
                        - tagesparameter
                        - profilart
                        - einspeisung
                        - verfahren
                      x-apidog-ignore-properties: []
                  zeitreihentyp:
                    type: string
                    title: Zeitreihentyp
                    description: >-
                      Zeitreihentyp | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+15+Z21.CAV
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
                  temperaturarbeit:
                    type: object
                    properties:
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+[265|Z08]
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
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+[265|Z08]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - einheit
                      - wert
                    x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z21,
                          SG4.IDE+24.SG8.SEQ+Z08
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z21,
                      SG4.IDE+24.SG8.SEQ+Z08
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
                  prognosegrundlage:
                    type: string
                    title: Prognosegrundlage
                    description: >-
                      Prognosegrundlage | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI
                    enum:
                      - WERTE
                      - PROFILE
                  bilanzkreis:
                    type: object
                    title: Bilanzkreis
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z19'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  detailsPrognosegrundlage:
                    type: array
                    items:
                      type: array
                      description: >-
                        Prognosegrundlage - Besteht der Bedarf ein
                        tagesparameteräbhängiges Lastprofil mit gemeinsamer
                        Messung anzugeben, so ist dies über die 2 -malige
                        Wiederholung des CAV Segments mit der Angabe der Codes
                        E02 und E14 möglich. | EDIFACT:
                        SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI.CAV+[E02|E14]
                      items:
                        type: string
                        title: Profiltyp
                        description: Profiltyp
                        enum:
                          - SLP_SEP
                          - TLP_TEP
                          - TEP
                  aggregationsverantwortung:
                    type: string
                    title: Aggregationsverantwortung
                    description: >-
                      Aggregationsverantwortung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+6
                    enum:
                      - UENB
                      - VNB
                  jahresverbrauchsprognose:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+31'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+31
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
                    x-apidog-orders:
                      - wert
                      - einheit
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - lastprofile
                  - zeitreihentyp
                  - temperaturarbeit
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - prognosegrundlage
                  - bilanzkreis
                  - detailsPrognosegrundlage
                  - aggregationsverantwortung
                  - jahresverbrauchsprognose
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z90
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z90
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
                      x-apidog-orders:
                        - rollencodenummer
                        - marktrolle
                      x-apidog-ignore-properties: []
                  regelzone:
                    type: string
                    description: >-
                      für EDIFACT mapping | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z18
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01'
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  bilanzierungsgebiet:
                    type: string
                    description: >-
                      Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist -
                      im Falle eines Strom Netzes. | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z20
                x-apidog-orders:
                  - marktrollen
                  - regelzone
                  - marktlokationsId
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - bilanzierungsgebiet
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
                x-apidog-orders:
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - BILANZIERUNG
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - vorgangsnummer
            - pruefidentifikator
            - transaktionsgrund
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55126 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55038:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E02'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E02'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            vertragsbeginn:
              type: string
              description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
              format: date-time
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - vertragsbeginn
            - empfaenger
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                x-apidog-orders:
                  - marktlokationsId
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                x-apidog-orders:
                  - tranchenId
                x-apidog-ignore-properties: []
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsbeginn:
                    type: string
                    description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
                    format: date-time
                x-apidog-orders:
                  - vertragsbeginn
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - TRANCHE
            - NETZNUTZUNGSVERTRAG
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55038 - NB an LFZ - Aufhebung der Zuordnung des LFZ zur Marklokation
        bzw. Tranche
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55037:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            vertragsende:
              type: string
              description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
              format: date-time
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E02'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E02'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - vertragsende
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsende:
                    type: string
                    description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
                    format: date-time
                x-apidog-orders:
                  - vertragsende
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                x-apidog-orders:
                  - marktlokationsId
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                x-apidog-orders:
                  - tranchenId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZNUTZUNGSVERTRAG
            - MARKTLOKATION
            - TRANCHE
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 55037 - NB an LFA - Beendigung der Zuordnung des LFA zur Tranche
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55016:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsende:
                    type: string
                    description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
                    format: date-time
                x-apidog-orders:
                  - vertragsende
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                x-apidog-orders:
                  - marktlokationsId
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                x-apidog-orders:
                  - tranchenId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZNUTZUNGSVERTRAG
            - MARKTLOKATION
            - TRANCHE
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            vertragsende:
              type: string
              description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
              format: date-time
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E35'
            freitext:
              type: object
              properties:
                freitext2:
                  type: string
                  description: 'Freitext Zeile 2 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext4:
                  type: string
                  description: 'Freitext Zeile 4 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext1:
                  type: string
                  description: 'Freitext Zeile 1 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext5:
                  type: string
                  description: 'Freitext Zeile 5 | EDIFACT: SG4.IDE+24.FTX+ACB'
                freitext3:
                  type: string
                  description: 'Freitext Zeile 3 | EDIFACT: SG4.IDE+24.FTX+ACB'
              x-apidog-orders:
                - freitext2
                - freitext4
                - freitext1
                - freitext5
                - freitext3
              x-apidog-ignore-properties: []
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E35'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            endezumtermin:
              type: string
              description: 'Kündigungsdatum / DTM+471 | EDIFACT: SG4.IDE+24.DTM+471'
              format: date-time
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - vertragsende
            - dokumentennummer
            - freitext
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - endezumtermin
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 55016 - LFN an LFA - Kündigung
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55013:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            ENERGIELIEFERVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen

                            beispielsweise der Nachname dargestellt werden.
                            Beispiele: Yellow Strom GmbH

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z65
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z65
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z65'
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z65
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
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z65
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z65
                      x-apidog-orders:
                        - name1
                        - name3
                        - name4
                        - geschaeftspartnerrolle
                        - name2
                        - anrede
                      x-apidog-ignore-properties: []
                  korrespondenzpartner:
                    type: object
                    properties:
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z66
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                      partneradresse:
                        type: object
                        properties:
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z66
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
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z66
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z66'
                        x-apidog-orders:
                          - landescode
                          - ortsteil
                          - hausnummer
                          - ort
                          - postleitzahl
                          - strasse
                          - postfach
                        x-apidog-ignore-properties: []
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z66
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z66
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z66
                    x-apidog-orders:
                      - name3
                      - name4
                      - partneradresse
                      - name1
                      - anrede
                      - name2
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragspartner2
                  - korrespondenzpartner
                x-apidog-ignore-properties: []
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen

                            beispielsweise der Nachname dargestellt werden.
                            Beispiele: Yellow Strom GmbH

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z67
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z67
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z67
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
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z67
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z67'
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z67
                      x-apidog-orders:
                        - name1
                        - anrede
                        - geschaeftspartnerrolle
                        - name3
                        - name4
                        - name2
                      x-apidog-ignore-properties: []
                  vertragsende:
                    type: string
                    description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
                    format: date-time
                  korrespondenzpartner:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z68
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
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z68
                        x-apidog-orders:
                          - postfach
                          - ortsteil
                          - postleitzahl
                          - ort
                          - landescode
                          - strasse
                          - hausnummer
                        x-apidog-ignore-properties: []
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z68
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z68
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z68'
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z68
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z68
                    x-apidog-orders:
                      - partneradresse
                      - name2
                      - anrede
                      - name4
                      - name3
                      - name1
                    x-apidog-ignore-properties: []
                  vertragsbeginn:
                    type: string
                    description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
                    format: date-time
                x-apidog-orders:
                  - vertragspartner2
                  - vertragsende
                  - korrespondenzpartner
                  - vertragsbeginn
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG12.NAD+Z69,
                      SG4.IDE+24.SG12.NAD+Z70, SG4.IDE+24.SG12.NAD+Z63
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
                  hausverwalter:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z70
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
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z70
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
                        x-apidog-orders:
                          - ortsteil
                          - landescode
                          - strasse
                          - postfach
                          - postleitzahl
                          - hausnummer
                          - ort
                        x-apidog-ignore-properties: []
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z70
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z70'
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z70
                      gewerbekennzeichnung:
                        type: boolean
                        description: >-
                          Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
                          (gewerbeKennzeichnung = true)

                          oder eine Privatperson handelt. (gewerbeKennzeichnung
                          = false) | EDIFACT: SG4.IDE+24.SG12.NAD+Z70
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z70
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z70
                    x-apidog-orders:
                      - partneradresse
                      - name1
                      - name4
                      - anrede
                      - gewerbekennzeichnung
                      - name2
                      - name3
                    x-apidog-ignore-properties: []
                  lokationsadresse:
                    type: object
                    properties:
                      landescode:
                        type: string
                        title: Landescode
                        description: >-
                          Der ISO-Landescode als Enumeration | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z63
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
                      zusatzInformation:
                        type: object
                        properties:
                          zusatz4:
                            type: string
                            description: 'Adresszusatz 4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                          zusatz1:
                            type: string
                            description: 'Adresszusatz 1 | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                          zusatz2:
                            type: string
                            description: 'Adresszusatz 2 | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                          zusatz5:
                            type: string
                            description: 'Adresszusatz 5 | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                          zusatz3:
                            type: string
                            description: 'Adresszusatz 3 | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                        x-apidog-orders:
                          - zusatz4
                          - zusatz1
                          - zusatz2
                          - zusatz5
                          - zusatz3
                        x-apidog-ignore-properties: []
                      ortsteil:
                        type: string
                        description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                      postleitzahl:
                        type: string
                        description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                      strasse:
                        type: string
                        description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                      hausnummer:
                        type: string
                        description: >-
                          Hausnummer und Ergänzung | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z63
                      ort:
                        type: string
                        description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                      postfach:
                        type: string
                        description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z63'
                    x-apidog-orders:
                      - landescode
                      - zusatzInformation
                      - ortsteil
                      - postleitzahl
                      - strasse
                      - hausnummer
                      - ort
                      - postfach
                    x-apidog-ignore-properties: []
                  eigentuemer:
                    type: object
                    properties:
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z69
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z69
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z69
                      partneradresse:
                        type: object
                        properties:
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z69
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z69
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
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z69'
                        x-apidog-orders:
                          - strasse
                          - postfach
                          - ort
                          - postleitzahl
                          - hausnummer
                          - landescode
                          - ortsteil
                        x-apidog-ignore-properties: []
                      gewerbekennzeichnung:
                        type: boolean
                        description: >-
                          Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
                          (gewerbeKennzeichnung = true)

                          oder eine Privatperson handelt. (gewerbeKennzeichnung
                          = false) | EDIFACT: SG4.IDE+24.SG12.NAD+Z69
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z69
                    x-apidog-orders:
                      - name3
                      - name4
                      - name2
                      - name1
                      - partneradresse
                      - gewerbekennzeichnung
                      - anrede
                    x-apidog-ignore-properties: []
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
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
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
                      x-apidog-orders:
                        - messstellenbetreiberEigenschaft
                        - weiterverpflichtet
                        - marktrolle
                        - rollencodenummer
                      x-apidog-ignore-properties: []
                  sperrstatus:
                    type: string
                    title: Sperrstatus
                    description: 'Sperrstatus | EDIFACT: SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+Z42'
                    enum:
                      - ENTSPERRT
                      - GESPERRT
                  netzebene:
                    type: string
                    title: Netzebene
                    description: >-
                      Netzebene | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++E03.CAV
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
                x-apidog-orders:
                  - marktlokationsId
                  - datenqualitaet
                  - hausverwalter
                  - lokationsadresse
                  - eigentuemer
                  - marktrollen
                  - sperrstatus
                  - netzebene
                x-apidog-ignore-properties: []
            NETZLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZD7.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZD7.SG10.CCI+++ZB3.CAV+Z91
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZD7.SG10.CCI+++ZB3.CAV+Z91
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
                      x-apidog-orders:
                        - messstellenbetreiberEigenschaft
                        - rollencodenummer
                        - marktrolle
                      x-apidog-ignore-properties: []
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18,
                      SG4.IDE+24.SG8.SEQ+ZD7.RFF+Z32
                x-apidog-orders:
                  - marktrollen
                  - netzlokationsId
                x-apidog-ignore-properties: []
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: >-
                      ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19,
                      SG4.IDE+24.SG8.SEQ+ZF1.RFF+Z38
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF1.SG10.CCI+++ZB3.CAV+Z91
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
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF1.SG10.CCI+++ZB3.CAV+Z91
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF1.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                      x-apidog-orders:
                        - marktrolle
                        - rollencodenummer
                        - messstellenbetreiberEigenschaft
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - ressourcenId
                  - marktrollen
                x-apidog-ignore-properties: []
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  prognosegrundlage:
                    type: string
                    title: Prognosegrundlage
                    description: >-
                      Prognosegrundlage | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI
                    enum:
                      - WERTE
                      - PROFILE
                  temperaturarbeit:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z98.SG9.QTY+[265|Z08]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z98.SG9.QTY+[265|Z08]
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
                    x-apidog-orders:
                      - wert
                      - einheit
                    x-apidog-ignore-properties: []
                  jahresverbrauchsprognose:
                    type: object
                    properties:
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z98.SG9.QTY+31
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
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z98.SG9.QTY+31'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - einheit
                      - wert
                    x-apidog-ignore-properties: []
                  detailsPrognosegrundlage:
                    type: array
                    items:
                      type: array
                      description: >-
                        Prognosegrundlage - Besteht der Bedarf ein
                        tagesparameteräbhängiges Lastprofil mit gemeinsamer
                        Messung anzugeben, so ist dies über die 2 -malige
                        Wiederholung des CAV Segments mit der Angabe der Codes
                        E02 und E14 möglich. | EDIFACT:
                        SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI.CAV+[E02|E14]
                      items:
                        type: string
                        title: Profiltyp
                        description: Profiltyp
                        enum:
                          - SLP_SEP
                          - TLP_TEP
                          - TEP
                x-apidog-orders:
                  - prognosegrundlage
                  - temperaturarbeit
                  - jahresverbrauchsprognose
                  - detailsPrognosegrundlage
                x-apidog-ignore-properties: []
            MESSLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+ZF0
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+ZF3.SG10.CCI+++ZB3.CAV+ZF0
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
                      x-apidog-orders:
                        - weiterverpflichtet
                        - messstellenbetreiberEigenschaft
                        - rollencodenummer
                        - marktrolle
                      x-apidog-ignore-properties: []
                  messlokationsId:
                    type: string
                    description: >-
                      Die Messlokations-Identifikation. Das ist die frühere
                      Zählpunktbezeichnung,

                      z.B. DE 47108151234567 | EDIFACT: SG4.IDE+24.SG5.LOC+Z17,
                      SG4.IDE+24.SG8.SEQ+ZF3.RFF+Z19
                x-apidog-orders:
                  - marktrollen
                  - messlokationsId
                x-apidog-ignore-properties: []
            TECHNISCHE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z20'
                x-apidog-orders:
                  - ressourcenId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - ENERGIELIEFERVERTRAG
            - NETZNUTZUNGSVERTRAG
            - MARKTLOKATION
            - NETZLOKATION
            - STEUERBARE_RESSOURCE
            - BILANZIERUNG
            - MESSLOKATION
            - TECHNISCHE_RESSOURCE
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            vertragsende:
              type: string
              description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
              format: date-time
            transaktionsgrundergaenzungBefristeteAnmeldung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund bei befristeten An-/Abmeldungen
                / UTILMD STS+7++E01+ZW4+### | EDIFACT: SG4.IDE+24.STS+7
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E01|Z89]'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                  x-apidog-orders:
                    - eMailAdresse
                    - nachname
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E01|Z89]
            vertragsbeginn:
              type: string
              description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
              format: date-time
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - vertragsende
            - transaktionsgrundergaenzungBefristeteAnmeldung
            - empfaenger
            - anfragereferenznummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - transaktionsgrund
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - dokumentennummer
            - vertragsbeginn
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55013 - NB an LF (Notz "entspricht E/G") - Zuordnung des E/G zur
        Marktlokation aufgrund fehlender Antwort
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55010:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            ENERGIELIEFERVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        name1:
                          type: string
                          description: >-
                            Erster Teil des Namens. Hier kann der Firmenname
                            oder bei Privatpersonen

                            beispielsweise der Nachname dargestellt werden.
                            Beispiele: Yellow Strom GmbH

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z09
                        name3:
                          type: string
                          description: >-
                            Dritter Teil des Namens. Hier können weitere
                            Ergänzungen zum Firmennamen oder

                            bei Privatpersonen Zusätze zum Namen dargestellt
                            werden. Beispiele: und Afrika

                            oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z09
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
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
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z09'
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z09
                      x-apidog-orders:
                        - name1
                        - name3
                        - anrede
                        - geschaeftspartnerrolle
                        - name4
                        - name2
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragspartner2
                x-apidog-ignore-properties: []
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsende:
                    type: string
                    description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
                    format: date-time
                x-apidog-orders:
                  - vertragsende
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16,
                      SG4.IDE+24.SG5.LOC+Z22
                  marktlokationsTyp:
                    type: array
                    items:
                      type: object
                      properties:
                        typ:
                          type: string
                          title: AbschlagTyp
                          description: >-
                            AbschlagTyp | EDIFACT: SG4.IDE+24.SG5.LOC+Z16,
                            SG4.IDE+24.SG5.LOC+Z22
                          enum:
                            - GEMEINDERABATT_KAV
                            - ANPASSUNG_P19_STROM_NEV
                      x-apidog-orders:
                        - typ
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - marktlokationsId
                  - marktlokationsTyp
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                x-apidog-orders:
                  - tranchenId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - ENERGIELIEFERVERTRAG
            - NETZNUTZUNGSVERTRAG
            - MARKTLOKATION
            - TRANCHE
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            vertragsende:
              type: string
              description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
              format: date-time
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E02'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E02'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            annahmedatum:
              type: string
              description: >-
                Annahmedatum eines Dokument / DTM+154 | EDIFACT:
                SG4.IDE+24.DTM+154
              format: date-time
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - vertragsende
            - dokumentennummer
            - kategorie
            - absender
            - annahmedatum
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55010 - NB an LFA - Anfrage zur Beendigung der Zuordnung des LFA zur
        Marktlokation bzw. Tranche
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55007:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            vertragsende:
              type: string
              description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
              format: date-time
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E02|Z90]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E02|Z90]'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - vertragsende
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsende:
                    type: string
                    description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
                    format: date-time
                x-apidog-orders:
                  - vertragsende
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16,
                      SG4.IDE+24.SG5.LOC+Z22
                  marktlokationsTyp:
                    type: array
                    items:
                      type: object
                      properties:
                        typ:
                          type: string
                          title: AbschlagTyp
                          description: >-
                            AbschlagTyp | EDIFACT: SG4.IDE+24.SG5.LOC+Z16,
                            SG4.IDE+24.SG5.LOC+Z22
                          enum:
                            - GEMEINDERABATT_KAV
                            - ANPASSUNG_P19_STROM_NEV
                      x-apidog-orders:
                        - typ
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - marktlokationsId
                  - marktlokationsTyp
                x-apidog-ignore-properties: []
            TRANCHE:
              type: array
              items:
                type: object
                properties:
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                x-apidog-orders:
                  - tranchenId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZNUTZUNGSVERTRAG
            - MARKTLOKATION
            - TRANCHE
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55007 - NB an LF - Beendigung der Zuordnung des LF zur Marktlokation
        bzw. Tranche aufgrund fehlender Antwort
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55691:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  paketId:
                    type: string
                    description: 'paketId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z67'
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01'
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
                x-apidog-orders:
                  - paketId
                  - marktlokationsId
                  - datenqualitaet
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                x-apidog-orders:
                  - datenqualitaet
                  - verwendungAb
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E03'
              enum:
                - PROZESSDATENBERICHT
                - GERAETEUEBERNAHME
                - WEITERVERPFLICHTUNG_BETRIEB_MELO
                - AENDERUNG_MELO
                - STAMMDATEN_MALO_ODER_MELO
                - BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
                - ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
                - ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
                - ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
                - AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
                - AENDERUNG_GERAETEKONFIGURATION
                - REKLAMATION_VON_WERTEN
                - LASTGANG_MALO_TRANCHE
                - SPERRUNG
                - ENTSPERRUNG
                - REKLAMATION_ZAEHLZEITDEFINITION
                - ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
                - GERAETEWECHSELABSICHT
                - AENDERUNG_KONZESSIONSABGABE
                - AENDERUNG_ZAEHLZEITDEFINITION
                - UEBERMITTLUNG_WERTE_AN_ESA
                - AENDERUNG
                - BILANZKREISZUORDNUNGSLISTE
                - CLEARINGLISTE
                - NORMIERTES_PROFIL_PROFILSCHAR
                - REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
                - REKLAMATION_PROFIL_PROFILSCHAR
                - STAMMDATEN_MALO
                - STAMMDATEN_MELO
                - STAMMDATEN_TRANCHE
                - BEENDIGUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINER_KONFIGURATION
                - BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
                - REKLAMATION_EINER_KONFIGURATION
                - >-
                  BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
                - AENDERUNG_DER_TECHNIK_DER_LOKATION
                - AENDERUNG_INDIVIDUELLER_KONFIGURATION
                - BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
                - EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
                - REKLAMATION_DEFINITION
            absender:
              type: object
              properties:
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: object
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                    x-apidog-orders:
                      - rufnummer
                      - nummerntyp
                    x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                ansprechpartner:
                  type: object
                  properties:
                    nachname:
                      type: string
                      description: >-
                        Nachname (Familienname) des Ansprechpartners | EDIFACT:
                        SG2.NAD+MS.SG3.CTA
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
            empfaenger:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            beteiligterMarktpartner:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: >-
                    Gibt die Codenummer der Marktrolle an. | EDIFACT:
                    SG4.IDE+24.SG12.NAD+VY
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG4.IDE+24.SG12.NAD+VY'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - beteiligterMarktpartner
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55691 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
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
