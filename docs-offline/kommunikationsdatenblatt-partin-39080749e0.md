# Kommunikationsdatenblatt PARTIN

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
      summary: Kommunikationsdatenblatt PARTIN
      deprecated: false
      description: Prozess zum Versand des Kommunikationsdatenblattes
      operationId: START_PARTIN
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht LF
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BLF%5D%20START_PARTIN'
            examples:
              '1':
                value:
                  stammdaten:
                    KOMMUNIKATIONSDATEN:
                      - boTyp: KOMMUNIKATIONSDATEN
                        versionStruktur: '1'
                        gueltigkeit: '2024-06-30T22:00:00Z'
                        kommunikationsDatenBlattInaktiv: true
                  transaktionsdaten:
                    absender:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      gewerbekennzeichnung: true
                      rollencodenummer: '9903790000002'
                      rollencodetyp: BDEW
                      ansprechpartner:
                        boTyp: ANSPRECHPARTNER
                        versionStruktur: '1'
                        nachname: Max Mustermann
                        rufnummern:
                          - nummerntyp: RUF_DURCHWAHL
                            rufnummer: '+49322227120'
                    empfaenger:
                      boTyp: MARKTTEILNEHMER
                      versionStruktur: '1'
                      gewerbekennzeichnung: true
                      rollencodenummer: '9900321000005'
                      rollencodetyp: BDEW
                    anwendungsreferenznummer: '1'
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_PARTIN
                summary: Datenblatt inaktiv
              '2':
                value:
                  businessKey: <businessKey>
                  processDate: null
                  dataSource: INBOUND
                  version: 1
                  edifactVersion: 202610
                  data:
                    stammdaten:
                      KOMMUNIKATIONSDATEN:
                        - boTyp: KOMMUNIKATIONSDATEN
                          versionStruktur: '1'
                          gueltigkeit: '2025-06-30T22:00:00Z'
                          marktteilnehmer:
                            boTyp: MARKTTEILNEHMER
                            versionStruktur: '1'
                            marktrolle: LF
                            bankverbindung:
                              - iban: DE00000000000000000000
                                kontoinhaber: Unternehmens GmbH
                                bic: BICXXXXXXXX
                                kreditinstitut: Bankname
                            erreichbarkeit:
                              - verfuegbarkeit: MONTAG
                                zeit: 08:00-17:00
                              - verfuegbarkeit: DIENSTAG
                                zeit: 08:00-17:00
                              - verfuegbarkeit: MITTWOCH
                                zeit: 08:00-17:00
                              - verfuegbarkeit: DONNERSTAG
                                zeit: 08:00-17:00
                              - verfuegbarkeit: FREITAG
                                zeit: 08:00-17:00
                              - verfuegbarkeit: PAUSE
                                zeit: 12:00-13:00
                            name1: Lieferant
                            gewerbekennzeichnung: true
                            hrnummer: '331079'
                            amtsgericht: 'Amtsgericht Mannheim:'
                            umsatzsteuerId: DE814905955
                            website: www.lieferant.de
                            faxnummer: '+012345678910'
                            partneradresse:
                              postleitzahl: '56789'
                              ort: Lieferantenort
                              strasse: Lieferantenstr
                              hausnummer: '1'
                              landescode: DE
                          kommunikationsangaben:
                            - boTyp: MARKTTEILNEHMER
                              versionStruktur: '1'
                              name1: Lieferant
                              gewerbekennzeichnung: true
                              partneradresse:
                                postleitzahl: '56789'
                                ort: Lieferantenort
                                strasse: Lieferantenstr
                                hausnummer: '1'
                                landescode: DE
                              kommunikationsrolle: DATENAUSTAUSCH
                              ansprechpartner:
                                boTyp: ANSPRECHPARTNER
                                versionStruktur: '1'
                                nachname: Mustermann
                                eMailAdresse: mustermann@max.de
                                rufnummern:
                                  - nummerntyp: RUF_DURCHWAHL
                                    rufnummer: '+01234567890'
                            - boTyp: MARKTTEILNEHMER
                              versionStruktur: '1'
                              name1: Lieferant
                              gewerbekennzeichnung: true
                              partneradresse:
                                postleitzahl: '12345'
                                ort: Lieferantenort
                                strasse: Lieferantenstr
                                landescode: DE
                              kommunikationsrolle: RAHMENVERTRAEGE
                              ansprechpartner:
                                boTyp: ANSPRECHPARTNER
                                versionStruktur: '1'
                                nachname: Mustermann
                                eMailAdresse: mustermann@max.de
                                rufnummern:
                                  - nummerntyp: RUF_DURCHWAHL
                                    rufnummer: '+012345678910'
                            - boTyp: MARKTTEILNEHMER
                              versionStruktur: '1'
                              name1: Lieferant
                              gewerbekennzeichnung: true
                              partneradresse:
                                postleitzahl: '12345'
                                ort: Lieferantenort
                                strasse: Lieferantenstr
                                hausnummer: '1'
                                landescode: DE
                              kommunikationsrolle: KUENDIGUNGSPROZESSE
                              ansprechpartner:
                                boTyp: ANSPRECHPARTNER
                                versionStruktur: '1'
                                nachname: Mustermann
                                eMailAdresse: mustermann@max.de
                                rufnummern:
                                  - nummerntyp: RUF_DURCHWAHL
                                    rufnummer: '+012345678910'
                            - boTyp: MARKTTEILNEHMER
                              versionStruktur: '1'
                              name1: Lieferant
                              gewerbekennzeichnung: true
                              partneradresse:
                                postleitzahl: '12345'
                                ort: Lieferantenort
                                strasse: Lieferantenstr
                                hausnummer: '1'
                                landescode: DE
                              kommunikationsrolle: WECHSELPROZESSE
                              ansprechpartner:
                                boTyp: ANSPRECHPARTNER
                                versionStruktur: '1'
                                nachname: Mustermann
                                eMailAdresse: mustermann@max.de
                                rufnummern:
                                  - nummerntyp: RUF_DURCHWAHL
                                    rufnummer: '+012345678910'
                            - boTyp: MARKTTEILNEHMER
                              versionStruktur: '1'
                              name1: Lieferant
                              gewerbekennzeichnung: true
                              partneradresse:
                                postleitzahl: '12345'
                                ort: Lieferantenort
                                strasse: Lieferantenstr
                                hausnummer: '1'
                                landescode: DE
                              kommunikationsrolle: STAMMDATENPROZESSE
                              ansprechpartner:
                                boTyp: ANSPRECHPARTNER
                                versionStruktur: '1'
                                nachname: Mustermann
                                eMailAdresse: mustermann@max.de
                                rufnummern:
                                  - nummerntyp: RUF_DURCHWAHL
                                    rufnummer: '+012345678910'
                            - boTyp: MARKTTEILNEHMER
                              versionStruktur: '1'
                              name1: Lieferant
                              gewerbekennzeichnung: true
                              partneradresse:
                                postleitzahl: '12345'
                                ort: Lieferantenort
                                strasse: Lieferantenstr
                                hausnummer: '1'
                                landescode: DE
                              kommunikationsrolle: EINSPEISEPROZESSE
                              ansprechpartner:
                                boTyp: ANSPRECHPARTNER
                                versionStruktur: '1'
                                nachname: Mustermann
                                eMailAdresse: mustermann@max.de
                                rufnummern:
                                  - nummerntyp: RUF_DURCHWAHL
                                    rufnummer: '+012345678910'
                            - boTyp: MARKTTEILNEHMER
                              versionStruktur: '1'
                              name1: Lieferant
                              gewerbekennzeichnung: true
                              partneradresse:
                                postleitzahl: '12345'
                                ort: Lieferantenort
                                strasse: Lieferantenstr
                                hausnummer: '1'
                                landescode: DE
                              kommunikationsrolle: ABRECHNUNGSPROZESSE
                              ansprechpartner:
                                boTyp: ANSPRECHPARTNER
                                versionStruktur: '1'
                                nachname: Mustermann
                                eMailAdresse: mustermann@max.de
                                rufnummern:
                                  - nummerntyp: RUF_DURCHWAHL
                                    rufnummer: '+012345678910'
                            - boTyp: MARKTTEILNEHMER
                              versionStruktur: '1'
                              name1: Lieferant
                              gewerbekennzeichnung: true
                              partneradresse:
                                postleitzahl: '12345'
                                ort: Lieferantenort
                                strasse: Lieferantenstr
                                hausnummer: '1'
                                landescode: DE
                              kommunikationsrolle: MMMA_PROZESSE
                              ansprechpartner:
                                boTyp: ANSPRECHPARTNER
                                versionStruktur: '1'
                                nachname: Mustermann
                                eMailAdresse: mustermann@max.de
                                rufnummern:
                                  - nummerntyp: RUF_DURCHWAHL
                                    rufnummer: '+012345678910'
                            - boTyp: MARKTTEILNEHMER
                              versionStruktur: '1'
                              name1: Lieferant
                              gewerbekennzeichnung: true
                              partneradresse:
                                postleitzahl: '12345'
                                ort: Lieferantenort
                                strasse: Lieferantenstr
                                hausnummer: '1'
                                landescode: DE
                              kommunikationsrolle: BEWEGUNGSDATEN
                              ansprechpartner:
                                boTyp: ANSPRECHPARTNER
                                versionStruktur: '1'
                                nachname: Mustermann
                                eMailAdresse: mustermann@max.de
                                rufnummern:
                                  - nummerntyp: RUF_DURCHWAHL
                                    rufnummer: '+012345678910'
                            - boTyp: MARKTTEILNEHMER
                              versionStruktur: '1'
                              name1: Lieferant
                              gewerbekennzeichnung: true
                              partneradresse:
                                postleitzahl: '12345'
                                ort: Lieferantenort
                                strasse: Lieferantenstr
                                hausnummer: '1'
                                landescode: DE
                              kommunikationsrolle: ENT_SPERR_PROZESSE
                              ansprechpartner:
                                boTyp: ANSPRECHPARTNER
                                versionStruktur: '1'
                                nachname: Mustermann
                                eMailAdresse: mustermann@max.de
                                rufnummern:
                                  - nummerntyp: RUF_DURCHWAHL
                                    rufnummer: '+012345678910'
                            - boTyp: MARKTTEILNEHMER
                              versionStruktur: '1'
                              name1: Lieferant
                              gewerbekennzeichnung: true
                              partneradresse:
                                postleitzahl: '12345'
                                ort: Lieferantenort
                                strasse: Lieferantenstr
                                landescode: DE
                              kommunikationsrolle: BILANZIERUNGSPROZESSE
                              ansprechpartner:
                                boTyp: ANSPRECHPARTNER
                                versionStruktur: '1'
                                nachname: Mustermann
                                eMailAdresse: mustermann@max.de
                                rufnummern:
                                  - nummerntyp: RUF_DURCHWAHL
                                    rufnummer: '+012345678910'
                    transaktionsdaten:
                      sparte: STROM
                      pruefidentifikator: '37000'
                      absender:
                        boTyp: MARKTTEILNEHMER
                        versionStruktur: '1'
                        gewerbekennzeichnung: true
                        rollencodenummer: '9903790000002'
                        rollencodetyp: BDEW
                      empfaenger:
                        boTyp: MARKTTEILNEHMER
                        versionStruktur: '1'
                        gewerbekennzeichnung: true
                        rollencodenummer: '4400321000005'
                        rollencodetyp: GLN
                      kategorie: '10'
                      vorgangsreferenznummer: '1'
                      anwendungsreferenznummer: '2'
                    zusatzdaten: {}
                summary: Datenblatt Aktiv
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-39080749-run
components:
  schemas:
    '[LF] START_PARTIN':
      allOf:
        - type: object
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
                        <TipInfo>SG2.NAD+MS</TipInfo>
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
                        <TipInfo>SG2.NAD+MS</TipInfo>
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
                empfaenger:
                  type: object
                  properties:
                    rollencodetyp:
                      type: string
                      title: Rollencodetyp
                      description: |-
                        Rollencodetyp | 
                        <TipInfo>SG2.NAD+MR</TipInfo>
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
                        <TipInfo>SG2.NAD+MR</TipInfo>
                  x-apidog-orders:
                    - rollencodetyp
                    - rollencodenummer
                  x-apidog-ignore-properties: []
                anwendungsreferenznummer:
                  type: string
                  description: |-
                    Anwendungsreferenznummer / RFF+AGK | 
                    <TipInfo>SG1.RFF+AGK</TipInfo>
                kategorie:
                  type: string
                  title: Anfragekategorie
                  description: |-
                    Anfragekategorie | 
                    <TipInfo>BGM+10</TipInfo>
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
              x-apidog-orders:
                - absender
                - empfaenger
                - anwendungsreferenznummer
                - kategorie
              required:
                - absender
                - empfaenger
                - anwendungsreferenznummer
                - kategorie
              x-apidog-ignore-properties: []
            stammdaten:
              type: object
              properties:
                KOMMUNIKATIONSDATEN:
                  type: array
                  items:
                    type: object
                    properties:
                      marktteilnehmer:
                        type: object
                        properties:
                          hrnummer:
                            type: string
                            description: |-
                              Handelsregisternummer des Geschäftspartners | 
                              <TipInfo>SG4.NAD.FTX+Z15</TipInfo>
                          partneradresse:
                            type: object
                            properties:
                              strasse:
                                type: string
                                description: |-
                                  Strasse | 
                                  <TipInfo>SG4.NAD</TipInfo>
                              hausnummer:
                                type: string
                                description: |-
                                  Hausnummer und Ergänzung | 
                                  <TipInfo>SG4.NAD</TipInfo>
                              ortsteil:
                                type: string
                                description: |-
                                  Ortsteil | 
                                  <TipInfo>SG4.NAD</TipInfo>
                              postfach:
                                type: string
                                description: |-
                                  Postfach | 
                                  <TipInfo>SG4.NAD</TipInfo>
                              landescode:
                                type: string
                                title: Landescode
                                description: |-
                                  Der ISO-Landescode als Enumeration | 
                                  <TipInfo>SG4.NAD</TipInfo>
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
                              postleitzahl:
                                type: string
                                description: |-
                                  Postleitzahl | 
                                  <TipInfo>SG4.NAD</TipInfo>
                              ort:
                                type: object
                                title: Sort
                                description: |-

                                  <TipInfo>SG4.NAD</TipInfo>
                                x-apidog-orders: []
                                properties: {}
                                x-apidog-ignore-properties: []
                            x-apidog-orders:
                              - strasse
                              - hausnummer
                              - ortsteil
                              - postfach
                              - landescode
                              - postleitzahl
                              - ort
                            x-apidog-ignore-properties: []
                          name3:
                            type: string
                            description: >-
                              Dritter Teil des Namens. Hier können weitere
                              Ergänzungen zum Firmennamen oder bei
                              Privatpersonen Zusätze zum  Namen dargestellt
                              werden. Beispiele: und Afrika oder Sängerin | 

                              <TipInfo>SG4.NAD</TipInfo>
                          name4:
                            type: string
                            description: |-
                              Name 4 | 
                              <TipInfo>SG4.NAD</TipInfo>
                          faxnummer:
                            type: string
                            description: |-
                              Faxnummer des Unternehmens
                              RFF Z25
                              PI 37000 37001 37002 37005 37004 37003 37006 | 
                              <TipInfo>SG4.NAD.SG6.RFF+Z25</TipInfo>
                          anrede:
                            type: string
                            description: >-
                              Die Anrede für den GePa, Z.B. Herr.

                              Z04 Korrespondenzanschrift des Kunden des
                              Lieferanten

                              PI 55001 55600 55601 55013 55014 55043 55168 55169
                              | 

                              <TipInfo>SG4.NAD</TipInfo>
                          umsatzsteuerId:
                            type: string
                            description: >-
                              Die Umsatzsteuer-ID des Geschäftspartners.
                              Beispiel: DE 813281825 | 

                              <TipInfo>SG4.NAD.SG6.RFF+[VA|FC]</TipInfo>
                          erreichbarkeit:
                            type: array
                            items:
                              type: object
                              properties:
                                zeit:
                                  type: object
                                  title: Schaltzeit
                                  description: |-

                                    <TipInfo>SG4.NAD.SG12.CCI+Z40.DTM</TipInfo>
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                                verfuegbarkeit:
                                  type: string
                                  title: Verfuegbarkeit
                                  description: |-
                                    Verfuegbarkeit | 
                                    <TipInfo>SG4.NAD.SG12.CCI+Z40.DTM</TipInfo>
                                  enum:
                                    - MONTAG
                                    - DIENSTAG
                                    - MITTWOCH
                                    - DONNERSTAG
                                    - FREITAG
                                    - PAUSE
                                  x-apidog-folder: Bo4e/ENUM
                              x-apidog-orders:
                                - zeit
                                - verfuegbarkeit
                              x-apidog-ignore-properties: []
                          gewerbekennzeichnung:
                            type: boolean
                            description: >-
                              Kennzeichnung ob es sich um einen
                              Gewerbe/Unternehmen (gewerbeKennzeichnung = true)

                              oder eine Privatperson handelt.
                              (gewerbeKennzeichnung = false)

                              Z01 Struktur von Personennamen

                              Z02 Struktur der Firmenbezeichnung | 

                              <TipInfo>SG4.NAD</TipInfo>
                          website:
                            type: string
                            description: >-
                              Internetseite des Marktpartners. Beispiel:
                              www.mp-energie.de | 

                              <TipInfo>SG4.NAD.FTX+Z13</TipInfo>
                          bankverbindung:
                            type: array
                            items:
                              type: object
                              properties:
                                kreditinstitut:
                                  type: string
                                  description: |-
                                    Name des Kreditinstitut | 
                                    <TipInfo>SG4.NAD.FII+BK</TipInfo>
                                bic:
                                  type: string
                                  description: |-
                                    BIC Code | 
                                    <TipInfo>SG4.NAD.FII+BK</TipInfo>
                                kontoinhaber:
                                  type: string
                                  description: |-
                                    Der Kontoinhaber | 
                                    <TipInfo>SG4.NAD.FII+BK</TipInfo>
                                iban:
                                  type: string
                                  description: |-
                                    IBAN | 
                                    <TipInfo>SG4.NAD.FII+BK</TipInfo>
                              x-apidog-orders:
                                - kreditinstitut
                                - bic
                                - kontoinhaber
                                - iban
                              x-apidog-ignore-properties: []
                          marktrolle:
                            type: string
                            title: Marktrolle
                            description: |-
                              Diese Rollen kann ein Marktteilnehmer einnehmen | 
                              <TipInfo>SG4.NAD</TipInfo>
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
                            x-apidog-folder: Bo4e/ENUM
                          amtsgericht:
                            type: string
                            description: >-
                              Amtsgericht bzw Handelsregistergericht, das die
                              Handelsregisternummer herausgegeben hat | 

                              <TipInfo>SG4.NAD.FTX+Z15</TipInfo>
                          steuernummer:
                            type: string
                            description: |-
                              Steuernummer
                              RFF FC
                              PI 37000 37001 37002 37005 37004 37003 37006 | 
                              <TipInfo>SG4.NAD.SG6.RFF+[VA|FC]</TipInfo>
                          name2:
                            type: string
                            description: >-
                              Zweiter Teil des Namens. Hier kann der eine
                              Erweiterung zum Firmennamen oder bei
                              Privatpersonen beispielsweise der Vorname
                              dargestellt werden. Beispiele: Bereich Süd oder
                              Nina | 

                              <TipInfo>SG4.NAD</TipInfo>
                          name1:
                            type: string
                            description: >-
                              Erster Teil des Namens. Hier kann der Firmenname
                              oder bei Privatpersonen beispielsweise der
                              Nachname dargestellt werden. Beispiele: Yellow
                              Strom GmbH oder Hagen | 

                              <TipInfo>SG4.NAD</TipInfo>
                        x-apidog-orders:
                          - hrnummer
                          - partneradresse
                          - name3
                          - name4
                          - faxnummer
                          - anrede
                          - umsatzsteuerId
                          - erreichbarkeit
                          - gewerbekennzeichnung
                          - website
                          - bankverbindung
                          - marktrolle
                          - amtsgericht
                          - steuernummer
                          - name2
                          - name1
                        x-apidog-ignore-properties: []
                      kommunikationsangaben:
                        type: array
                        items:
                          type: object
                          properties:
                            ansprechpartner:
                              type: object
                              properties:
                                nachname:
                                  type: string
                                  description: >-
                                    Nachname (Familienname) des Ansprechpartners
                                    | 

                                    <TipInfo>SG4.NAD+Z10.SG7.CTA+IC,
                                    SG4.NAD+Z11.SG7.CTA+IC,
                                    SG4.NAD+Z12.SG7.CTA+IC,
                                    SG4.NAD+Z13.SG7.CTA+IC,
                                    SG4.NAD+Z14.SG7.CTA+IC,
                                    SG4.NAD+Z16.SG7.CTA+IC,
                                    SG4.NAD+Z17.SG7.CTA+IC,
                                    SG4.NAD+Z18.SG7.CTA+IC,
                                    SG4.NAD+Z19.SG7.CTA+IC,
                                    SG4.NAD+Z20.SG7.CTA+IC,
                                    SG4.NAD+Z21.SG7.CTA+IC</TipInfo>
                                rufnummern:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      nummerntyp:
                                        type: string
                                        title: Rufnummernart
                                        description: >-

                                          <TipInfo>SG4.NAD+Z10.SG7.CTA+IC.COM,
                                          SG4.NAD+Z11.SG7.CTA+IC.COM,
                                          SG4.NAD+Z12.SG7.CTA+IC.COM,
                                          SG4.NAD+Z13.SG7.CTA+IC.COM,
                                          SG4.NAD+Z14.SG7.CTA+IC.COM,
                                          SG4.NAD+Z16.SG7.CTA+IC.COM,
                                          SG4.NAD+Z17.SG7.CTA+IC.COM,
                                          SG4.NAD+Z18.SG7.CTA+IC.COM,
                                          SG4.NAD+Z19.SG7.CTA+IC.COM,
                                          SG4.NAD+Z20.SG7.CTA+IC.COM,
                                          SG4.NAD+Z21.SG7.CTA+IC.COM</TipInfo>
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
                                      rufnummer:
                                        type: object
                                        title: Rufnummer
                                        description: >-

                                          <TipInfo>SG4.NAD+Z10.SG7.CTA+IC.COM,
                                          SG4.NAD+Z11.SG7.CTA+IC.COM,
                                          SG4.NAD+Z12.SG7.CTA+IC.COM,
                                          SG4.NAD+Z13.SG7.CTA+IC.COM,
                                          SG4.NAD+Z14.SG7.CTA+IC.COM,
                                          SG4.NAD+Z16.SG7.CTA+IC.COM,
                                          SG4.NAD+Z17.SG7.CTA+IC.COM,
                                          SG4.NAD+Z18.SG7.CTA+IC.COM,
                                          SG4.NAD+Z19.SG7.CTA+IC.COM,
                                          SG4.NAD+Z20.SG7.CTA+IC.COM,
                                          SG4.NAD+Z21.SG7.CTA+IC.COM</TipInfo>
                                        x-apidog-orders: []
                                        properties: {}
                                        x-apidog-ignore-properties: []
                                    x-apidog-orders:
                                      - nummerntyp
                                      - rufnummer
                                    x-apidog-ignore-properties: []
                                eMailAdresse:
                                  type: string
                                  description: >-
                                    E-Mail Adresse | 

                                    <TipInfo>SG4.NAD+Z10.SG7.CTA+IC.COM,
                                    SG4.NAD+Z11.SG7.CTA+IC.COM,
                                    SG4.NAD+Z12.SG7.CTA+IC.COM,
                                    SG4.NAD+Z13.SG7.CTA+IC.COM,
                                    SG4.NAD+Z14.SG7.CTA+IC.COM,
                                    SG4.NAD+Z16.SG7.CTA+IC.COM,
                                    SG4.NAD+Z17.SG7.CTA+IC.COM,
                                    SG4.NAD+Z18.SG7.CTA+IC.COM,
                                    SG4.NAD+Z19.SG7.CTA+IC.COM,
                                    SG4.NAD+Z20.SG7.CTA+IC.COM,
                                    SG4.NAD+Z21.SG7.CTA+IC.COM</TipInfo>
                              x-apidog-orders:
                                - nachname
                                - rufnummern
                                - eMailAdresse
                              x-apidog-ignore-properties: []
                            marktteilnehmer:
                              type: object
                              properties:
                                kommunikationsrolle:
                                  type: string
                                  title: Kommunikationsrolle
                                  description: >-
                                    Kommunikationsrolle | 

                                    <TipInfo>SG4.NAD+Z10.SG7.CTA+IC.COM,
                                    SG4.NAD+Z11.SG7.CTA+IC.COM,
                                    SG4.NAD+Z12.SG7.CTA+IC.COM,
                                    SG4.NAD+Z13.SG7.CTA+IC.COM,
                                    SG4.NAD+Z14.SG7.CTA+IC.COM,
                                    SG4.NAD+Z16.SG7.CTA+IC.COM,
                                    SG4.NAD+Z17.SG7.CTA+IC.COM,
                                    SG4.NAD+Z18.SG7.CTA+IC.COM,
                                    SG4.NAD+Z19.SG7.CTA+IC.COM,
                                    SG4.NAD+Z20.SG7.CTA+IC.COM,
                                    SG4.NAD+Z21.SG7.CTA+IC.COM</TipInfo>
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
                                  x-apidog-folder: Bo4e/ENUM
                                name1:
                                  type: string
                                  description: >-
                                    Erster Teil des Namens. Hier kann der
                                    Firmenname oder bei Privatpersonen
                                    beispielsweise der Nachname dargestellt
                                    werden. Beispiele: Yellow Strom GmbH oder
                                    Hagen | 

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
                                postfach:
                                  type: string
                                  description: >-
                                    Postfach | 

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
                                name3:
                                  type: string
                                  description: >-
                                    Dritter Teil des Namens. Hier können weitere
                                    Ergänzungen zum Firmennamen oder bei
                                    Privatpersonen Zusätze zum  Namen
                                    dargestellt werden. Beispiele: und Afrika
                                    oder Sängerin | 

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
                                anrede:
                                  type: string
                                  description: >-
                                    Die Anrede für den GePa, Z.B. Herr.

                                    Z04 Korrespondenzanschrift des Kunden des
                                    Lieferanten

                                    PI 55001 55600 55601 55013 55014 55043 55168
                                    55169 | 

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
                                landescode:
                                  type: string
                                  title: Landescode
                                  description: >-
                                    Der ISO-Landescode als Enumeration | 

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
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
                                name2:
                                  type: string
                                  description: >-
                                    Zweiter Teil des Namens. Hier kann der eine
                                    Erweiterung zum Firmennamen oder bei
                                    Privatpersonen beispielsweise der Vorname
                                    dargestellt werden. Beispiele: Bereich Süd
                                    oder Nina | 

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
                                rufnummern:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      nummerntyp:
                                        type: string
                                        title: Rufnummernart
                                        description: >-

                                          <TipInfo>SG4.NAD+Z10.SG7.CTA+IC.COM,
                                          SG4.NAD+Z11.SG7.CTA+IC.COM,
                                          SG4.NAD+Z12.SG7.CTA+IC.COM,
                                          SG4.NAD+Z13.SG7.CTA+IC.COM,
                                          SG4.NAD+Z14.SG7.CTA+IC.COM,
                                          SG4.NAD+Z16.SG7.CTA+IC.COM,
                                          SG4.NAD+Z17.SG7.CTA+IC.COM,
                                          SG4.NAD+Z18.SG7.CTA+IC.COM,
                                          SG4.NAD+Z19.SG7.CTA+IC.COM,
                                          SG4.NAD+Z20.SG7.CTA+IC.COM,
                                          SG4.NAD+Z21.SG7.CTA+IC.COM</TipInfo>
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
                                      rufnummer:
                                        type: object
                                        title: Rufnummer
                                        description: >-

                                          <TipInfo>SG4.NAD+Z10.SG7.CTA+IC.COM,
                                          SG4.NAD+Z11.SG7.CTA+IC.COM,
                                          SG4.NAD+Z12.SG7.CTA+IC.COM,
                                          SG4.NAD+Z13.SG7.CTA+IC.COM,
                                          SG4.NAD+Z14.SG7.CTA+IC.COM,
                                          SG4.NAD+Z16.SG7.CTA+IC.COM,
                                          SG4.NAD+Z17.SG7.CTA+IC.COM,
                                          SG4.NAD+Z18.SG7.CTA+IC.COM,
                                          SG4.NAD+Z19.SG7.CTA+IC.COM,
                                          SG4.NAD+Z20.SG7.CTA+IC.COM,
                                          SG4.NAD+Z21.SG7.CTA+IC.COM</TipInfo>
                                        x-apidog-orders: []
                                        properties: {}
                                        x-apidog-ignore-properties: []
                                    x-apidog-orders:
                                      - nummerntyp
                                      - rufnummer
                                    x-apidog-ignore-properties: []
                                ort:
                                  type: object
                                  title: Sort
                                  description: >-

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                                strasse:
                                  type: string
                                  description: >-
                                    Strasse | 

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
                                ortsteil:
                                  type: string
                                  description: >-
                                    Ortsteil | 

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
                                name4:
                                  type: string
                                  description: >-
                                    Name 4 | 

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
                                postleitzahl:
                                  type: string
                                  description: >-
                                    Postleitzahl | 

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
                                hausnummer:
                                  type: string
                                  description: >-
                                    Hausnummer und Ergänzung | 

                                    <TipInfo>SG4.NAD+Z10, SG4.NAD+Z11,
                                    SG4.NAD+Z12, SG4.NAD+Z13, SG4.NAD+Z14,
                                    SG4.NAD+Z16, SG4.NAD+Z17, SG4.NAD+Z18,
                                    SG4.NAD+Z19, SG4.NAD+Z20,
                                    SG4.NAD+Z21</TipInfo>
                              x-apidog-orders:
                                - kommunikationsrolle
                                - name1
                                - postfach
                                - name3
                                - anrede
                                - landescode
                                - name2
                                - rufnummern
                                - ort
                                - strasse
                                - ortsteil
                                - name4
                                - postleitzahl
                                - hausnummer
                              x-apidog-ignore-properties: []
                          x-apidog-orders:
                            - ansprechpartner
                            - marktteilnehmer
                          x-apidog-ignore-properties: []
                      gueltigkeit:
                        type: string
                        description: >-
                          Gültig Ab - Gültigkeit, Beginndatum der
                          Kommunikationsdaten

                          DTM 157

                          PI 37000 37001 37002 37003 37004 37005 37006  | 

                          <TipInfo>SG1.RFF+AGK.DTM+157</TipInfo>
                        format: date-time
                    x-apidog-orders:
                      - marktteilnehmer
                      - kommunikationsangaben
                      - gueltigkeit
                    x-apidog-ignore-properties: []
                kommunikationsdaten:
                  type: object
                  properties:
                    kommunikationsDatenBlattInaktiv:
                      type: boolean
                      description: >-
                        Partnerstammdaten - Kommunikationsdatenblatt mit oder
                        ohne Inhalt

                        11 Dokument nicht verfügbar

                        BGM 10

                        PI 37000 37001 37002 37003 37004 37005 37006  | 

                        <TipInfo>BGM+10</TipInfo>
                  x-apidog-orders:
                    - kommunikationsDatenBlattInaktiv
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - KOMMUNIKATIONSDATEN
                - kommunikationsdaten
              x-apidog-ignore-properties: []
          x-apidog-refs: {}
          x-apidog-orders:
            - transaktionsdaten
            - stammdaten
          required:
            - transaktionsdaten
            - stammdaten
          x-apidog-ignore-properties: []
        - type: object
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
                  examples:
                    - 00505688-E4A2-1EDF-A0C2-C81842E2515E
                eventname:
                  type: string
                  description: Name des Events
                  default: START_LIEFERENDE
                  examples:
                    - START_PARTIN
              x-apidog-orders:
                - prozessId
                - eventname
              required:
                - prozessId
                - eventname
              x-apidog-ignore-properties: []
          x-apidog-refs: {}
          x-apidog-orders:
            - zusatzdaten
          required:
            - zusatzdaten
          x-apidog-ignore-properties: []
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
