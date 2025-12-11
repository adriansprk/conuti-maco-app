# Stammdatenänderung vom Netzbetreiber (verantwortlich)

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
      summary: Stammdatenänderung vom Netzbetreiber (verantwortlich)
      deprecated: false
      description: >-
        Triggert den Versand von Stammdatenänderungen vom verantwortlichen
        Netzbetreiber an Marktpartner durch die MACO APP. Die Anfrage wird
        identifiziert durch den Eventnamen START_VERSAND_SDAE. Zusätzlich ist
        eine eindeutige ID prozessId aus dem Backend mit zu übergeben, mit der
        die spätere Antwort vom Marktpartner wieder an das Backend übergeben
        werden kann.
      operationId: START_VERSAND_SDAE
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BNB%5D%20START_VERSAND_SDAE'
            examples:
              '1':
                value:
                  stammdaten:
                    VERWENDUNGSZEITRAUM:
                      - boTyp: VERWENDUNGSZEITRAUM
                        versionStruktur: '1'
                        verwendungAb: '2025-04-02T22:00:00Z'
                        zeitraumId: 1
                        datenqualitaet: GUELTIGE_DATEN
                    NETZLOKATION:
                      - boTyp: NETZLOKATION
                        versionStruktur: '1'
                        netzlokationsId: E1688117482
                        sparte: STROM
                        zeitraumId: 1
                        datenqualitaet: DATEN
                        marktrollen:
                          - boTyp: MARKTTEILNEHMER
                            versionStruktur: '1'
                            marktrolle: MSB
                            rollencodenummer: '9904446000007'
                            rollencodetyp: BDEW
                            messstellenbetreiberEigenschaft: GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                  transaktionsdaten:
                    sparte: STROM
                    transaktionsgrund: ZX8
                    absender:
                      rollencodenummer: '9900321000005'
                      rollencodetyp: BDEW
                    empfaenger:
                      rollencodenummer: '9903790000002'
                      rollencodetyp: BDEW
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_VERSAND_SDAE
                summary: '55615'
              '2':
                value:
                  stammdaten:
                    VERWENDUNGSZEITRAUM:
                      - boTyp: VERWENDUNGSZEITRAUM
                        versionStruktur: '1'
                        zeitraumId: 1
                        datenqualitaet: KEINE_DATEN
                        verwendungAb: '2025-02-28T23:00:00Z'
                        verwendungBis: '2025-03-31T22:00:00Z'
                      - boTyp: VERWENDUNGSZEITRAUM
                        versionStruktur: '1'
                        zeitraumId: 2
                        datenqualitaet: GUELTIGE_DATEN
                        verwendungAb: '2025-03-31T22:00:00Z'
                        verwendungBis: '2025-04-02T22:00:00Z'
                      - boTyp: VERWENDUNGSZEITRAUM
                        versionStruktur: '1'
                        zeitraumId: 3
                        datenqualitaet: GUELTIGE_DATEN
                        verwendungAb: '2025-04-02T22:00:00Z'
                    MARKTLOKATION:
                      - boTyp: MARKTLOKATION
                        versionStruktur: '1'
                        datenqualitaet: DATEN
                        zeitraumId: 2
                        marktlokationsId: '50074561188'
                        sparte: STROM
                        lokationsadresse:
                          postleitzahl: '12345'
                          ort: Ort
                          strasse: Str
                          hausnummer: '1'
                          landescode: DE
                          zusatzInformation:
                            zusatz1: Mustermann
                            zusatz2: Max
                        marktrollen:
                          - boTyp: MARKTTEILNEHMER
                            versionStruktur: '1'
                            rollencodenummer: '9904446000007'
                            marktrolle: MSB
                            weiterverpflichtet: true
                            messstellenbetreiberEigenschaft: GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                        messtechnischeEinordnung: KME_MME
                      - boTyp: MARKTLOKATION
                        versionStruktur: '1'
                        datenqualitaet: DATEN
                        zeitraumId: 3
                        marktlokationsId: '50074561188'
                        sparte: STROM
                        lokationsadresse:
                          postleitzahl: '12345'
                          ort: Ort
                          strasse: Str
                          hausnummer: '1'
                          landescode: DE
                          zusatzInformation:
                            zusatz1: Musterfrau
                            zusatz2: Erika
                        marktrollen:
                          - boTyp: MARKTTEILNEHMER
                            versionStruktur: '1'
                            rollencodenummer: '9904446000007'
                            marktrolle: MSB
                            weiterverpflichtet: false
                            messstellenbetreiberEigenschaft: GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                        messtechnischeEinordnung: KME_MME
                  transaktionsdaten:
                    sparte: STROM
                    transaktionsgrund: ZX6
                    transaktionsgrundergaenzung: ZW4
                    absender:
                      rollencodenummer: '9900321000005'
                      rollencodetyp: BDEW
                    empfaenger:
                      rollencodenummer: '9903790000002'
                      rollencodetyp: BDEW
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_VERSAND_SDAE
                summary: '55616'
              '3':
                value:
                  stammdaten:
                    VERWENDUNGSZEITRAUM:
                      - boTyp: VERWENDUNGSZEITRAUM
                        versionStruktur: '1'
                        zeitraumId: 1
                        datenqualitaet: GUELTIGE_DATEN
                        verwendungAb: '2025-06-23T22:00:00Z'
                        verwendungBis: '2025-07-23T22:00:00Z'
                      - boTyp: VERWENDUNGSZEITRAUM
                        versionStruktur: '1'
                        zeitraumId: 2
                        datenqualitaet: GUELTIGE_DATEN
                        verwendungAb: '2025-07-23T22:00:00Z'
                    TECHNISCHE_RESSOURCE:
                      - boTyp: TECHNISCHE_RESSOURCE
                        versionStruktur: '1'
                        ressourcenId: D417MLM8164
                        sparte: STROM
                        gueltigkeitszeitraum:
                          zeitraumId: 1
                          startdatum: '2025-06-23T22:00:00Z'
                          enddatum: '2025-07-23T22:00:00Z'
                        datenqualitaet: GUELTIGE_DATEN
                        referenzNetzlokation: E1688117482
                        referenzSteuerbareRessource: C816417ST77
                        nennleistung:
                          aufnahme: 100
                        verbrauchsart: EMOB
                        artEMobilitaet: LS
                        enwg: true
                        inbetriebsetzungsdatum: INBETRIEBSETZUN_VOR_2024
                        einordnung: WECHSELMOEGLICHKEIT_EINMALIG_NOCH_MOEGLICH
                        weitereEinrichtung: false
                        art: STROMVERBRAUCH
                      - boTyp: TECHNISCHE_RESSOURCE
                        versionStruktur: '1'
                        ressourcenId: D417MLM8164
                        sparte: STROM
                        gueltigkeitszeitraum:
                          zeitraumId: 2
                          startdatum: '2025-07-23T22:00:00Z'
                        datenqualitaet: GUELTIGE_DATEN
                        referenzNetzlokation: E1688117482
                        referenzSteuerbareRessource: C816417ST77
                        nennleistung:
                          aufnahme: 100
                        verbrauchsart: EMOB
                        artEMobilitaet: LS
                        enwg: true
                        inbetriebsetzungsdatum: INBETRIEBSETZUN_VOR_2024
                        einordnung: WECHSELMOEGLICHKEIT_EINMALIG_NOCH_MOEGLICH
                        weitereEinrichtung: false
                        art: STROMVERBRAUCH
                    STEUERBARE_RESSOURCE:
                      - boTyp: STEUERBARE_RESSOURCE
                        versionStruktur: '1'
                        ressourcenId: C816417ST77
                        sparte: STROM
                  transaktionsdaten:
                    sparte: STROM
                    transaktionsgrund: ZY0
                    absender:
                      rollencodenummer: '9900327000009'
                      rollencodetyp: BDEW
                      ansprechpartner:
                        boTyp: ANSPRECHPARTNER
                        versionStruktur: '1'
                        nachname: P GETTY
                        rufnummern:
                          - nummerntyp: RUF_DURCHWAHL
                            rufnummer: '+3222271020'
                    empfaenger:
                      rollencodenummer: '9903729000007'
                      rollencodetyp: BDEW
                  zusatzdaten:
                    prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                    eventname: START_VERSAND_SDAE
                summary: '55617'
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
      x-apidog-folder: Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14994280-run
