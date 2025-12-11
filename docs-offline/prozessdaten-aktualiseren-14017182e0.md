# Prozessdaten aktualiseren

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /updateProcessData:
    post:
      summary: Prozessdaten aktualiseren
      deprecated: false
      description: Aktualisieren der Prozessdaten anhand des BusinessKey.
      operationId: AKTUALISIEREN_PROZESSDATEN
      tags:
        - Schnittstellen/Prozessdaten LF (Backend)
        - AKTUALISIEREN | UPDATE
      parameters:
        - name: command
          in: query
          description: >
            Name der Operation | Name of the operation (MACO APP internal
            assignment  between process and interface)
          required: true
          schema:
            type: string
            default: AKTUALISIEREN_PROZESSDATEN
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Prozessdaten%20aktualisieren%20LF'
            example: ''
      responses:
        '200':
          description: Erfolgreiches Aktualisieren des MDOCS
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
          description: Fehler beim Aktualisieren des MDOCS
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017182-run
components:
  schemas:
    Prozessdaten aktualisieren LF:
      allOf:
        - anyOf:
            - $ref: '#/components/schemas/PI_55017'
            - $ref: '#/components/schemas/PI_55018'
            - $ref: '#/components/schemas/PI_55005'
            - $ref: '#/components/schemas/PI_55006'
            - $ref: '#/components/schemas/PI_55008'
            - $ref: '#/components/schemas/PI_55009'
            - $ref: '#/components/schemas/PI_55002'
            - $ref: '#/components/schemas/PI_55003'
            - &ref_0
              $ref: '#/components/schemas/PI_55078'
            - &ref_1
              $ref: '#/components/schemas/PI_55080'
            - $ref: '#/components/schemas/PI_55011'
            - $ref: '#/components/schemas/PI_55012'
            - $ref: '#/components/schemas/PI_55038'
            - $ref: '#/components/schemas/PI_55037'
            - $ref: '#/components/schemas/PI_55014'
            - $ref: '#/components/schemas/PI_55015'
            - $ref: '#/components/schemas/PI_55156'
            - $ref: '#/components/schemas/PI_55220'
            - $ref: '#/components/schemas/PI_21047'
            - $ref: '#/components/schemas/PI_55621'
            - $ref: '#/components/schemas/PI_55622'
            - $ref: '#/components/schemas/PI_55623'
            - $ref: '#/components/schemas/PI_55624'
            - $ref: '#/components/schemas/PI_55625'
            - $ref: '#/components/schemas/PI_55626'
            - $ref: '#/components/schemas/PI_55627'
            - $ref: '#/components/schemas/PI_55180'
            - $ref: '#/components/schemas/PI_55654'
            - $ref: '#/components/schemas/PI_55655'
            - $ref: '#/components/schemas/PI_55656'
            - $ref: '#/components/schemas/PI_55657'
            - $ref: '#/components/schemas/PI_25001'
            - $ref: '#/components/schemas/PI_55608'
            - $ref: '#/components/schemas/PI_55609'
            - $ref: '#/components/schemas/PI_55077'
            - *ref_0
            - *ref_1
            - $ref: '#/components/schemas/PI_55023'
            - $ref: '#/components/schemas/PI_55024'
            - $ref: '#/components/schemas/PI_55022'
        - $ref: '#/components/schemas/ZUSATZDATEN%20(%20SST%20Aktualisieren)'
      x-apidog-folder: ''
    ZUSATZDATEN ( SST Aktualisieren):
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
            - targetBusinessKey
          x-apidog-ignore-properties: []
      x-apidog-orders:
        - zusatzdaten
      required:
        - zusatzdaten
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
    PI_55024:
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
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
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
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
      description: >-
        55024 - Empfänger einer Stornierungsanfrage an Sender einer
        Stornierungsanfrage - Ablehnung Anfrage Stornierung
      x-apidog-orders:
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55023:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            absender:
              type: object
              properties:
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
                - rollencodetyp
                - rollencodenummer
                - rufnummern
                - ansprechpartner
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            empfaenger:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
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
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E01|E02|E35]
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
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            antwortstatus:
              type: string
              description: 'Antwortstatus / STS+E01 | EDIFACT: SG4.IDE+24.STS+E01'
            antwortstatusCodeliste:
              type: string
              description: 'Antwortstatus Codeliste / STS+E01 | EDIFACT: SG4.IDE+24.STS+E01'
          x-apidog-orders:
            - absender
            - anfragereferenznummer
            - empfaenger
            - nachrichtendatum
            - nachrichtenreferenznummer
            - pruefidentifikator
            - dokumentennummer
            - kategorie
            - vorgangsnummer
            - transaktionsgrund
            - antwortstatus
            - antwortstatusCodeliste
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
      description: >-
        55023 - Empfänger einer Stornierungsanfrage an Sender einer
        Stornierungsanfrage - Bestätigung Anfrage Stornierung
      x-apidog-orders:
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
    PI_55609:
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
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - transaktionsgrundergaenzung
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
      description: >-
        55609 - LFN an NB - Antwort auf Ankündigung der Zuordnung des LFN zur
        Tranche
      x-apidog-orders:
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55608:
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
            - vertragsende
            - dokumentennummer
            - kategorie
            - absender
            - transaktionsgrundergaenzungBefristeteAnmeldung
            - nachrichtendatum
            - abtretungserklaerung
            - nachrichtenreferenznummer
            - vertragsbeginn
            - empfaenger
            - anfragereferenznummer
            - transaktionsgrundergaenzung
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
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
                x-apidog-orders:
                  - erforderlichesProduktpaket
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
          x-apidog-orders:
            - MARKTLOKATION
            - NETZNUTZUNGSVERTRAG
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55608 - LFN an NB - Antwort auf Ankündigung der Zuordnung des LFN zur
        Tranche
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_25001:
      type: object
      properties:
        stammdaten:
          type: object
          properties:
            VERWENDUNGSZEITRAUM:
              type: array
              items:
                type: object
                properties:
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG5.IDE+24.SG6.RFF+[Z49|Z53]'
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
                      SG5.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG5.IDE+24.SG6.RFF+[Z49|Z53]'
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG5.IDE+24.SG6.RFF+[Z49|Z53].DTM+Z26
                    format: date-time
                x-apidog-orders:
                  - datenqualitaet
                  - verwendungAb
                  - zeitraumId
                  - verwendungBis
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - VERWENDUNGSZEITRAUM
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            absender:
              type: object
              properties:
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
                        SG2.NAD+MS.SG3.CTA+IC
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | EDIFACT:
                        SG2.NAD+MS.SG3.CTA+IC.COM+[EM|FX|TE|AJ|AL]
                  x-apidog-orders:
                    - nachname
                    - eMailAdresse
                  x-apidog-ignore-properties: []
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      nummerntyp:
                        type: string
                        title: Rufnummernart
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA+IC.COM+[EM|FX|TE|AJ|AL]'
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
                        description: 'EDIFACT: SG2.NAD+MS.SG3.CTA+IC.COM+[EM|FX|TE|AJ|AL]'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
                - ansprechpartner
                - rufnummern
              x-apidog-ignore-properties: []
            lokationsId:
              type: string
              description: 'Referenz auf die Lokation / LOC | EDIFACT: SG5.IDE+24.LOC+172'
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG5.IDE+24.SG6.RFF+Z13
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+Z36'
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG5.IDE+24
          x-apidog-orders:
            - absender
            - lokationsId
            - pruefidentifikator
            - dokumentennummer
            - nachrichtendatum
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 25001 - NB an LF - Berechnungsformel
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55657:
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
                                    SG4.IDE+24.SG8.SEQ+[Z99|ZA0].SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[Z99|ZA0].SG10.CCI+++ZA7.CAV
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
                            SG4.IDE+24.SG8.SEQ+[Z99|ZA0].PIA+5
                      x-apidog-orders:
                        - verwendungszwecke
                        - obisKennzahl
                      x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z99|ZA0]'
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
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z99|ZA0]'
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
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
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55657 - LF an MSB - Bestellung einer Änderung von Stammdaten vom LF an
        MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55656:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
            - anfragereferenznummer
            - antwortStatusZeitraum
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
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++ZA7'
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
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2],
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  zugeordneteDefinition:
                    type: object
                    properties:
                      schaltzeitdefinition:
                        type: object
                        title: Schaltzeitdefinition
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+[Z52|Z53]
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
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+[Z52|Z53]
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
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++ZB3.CAV+[Z88|Z89]
                      marktrolle:
                        type: string
                        title: Marktrolle
                        description: >-
                          Diese Rollen kann ein Marktteilnehmer einnehmen |
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].SG10.CCI+++ZB3.CAV+[Z88|Z89]
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
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2],
                      SG4.IDE+24.SG8.SEQ+[ZB3|ZB4]
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
                      SG4.IDE+24.SG8.SEQ+[ZB3|ZB4].PIA+5
                  ressourcenId:
                    type: string
                    description: 'ressourcenId | EDIFACT: SG4.IDE+24.SG5.LOC+Z19'
                  steuerkanal:
                    type: object
                    title: AdHocSteuerkanal
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2].SG10.CCI+Z49.CAV+ZF2'
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
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
        55656 - LF an MSB - Bestellung einer Änderung von Stammdaten vom LF an
        MSB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55655:
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
                            SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].PIA+5
                        wertegranularitaet:
                          type: string
                          title: Wertegranularitaet
                          description: >-
                            Wertegranularitaet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZE4.CAV+[ZD9|ZE8|ZE9|ZB7]
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
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+Z39
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
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+Z38
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
                                    SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[ZA1|ZA2].SG10.CCI+++ZA7.CAV
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
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z51|Z52],
                      SG4.IDE+24.SG8.SEQ+[ZA1|ZA2], SG4.IDE+24.SG8.SEQ+[ZB5|ZB6]
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
                          zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z51|Z52],
                          SG4.IDE+24.SG8.SEQ+[ZA1|ZA2],
                          SG4.IDE+24.SG8.SEQ+[ZB5|ZB6]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  produktdatenRelevanteRolle:
                    type: string
                    title: Marktrolle
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+++ZA7'
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
                      SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].PIA+5,
                      SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+11
                  leistungskurvendefinition:
                    type: object
                    title: Leistungskurvendefinition
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB5|ZB6].SG10.CCI+Z53'
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
                              SG4.IDE+24.SG6.RFF+[Z51|Z52].DTM+752
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
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
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55655 - LF an MSB - Bestellung einer Änderung von Stammdaten vom LF an
        MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55654:
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
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++ZB3.CAV+[Z88|Z89]
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
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++ZB3.CAV+[Z88|Z89]
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
                            SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].PIA+5
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
                                    SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].SG10.CCI+++ZA7.CAV
                                  x-apidog-orders: []
                                  properties: {}
                                  x-apidog-ignore-properties: []
                              marktrolle:
                                type: string
                                title: Marktrolle
                                description: >-
                                  Diese Rollen kann ein Marktteilnehmer
                                  einnehmen | EDIFACT:
                                  SG4.IDE+24.SG8.SEQ+[ZA7|ZA8].SG10.CCI+++ZA7.CAV
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
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+++[ZA7|ZA8]'
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
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0],
                          SG4.IDE+24.SG8.SEQ+[ZA7|ZA8],
                          SG4.IDE+24.SG8.SEQ+[ZG8|ZG9]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  steuerkanal:
                    type: object
                    title: AdHocSteuerkanal
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0].SG10.CCI+Z49'
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
                      SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+11
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0],
                      SG4.IDE+24.SG8.SEQ+[ZA7|ZA8], SG4.IDE+24.SG8.SEQ+[ZG8|ZG9]
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
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].SG10.CCI+Z53'
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
                      SG4.IDE+24.SG8.SEQ+[ZG8|ZG9].PIA+5
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48]'
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48]'
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
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55654 - LF an MSB - Bestellung einer Änderung von Stammdaten vom LF an
        MSB
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55180:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - vorgangsnummer
            - antwortStatusZeitraum
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
                      SG4.IDE+24.SG8.SEQ+[ZC7|ZC8].RFF+[Z31|Z39]
                  lokationsbuendelstrukturId:
                    type: string
                    description: >-
                      lokationsbuendelstrukturId | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZC7|ZC8].RFF+[Z31|Z39]
                  standardisierteLokationsbuendelstruktur:
                    type: boolean
                    description: >-
                      standardisierteLokationsbuendelstruktur | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZC7|ZC8].RFF+[Z31|Z39]
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZC7|ZC8],
                      SG4.IDE+24.SG8.SEQ+[ZC9|ZD0]
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
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZC7|ZC8],
                          SG4.IDE+24.SG8.SEQ+[ZC9|ZD0]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - lokationsbuendelNummer
                  - lokationsbuendelstrukturId
                  - standardisierteLokationsbuendelstruktur
                  - datenqualitaet
                  - gueltigkeitszeitraum
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
                                SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+Z33
                            objectcode:
                              type: object
                              title: Objectcode
                              description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+Z33'
                              x-apidog-orders: []
                          x-apidog-orders:
                            - lokationsbuendelNummer
                            - objectcode
                      vorgelagerteLokationId:
                        type: string
                        description: >-
                          vorgelagerteLokationId | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+[Z34|Z35]
                      referenzMarktlokationTechnischeRessource:
                        type: array
                        items:
                          type: array
                          description: >-
                            referenzMarktlokationTechnischeRessource | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+Z16
                          items:
                            type: string
                      referenzLokationsTyp:
                        type: string
                        title: Lokationstyp
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+[Z32|Z18|Z19|Z37]
                        enum:
                          - MALO
                          - MELO
                          - NELO
                          - TECHNISCHE_RESSOURCE
                      vorgelagerteLokationTyp:
                        type: string
                        title: Lokationstyp
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+[Z34|Z35]'
                        enum:
                          - MALO
                          - MELO
                          - NELO
                          - TECHNISCHE_RESSOURCE
                      referenzLokationsId:
                        type: string
                        description: >-
                          referenzLokationsId | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZC9|ZD0].RFF+[Z32|Z18|Z19|Z37]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
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
      description: "55180 - LF an NB - Bestellung einer Änderung von Stammdaten vom \_LF an NB"
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55627:
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
      description: 55627 - NB an MSB - Änderung vom NB an MSB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55626:
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
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+ZF0
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+Z91
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+Z91
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
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+Z91,
                            SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].SG10.CCI+++ZB3.CAV+ZF0
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
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG6|ZG7]'
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
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG6|ZG7]'
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
                          SG4.IDE+24.SG8.SEQ+[ZG6|ZG7].RFF+Z05
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
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
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: "55626 - LF an NB - Bestellung einer Änderung von Stammdaten vom \_LF an NB"
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55625:
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
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z94|Z95]'
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
                      SG4.IDE+24.SG8.SEQ+[Z94|Z95].SG10.CCI+++Z89.CAV
                    enum:
                      - KUNDE
                      - LIEFERANT
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z94|Z95]'
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
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
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
            - anfragereferenznummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: "55625 - LF an NB - Bestellung einer Änderung von Stammdaten vom \_LF an NB"
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55624:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
            - anfragereferenznummer
            - antwortStatusZeitraum
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
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZB1|ZB2]'
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
                            SG4.IDE+24.SG8.SEQ+[ZB1|ZB2].SG10.CCI+++ZB3.CAV+Z91
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
                            SG4.IDE+24.SG8.SEQ+[ZB1|ZB2].SG10.CCI+++ZB3.CAV+Z91
                        messstellenbetreiberEigenschaft:
                          type: string
                          title: MSBEigenschaft
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZB1|ZB2].SG10.CCI+++ZB3.CAV+Z91
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
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
      description: "55624 - LF an NB - Bestellung einer Änderung von Stammdaten vom \_LF an NB"
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55623:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03+Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03+Z88]'
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
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - vorgangsnummer
            - antwortStatusZeitraum
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
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56].CAV+[ZH2|ZH3|ZH4|ZH5]
                    enum:
                      - IMS
                      - KME_MME
                      - KEINE_MESSUNG
                  weitereEinrichtung:
                    type: boolean
                    description: >-
                      weitereEinrichtung | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+Z63.CAV+[ZH7|ZH8]
                  nennleistung:
                    type: object
                    properties:
                      aufnahme:
                        type: number
                        description: >-
                          Aufnahme der Nennleistung | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG9.QTY+Z43
                        format: float
                      abgabe:
                        type: object
                        title: Konzessionsabgabe
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG9.QTY+Z44'
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
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].RFF+Z32
                  enwg:
                    type: boolean
                    description: >-
                      enwg | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56].CAV+[ZG8|ZG9]
                  speicherkapazitaet:
                    type: number
                    description: >-
                      Speicherkapazität

                      Beispiel: QTY+Z42:100:KWH' | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG9.QTY+Z42
                    format: float
                  gueltigkeitszeitraum:
                    type: object
                    properties:
                      zeitraumId:
                        type: integer
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG4|ZG5]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  erzeugungsart:
                    type: string
                    title: Erzeugungsart
                    description: >-
                      Auflistung der Erzeugungsarten von Energie. | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56].CAV+[ZF5|ZF6|ZG0|ZG1|ZG5]
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
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].RFF+Z38
                  speicherart:
                    type: string
                    title: Speicherart
                    description: >-
                      Speicherart | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56].CAV+[ZF7|ZF8|ZF9|ZG6]
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
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56]
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
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56].CAV
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
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZG4|ZG5]'
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
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56].CAV+[Z64|Z65|ZE5|ZA8]
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
                      SG4.IDE+24.SG8.SEQ+[ZG4|ZG5].SG10.CCI+[Z17|Z50|Z56].CAV+[ZH0|ZH1]
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
                  - gueltigkeitszeitraum
                  - erzeugungsart
                  - referenzSteuerbareRessource
                  - speicherart
                  - art
                  - waermenutzung
                  - datenqualitaet
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
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
      description: "55623 - LF an NB - Bestellung einer Änderung von Stammdaten vom \_LF an NB"
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55622:
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

                            oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z51|Z52]
                        anrede:
                          type: string
                          description: >-
                            Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z51|Z52]
                        geschaeftspartnerrolle:
                          type: string
                          title: Geschaeftspartnerrolle
                          description: >-
                            Geschaeftspartnerrolle | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z51|Z52]
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

                            oder Sängerin | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z51|Z52]
                        name4:
                          type: string
                          description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z51|Z52]'
                        name2:
                          type: string
                          description: >-
                            Zweiter Teil des Namens. Hier kann der eine
                            Erweiterung zum Firmennamen oder

                            bei Privatpersonen beispielsweise der Vorname
                            dargestellt werden. Beispiele:

                            Bereich Süd oder Nina | EDIFACT:
                            SG4.IDE+24.SG12.NAD+[Z51|Z52]
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
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]'
                          ortsteil:
                            type: string
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]'
                          postleitzahl:
                            type: string
                            description: >-
                              Postleitzahl | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z53|Z54]
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z53|Z54]
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
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]'
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]'
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z53|Z54]
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
                          SG4.IDE+24.SG12.NAD+[Z53|Z54]
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z53|Z54]
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]'
                      name3:
                        type: string
                        description: >-
                          Dritter Teil des Namens. Hier können weitere
                          Ergänzungen zum Firmennamen oder

                          bei Privatpersonen Zusätze zum Namen dargestellt
                          werden. Beispiele: und Afrika

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z53|Z54]
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
                          zeitraumId | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z51|Z52].RFF+Z46,
                          SG4.IDE+24.SG12.NAD+[Z53|Z54].RFF+Z46
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG12.NAD+[Z51|Z52],
                      SG4.IDE+24.SG12.NAD+[Z53|Z54]
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
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z80|Z81],
                      SG4.IDE+24.SG8.SEQ+[ZD1|ZD2],
                      SG4.IDE+24.SG8.SEQ+[ZD3|ZD4],
                      SG4.IDE+24.SG12.NAD+[Z55|Z56],
                      SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58],
                      SG4.IDE+24.SG12.NAD+[Z59|Z60]
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
                          SG4.IDE+24.SG12.NAD+[Z59|Z60]
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
                            description: >-
                              Adresszusatz 4 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z59|Z60]
                          zusatz1:
                            type: string
                            description: >-
                              Adresszusatz 1 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z59|Z60]
                          zusatz2:
                            type: string
                            description: >-
                              Adresszusatz 2 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z59|Z60]
                          zusatz5:
                            type: string
                            description: >-
                              Adresszusatz 5 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z59|Z60]
                          zusatz3:
                            type: string
                            description: >-
                              Adresszusatz 3 | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z59|Z60]
                        x-apidog-orders:
                          - zusatz4
                          - zusatz1
                          - zusatz2
                          - zusatz5
                          - zusatz3
                        x-apidog-ignore-properties: []
                      ortsteil:
                        type: string
                        description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z59|Z60]'
                      postleitzahl:
                        type: string
                        description: 'Postleitzahl | EDIFACT: SG4.IDE+24.SG12.NAD+[Z59|Z60]'
                      strasse:
                        type: string
                        description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z59|Z60]'
                      hausnummer:
                        type: string
                        description: >-
                          Hausnummer und Ergänzung | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z59|Z60]
                      ort:
                        type: string
                        description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z59|Z60]'
                      postfach:
                        type: string
                        description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z59|Z60]'
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
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+Z22'
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

                          oder Sängerin | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]
                      name4:
                        type: string
                        description: 'name4 | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]'
                      name2:
                        type: string
                        description: >-
                          Zweiter Teil des Namens. Hier kann der eine
                          Erweiterung zum Firmennamen oder

                          bei Privatpersonen beispielsweise der Vorname
                          dargestellt werden. Beispiele:

                          Bereich Süd oder Nina | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z55|Z56]
                      name1:
                        type: string
                        description: >-
                          Erster Teil des Namens. Hier kann der Firmenname oder
                          bei Privatpersonen

                          beispielsweise der Nachname dargestellt werden.
                          Beispiele: Yellow Strom GmbH

                          oder Hagen | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]
                      partneradresse:
                        type: object
                        properties:
                          strasse:
                            type: string
                            description: 'Strasse | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]'
                          postfach:
                            type: string
                            description: 'Postfach | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]'
                          ort:
                            type: string
                            description: 'Ort | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]'
                          postleitzahl:
                            type: string
                            description: >-
                              Postleitzahl | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z55|Z56]
                          hausnummer:
                            type: string
                            description: >-
                              Hausnummer und Ergänzung | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z55|Z56]
                          landescode:
                            type: string
                            title: Landescode
                            description: >-
                              Der ISO-Landescode als Enumeration | EDIFACT:
                              SG4.IDE+24.SG12.NAD+[Z55|Z56]
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
                            description: 'Ortsteil | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]'
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
                          = false) | EDIFACT: SG4.IDE+24.SG12.NAD+[Z55|Z56]
                      anrede:
                        type: string
                        description: >-
                          Die Anrede für den GePa, Z.B. Herr. | EDIFACT:
                          SG4.IDE+24.SG12.NAD+[Z55|Z56]
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
                    description: 'redispatch | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZD3|ZD4].PIA+5'
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
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z91
                          enum:
                            - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                            - WETTBEWERBLICHER_MESSSTELLENBETREIBER
                            - AUFFANGMESSSTELLENBETREIBER
                        weiterverpflichtet:
                          type: boolean
                          description: >-
                            weiterverpflichtet | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z91
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z91
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
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z91
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
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z80|Z81],
                          SG4.IDE+24.SG8.SEQ+[ZD1|ZD2],
                          SG4.IDE+24.SG8.SEQ+[ZD3|ZD4],
                          SG4.IDE+24.SG12.NAD+[Z55|Z56].RFF+Z46,
                          SG4.IDE+24.SG12.NAD+[DDO|Z57|Z58].RFF+Z46,
                          SG4.IDE+24.SG12.NAD+[Z59|Z60].RFF+Z46
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  verguetungEmpfaenger:
                    type: string
                    title: VerguetungEmpfaenger
                    description: >-
                      VerguetungEmpfaenger | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++Z89.CAV
                    enum:
                      - KUNDE
                      - LIEFERANT
                  fernsteuerbarkeit:
                    type: string
                    title: Fernsteuerbarkeit
                    description: >-
                      Fernsteuerbarkeit | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+Z24
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
                            SG4.IDE+24.SG8.SEQ+[ZD1|ZD2].RFF+Z10
                        verbrauchsart:
                          type: string
                          title: Verbrauchsart
                          description: >-
                            Verbrauchsart | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[ZD1|ZD2].SG10.CCI+Z17.CAV
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
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++Z34.CAV
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
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++Z83.CAV
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
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
                  verwendungBis:
                    type: string
                    description: >-
                      Verarbeitung, Endedatum/-zeit / DTM+164 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  verwendungAb:
                    type: string
                    description: >-
                      Verarbeitung, Beginndatum/-zeit / DTM+163 | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++Z84.CAV
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
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - liste
                  - code
                  - zeitraumId
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
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
          x-apidog-orders:
            - empfaenger
            - anfragereferenznummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - antwortStatusZeitraum
            - transaktionsgrund
            - transaktionsgrundergaenzung
            - pruefidentifikator
            - dokumentennummer
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: "55622 - LF an NB - Bestellung einer Änderung von Stammdaten vom \_LF an NB"
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55621:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
            - anfragereferenznummer
            - antwortStatusZeitraum
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
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0]'
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
                            SG4.IDE+24.SG8.SEQ+[ZA9|ZB0].SG10.CCI+++ZB3.CAV+Z91
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
                            SG4.IDE+24.SG8.SEQ+[ZA9|ZB0].SG10.CCI+++ZB3.CAV+Z91
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
                            SG4.IDE+24.SG8.SEQ+[ZA9|ZB0].SG10.CCI+++ZB3.CAV+Z91
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
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[ZA9|ZB0]'
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
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
      description: "55621 - LF an NB - Bestellung einer Änderung von Stammdaten vom \_LF an NB"
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_21047:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            vorgangsreferenznummer:
              type: string
              description: >-
                Referenznummer des Vorgangs der Anmeldung nach WiM / ORDERS
                RFF+Z41 / IFTSTA RFF+ACW | EDIFACT:
                SG14.CNI.SG15.STS+Z43.RFF+ACW
            absender:
              type: object
              properties:
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG1.NAD+MS'
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
                        SG1.NAD+MS.SG2.CTA+IC
                  x-apidog-orders:
                    - nachname
                  x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG1.NAD+MS'
              x-apidog-orders:
                - rollencodetyp
                - ansprechpartner
                - rollencodenummer
              x-apidog-ignore-properties: []
            antwortstatusCodeliste:
              type: string
              description: >-
                Antwortstatus Codeliste / STS+E01 | EDIFACT:
                SG14.CNI.SG15.STS+Z43
            nachrichtendatum:
              type: string
              description: 'Erstellungdatum der EDIFact / DTM+137 | EDIFACT: DTM+137'
              format: date-time
            empfaenger:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG1.NAD+MR'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG1.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            transaktionsdaten:
              type: object
              properties:
                absender:
                  type: object
                  properties:
                    ansprechpartner:
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
                                description: >-
                                  EDIFACT:
                                  SG1.NAD+MS.SG2.CTA+IC.COM+[EM|FX|TE|AJ|AL]
                                x-apidog-orders: []
                                properties: {}
                                x-apidog-ignore-properties: []
                              nummerntyp:
                                type: string
                                title: Rufnummernart
                                description: >-
                                  EDIFACT:
                                  SG1.NAD+MS.SG2.CTA+IC.COM+[EM|FX|TE|AJ|AL]
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
                        eMailAdresse:
                          type: string
                          description: >-
                            E-Mail Adresse | EDIFACT:
                            SG1.NAD+MS.SG2.CTA+IC.COM+[EM|FX|TE|AJ|AL]
                      x-apidog-orders:
                        - rufnummern
                        - eMailAdresse
                      x-apidog-ignore-properties: []
                  x-apidog-orders:
                    - ansprechpartner
                  x-apidog-ignore-properties: []
              x-apidog-orders:
                - absender
              x-apidog-ignore-properties: []
            sendungsposition:
              type: string
              description: 'Sendungsposition / GID | EDIFACT: SG14.CNI.SG15.STS+Z43.SG25.GID'
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+Z33'
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG14.CNI.SG15.STS+Z43.RFF+Z13
            antwortstatus:
              type: string
              description: 'Antwortstatus / STS+E01 | EDIFACT: SG14.CNI.SG15.STS+Z43'
            nachrichtenreferenznummer:
              type: string
              description: >-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | EDIFACT:
                UNH
          x-apidog-orders:
            - vorgangsreferenznummer
            - absender
            - antwortstatusCodeliste
            - nachrichtendatum
            - empfaenger
            - transaktionsdaten
            - sendungsposition
            - dokumentennummer
            - pruefidentifikator
            - antwortstatus
            - nachrichtenreferenznummer
          x-apidog-ignore-properties: []
        stammdaten:
          type: object
          properties:
            STATUSMITTEILUNG:
              type: array
              items:
                type: object
                properties:
                  auftragsstatus:
                    type: string
                    title: Auftragsstatus
                    description: 'Auftragsstatus | EDIFACT: SG14.CNI.SG15.STS+Z43'
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
                  positionsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        allgemeineInformationen:
                          type: object
                          properties:
                            info3:
                              type: string
                              description: >-
                                Allgemeine Info 3 | EDIFACT:
                                SG14.CNI.SG15.STS+Z43.SG25.GID.FTX+ACB
                            info1:
                              type: string
                              description: >-
                                Allgemeine Info 1 | EDIFACT:
                                SG14.CNI.SG15.STS+Z43.SG25.GID.FTX+ACB
                            info2:
                              type: string
                              description: >-
                                Allgemeine Info 2 | EDIFACT:
                                SG14.CNI.SG15.STS+Z43.SG25.GID.FTX+ACB
                            info4:
                              type: string
                              description: >-
                                Allgemeine Info 4 | EDIFACT:
                                SG14.CNI.SG15.STS+Z43.SG25.GID.FTX+ACB
                            info5:
                              type: string
                              description: >-
                                Allgemeine Info 5 | EDIFACT:
                                SG14.CNI.SG15.STS+Z43.SG25.GID.FTX+ACB
                          x-apidog-orders:
                            - info3
                            - info1
                            - info2
                            - info4
                            - info5
                          x-apidog-ignore-properties: []
                        positionsnummer:
                          type: integer
                          description: 'Positionsnummer / LIN | EDIFACT: SG14.CNI'
                      x-apidog-orders:
                        - allgemeineInformationen
                        - positionsnummer
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - auftragsstatus
                  - positionsdaten
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - STATUSMITTEILUNG
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 21047 - NB an ÜNB - Bearbeitungsstand zur Rückmeldung
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55220:
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
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++E17.CAV+Z22
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++E17.CAV+Z22
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
                            SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].PIA+Z02
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
                                SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].SG10.CCI+Z38
                              x-apidog-orders: []
                              properties: {}
                              x-apidog-ignore-properties: []
                            zaehlzeitDefinition:
                              type: object
                              title: Zaehlzeitdefinition
                              description: >-
                                EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].SG10.CCI+Z39
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
                                SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].SG9.QTY+Z33,
                                SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].SG10.CCI+Z44+ZD8
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
                            SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].PIA+Z02
                          items:
                            type: string
                        gemeinderabatt:
                          type: object
                          title: Gemeinderabatt
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].SG9.QTY+Z16,
                            SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].SG9.QTY
                          x-apidog-orders: []
                          properties: {}
                          x-apidog-ignore-properties: []
                        zuschlag:
                          type: object
                          title: Zuschlag
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].SG9.QTY
                          x-apidog-orders: []
                          properties: {}
                          x-apidog-ignore-properties: []
                        abschlag:
                          type: object
                          title: Abschlag
                          description: >-
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].SG9.QTY
                          x-apidog-orders: []
                          properties: {}
                          x-apidog-ignore-properties: []
                        anzahl:
                          type: string
                          title: Registeranzahl
                          description: >-
                            Registeranzahl | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].SG9.QTY+Z38
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
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG6.RFF+[Z51|Z52],
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81],
                      SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97]
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
                          zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z51|Z52],
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81],
                          SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  netzbetreiberCodeNr:
                    type: string
                    description: >-
                      Codenummer des Netzbetreibers, an dessen Netz diese
                      Marktlokation

                      angeschlossen ist. | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[Z82|Z83|Z96|Z97].SG10.CCI+++ZB3.CAV+Z88
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
                          SG4.IDE+24.SG6.RFF+[Z51|Z52].DTM+Z09
                      netznutzungsvertrag:
                        type: string
                        title: Netznutzungsvertrag
                        description: >-
                          Netznutzungsvertrag | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++Z88.CAV+Z74
                        enum:
                          - KUNDEN_NB
                          - LIEFERANTEN_NB
                      netznutzungsabrechnungIntervall:
                        type: integer
                        description: >-
                          netznutzungsabrechnungIntervall | EDIFACT:
                          SG4.IDE+24.SG6.RFF+[Z51|Z52].DTM+Z22
                      netznutzungszahler:
                        type: string
                        title: Netznutzungszahler
                        description: >-
                          Netznutzungszahler | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++Z88.CAV+Z73
                        enum:
                          - KUNDE
                          - LIEFERANT
                      netznutzungsabrechnungsgrundlage:
                        type: string
                        title: Netznutzungsabrechnungsgrundlage
                        description: >-
                          Netznutzungsabrechnungsgrundlage | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++Z88.CAV+ZA7
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
                              SG4.IDE+24.SG6.RFF+[Z51|Z52].DTM+Z21
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
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
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - vorgangsnummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 55220 - LF an NB - Bestellung einer Änderung von Abrechnungsdaten
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55156:
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
                            SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+++Z12.CAV
                        bezeichnung:
                          type: string
                          description: >-
                            Externe Bezeichnung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z85|Z86].SG10.CCI+Z02.CAV,
                            SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+Z03.CAV
                        tagesparameter:
                          type: object
                          properties:
                            herausgeber:
                              type: string
                              title: Herausgeber
                              description: >-
                                Herausgeber | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+[ZA0|Z99]
                              enum:
                                - NB
                                - BDEW
                                - TUM
                            dienstanbieter:
                              type: string
                              description: >-
                                dienstanbieter | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+[ZA0|Z99]
                            klimazone:
                              type: string
                              description: >-
                                klimazone | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+[ZA0|Z99]
                            temperaturmessstelle:
                              type: string
                              description: >-
                                temperaturmessstelle | EDIFACT:
                                SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+[ZA0|Z99]
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
                            SG4.IDE+24.SG8.SEQ+[Z85|Z86].SG10.CCI+Z02,
                            SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+Z03
                          enum:
                            - ART_STANDARDLASTPROFIL
                            - ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL
                            - ART_LASTPROFIL
                        einspeisung:
                          type: boolean
                          description: >-
                            Kennzeichen Einspeisung | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z85|Z86].SG10.CCI+Z02,
                            SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+Z03
                        verfahren:
                          type: string
                          title: Profilverfahren
                          description: >-
                            Profilverfahren | EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z85|Z86].SG10.CCI+Z02,
                            SG4.IDE+24.SG8.SEQ+[Z87|Z88].SG10.CCI+Z03
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
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+15+Z21.CAV
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
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG9.QTY+[265|Z08]
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
                        description: >-
                          EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG9.QTY+[265|Z08]
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
                          zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z85|Z86],
                          SG4.IDE+24.SG8.SEQ+[Z87|Z88]
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z85|Z86],
                      SG4.IDE+24.SG8.SEQ+[Z87|Z88]
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
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI
                    enum:
                      - WERTE
                      - PROFILE
                  bilanzkreis:
                    type: object
                    title: Bilanzkreis
                    description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+Z19'
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
                        SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI.CAV+[E02|E14]
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
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+6
                    enum:
                      - UENB
                      - VNB
                  jahresverbrauchsprognose:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG9.QTY+31'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG9.QTY+31
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
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z90
                        marktrolle:
                          type: string
                          title: Marktrolle
                          description: >-
                            Diese Rollen kann ein Marktteilnehmer einnehmen |
                            EDIFACT:
                            SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+++ZB3.CAV+Z90
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
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+Z18
                  marktlokationsId:
                    type: string
                    description: >-
                      Die ID der Marktlokation der der zu sperrende Zähler
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: 'Datenqualitaet | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z80|Z81]'
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
                        description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG8.SEQ+[Z80|Z81]'
                    x-apidog-orders:
                      - zeitraumId
                    x-apidog-ignore-properties: []
                  bilanzierungsgebiet:
                    type: string
                    description: >-
                      Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist -
                      im Falle eines Strom Netzes. | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+[Z80|Z81].SG10.CCI+Z20
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z26
                    format: date-time
                  datenqualitaet:
                    type: string
                    title: Datenqualitaet
                    description: >-
                      Datenqualitaet | EDIFACT:
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]
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
                      SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55].DTM+Z25
                    format: date-time
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.SG6.RFF+[Z47|Z48|Z54|Z55]'
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
              description: >-
                EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT:
                BGM+[E03|Z88]
            kategorie:
              type: string
              title: Anfragekategorie
              description: 'Anfragekategorie | EDIFACT: BGM+[E03|Z88]'
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
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            antwortStatusZeitraum:
              type: array
              items:
                type: object
                properties:
                  code:
                    type: object
                    title: Objectcode
                    description: 'EDIFACT: SG4.IDE+24.STS+E01'
                    x-apidog-orders: []
                    properties: {}
                    x-apidog-ignore-properties: []
                  zeitraumId:
                    type: integer
                    description: 'zeitraumId | EDIFACT: SG4.IDE+24.STS+E01'
                  liste:
                    type: string
                    description: 'liste | EDIFACT: SG4.IDE+24.STS+E01'
                x-apidog-orders:
                  - code
                  - zeitraumId
                  - liste
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
          x-apidog-orders:
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - vorgangsnummer
            - antwortStatusZeitraum
            - pruefidentifikator
            - transaktionsgrund
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 55156 - LF an NB - Bestellung einer Änderung von Abrechnungsdaten
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55015:
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
            - transaktionsgrundergaenzungBefristeteAnmeldung
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - transaktionsgrundergaenzung
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
      description: >-
        55015 - LF (Notz "entspricht E/G") an NB - Antwort auf Ankündigung der
        Zuordnung des E/G zur Marktlokation
      x-apidog-orders:
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55014:
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
                            type: string
                            title: Abweichungsgrund
                            description: >-
                              Abweichungsgrund | EDIFACT:
                              SG4.IDE+24.SG8.SEQ+Z75.SG10.CCI+Z61.CAV
                            enum:
                              - PREIS_RECHENREGEL_FALSCH
                              - FALSCHER_ABRECHNUNGSZEITRAUM
                              - UNBEKANNTE_MARKTLOKATION_MESSLOKATION
                              - SONSTIGER_ABWEICHUNGSGRUND
                              - DOPPELTE_RECHNUNG
                              - ABRECHNUNGSBEGINN_UNGLEICH_VERTRAGSBEGINN
                              - ABRECHNUNGSENDE_UNGLEICH_VERTRAGSENDE
                              - BETRAG_DER_ABSCHLAGSRECHNUNG_FALSCH
                              - VORAUSBEZAHLTER_BETRAG_FALSCH
                              - ARTIKEL_NICHT_VEREINBART
                              - NETZNUTZUNGSMESSWERTE_ENERGIEMENGEN_FEHLEN
                              - RECHNUNGSNUMMER_BEREITS_ERHALTEN
                              - NETZNUTZUNGSMESSWERTE_ENERGIEMENGEN_FALSCH
                              - ZEITLICHE_MENGENANGABE_FEHLERHAFT
                              - FALSCHER_BILANZIERUNGSBEGINN
                              - FALSCHES_NETZNUTZUNGSENDE
                              - BILANZIERTE_MENGE_FEHLT
                              - BILANZIERTE_MENGE_FALSCH
                              - NETZNUTZUNGSABRECHNUNG_FEHLT
                              - REVERSE_CHARGE_ANWENDUNG_FEHLT_ODER_FEHLERHAFT
                              - ALLOKATIONSLISTE_FEHLT
                              - MEHR_MINDERMENGE_FALSCH
                              - UNGUELTIGES_RECHNUNGSDATUM
                              - >-
                                ZEITINTERVALL_DER_BILANZIERTEN_MENGE_INKONSISTENT
                              - >-
                                RECHNUNGSEMPFAENGER_WIDERSPRICHT_DER_STEUERRECHTLICHEN_EINSCHAETZUNG_DES_RECHNUNGSSTELLERS
                              - >-
                                ANGEGEBENE_QUOTES_AN_MARKTLOKATION_NICHT_VORHANDEN
                              - RECHNUNGSABWICKLUNG_NICHT_VEREINBART
                              - COMDIS_WIRD_ABGELEHNT
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
                  versorgungsart:
                    type: string
                    title: Versorgungsart
                    description: >-
                      Versorgungsart | EDIFACT:
                      SG4.IDE+24.SG8.SEQ+Z01.SG10.CCI+Z36
                    enum:
                      - ERSATZVERSORGUNG
                      - GRUNDVERSORGUNG
                      - ERSATZBELIEFERUNG
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
                x-apidog-orders:
                  - versorgungsart
                  - erforderlichesProduktpaket
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
            - vertragsende
            - dokumentennummer
            - kategorie
            - absender
            - transaktionsgrundergaenzungBefristeteAnmeldung
            - nachrichtendatum
            - nachrichtenreferenznummer
            - vertragsbeginn
            - empfaenger
            - anfragereferenznummer
            - transaktionsgrundergaenzung
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: >-
        55014 - LF (Notz "entspricht E/G") an NB - Antwort auf Ankündigung der
        Zuordnung des E/G zur Marktlokation
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
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
    PI_55012:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            absender:
              type: object
              properties:
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
                - rollencodetyp
                - rollencodenummer
                - rufnummern
                - ansprechpartner
              x-apidog-ignore-properties: []
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            empfaenger:
              type: object
              properties:
                rollencodenummer:
                  type: string
                  description: 'Gibt die Codenummer der Marktrolle an. | EDIFACT: SG2.NAD+MR'
                rollencodetyp:
                  type: string
                  title: Rollencodetyp
                  description: 'Rollencodetyp | EDIFACT: SG2.NAD+MR'
                  enum:
                    - BDEW
                    - GS1
                    - GLN
                    - DVGW
              x-apidog-orders:
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
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | EDIFACT: SG4.IDE+24.SG6.RFF+Z13
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
            vorgangsnummer:
              type: string
              description: >-
                Nummer des Vorgangs / UTILMD UTILTS IDE+24 / INSRPT INVOIC DOC |
                EDIFACT: SG4.IDE+24
            transaktionsgrund:
              type: string
              description: >-
                Der Transaktionsgrund beschreibt den Geschäftsvorfall zur
                Kategorie genauer / UTILMD STS+7++###+ZW4+E03 | EDIFACT:
                SG4.IDE+24.STS+7
            antwortstatus:
              type: string
              description: 'Antwortstatus / STS+E01 | EDIFACT: SG4.IDE+24.STS+E01'
            antwortstatusCodeliste:
              type: string
              description: 'Antwortstatus Codeliste / STS+E01 | EDIFACT: SG4.IDE+24.STS+E01'
          x-apidog-orders:
            - absender
            - anfragereferenznummer
            - empfaenger
            - nachrichtendatum
            - nachrichtenreferenznummer
            - pruefidentifikator
            - dokumentennummer
            - kategorie
            - vorgangsnummer
            - transaktionsgrund
            - antwortstatus
            - antwortstatusCodeliste
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
      description: >-
        55012 - LFA an NB - Antwort auf Anfrage zur Beendigung der Zuordnung des
        LFA zur Marktlokation bzw. Tranche
      x-apidog-orders:
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55011:
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
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
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
            - vertragsende
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
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
          x-apidog-orders:
            - NETZNUTZUNGSVERTRAG
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55011 - LFA an NB - Antwort auf Anfrage zur Beendigung der Zuordnung des
        LFA zur Marktlokation bzw. Tranche
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
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
    PI_55078:
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
                x-apidog-orders:
                  - marktrollen
                  - marktlokationsId
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
            - NETZLOKATION
            - TRANCHE
            - STEUERBARE_RESSOURCE
            - NETZNUTZUNGSVERTRAG
            - TECHNISCHE_RESSOURCE
          x-apidog-ignore-properties: []
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
            geplantesProduktpaket:
              type: integer
              description: >-
                Informativ zur Umsetzung geplantes Produktpaket / RFF+Z60 |
                EDIFACT: SG4.IDE+24.SG6.RFF+Z60
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
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - vertragsbeginn
            - empfaenger
            - geplantesProduktpaket
            - anfragereferenznummer
            - transaktionsgrundergaenzung
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 55078 - NB an LFN - Zuordnung des LFN zur Marktlokation bzw. Tranche
      x-apidog-orders:
        - stammdaten
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
    PI_55002:
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
                      zugeordnet ist. | EDIFACT: SG4.IDE+24.SG5.LOC+Z16,
                      SG4.IDE+24.SG5.LOC+Z22
                x-apidog-orders:
                  - marktrollen
                  - marktlokationsId
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
            - STEUERBARE_RESSOURCE
            - TECHNISCHE_RESSOURCE
          x-apidog-ignore-properties: []
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E01'
            vertragsende:
              type: string
              description: 'Datum Vertragsende / DTM+93 | EDIFACT: SG4.IDE+24.DTM+93'
              format: date-time
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
            geplantesProduktpaket:
              type: integer
              description: >-
                Informativ zur Umsetzung geplantes Produktpaket / RFF+Z60 |
                EDIFACT: SG4.IDE+24.SG6.RFF+Z60
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
            - vertragsende
            - kategorie
            - absender
            - transaktionsgrundergaenzungBefristeteAnmeldung
            - nachrichtendatum
            - nachrichtenreferenznummer
            - vertragsbeginn
            - empfaenger
            - geplantesProduktpaket
            - anfragereferenznummer
            - transaktionsgrundergaenzung
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - stammdaten
        - transaktionsdaten
      description: 55002 - NB an LFN - Zuordnung des LFN zur Marktlokation bzw. Tranche
      x-apidog-orders:
        - stammdaten
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55009:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E02'
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
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
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
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
      description: >-
        55009 - LF an NB - Antwort auf Ankündigung der Beendigung der Zuordnung
        des LF zur Marktlokation bzw. Tranche
      x-apidog-orders:
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55008:
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
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
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
            - vertragsende
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
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
          x-apidog-orders:
            - NETZNUTZUNGSVERTRAG
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55008 - LF an NB - Antwort auf Ankündigung der Beendigung der Zuordnung
        des LF zur Marktlokation bzw. Tranche
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55006:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            dokumentennummer:
              type: string
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E02'
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
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
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
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
            - vorgangsnummer
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
      description: >-
        55006 - NB an LF - Ablehnung der Abmeldung einer Zuordnung des LF zur
        Marktlokation bzw. Tranche
      x-apidog-orders:
        - transaktionsdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55005:
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
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
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
            - vertragsende
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - vertragsbeginn
            - empfaenger
            - anfragereferenznummer
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
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
          x-apidog-orders:
            - NETZNUTZUNGSVERTRAG
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: >-
        55005 - NB an LF - Beendigung der Zuordnung des LF zur Marktlokation
        bzw. Tranche
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55018:
      type: object
      properties:
        transaktionsdaten:
          type: object
          properties:
            datumKuendigungLf:
              type: string
              description: >-
                Kündigungsdatum, was dem Lieferanten mitgeteilt worden ist /
                DTM+Z06 | EDIFACT: SG4.IDE+24.DTM+[Z05|Z06]
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
            anfragereferenznummer:
              type: string
              description: >-
                Referenz Vorgangsnummer 'aus Anfragenachricht' / ORDERS RFF+TN /
                IFTSTA RFF+AAV / INSRPT RFF+TN RFF+AAV | EDIFACT:
                SG4.IDE+24.SG6.RFF+TN
            datumKuendigungKd:
              type: string
              description: >-
                Kündigungsdatum, was dem Kunden mitgeteilt worden ist / DTM+Z05
                | EDIFACT: SG4.IDE+24.DTM+[Z05|Z06]
              format: date-time
            gueltigAb:
              type: string
              description: 'Gültigkeitsdatum/-zeit / DTM+7 | EDIFACT: SG4.IDE+24.DTM+157'
              format: date-time
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
            - datumKuendigungLf
            - dokumentennummer
            - freitext
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - anfragereferenznummer
            - datumKuendigungKd
            - gueltigAb
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
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
                  vertragskonditionen:
                    type: object
                    properties:
                      kuendigungstermin:
                        type: string
                        description: 'kuendigungstermin | EDIFACT: SG4.IDE+24.DTM+Z10'
                      kuendigungsfrist:
                        type: object
                        properties:
                          zeitraumText:
                            type: string
                            description: 'zeitraumText | EDIFACT: SG4.IDE+24.DTM+Z01'
                        x-apidog-orders:
                          - zeitraumText
                        x-apidog-ignore-properties: []
                    x-apidog-orders:
                      - kuendigungstermin
                      - kuendigungsfrist
                    x-apidog-ignore-properties: []
                x-apidog-orders:
                  - vertragskonditionen
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - ENERGIELIEFERVERTRAG
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 55018 - LFA an LFN - Antwort auf Kündigung
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    PI_55017:
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
              description: 'EDIFact Referenz aus dem BGM Segment / BGM | EDIFACT: BGM+E35'
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
            - vertragsende
            - dokumentennummer
            - kategorie
            - absender
            - nachrichtendatum
            - nachrichtenreferenznummer
            - empfaenger
            - endezumtermin
            - anfragereferenznummer
            - transaktionsgrundergaenzung
            - antwortstatusCodeliste
            - pruefidentifikator
            - transaktionsgrund
            - antwortstatus
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
            BILANZIERUNG:
              type: array
              items:
                type: object
                properties:
                  vorjahresverbrauch:
                    type: object
                    properties:
                      wert:
                        type: object
                        title: Schwellwert
                        description: 'EDIFACT: SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+Z09'
                        x-apidog-orders: []
                        properties: {}
                        x-apidog-ignore-properties: []
                      einheit:
                        type: string
                        title: Mengeneinheit
                        description: >-
                          Einheit: Messgrößen, die per Messung oder Vorgabe
                          ermittelt werden können | EDIFACT:
                          SG4.IDE+24.SG8.SEQ+Z01.SG9.QTY+Z09
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
                  - vorjahresverbrauch
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - NETZNUTZUNGSVERTRAG
            - BILANZIERUNG
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 55017 - LFA an LFN - Antwort auf Kündigung
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
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
