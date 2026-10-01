# Abrechnungsdaten Netznutzungsabrechnung versenden

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
      summary: Abrechnungsdaten Netznutzungsabrechnung versenden
      deprecated: false
      description: >-
        Triggert den Versand von Abrechnungsdaten Netznutzungsabrechnung
        Nachrichten an Marktpartner durch die MACO APP. Die Anfrage wird
        identifiziert durch den Eventnamen START_ABR_NN. Zusätzlich ist eine
        eindeutige ID prozessId aus dem Backend mit zu übergeben, mit der die
        spätere Antwort vom Marktpartner wieder an das Backend übergeben werden
        kann.
      operationId: START_ABR_NN
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht NB
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BNB%5D%20START_ABR_NN'
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
                eventname: START_ABR_NN
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14333071-run
components:
  schemas:
    '[NB] START_ABR_NN':
      allOf:
        - $ref: '#/components/schemas/PI_55218'
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
                  const: START_ABR_NN
                  default: START_ABR_NN
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
                              type: string
                              title: Zaehlzeitdefinition
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[Z45|Z84].SG10.CCI+Z39
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
                      required:
                        - artikelIdTyp
                        - artikelId
                        - gemeinderabatt
                      x-apidog-ignore-properties: []
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
                  - marktlokationsId
                  - datenqualitaet
                  - netznutzungsabrechnungsdaten
                  - gueltigkeitszeitraum
                  - netzbetreiberCodeNr
                required:
                  - marktlokationsId
                  - netznutzungsabrechnungsdaten
                  - netzbetreiberCodeNr
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
                        required:
                          - abrechnungsZeitraum
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - naechstenetznutzungsabrechnung
                      - netznutzungsvertrag
                      - netznutzungsabrechnungIntervall
                      - netznutzungszahler
                      - netznutzungsabrechnungsgrundlage
                      - netznutzungsabrechnung
                    required:
                      - naechstenetznutzungsabrechnung
                      - netznutzungsvertrag
                      - netznutzungsabrechnungIntervall
                      - netznutzungszahler
                      - netznutzungsabrechnungsgrundlage
                      - netznutzungsabrechnung
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragsart
                  - vertragskonditionen
                required:
                  - vertragsart
                  - vertragskonditionen
                x-apidog-ignore-properties: []
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  boTyp:
                    type: string
                  versionStruktur:
                    type: string
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
                  - boTyp
                  - versionStruktur
                  - verwendungBis
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                required:
                  - boTyp
                  - versionStruktur
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - BILANZIERUNG
            - MARKTLOKATION
            - NETZNUTZUNGSVERTRAG
            - VERWENDUNGSZEITRAUM
          required:
            - MARKTLOKATION
            - NETZNUTZUNGSVERTRAG
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
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
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
            - nachrichtendatum
            - empfaenger
            - transaktionsgrund
          required:
            - kategorie
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
