# Kommunikationsdaten des Serviceanbieters lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getCommunicationDataBasic:
    get:
      summary: Kommunikationsdaten des Serviceanbieters lesen
      deprecated: false
      description: >-
        Lesen der Kommunikationsdaten des Serviceanbieters (Parameter1) zum
        Zeitpunkt (Parameter2)
      operationId: LESEN_KOMMUNIKATIONSDATEN_BASIS
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: ILN Nummer
          required: true
          schema:
            type: string
            examples:
              - '9903790000002'
        - name: parameter2
          in: query
          description: Stichtag
          required: true
          schema:
            type: string
            format: date-time
            examples:
              - '2024-06-28T12:18:00Z'
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
        - name: command
          in: query
          description: >-
            Entspricht der operationId dieser Schnittstelle. Diese Operation Id
            entspricht dem Command im Camunda Konnektor Prozess. Wenn das
            Backend einen generischen Endpunkt bereitstellt, kann dieses Command
            gentutzt werden um zu definieren welche Operation ausgeführt werden
            soll.
          required: false
          example: SAP_LESEN_KOMMUNIKATIONSDATEN_BASIS
          schema:
            type: string
      responses:
        '200':
          description: Erfolgreiches Lesen der Kommunikationsdaten
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Kommunikationsdaten'
              example:
                boTyp: KOMMUNIKATIONSDATEN
                versionStruktur: '1'
                gueltigkeit: '2024-06-30T22:00:00Z'
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
                  - boTyp: MARKTTEILNEHMER
                    versionStruktur: '1'
                    name1: Lieferant
                    gewerbekennzeichnung: true
                    partneradresse:
                      postleitzahl: '12345'
                      ort: Lieferantenort
                      strasse: Lieferantenstr
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
      x-apidog-status: developing
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017018-run
components:
  schemas:
    Kommunikationsdaten:
      title: Kommunikationsdaten
      type: object
      properties:
        boTyp: &ref_1
          $ref: '#/components/schemas/BOTyp'
          default: KOMMUNIKATIONSDATEN
          description: .
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        gueltigkeit:
          type: string
          format: date-time
          description: |-
            Gültig Ab - Gültigkeit, Beginndatum der Kommunikationsdaten
            DTM 157
            PI 37000 37001 37002 37003 37004 37005 37006 
        kommunikationsDatenBlattInaktiv:
          type: boolean
          description: |-
            Partnerstammdaten - Kommunikationsdatenblatt mit oder ohne Inhalt
            11 Dokument nicht verfügbar
            BGM 10
            PI 37000 37001 37002 37003 37004 37005 37006 
        marktteilnehmer: &ref_0
          $ref: '#/components/schemas/Marktteilnehmer'
          description: |-
            Name und Adresse des Unternehmens
            NAD SU Lieferant
            PI 37000
            DDM Netzbetreiber
            PI 37001
            DEB Messstellenbetreiber
            PI 37002
            Z31 Übertragungsnetzbetreiber
            PI 37005
            Z34 Bilanzkoordinator
            PI 37004
            Z35 Bilanzkreisverantwortlicher
            PI 37003
            Z36 Energieserviceanbieter
            PI 37006
        kommunikationsangaben:
          type: array
          items: *ref_0
          description: |-
            Name und Anschrift Ansprechpartner
            NAD Z10 
            PI 37000 37001 37002 37005 37004 37003 37006
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - gueltigkeit
        - kommunikationsDatenBlattInaktiv
        - marktteilnehmer
        - kommunikationsangaben
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Kommunikationsdaten.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Marktteilnehmer:
      title: Marktteilnehmer
      type: object
      properties:
        boTyp: *ref_1
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
        marktrolle:
          $ref: '#/components/schemas/Marktrolle'
          description: >-
            Gibt im Klartext die Bezeichnung der Marktrolle an.

            CAV Z91 

            PI 55002 55078 55602 55603 55013 55607 55613 55674 55615 55621 55627
            55633 55688 55689 55616 55622 55628 55634 55618 55624 55630 55636
            55620 55626 55632 55638 55690 55670 55035 55095 55060 55194 55043
            55168 55169 55239 

            CAV Z88 

            PI 55639 55644 55649 55654 55659 55664 55043 55168 55169

            CAV Z89

            PI 55613 55614 55674 55675 55690 55670 55671 55060 55043 55169 55074
            55075 55076 55195 55196

            CAV Z90

            PI 55043 55168 55169 55195 55196 

            CAV ZF0

            PI 55002 55078 55602 55603 55013 55607 55620 55626 55632 55638 55035
            55095 55060 55194 55043 55168 55169

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
        boTyp: *ref_1
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
