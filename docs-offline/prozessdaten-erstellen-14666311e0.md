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
        - Schnittstellen/Prozessdaten NB (Backend)
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
          required: true
          schema:
            type: string
            default: ERSTELLEN_PROZESSDATEN
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Prozessdaten%20erstellen%20NB'
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
      x-apidog-folder: Schnittstellen/Prozessdaten NB (Backend)
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14666311-run
components:
  schemas:
    Prozessdaten erstellen NB:
      allOf:
        - anyOf:
            - $ref: '#/components/schemas/PI_55001'
            - $ref: '#/components/schemas/PI_55004'
            - $ref: '#/components/schemas/PI_55077'
            - $ref: '#/components/schemas/PI_55553'
            - $ref: '#/components/schemas/PI_55557'
            - $ref: '#/components/schemas/PI_55639'
            - $ref: '#/components/schemas/PI_55640'
            - $ref: '#/components/schemas/PI_55641'
            - $ref: '#/components/schemas/PI_55642'
            - $ref: '#/components/schemas/PI_55003'
            - $ref: '#/components/schemas/PI_55080'
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
    PI_55080:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            antwortstatusdritterReferenz:
              type: string
              description: 'Antwortstatus Referenz / STS+Z35 | EDIFACT: SG4.IDE+24.STS+Z35'
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E01'
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
              description: 'Anfragekategorie | EDIFACT: BGM+E01'
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
            naechsteBearbeitung:
              type: string
              description: >-
                Datum für nächste Bearbeitung / DTM+Z08 | EDIFACT:
                SG4.IDE+24.DTM+Z08
              format: date-time
            antwortstatusdritterBetroffeneLokation:
              type: string
              description: 'Antwortstatus Lokation / STS+Z35 | EDIFACT: SG4.IDE+24.STS+Z35'
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
            lieferbeginndatuminbearbeitung:
              type: string
              description: >-
                Lieferbeginndatum in Bearbeitung / DTM+Z07 | EDIFACT:
                SG4.IDE+24.DTM+Z07
              format: date-time
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            antwortstatusdritter:
              type: string
              description: 'Antwortstatus / STS+Z35 | EDIFACT: SG4.IDE+24.STS+Z35'
            antwortstatusdritterCodeliste:
              type: string
              description: 'Antwortstatus Codeliste / STS+Z35 | EDIFACT: SG4.IDE+24.STS+Z35'
            antwortstatusCodeliste:
              type: string
              description: 'Antwortstatus Codeliste / STS+E01 | EDIFACT: SG4.IDE+24.STS+E01'
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
            antwortstatus:
              type: string
              description: 'Antwortstatus / STS+E01 | EDIFACT: SG4.IDE+24.STS+E01'
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - antwortstatusdritterReferenz
            - dokumentennummer
            - freitext
            - kategorie
            - absender
            - naechsteBearbeitung
            - antwortstatusdritterBetroffeneLokation
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - lieferbeginndatuminbearbeitung
            - transaktionsgrundergaenzung
            - antwortstatusdritter
            - antwortstatusdritterCodeliste
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
      description: >-
        55080 - NB an LFN - Ablehnung der Anmeldung einer Zuordnung des LFN zur
        Marktlokation bzw. Tranche
      x-apidog-orders:
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55003:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E01'
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
              description: 'Anfragekategorie | EDIFACT: BGM+E01'
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
            naechsteBearbeitung:
              type: string
              description: >-
                Datum für nächste Bearbeitung / DTM+Z08 | EDIFACT:
                SG4.IDE+24.DTM+Z08
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
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            lieferbeginndatuminbearbeitung:
              type: string
              description: >-
                Lieferbeginndatum in Bearbeitung / DTM+Z07 | EDIFACT:
                SG4.IDE+24.DTM+Z07
              format: date-time
            transaktionsgrundergaenzung:
              type: string
              description: >-
                Ergänzung zum Transaktionsgrund / UTILMD STS+7++E01+###+E03 |
                EDIFACT: SG4.IDE+24.STS+7
            antwortstatusdritter:
              type: string
              description: 'Antwortstatus / STS+Z35 | EDIFACT: SG4.IDE+24.STS+Z35'
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
            antwortstatusdritterCodeliste:
              type: string
              description: 'Antwortstatus Codeliste / STS+Z35 | EDIFACT: SG4.IDE+24.STS+Z35'
            antwortstatusCodeliste:
              type: string
              description: 'Antwortstatus Codeliste / STS+E01 | EDIFACT: SG4.IDE+24.STS+E01'
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
            antwortstatus:
              type: string
              description: 'Antwortstatus / STS+E01 | EDIFACT: SG4.IDE+24.STS+E01'
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
            - naechsteBearbeitung
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - lieferbeginndatuminbearbeitung
            - transaktionsgrundergaenzung
            - antwortstatusdritter
            - beteiligterMarktpartner
            - antwortstatusdritterCodeliste
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
      description: >-
        55003 - NB an LFN - Ablehnung der Anmeldung einer Zuordnung des LFN zur
        Marktlokation bzw. Tranche
      x-apidog-orders:
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55642:
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
                                    SG4.IDE+24.SG8.SEQ+Z17.SG10.CCI+++ZA8.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+Z17.SG10.CCI+++ZA8.CAV
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
      description: 55642 - MSB an NB - Änderung vom MSB an NB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55641:
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
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z61.SG10.CCI+++ZA8'
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
      description: 55641 - MSB an NB - Änderung vom MSB an NB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55640:
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
                                    SG4.IDE+24.SG8.SEQ+Z02.SG10.CCI+++ZA8.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+Z02.SG10.CCI+++ZA8.CAV
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
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z59.SG10.CCI+++ZA8'
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
      description: 55640 - MSB an NB - Änderung vom MSB an NB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55639:
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
                                    SG4.IDE+24.SG8.SEQ+Z57.SG10.CCI+++ZA8.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+Z57.SG10.CCI+++ZA8.CAV
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
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z60.SG10.CCI+++ZA8'
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
            kategorie:
              type: string
              title: 'Anfragekategorie EDIFACT: BGM+E03'
              description: 'Anfragekategorie | '
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
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E03'
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
              description: 'Erstellungdatum der EDIFact '
              format: date-time
              title: '/ DTM+137 | EDIFACT: DTM+137'
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
            - kategorie
            - dokumentennummer
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
      description: 55639 - MSB an NB - Änderung vom MSB an NB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55557:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | '
              title: 'EDIFACT: BGM+E03'
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
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+Z76'
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
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+Z76'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  messstellenbetriebsabrechnungsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        anzahl:
                          type: string
                          title: Registeranzahl
                          description: >-
                            Registeranzahl | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z76.SG9.QTY+Z38
                          enum:
                            - EINTARIF
                            - MEHRTARIF
                            - ZWEITARIF
                        artikelId:
                          type: array
                          description: >-
                            ArtikelId gem. BDEW | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z76.PIA+[Z02|Z03]
                          items:
                            type: string
                        messstellenbetriebsabrechnung:
                          type: boolean
                          description: >-
                            messstellenbetriebsabrechnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z76.PIA+[Z02|Z03]
                        abschlag:
                          type: object
                          title: Abschlag
                          description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z76.SG9.QTY+[Z35|Z46]'
                          x-apidog-orders: []
                          properties: {}
                          x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - anzahl
                        - artikelId
                        - messstellenbetriebsabrechnung
                        - abschlag
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - marktlokationsId
                  - datenqualitaet
                  - gueltigkeitszeitraum
                  - messstellenbetriebsabrechnungsdaten
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
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 55557 - MSB an NB - Änderung vom MSB an NB
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
    PI_55077:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E01'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E01'
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
            abtretungserklaerung:
              type: object
              properties:
                link3:
                  type: string
                  description: 'Link Zeile 3 | EDIFACT: SG4.IDE+24.FTX+Z13'
                link1:
                  type: string
                  description: 'Link Zeile 1 | EDIFACT: SG4.IDE+24.FTX+Z13'
                passwort:
                  type: string
                  description: 'Passwort zum Abruf | EDIFACT: SG4.IDE+24.FTX+Z13'
                link5:
                  type: string
                  description: 'Link Zeile 5 | EDIFACT: SG4.IDE+24.FTX+Z13'
                link2:
                  type: string
                  description: 'Link Zeile 2 | EDIFACT: SG4.IDE+24.FTX+Z13'
                link4:
                  type: string
                  description: 'Link Zeile 4 | EDIFACT: SG4.IDE+24.FTX+Z13'
              x-apidog-orders:
                - link3
                - link1
                - passwort
                - link5
                - link2
                - link4
              x-apidog-ignore-properties: []
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
            - abtretungserklaerung
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
                  erforderlichesProduktpaket:
                    type: array
                    items:
                      type: object
                      properties:
                        produktpaket:
                          type: object
                          properties:
                            priorisierung:
                              type: string
                              title: Priorisierung
                              description: >-
                                Priorisierung | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+ZH0.SG10.CCI+Z65.CAV
                              enum:
                                - PRIORITAET1
                                - PRIORITAET2
                                - PRIORITAET3
                                - PRIORITAET4
                                - PRIORITAET5
                            produktpaketId:
                              type: integer
                              description: >-
                                produktpaketId | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z79, SG4.IDE+24.SG8.SEQ+ZH0
                            umsetzungsgradvorgabe:
                              type: string
                              title: Umsetzungsgradvorgabe
                              description: >-
                                Umsetzungsgradvorgabe | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+ZH0.SG10.CCI+Z65
                              enum:
                                - ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
                                - >-
                                  ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR
                          x-apidog-orders:
                            - priorisierung
                            - produktpaketId
                            - umsetzungsgradvorgabe
                          x-apidog-ignore-properties: []
                        produkt:
                          type: array
                          items:
                            type: object
                            properties:
                              produkt:
                                type: object
                                properties:
                                  wertedetails:
                                    type: string
                                    description: >-
                                      wertedetails | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.SG10.CCI+Z66.CAV+ZV4
                                  produktCode:
                                    type: string
                                    description: >-
                                      produktCode | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.PIA+5
                                  codeProdukteigenschaft:
                                    type: string
                                    description: >-
                                      codeProdukteigenschaft | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.SG10.CCI+Z66.CAV+ZH9
                                x-apidog-orders:
                                  - wertedetails
                                  - produktCode
                                  - codeProdukteigenschaft
                                x-apidog-ignore-properties: []
                            x-apidog-orders:
                              - produkt
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - produktpaket
                        - produkt
                      x-apidog-ignore-properties: []
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  foerderungsLand:
                    type: string
                    description: >-
                      foerderungsLand | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z23
                x-apidog-orders:
                  - erforderlichesProduktpaket
                  - marktlokationsId
                  - foerderungsLand
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
        55077 - LFN an NB - Anmeldung einer Zuordnung des LFN zur Marktlokation
        bzw. Tranche
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55004:
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
            - vertragsende
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
        55004 - LF an NB - Abmeldung einer Zuordnung des LF zur Marktlokation
        bzw. Tranche
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55001:
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
                  korrespondenzpartner:
                    type: object
                    properties:
                      partneradresse:
                        type: object
                        properties:
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z04
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+Z04
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
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                          postleitzahl:
                            type: string
                            description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                        x-apidog-orders:
                          - ortsteil
                          - hausnummer
                          - landescode
                          - ort
                          - strasse
                          - postfach
                          - postleitzahl
                        x-apidog-ignore-properties: []
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+Z04
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+Z04'
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z04
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+Z04
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+Z04
                    x-apidog-orders:
                      - partneradresse
                      - name3
                      - name4
                      - name2
                      - name1
                      - anrede
                    x-apidog-ignore-properties: []
                  enFG:
                    type: array
                    items:
                      type: object
                      properties:
                        grund:
                          type: array
                          items:
                            title: Abweichungsgrund
                            description: >-
                              Abweichungsgrund | EDIFACT:
                              SG4.IDE+24.SG8.SEQ+Z75.SG10.CCI+Z61.CAV
                            $ref: >-
                              #/components/schemas/GrundlageVerringerungUmlagenGrund
                        grundlageVerringerungUmlagen:
                          type: string
                          title: GrundlageVerringerungUmlagen
                          description: >-
                            GrundlageVerringerungUmlagen | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+Z75.SG10.CCI+Z61
                          enum:
                            - ERFUELLT_VORAUSSETZUNG_NACH_ENFG
                            - ERFUELLT_NICHT_VORAUSSETZUNG_NACH_ENFG
                            - KEINE_ANGABE
                      x-apidog-orders:
                        - grund
                        - grundlageVerringerungUmlagen
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragspartner2
                  - korrespondenzpartner
                  - enFG
                x-apidog-ignore-properties: []
            MARKTLOKATION:
              type: array
              items:
                type: object
                properties:
                  erforderlichesProduktpaket:
                    type: array
                    items:
                      type: object
                      properties:
                        produktpaket:
                          type: object
                          properties:
                            priorisierung:
                              type: string
                              title: Priorisierung
                              description: >-
                                Priorisierung | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+ZH0.SG10.CCI+Z65.CAV
                              enum:
                                - PRIORITAET1
                                - PRIORITAET2
                                - PRIORITAET3
                                - PRIORITAET4
                                - PRIORITAET5
                            produktpaketId:
                              type: integer
                              description: >-
                                produktpaketId | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+Z79, SG4.IDE+24.SG8.SEQ+ZH0
                            umsetzungsgradvorgabe:
                              type: string
                              title: Umsetzungsgradvorgabe
                              description: >-
                                Umsetzungsgradvorgabe | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+ZH0.SG10.CCI+Z65
                              enum:
                                - ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
                                - >-
                                  ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR
                          x-apidog-orders:
                            - priorisierung
                            - produktpaketId
                            - umsetzungsgradvorgabe
                          x-apidog-ignore-properties: []
                        produkt:
                          type: array
                          items:
                            type: object
                            properties:
                              produkt:
                                type: object
                                properties:
                                  wertedetails:
                                    type: string
                                    description: >-
                                      wertedetails | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.SG10.CCI+Z66.CAV+ZV4
                                  produktCode:
                                    type: string
                                    description: >-
                                      produktCode | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.PIA+5
                                  codeProdukteigenschaft:
                                    type: string
                                    description: >-
                                      codeProdukteigenschaft | EDIFACT:
                                      SG4.IDE+24.SG8.SEQ+Z79.SG10.CCI+Z66.CAV+ZH9
                                x-apidog-orders:
                                  - wertedetails
                                  - produktCode
                                  - codeProdukteigenschaft
                                x-apidog-ignore-properties: []
                            x-apidog-orders:
                              - produkt
                            x-apidog-ignore-properties: []
                      x-apidog-orders:
                        - produktpaket
                        - produkt
                      x-apidog-ignore-properties: []
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
                  - erforderlichesProduktpaket
                  - marktlokationsId
                  - marktlokationsTyp
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
                  vertragskonditionen:
                    type: object
                    properties:
                      haushaltskunde:
                        type: boolean
                        description: >-
                          haushaltskunde | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI
                    x-apidog-orders:
                      - haushaltskunde
                    x-apidog-ignore-properties: []
                  vertragsbeginn:
                    type: string
                    description: 'Datum Vertragsbeginn / DTM+92 | EDIFACT: SG4.IDE+24.DTM+92'
                    format: date-time
                x-apidog-orders:
                  - vertragsende
                  - vertragskonditionen
                  - vertragsbeginn
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - ENERGIELIEFERVERTRAG
            - MARKTLOKATION
            - NETZNUTZUNGSVERTRAG
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
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E01'
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+E01'
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
            - transaktionsgrundergaenzungBefristeteAnmeldung
            - nachrichtendatum
            - nachrichtenreferenznummer
            - vertragsbeginn
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
        55001 - LFN an NB - Anmeldung einer Zuordnung des LFN zur Marktlokation
        bzw. Tranche
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    GrundlageVerringerungUmlagenGrund:
      type: string
      title: GrundlageVerringerungUmlagenGrund
      description: GrundlageVerringerungUmlagenGrund
      enum:
        - ENFG_STROMSPEICHER_UND_VERLUSTENERGIE
        - ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
        - ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN
        - ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF
        - ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN
        - ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN
        - ENFG_SCHIENENBAHNEN
        - ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR
        - ENFG_LANDSTROMANLAGEN
      x-apidog-enum:
        - value: ENFG_STROMSPEICHER_UND_VERLUSTENERGIE
          name: § 21 EnFG Stromspeicher und Verlustenergie
          description: ZU5
        - value: ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN
          name: § 22 EnFG elektrisch angetriebene Wärmepumpen
          description: ZU6
        - value: ENFG_UMLAGEERHEBUNG_BEI_ANLAGEN_ZUR_VERSTROMUNG_VON_KUPPELGASEN
          name: § 23 EnFG Umlageerhebung bei Anlagen zur Verstromung von Kuppelgasen
          description: ZU7
        - value: ENFG_HERSTELLUNG_VON_GRUENEN_WASSERSTOFF
          name: § 24 EnFG Herstellung von Grünen Wasserstof
          description: ZU8
        - value: ENFG_STROMKOSTENINTENSIVE_UNTERNEHMEN
          name: §§ 30 - 35 EnFG stromkostenintensive Unternehmen
          description: ZU9
        - value: >-
            ENFG_HERSTELLUNG_VON_WASSERSTOFF_IN_STROMKOSTENINTENSIVEN_UNTERNEHMEN
          name: >-
            § 36 EnFG Herstellung von Wasserstoff in stromkostenintensiven
            Unternehmen
          description: ZV0
        - value: ENFG_SCHIENENBAHNEN
          name: § 37 EnFG Schienenbahnen
          description: ZV1
        - value: ENFG_ELEKTRISCHE_BETRIEBENE_BUSSEN_IM_LINIENVERKEHR
          name: § 38 EnFG elektrische betriebene Bussen im Linienverkehr
          description: ZV2
        - value: ENFG_LANDSTROMANLAGEN
          name: § 39 EnFG Landstromanlagen
          description: ZV3
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
