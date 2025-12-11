# Abrechnungsdaten Bilanzkreisabrechnung versenden

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
      summary: Abrechnungsdaten Bilanzkreisabrechnung versenden
      deprecated: false
      description: >-
        Triggert den Versand von Abrechnungsdaten Netznutzungsabrechnung
        Nachrichten an Marktpartner durch die MACO APP. Die Anfrage wird
        identifiziert durch den Eventnamen START_ABR_BK. Zusätzlich ist eine
        eindeutige ID prozessId aus dem Backend mit zu übergeben, mit der die
        spätere Antwort vom Marktpartner wieder an das Backend übergeben werden
        kann.
      operationId: START_ABR_BK
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BNB%5D%20START_ABR_BK'
            example:
              stammdaten:
                MARKTLOKATION:
                  - boTyp: MARKTLOKATION
                    versionStruktur: '1'
                    marktlokationsId: '50754496000'
                    sparte: STROM
                    erforderlichesProduktpaket:
                      - produktpaketId: 1
                        produkt:
                          - produktCode: '9991000002082'
                            wertedetails: 11Y0-0000-0077-K
                          - produktCode: '9991000002008'
                            codeProdukteigenschaft: '9991000002115'
                        umsetzungsgradvorgabe: ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
                NETZNUTZUNGSVERTRAG:
                  - boTyp: VERTRAG
                    versionStruktur: '1'
                    vertragsart: NETZNUTZUNGSVERTRAG
                    sparte: STROM
                    vertragsbeginn: '2025-10-31T23:00:00Z'
                    vertragskonditionen:
                      haushaltskunde: true
                ENERGIELIEFERVERTRAG:
                  - boTyp: VERTRAG
                    versionStruktur: '1'
                    vertragsart: ENERGIELIEFERVERTRAG
                    sparte: STROM
                    vertragspartner2:
                      - boTyp: GESCHAEFTSPARTNER
                        versionStruktur: '1'
                        anrede: Herr
                        name1: Glöppel
                        name2: Walter
                        gewerbekennzeichnung: false
                        geschaeftspartnerrolle:
                          - KUNDE
                    korrespondenzpartner:
                      boTyp: GESCHAEFTSPARTNER
                      versionStruktur: '1'
                      name1: Glöppel
                      gewerbekennzeichnung: false
                      partneradresse:
                        postleitzahl: '41515'
                        ort: Grevenbroich
                        strasse: Bahnstraße
                        hausnummer: '49'
                        landescode: DE
                    enFG:
                      - grundlageVerringerungUmlagen: ERFUELLT_VORAUSSETZUNG_NACH_ENFG
                        grund:
                          - ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
              transaktionsdaten:
                sparte: STROM
                transaktionsgrund: E01
                transaktionsgrundergaenzung: ZW4
                absender:
                  boTyp: MARKTTEILNEHMER
                  versionStruktur: '1'
                  rollencodenummer: '9903526000002'
                  rollencodetyp: BDEW
                empfaenger:
                  boTyp: MARKTTEILNEHMER
                  versionStruktur: '1'
                  rollencodenummer: '9900683000008'
                  rollencodetyp: BDEW
                kategorie: E01
              zusatzdaten:
                prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                eventname: START_ABR_BK
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14994259-run
components:
  schemas:
    '[NB] START_ABR_BK':
      allOf:
        - oneOf:
            - $ref: '#/components/schemas/PI_55126'
            - $ref: '#/components/schemas/PI_55613'
            - $ref: '#/components/schemas/PI_55672'
            - $ref: '#/components/schemas/PI_55674'
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
                  const: START_ABR_BK
                  default: START_ABR_BK
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
    PI_55674:
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
                            SG4.IDE+24.SG8.SEQ+Z15.SG10.CCI+++ZB3.CAV+Z89
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
                            SG4.IDE+24.SG8.SEQ+Z15.SG10.CCI+++ZB3.CAV+Z89
                      x-apidog-orders:
                        - marktrolle
                        - rollencodenummer
                      x-apidog-ignore-properties: []
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
                  - marktrollen
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
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z89,
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z89,
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z89,
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z89,
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
                      x-apidog-orders:
                        - rollencodenummer
                        - marktrolle
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
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01,
                      SG4.IDE+24.SG8.SEQ+Z98
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
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z20,
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+Z20
                  netzebene:
                    type: string
                    title: Netzebene
                    description: >-
                      Netzebene | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++E03.CAV,
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
                  - marktrollen
                  - marktlokationsId
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - bilanzierungsgebiet
                  - netzebene
                x-apidog-ignore-properties: []
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  zeitreihentyp:
                    type: string
                    title: Zeitreihentyp
                    description: >-
                      Zeitreihentyp | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+15+Z21.CAV,
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+15+Z21.CAV
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
                  prognosegrundlage:
                    type: string
                    title: Prognosegrundlage
                    description: >-
                      Prognosegrundlage | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZC0,
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZC0
                    enum:
                      - WERTE
                      - PROFILE
                  bilanzkreis:
                    type: object
                    title: Bilanzkreis
                    description: >-
                      EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z19,
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+Z19
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zeitreihentyp
                  - prognosegrundlage
                  - bilanzkreis
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
            - MARKTLOKATION
            - BILANZIERUNG
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle: &ref_0
                  $ref: '#/components/schemas/Marktrolle'
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp: &ref_1
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MS'
                  $ref: '#/components/schemas/Rollencodetyp'
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: string
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                      nummerntyp: &ref_2
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                        $ref: '#/components/schemas/Rufnummernart'
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
                - rollencodenummer
                - rollencodetyp
                - rufnummern
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle: *ref_0
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
                rollencodetyp: *ref_1
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
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
            - empfaenger
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          required:
            - absender
            - empfaenger
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z21,
                          SG4.IDE+24.SG8.SEQ+Z08, SG4.IDE+24.SG8.SEQ+Z38
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
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - lastprofile
                  - zeitreihentyp
                  - temperaturarbeit
                  - prognosegrundlage
                  - bilanzkreis
                  - detailsPrognosegrundlage
                  - aggregationsverantwortung
                  - jahresverbrauchsprognose
                required:
                  - prognosegrundlage
                  - aggregationsverantwortung
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
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
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
                        - boTyp
                        - versionStruktur
                        - rollencodenummer
                        - marktrolle
                      required:
                        - boTyp
                        - versionStruktur
                        - rollencodenummer
                        - marktrolle
                      x-apidog-ignore-properties: []
                  regelzone:
                    type: string
                    description: >-
                      für EDIFACT mapping | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z18
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
                  bilanzierungsgebiet:
                    type: string
                    description: >-
                      Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist -
                      im Falle eines Strom Netzes. | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z20
                x-apidog-orders:
                  - marktlokationsId
                  - marktrollen
                  - regelzone
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - bilanzierungsgebiet
                required:
                  - marktlokationsId
                  - marktrollen
                  - regelzone
                  - datenqualitaet
                  - gueltigkeitszeitraum
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
            - BILANZIERUNG
            - TRANCHE
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle: *ref_0
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp: *ref_1
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: string
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
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
                - rollencodenummer
                - rollencodetyp
                - rufnummern
                - ansprechpartner
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
                rollencodetyp: *ref_1
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
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
            - transaktionsgrundergaenzung
            - transaktionsgrund
          required:
            - kategorie
            - absender
            - empfaenger
            - transaktionsgrundergaenzung
            - transaktionsgrund
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55613:
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
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01'
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
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01,
                      SG4.IDE+24.SG8.SEQ+Z98
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
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z89,
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z89,
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z91
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z89,
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+++ZB3.CAV+Z89,
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
                      x-apidog-orders:
                        - boTyp
                        - versionStruktur
                        - rollencodenummer
                        - marktrolle
                      required:
                        - boTyp
                        - versionStruktur
                        - rollencodenummer
                        - marktrolle
                      x-apidog-ignore-properties: []
                  bilanzierungsgebiet:
                    type: string
                    description: >-
                      Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist -
                      im Falle eines Strom Netzes. | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z20,
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+Z20
                  netzebene:
                    type: string
                    title: Netzebene
                    description: >-
                      Netzebene | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++E03.CAV,
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
                  umspannung:
                    type: string
                x-apidog-orders:
                  - marktlokationsId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                  - bilanzierungsgebiet
                  - netzebene
                  - umspannung
                required:
                  - marktlokationsId
                  - marktrollen
                x-apidog-ignore-properties: []
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  zeitreihentyp:
                    type: string
                    title: Zeitreihentyp
                    description: >-
                      Zeitreihentyp | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+15+Z21.CAV,
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+15+Z21.CAV
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
                  lastprofile:
                    type: array
                    items:
                      type: object
                      properties:
                        bezeichnung:
                          type: string
                          description: >-
                            Externe Bezeichnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02.CAV
                        profilart:
                          type: string
                          title: Profilart
                          description: >-
                            Profilart | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02
                          enum:
                            - ART_STANDARDLASTPROFIL
                            - ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL
                            - ART_LASTPROFIL
                        einspeisung:
                          type: boolean
                          description: >-
                            Kennzeichen Einspeisung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02
                        verfahren:
                          type: string
                          title: Profilverfahren
                          description: >-
                            Profilverfahren | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z21.SG10.CCI+Z02
                          enum:
                            - SYNTHETISCH
                            - ANALYTISCH
                      x-apidog-orders:
                        - bezeichnung
                        - profilart
                        - einspeisung
                        - verfahren
                      x-apidog-ignore-properties: []
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z21'
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
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z21'
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
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI,
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI
                    enum:
                      - WERTE
                      - PROFILE
                  bilanzkreis:
                    type: string
                    title: Bilanzkreis
                    description: >-
                      EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z19,
                      SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI+Z19
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
                        SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI.CAV+E02,
                        SG4.IDE+24.SG8.SEQ+Z98.SG10.CCI.CAV+E02
                      items:
                        type: string
                        title: Profiltyp
                        description: Profiltyp
                        enum:
                          - SLP_SEP
                          - TLP_TEP
                          - TEP
                  jahresverbrauchsprognose:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: >-
                          EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+31,
                          SG4.IDE+24.SG8.SEQ+Z98.SG9.QTY+31
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+31,
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
                    x-apidog-orders:
                      - wert
                      - einheit
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - zeitreihentyp
                  - lastprofile
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - prognosegrundlage
                  - bilanzkreis
                  - detailsPrognosegrundlage
                  - jahresverbrauchsprognose
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
            - MARKTLOKATION
            - BILANZIERUNG
            - VERWENDUNGSZEITRAUM
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle: *ref_0
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp: *ref_1
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: string
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                      nummerntyp: *ref_2
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
                - rollencodenummer
                - rollencodetyp
                - rufnummern
                - ansprechpartner
              required:
                - boTyp
                - versionStruktur
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
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
                rollencodetyp: *ref_1
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
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
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
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
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: >-
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z21,
                          SG4.IDE+24.SG8.SEQ+Z08
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
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - lastprofile
                  - zeitreihentyp
                  - temperaturarbeit
                  - prognosegrundlage
                  - bilanzkreis
                  - detailsPrognosegrundlage
                  - aggregationsverantwortung
                  - jahresverbrauchsprognose
                required:
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - prognosegrundlage
                  - aggregationsverantwortung
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
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z01'
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
                            SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+++ZB3.CAV+Z90
                        rollencodetyp:
                          type: string
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
                        - boTyp
                        - versionStruktur
                        - rollencodenummer
                        - rollencodetyp
                        - marktrolle
                      required:
                        - boTyp
                        - versionStruktur
                        - rollencodenummer
                        - rollencodetyp
                        - marktrolle
                      x-apidog-ignore-properties: []
                  regelzone:
                    type: string
                    description: >-
                      für EDIFACT mapping | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z18
                  bilanzierungsgebiet:
                    type: string
                    description: >-
                      Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist -
                      im Falle eines Strom Netzes. | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z20
                x-apidog-orders:
                  - marktlokationsId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                  - regelzone
                  - bilanzierungsgebiet
                required:
                  - marktlokationsId
                  - gueltigkeitszeitraum
                  - datenqualitaet
                  - marktrollen
                  - regelzone
                  - bilanzierungsgebiet
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
            - BILANZIERUNG
            - MARKTLOKATION
            - VERWENDUNGSZEITRAUM
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
                boTyp:
                  type: string
                versionStruktur:
                  type: string
                marktrolle: *ref_0
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MS'
                rollencodetyp: *ref_1
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      rufnummer:
                        type: string
                        title: Rufnummer
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA.COM+[EM|FX|TE|AJ|AL]'
                      nummerntyp: *ref_2
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
                - rollencodenummer
                - rollencodetyp
                - rufnummern
                - ansprechpartner
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
                marktrolle: *ref_0
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
                rollencodetyp: *ref_1
              x-apidog-orders:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
              required:
                - boTyp
                - versionStruktur
                - marktrolle
                - rollencodenummer
                - rollencodetyp
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
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
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