components:
  schemas:
    '[NB] START_VERSAND_SDAE':
      allOf:
        - oneOf:
            - $ref: '#/components/schemas/PI_55173'
            - $ref: '#/components/schemas/PI_55175'
            - $ref: '#/components/schemas/PI_55225'
            - $ref: '#/components/schemas/PI_55615'
            - $ref: '#/components/schemas/PI_55616'
            - $ref: '#/components/schemas/PI_55617'
            - $ref: '#/components/schemas/PI_55618'
            - $ref: '#/components/schemas/PI_55619'
            - $ref: '#/components/schemas/PI_55620'
            - $ref: '#/components/schemas/PI_55627'
            - $ref: '#/components/schemas/PI_55628'
            - $ref: '#/components/schemas/PI_55629'
            - $ref: '#/components/schemas/PI_55630'
            - $ref: '#/components/schemas/PI_55632'
            - $ref: '#/components/schemas/PI_55688'
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
                  const: START_VERSAND_SDAE
                  default: START_VERSAND_SDAE
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
    PI_55688:
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
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
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
                      x-apidog-orders:
                        - rollencodenummer
                        - marktrolle
                      x-apidog-ignore-properties: []
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                x-apidog-orders:
                  - marktrollen
                  - marktlokationsId
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
      description: 55688 - NB an ÜNB - Änderung vom NB an ÜNB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55632:
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
                  betriebszustand:
                    type: string
                    title: Betriebszustand
                    description: >-
                      Betriebszustand | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z18.SG10.CCI+Z32
                    enum:
                      - GESPERRT_NICHT_ENTSPERREN
                      - GESPERRT
                      - REGELBETRIEB
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
                  - betriebszustand
                  - gueltigkeitszeitraum
                  - messlokationsId
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
            - MESSLOKATION
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
      description: 55632 - NB an MSB - Änderung vom NB an MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55630:
      type: object
      properties:
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
      description: 55630 - NB an MSB - Änderung vom NB an MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55629:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            TECHNISCHE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
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
                  speicherkapazitaet:
                    type: number
                    description: >-
                      Speicherkapazität

                      Beispiel: QTY+Z42:100:KWH' | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG9.QTY+Z42
                    format: float
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z52'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
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
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z52'
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
                x-apidog-orders:
                  - weitereEinrichtung
                  - nennleistung
                  - referenzNetzlokation
                  - speicherkapazitaet
                  - gueltigkeitszeitraum
                  - erzeugungsart
                  - referenzSteuerbareRessource
                  - speicherart
                  - art
                  - waermenutzung
                  - datenqualitaet
                  - ressourcenId
                  - verbrauchsart
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
            - TECHNISCHE_RESSOURCE
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
      description: 55629 - NB an MSB - Änderung vom NB an MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55628:
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
                        boTyp:
                          type: string
                        versionStruktur:
                          type: string
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
                        - boTyp
                        - versionStruktur
                        - name1
                        - anrede
                        - geschaeftspartnerrolle
                        - name3
                        - name4
                        - name2
                      x-apidog-ignore-properties: []
                  vertragsart:
                    type: string
                    enum:
                      - NETZNUTZUNGSVERTRAG
                    x-apidog-enum:
                      - value: NETZNUTZUNGSVERTRAG
                        name: ''
                        description: ''
                    default: NETZNUTZUNGSVERTRAG
                  korrespondenzpartner:
                    type: object
                    properties:
                      boTyp:
                        type: string
                      versionStruktur:
                        type: string
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
                      - boTyp
                      - versionStruktur
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
                      startdatum:
                        type: string
                        description: >-
                          Datum Vertragsbeginn / DTM+92 | EDIFACT:
                          SG4.IDE+24.DTM+92
                        format: date-time
                      enddatum:
                        type: string
                        description: >-
                          Datum Vertragsbeginn / DTM+92 | EDIFACT:
                          SG4.IDE+24.DTM+92
                        format: date-time
                    x-apidog-orders:
                      - zeitraumId
                      - startdatum
                      - enddatum
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
                  - vertragsart
                  - korrespondenzpartner
                  - gueltigkeitszeitraum
                  - datenqualitaet
                required:
                  - vertragsart
                x-apidog-ignore-properties: []
            BILANZIERUNG:
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
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z21,
                          SG4.IDE+24.SG8.SEQ+[Z08|Z87],
                          SG4.IDE+24.SG8.SEQ+[Z38|Z90]
                      startdatum:
                        type: string
                        description: >-
                          Datum Vertragsbeginn / DTM+92 | EDIFACT:
                          SG4.IDE+24.DTM+92
                        format: date-time
                      enddatum:
                        type: string
                        description: >-
                          Datum Vertragsbeginn / DTM+92 | EDIFACT:
                          SG4.IDE+24.DTM+92
                        format: date-time
                    x-apidog-orders:
                      - zeitraumId
                      - startdatum
                      - enddatum
                    required:
                      - zeitraumId
                      - startdatum
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z21,
                      SG4.IDE+24.SG8.SEQ+[Z08|Z87], SG4.IDE+24.SG8.SEQ+[Z38|Z90]
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
                  lastprofile:
                    type: array
                    items:
                      type: object
                      properties:
                        bezeichnung:
                          type: string
                          description: >-
                            Externe Bezeichnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+[Z02|Z04]].CAV,
                            SG4.IDE+24.SG8.SEQ+[Z08|Z87].SG10.CCI+[Z03|Z05].CAV
                        referenzprofilbezeichnung:
                          type: string
                          description: >-
                            Bezeichnung des Referenzprofils | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z38|Z90].SG10.CCI+Z05.CAV
                        verfahren:
                          type: string
                          title: Profilverfahren
                          description: >-
                            Profilverfahren | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+[Z02|Z04]],
                            SG4.IDE+24.SG8.SEQ+[Z08|Z87].SG10.CCI+[Z03|Z05]
                          enum:
                            - SYNTHETISCH
                            - ANALYTISCH
                        einspeisung:
                          type: boolean
                          description: >-
                            Kennzeichen Einspeisung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+[Z02|Z04]],
                            SG4.IDE+24.SG8.SEQ+[Z08|Z87].SG10.CCI+[Z03|Z05]
                        profilart:
                          type: string
                          title: Profilart
                          description: >-
                            Profilart | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+[Z02|Z04]],
                            SG4.IDE+24.SG8.SEQ+[Z08|Z87].SG10.CCI+[Z03|Z05]
                          enum:
                            - ART_STANDARDLASTPROFIL
                            - ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL
                            - ART_LASTPROFIL
                      x-apidog-orders:
                        - bezeichnung
                        - referenzprofilbezeichnung
                        - verfahren
                        - einspeisung
                        - profilart
                      x-apidog-ignore-properties: []
                  prognosegrundlage:
                    type: string
                    title: Prognosegrundlage
                    description: >-
                      Prognosegrundlage | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI
                    enum:
                      - WERTE
                      - PROFILE
                  temperaturarbeit:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+[Z10|265|Z08]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+[Z10|265|Z08]
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
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+31'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - einheit
                      - wert
                    x-apidog-ignore-properties: []
                  abwicklungsmodell:
                    type: string
                    title: Abwicklungsmodell
                    description: >-
                      Abwicklungsmodell | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+ZA2++[ZE9|ZF0]
                    enum:
                      - MODELL_1_BILANZIERUNG_AN_MARKTLOKATION
                      - MODELL_2_BILANZIERUNG_IM_BILANZIERUNGSGEBIET
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
                        SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI.CAV+[E02|E14|Z36]
                      items:
                        type: string
                        title: Profiltyp
                        description: Profiltyp
                        enum:
                          - SLP_SEP
                          - TLP_TEP
                          - TEP
                x-apidog-orders:
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - lastprofile
                  - prognosegrundlage
                  - temperaturarbeit
                  - jahresverbrauchsprognose
                  - abwicklungsmodell
                  - detailsPrognosegrundlage
                required:
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - prognosegrundlage
                  - abwicklungsmodell
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01,
                          SG4.IDE+24.SG12.NAD+EO.RFF+Z46,
                          SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58].RFF+Z46
                      startdatum:
                        type: string
                        description: >-
                          Datum Vertragsbeginn / DTM+92 | EDIFACT:
                          SG4.IDE+24.DTM+92
                        format: date-time
                      enddatum:
                        type: string
                        description: >-
                          Datum Vertragsbeginn / DTM+92 | EDIFACT:
                          SG4.IDE+24.DTM+92
                        format: date-time
                    x-apidog-orders:
                      - zeitraumId
                      - startdatum
                      - enddatum
                    required:
                      - zeitraumId
                      - startdatum
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01,
                      SG4.IDE+24.SG12.NAD+EO, SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58]
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
                      boTyp:
                        type: string
                      versionStruktur:
                        type: string
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
                      - boTyp
                      - versionStruktur
                      - partneradresse
                      - name1
                      - name4
                      - anrede
                      - gewerbekennzeichnung
                      - name2
                      - name3
                    x-apidog-ignore-properties: []
                  eigentuemer:
                    type: object
                    properties:
                      boTyp:
                        type: string
                      versionStruktur:
                        type: string
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
                      - boTyp
                      - versionStruktur
                      - name3
                      - name4
                      - name2
                      - name1
                      - partneradresse
                      - gewerbekennzeichnung
                      - anrede
                    required:
                      - versionStruktur
                    x-apidog-ignore-properties: []
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                        versionStruktur:
                          type: string
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
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z90,
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
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z90,
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z91
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - messstellenbetreiberEigenschaft
                        - weiterverpflichtet
                        - marktrolle
                        - rollencodenummer
                      required:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
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
                  netzebene:
                    type: string
                    title: Netzebene
                    description: >-
                      Netzebene | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++E03.CAV
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
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - hausverwalter
                  - eigentuemer
                  - marktrollen
                  - energieherkunft
                  - messtechnischeEinordnung
                  - netzebene
                required:
                  - marktlokationsId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                  - messtechnischeEinordnung
                  - netzebene
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
                required:
                  - zeitraumId
                  - verwendungAb
                  - datenqualitaet
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZNUTZUNGSVERTRAG
            - BILANZIERUNG
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
          required:
            - BILANZIERUNG
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
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
                marktrolle:
                  type: string
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
                - marktrolle
              required:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
                - marktrolle
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
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
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
                - rufnummern
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
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
          x-apidog-orders:
            - empfaenger
            - kategorie
            - absender
            - transaktionsgrund
            - transaktionsgrundergaenzung
          required:
            - empfaenger
            - kategorie
            - absender
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 55628 - NB an MSB - Änderung vom NB an MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55627:
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
      description: 55627 - NB an MSB - Änderung vom NB an MSB
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
                  messlokationsId:
                    type: string
                    description: >-
                      Die Messlokations-Identifikation. Das ist die frühere
                      Zählpunktbezeichnung,

                      z.B. DE 47108151234567 | EDIFACT: SG4.IDE+24.SG5.LOC+Z17
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z18'
                      startdatum:
                        type: string
                      enddatum:
                        type: string
                    x-apidog-orders:
                      - zeitraumId
                      - startdatum
                      - enddatum
                    required:
                      - zeitraumId
                      - startdatum
                    x-apidog-ignore-properties: []
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
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                        versionStruktur:
                          type: string
                        rollencodenummer:
                          type: string
                          description: >-
                            Gibt die Codenummer der Marktrolle an. | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z18.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+Z18.SG10.CCI+++ZB3.CAV+ZF0
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
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - rollencodenummer
                        - marktrolle
                        - weiterverpflichtet
                        - messstellenbetreiberEigenschaft
                      required:
                        - boTyp
                        - versionStruktur
                        - rollencodenummer
                        - marktrolle
                        - weiterverpflichtet
                        - messstellenbetreiberEigenschaft
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - messlokationsId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                required:
                  - messlokationsId
                  - gueltigkeitszeitraum
                  - marktrollen
                x-apidog-ignore-properties: []
            MESSSTELLENBETRIEBSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsart:
                    type: string
                    enum:
                      - MESSSTELLENBETRIEBSVERTRAG
                    x-apidog-enum:
                      - value: MESSSTELLENBETRIEBSVERTRAG
                        name: ''
                        description: ''
                    default: MESSSTELLENBETRIEBSVERTRAG
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
                  - vertragsart
                  - vertragskonditionen
                required:
                  - vertragsart
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                x-apidog-orders:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                  - verwendungBis
                required:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MESSLOKATION
            - MESSSTELLENBETRIEBSVERTRAG
            - VERWENDUNGSZEITRAUM
          required:
            - MESSLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
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
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
                - ansprechpartner
                - rufnummern
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle:
                  type: string
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
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodetyp
                - rollencodenummer
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            sparte:
              type: string
          x-apidog-orders:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
            - sparte
          required:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
            - sparte
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
                  tranchenId:
                    type: string
                    description: 'tranchenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z21'
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z15'
                      startdatum:
                        type: string
                        format: date-time
                      enddatum:
                        type: string
                        format: date-time
                    x-apidog-orders:
                      - zeitraumId
                      - startdatum
                      - enddatum
                    required:
                      - zeitraumId
                      - startdatum
                    x-apidog-ignore-properties: []
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
                  verguetungEmpfaenger:
                    type: string
                    title: VerguetungEmpfaenger
                    description: >-
                      VerguetungEmpfaenger | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z15.SG10.CCI+++Z89.CAV
                    enum:
                      - KUNDE
                      - LIEFERANT
                x-apidog-orders:
                  - tranchenId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - verguetungEmpfaenger
                required:
                  - tranchenId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - verguetungEmpfaenger
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                x-apidog-orders:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                  - verwendungBis
                required:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - TRANCHE
            - VERWENDUNGSZEITRAUM
          required:
            - TRANCHE
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
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
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
                - rufnummern
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
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
                marktrolle:
                  type: string
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
                - marktrolle
              required:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
                - marktrolle
              x-apidog-ignore-properties: []
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            sparte:
              type: string
          x-apidog-orders:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
            - sparte
          required:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
            - sparte
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
        stammdaten:
          type: object
          properties:
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z62'
                      startdatum:
                        type: string
                        format: date-time
                      enddatum:
                        type: string
                        format: date-time
                    x-apidog-orders:
                      - zeitraumId
                      - startdatum
                      - enddatum
                    required:
                      - zeitraumId
                      - startdatum
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
                        boTyp:
                          type: string
                        versionStruktur:
                          type: string
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
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                        - messstellenbetreiberEigenschaft
                      required:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - ressourcenId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                required:
                  - ressourcenId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                x-apidog-orders:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                  - verwendungBis
                required:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - STEUERBARE_RESSOURCE
            - VERWENDUNGSZEITRAUM
          required:
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle:
                  type: string
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
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
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodetyp
                - rollencodenummer
                - rufnummern
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle:
                  type: string
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
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodetyp
                - rollencodenummer
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            sparte:
              type: string
          x-apidog-orders:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
            - sparte
          required:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
            - sparte
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55618 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55617:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            TECHNISCHE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z20'
                  gueltigkeitszeitraum:
                    type: array
                    items:
                      type: object
                      properties:
                        zeitraumId:
                          type: integer
                        startdatum:
                          type: string
                          format: date-time
                        enddatum:
                          type: string
                          format: date-time
                      x-apidog-orders:
                        - zeitraumId
                        - startdatum
                        - enddatum
                      required:
                        - zeitraumId
                        - startdatum
                        - enddatum
                      x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                  referenzSteuerbareRessource:
                    type: string
                    description: >-
                      referenzSteuerbareRessource | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.RFF+Z38
                  referenzNetzlokation:
                    type: string
                    description: >-
                      referenzNetzlokation | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.RFF+Z32
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
                  speicherkapazitaet:
                    type: number
                    description: >-
                      Speicherkapazität

                      Beispiel: QTY+Z42:100:KWH' | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG9.QTY+Z42
                    format: float
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
                  enwg:
                    type: boolean
                    description: >-
                      enwg | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+[Z17|Z50|Z56].CAV+[ZG8|ZG9]
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
                  verbrauchsart:
                    type: array
                    items:
                      $ref: '#/components/schemas/Verbrauchsart'
                    title: Verbrauchsart
                    description: >-
                      Verbrauchsart | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+[Z17|Z50|Z56].CAV+[Z64|Z65|ZE5|ZA8]
                  inbetriebsetzungsdatum:
                    type: string
                    title: Inbetriebsetzung
                    description: >-
                      EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z52.SG10.CCI+[Z17|Z50|Z56].CAV+[ZH0|ZH1]
                    enum:
                      - INBETRIEBSETZUNG_NACH_2023
                      - INBETRIEBSETZUN_VOR_2024
                  artEMobilitaet:
                    type: string
                x-apidog-orders:
                  - ressourcenId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - referenzSteuerbareRessource
                  - referenzNetzlokation
                  - nennleistung
                  - speicherkapazitaet
                  - einordnung
                  - weitereEinrichtung
                  - enwg
                  - erzeugungsart
                  - speicherart
                  - art
                  - waermenutzung
                  - verbrauchsart
                  - inbetriebsetzungsdatum
                  - artEMobilitaet
                required:
                  - ressourcenId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - weitereEinrichtung
                  - art
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  zeitraumId:
                    type: integer
                    description: >-
                      zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53],
                      SG4.IDE+24.SG8.SEQ+Z52
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
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                x-apidog-orders:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                  - verwendungBis
                required:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - TECHNISCHE_RESSOURCE
            - VERWENDUNGSZEITRAUM
          required:
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
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
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
                - rufnummern
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
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
                marktrolle:
                  type: string
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
                - marktrolle
              required:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
                - marktrolle
              x-apidog-ignore-properties: []
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
          x-apidog-orders:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
          required:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55617 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
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
    PI_55616:
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
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
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
                      startdatum:
                        type: string
                        description: >-
                          Datum Vertragsbeginn / DTM+92 | EDIFACT:
                          SG4.IDE+24.DTM+92
                        format: date-time
                      enddatum:
                        type: string
                        description: >-
                          Datum Vertragsbeginn / DTM+92 | EDIFACT:
                          SG4.IDE+24.DTM+92
                        format: date-time
                    x-apidog-orders:
                      - zeitraumId
                      - startdatum
                      - enddatum
                    required:
                      - zeitraumId
                      - startdatum
                    x-apidog-ignore-properties: []
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
                      boTyp:
                        type: string
                      versionStruktur:
                        type: string
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
                      - boTyp
                      - versionStruktur
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
                      boTyp:
                        type: string
                      versionStruktur:
                        type: string
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
                      - boTyp
                      - versionStruktur
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
                      boTyp:
                        type: string
                      versionStruktur:
                        type: string
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
                      - boTyp
                      - versionStruktur
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
                        boTyp:
                          type: string
                        versionStruktur:
                          type: string
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
                        - boTyp
                        - versionStruktur
                        - messstellenbetreiberEigenschaft
                        - weiterverpflichtet
                        - marktrolle
                        - rollencodenummer
                      required:
                        - boTyp
                        - versionStruktur
                        - marktrolle
                        - rollencodenummer
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
                        unterbrechbarkeit:
                          type: string
                        waermenutzung:
                          type: string
                        artEMobilitaet:
                          type: string
                      x-apidog-orders:
                        - obisKennzahl
                        - verbrauchsart
                        - unterbrechbarkeit
                        - waermenutzung
                        - artEMobilitaet
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
                  netzebene:
                    type: string
                  umspannung:
                    type: string
                x-apidog-orders:
                  - marktlokationsId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - hausverwalter
                  - lokationsadresse
                  - statusErzeugendeMalo
                  - eigentuemer
                  - redispatch
                  - marktrollen
                  - verguetungEmpfaenger
                  - fernsteuerbarkeit
                  - zaehlwerke
                  - energieherkunft
                  - messtechnischeEinordnung
                  - netzebene
                  - umspannung
                required:
                  - marktlokationsId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                  - messtechnischeEinordnung
                  - netzebene
                  - umspannung
                x-apidog-ignore-properties: []
            NETZNUTZUNGSVERTRAG:
              type: array
              items:
                type: object
                properties:
                  vertragsart:
                    type: string
                    enum:
                      - NETZNUTZUNGSVERTRAG
                    x-apidog-enum:
                      - value: NETZNUTZUNGSVERTRAG
                        name: ''
                        description: ''
                    default: NETZNUTZUNGSVERTRAG
                  vertragspartner2:
                    type: array
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                        versionStruktur:
                          type: string
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
                          type: array
                          items:
                            type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+Z25
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
                        - boTyp
                        - versionStruktur
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
                      boTyp:
                        type: string
                      versionStruktur:
                        type: string
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
                      - boTyp
                      - versionStruktur
                      - partneradresse
                      - name2
                      - anrede
                      - name4
                      - name3
                      - name1
                    required:
                      - boTyp
                      - versionStruktur
                    x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG12.NAD+Z25.RFF+Z46,
                          SG4.IDE+24.SG12.NAD+Z26.RFF+Z46
                      startdatum:
                        type: string
                        description: >-
                          Datum Vertragsbeginn / DTM+92 | EDIFACT:
                          SG4.IDE+24.DTM+92
                        format: date-time
                      enddatum:
                        type: string
                        description: >-
                          Datum Vertragsbeginn / DTM+92 | EDIFACT:
                          SG4.IDE+24.DTM+92
                        format: date-time
                    x-apidog-orders:
                      - zeitraumId
                      - startdatum
                      - enddatum
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
                  - vertragsart
                  - vertragspartner2
                  - korrespondenzpartner
                  - gueltigkeitszeitraum
                  - datenqualitaet
                required:
                  - vertragsart
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
                required:
                  - zeitraumId
                  - verwendungAb
                  - datenqualitaet
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - NETZNUTZUNGSVERTRAG
            - VERWENDUNGSZEITRAUM
          required:
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
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
                marktrolle:
                  type: string
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
                - marktrolle
              required:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
                - marktrolle
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
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
                marktrolle:
                  type: string
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
                - marktrolle
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
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
          x-apidog-orders:
            - empfaenger
            - kategorie
            - absender
            - transaktionsgrund
            - transaktionsgrundergaenzung
          required:
            - empfaenger
            - kategorie
            - absender
            - transaktionsgrund
            - transaktionsgrundergaenzung
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
        stammdaten:
          type: object
          properties:
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z51'
                      startdatum:
                        type: string
                        format: date-time
                      enddatum:
                        type: string
                        format: date-time
                    x-apidog-orders:
                      - zeitraumId
                      - startdatum
                      - enddatum
                    required:
                      - zeitraumId
                      - startdatum
                    x-apidog-ignore-properties: []
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
                  marktrollen:
                    type: array
                    items:
                      type: object
                      properties:
                        boTyp:
                          type: string
                        versionStruktur:
                          type: string
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
                        - boTyp
                        - versionStruktur
                        - messstellenbetreiberEigenschaft
                        - marktrolle
                        - rollencodenummer
                      required:
                        - boTyp
                        - versionStruktur
                        - messstellenbetreiberEigenschaft
                        - marktrolle
                        - rollencodenummer
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - netzlokationsId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                required:
                  - netzlokationsId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z49|Z53]'
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
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                x-apidog-orders:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                  - verwendungBis
                required:
                  - zeitraumId
                  - datenqualitaet
                  - verwendungAb
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZLOKATION
            - VERWENDUNGSZEITRAUM
          required:
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
                marktrolle:
                  type: string
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
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
                - rufnummern
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
                - rollencodenummer
                - rollencodetyp
                - marktrolle
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
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
                marktrolle:
                  type: string
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
                - marktrolle
              required:
                - boTyp
                - versionStruktur
                - rollencodetyp
                - rollencodenummer
                - marktrolle
              x-apidog-ignore-properties: []
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
          x-apidog-orders:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
          required:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55615 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55225:
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
                  netzlokationsId:
                    type: string
                    description: >-
                      Identifikationsnummer einer Netzlokation, an der Energie
                      entweder

                      verbraucht, oder erzeugt wird (Like MarktlokationsId
                      Marktlokation) | EDIFACT: SG4.IDE+24.SG5.LOC+Z18
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                      startdatum:
                        type: string
                        format: date-time
                      enddatum:
                        type: string
                        format: date-time
                    x-apidog-orders:
                      - zeitraumId
                      - startdatum
                      - enddatum
                    required:
                      - zeitraumId
                      - startdatum
                    x-apidog-ignore-properties: []
                  abrechnungsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        artikelId:
                          type: string
                          description: >-
                            ArtikelId gem. BDEW | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z71.PIA+Z02
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
                        abrechnungBlindarbeit:
                          type: boolean
                          description: >-
                            abrechnungBlindarbeit | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z71.SG10.CCI+Z45
                      x-apidog-orders:
                        - artikelId
                        - artikelIdTyp
                        - zahlerBlindarbeit
                        - abrechnungBlindarbeit
                      required:
                        - artikelId
                        - artikelIdTyp
                        - abrechnungBlindarbeit
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - netzlokationsId
                  - gueltigkeitszeitraum
                  - abrechnungsdaten
                required:
                  - gueltigkeitszeitraum
                  - abrechnungsdaten
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
                required:
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZLOKATION
            - VERWENDUNGSZEITRAUM
          required:
            - NETZLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle:
                  type: string
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
                - boTyp
                - versionStruktur
                - marktrolle
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle:
                  type: string
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
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodetyp
                - rollencodenummer
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            sparte:
              type: string
          x-apidog-orders:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
            - sparte
          required:
            - absender
            - empfaenger
            - transaktionsgrund
            - sparte
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55225 - NB (entspricht NBA) an NB (entspricht NBN) - ergänzende Daten
        zum Lokationsbündel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55175:
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
                      x-apidog-orders:
                        - typ
                      required:
                        - typ
                      x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: array
                    items:
                      type: object
                      properties:
                        zeitraumId:
                          type: integer
                      x-apidog-orders:
                        - zeitraumId
                      required:
                        - zeitraumId
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - marktlokationsId
                  - marktlokationsTyp
                  - gueltigkeitszeitraum
                required:
                  - marktlokationsId
                  - marktlokationsTyp
                  - gueltigkeitszeitraum
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
                  gueltigkeitszeitraum:
                    type: array
                    items:
                      type: object
                      properties:
                        zeitraumId:
                          type: integer
                        startdatum:
                          type: string
                          format: date-time
                        enddatum:
                          type: string
                          format: date-time
                      x-apidog-orders:
                        - zeitraumId
                        - startdatum
                        - enddatum
                      required:
                        - zeitraumId
                        - startdatum
                      x-apidog-ignore-properties: []
                  zuordnungObjectcode:
                    type: array
                    items:
                      type: object
                      properties:
                        referenzLokationsTyp:
                          type: string
                        referenzLokationsId:
                          type: string
                        objectcode:
                          type: array
                          items:
                            type: object
                            properties:
                              objectcode:
                                type: string
                              lokationsbuendelNummer:
                                type: integer
                            x-apidog-orders:
                              - objectcode
                              - lokationsbuendelNummer
                            required:
                              - objectcode
                            x-apidog-ignore-properties: []
                        vorgelagerteLokationTyp:
                          type: string
                        vorgelagerteLokationId:
                          type: string
                        referenzMarktlokationTechnischeRessource:
                          type: array
                          items:
                            type: string
                      x-apidog-orders:
                        - referenzLokationsTyp
                        - referenzLokationsId
                        - objectcode
                        - vorgelagerteLokationTyp
                        - vorgelagerteLokationId
                        - referenzMarktlokationTechnischeRessource
                      required:
                        - referenzLokationsTyp
                        - referenzLokationsId
                        - objectcode
                      x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                x-apidog-orders:
                  - lokationsbuendelNummer
                  - lokationsbuendelstrukturId
                  - standardisierteLokationsbuendelstruktur
                  - gueltigkeitszeitraum
                  - zuordnungObjectcode
                  - datenqualitaet
                required:
                  - lokationsbuendelstrukturId
                  - gueltigkeitszeitraum
                  - zuordnungObjectcode
                  - datenqualitaet
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
                  gueltigkeitszeitraum:
                    type: array
                    items:
                      type: object
                      properties:
                        zeitraumId:
                          type: integer
                      x-apidog-orders:
                        - zeitraumId
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - netzlokationsId
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            STEUERBARE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                  gueltigkeitszeitraum:
                    type: array
                    items:
                      type: object
                      properties:
                        zeitraumId:
                          type: string
                      x-apidog-orders:
                        - zeitraumId
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - ressourcenId
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  verwendungBis:
                    type: string
                    format: date-time
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
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
                required:
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
                  gueltigkeitszeitraum:
                    type: array
                    items:
                      type: object
                      properties:
                        zeitraumId:
                          type: string
                      x-apidog-orders:
                        - zeitraumId
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - messlokationsId
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
            TECHNISCHE_RESSOURCE:
              type: array
              items:
                type: object
                properties:
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z20'
                  gueltigkeitszeitraum:
                    type: array
                    items:
                      type: object
                      properties:
                        zeitraumId:
                          type: integer
                      x-apidog-orders:
                        - zeitraumId
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - ressourcenId
                  - gueltigkeitszeitraum
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - MARKTLOKATION
            - LOKATIONSBUENDEL
            - NETZLOKATION
            - STEUERBARE_RESSOURCE
            - VERWENDUNGSZEITRAUM
            - MESSLOKATION
            - TECHNISCHE_RESSOURCE
          required:
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle:
                  type: string
              x-apidog-orders:
                - rufnummern
                - rollencodenummer
                - ansprechpartner
                - rollencodetyp
                - boTyp
                - versionStruktur
                - marktrolle
              required:
                - rollencodenummer
                - rollencodetyp
                - boTyp
                - versionStruktur
                - marktrolle
              x-apidog-ignore-properties: []
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle:
                  type: string
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
                - boTyp
                - versionStruktur
                - marktrolle
              required:
                - rollencodetyp
                - rollencodenummer
                - boTyp
                - versionStruktur
                - marktrolle
              x-apidog-ignore-properties: []
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            sparte:
              type: string
          x-apidog-orders:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
            - sparte
          required:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrund
            - sparte
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 55175 - NB an LF - Änderung vom NB an LF
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55173:
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
      description: 55173 - NB an MSB - Änderung vom NB an MSB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
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
