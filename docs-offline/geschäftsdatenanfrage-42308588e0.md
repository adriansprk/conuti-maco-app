# Geschäftsdatenanfrage

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
      summary: Geschäftsdatenanfrage
      deprecated: false
      description: Prozess zur Anfrage nach Stornierung im Auftrag des Endkunden anstoßen
      operationId: START_GESCHAEFTSDATENANFRAGE
      tags:
        - Schnittstellen/Trigger (MACO APP)/Einzelansicht LF
        - TRIGGER
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/%5BLF%5D%20START_GESCHAEFTSDATENANFRAGE'
            example:
              stammdaten:
                ANFRAGE:
                  - boTyp: ANFRAGE
                    versionStruktur: '1'
                    anfragekategorie: STAMMDATEN_MALO_ODER_MELO
                    lokationsId: '57685676748'
                    lokationsTyp: MALO
              transaktionsdaten:
                sparte: STROM
                absender:
                  boTyp: MARKTTEILNEHMER
                  versionStruktur: '1'
                  gewerbekennzeichnung: true
                  rollencodenummer: '9906464000001'
                  rollencodetyp: BDEW
                  marktrolle: LF
                empfaenger:
                  boTyp: MARKTTEILNEHMER
                  versionStruktur: '1'
                  gewerbekennzeichnung: true
                  rollencodenummer: '9900683000008'
                  rollencodetyp: BDEW
              zusatzdaten:
                prozessId: 00505688-E4A2-1EDF-A0C2-C81842E2515E
                eventname: START_GESCHAEFTSDATENANFRAGE
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-42308588-run
components:
  schemas:
    '[LF] START_GESCHAEFTSDATENANFRAGE':
      allOf:
        - oneOf:
            - $ref: '#/components/schemas/PI_17132'
            - $ref: '#/components/schemas/PI_17102'
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
                  const: START_GESCHAEFTSDATENANFRAGE
                  default: START_GESCHAEFTSDATENANFRAGE
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
    PI_17102:
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
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | 

                        <TipInfo>SG2.NAD+MS.SG5.CTA+IC.COM+[EM|FX|TE|AJ|AL]</TipInfo>
                    nachname:
                      type: string
                      description: |-
                        Nachname (Familienname) des Ansprechpartners | 
                        <TipInfo>SG2.NAD+MS.SG5.CTA+IC</TipInfo>
                  x-apidog-orders:
                    - eMailAdresse
                    - nachname
                  x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: |-
                    Gibt die Codenummer der Marktrolle an - MP ID
                    ORDERS NAD Z31 Übertragungsnetzbetreiber 
                    PI 17134
                    ORDERS NAD DEB Messstellenbetreiber
                    PI 17003 17134 17135
                    IFTSTA NAD DEB Messstellenbetreiber 
                    PI 21007 21015 21018 | 
                    <TipInfo>SG2.NAD+MS</TipInfo>
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      nummerntyp: &ref_1
                        description: >-
                          Art des Kommunikationsmittels

                          COM | 

                          <TipInfo>SG2.NAD+MS.SG5.CTA+IC.COM+[EM|FX|TE|AJ|AL]</TipInfo>
                        $ref: '#/components/schemas/Rufnummernart'
                      rufnummer:
                        type: string
                        description: >-
                          Rufnummer | 

                          <TipInfo>SG2.NAD+MS.SG5.CTA+IC.COM+[EM|FX|TE|AJ|AL]</TipInfo>
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
                rollencodetyp: &ref_0
                  description: >-
                    Gibt den Typ des Codes an - Verantwortliche Stelle für die
                    Codepflege

                    9 GS1

                    293 DE, BDEW (Bundesverband der Energie- und
                    Wasserwirtschaft e.V.)

                    332 DE, DVGW Service & Consult GmbH  | 

                    <TipInfo>SG2.NAD+MS</TipInfo>
                  $ref: '#/components/schemas/Rollencodetyp'
              x-apidog-orders:
                - ansprechpartner
                - rollencodenummer
                - rufnummern
                - rollencodetyp
              required:
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                rollencodetyp: *ref_0
                rollencodenummer:
                  type: string
                  description: |-
                    Gibt die Codenummer der Marktrolle an - MP ID
                    ORDERS NAD Z31 Übertragungsnetzbetreiber 
                    PI 17134
                    ORDERS NAD DEB Messstellenbetreiber
                    PI 17003 17134 17135
                    IFTSTA NAD DEB Messstellenbetreiber 
                    PI 21007 21015 21018 | 
                    <TipInfo>SG2.NAD+MR</TipInfo>
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              required:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: |-
                Erstellungdatum der EDIFact / DTM+137 | 
                <TipInfo>DTM+137</TipInfo>
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: |-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | 
                <TipInfo>UNH</TipInfo>
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | 

                <TipInfo>SG1.RFF+Z13</TipInfo>
          x-apidog-orders:
            - absender
            - empfaenger
            - nachrichtendatum
            - nachrichtenreferenznummer
            - pruefidentifikator
          required:
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
                  dokumentennummer:
                    type: string
                    description: |-
                      EDIFact Referenz aus dem BGM Segment / BGM | 
                      <TipInfo>BGM+[7|Z28|Z48]</TipInfo>
                  anfragekategorie:
                    description: >-
                      Kategorie der Anfrage - Darin ist die Kategorie der
                      gesamten Nachricht festgelegt

                      BGM 7 | 

                      <TipInfo>BGM+[7|Z28|Z48]</TipInfo>
                    $ref: '#/components/schemas/Anfragekategorie'
                  lokationsId:
                    type: string
                    description: |-
                      LokationsId | 
                      <TipInfo>SG2.NAD+DP.LOC+172</TipInfo>
                  anfragetyp:
                    description: >-
                      Typ/Art der Anfrage

                      IMD Z11

                      PI 17102 17113 17301 17103 17117 17009 17004 17123 17118
                      17134 17135 

                      ORDRSP

                      IMD Z10

                      PI 19103 19102 19114 19301 19007

                      REQOTE

                      PI 35004

                      QUOTES

                      IMD Z07 

                      PI 15001 15002 15004 | 

                      <TipInfo>IMD++[Z11|Z12|Z35]</TipInfo>
                    $ref: '#/components/schemas/Anfragetyp'
                x-apidog-orders:
                  - dokumentennummer
                  - anfragekategorie
                  - lokationsId
                  - anfragetyp
                x-apidog-ignore-properties: []
            AUFTRAG:
              type: array
              items:
                type: object
                properties:
                  positionsdaten:
                    type: array
                    items:
                      type: object
                      properties:
                        enddatum:
                          type: string
                          description: |-
                            Ende Zeitraum für Wertanfrage, Endedatum/-zeit
                            DTM 164
                            PI 17103 17114 17113 17209 | 
                            <TipInfo>SG29.LIN.DTM+164</TipInfo>
                          format: date-time
                        startdatum:
                          type: string
                          description: |-
                            Beginn Zeitraum für Wertanfrage, Beginndatum/-zeit
                            DTM 163
                            PI 17102 17103 17114 17113 17209 | 
                            <TipInfo>SG29.LIN.DTM+163</TipInfo>
                          format: date-time
                      x-apidog-orders:
                        - enddatum
                        - startdatum
                      x-apidog-ignore-properties: []
                x-apidog-orders:
                  - positionsdaten
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - ANFRAGE
            - AUFTRAG
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 17102 - Geschäftsdatefrage [LF an MSB/ LF an NB/ NB an MSB] ORDERS AHB
      x-apidog-orders:
        - transaktionsdaten
        - stammdaten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Anfragetyp:
      type: string
      title: Anfragetyp
      description: Anfragetyp
      enum:
        - KAUF
        - NUTZUNGSUEBERLASSUNG
        - ABRECHNUNGSBRENNWERT_UND_ZUSTANDSZAHL
        - LASTGANGDATEN
        - ZAEHLERSTAENDE
        - WERTEERMITTLUNG
        - ENERGIEMENGE_EINZELWERT
        - INNERHALB_DER_ARBEITSZEIT
        - AUCH_AUSSERHALB_DER_ARBEITSZEIT
        - WECHSEL_SAEMTLICHER_EINRICHTUNGEN
        - TEILWEISER_WECHSEL
        - AENDERUNG_ZAEHLZEITDEFINITION
        - ABBESTELLUNG_ZAEHLZEITEN
        - ABBESTELLUNG_MESSPRODUKT
        - ANGEBOT_AUF_BASIS_PREISBLATT
        - INDIVIDUELLES_ANGEBOT
        - AENDERUNG_KONFIGURATION
        - KANN_NICHT_ANGEBOTEN_WERDEN
        - NEUKONFIGURATION
        - BEENDIGUNG_KONFIGURATION
        - AKTIVIERUNG_KONFIGURATION
      x-apidog-enum:
        - value: KAUF
          name: Kauf
          description: Z07
        - value: NUTZUNGSUEBERLASSUNG
          name: Nutzungsüberlassung
          description: Z08
        - value: ABRECHNUNGSBRENNWERT_UND_ZUSTANDSZAHL
          name: Abrechnungsbrennwert und Zustandszahl
          description: Z10
        - value: LASTGANGDATEN
          name: Lastgangdaten
          description: Z11
        - value: ZAEHLERSTAENDE
          name: Zählerstände
          description: Z12
        - value: WERTEERMITTLUNG
          name: Werteermittlung
          description: Z13
        - value: ENERGIEMENGE_EINZELWERT
          name: Energiemenge Einzelwert
          description: Z35
        - value: INNERHALB_DER_ARBEITSZEIT
          name: innerhalb der Arbeitszeit
          description: Z53
        - value: AUCH_AUSSERHALB_DER_ARBEITSZEIT
          name: auch außerhalb der Arbeitszeit
          description: Z54
        - value: WECHSEL_SAEMTLICHER_EINRICHTUNGEN
          name: Wechsel sämtlicher technischen Einrichtungen
          description: Z58
        - value: TEILWEISER_WECHSEL
          name: Teilweiser Wechsel technischer Einrichtungen
          description: Z59
        - value: AENDERUNG_ZAEHLZEITDEFINITION
          name: ''
          description: ''
        - value: ABBESTELLUNG_ZAEHLZEITEN
          name: Abbestellung Zählzeitdefinition
          description: Z57
        - value: ABBESTELLUNG_MESSPRODUKT
          name: Abbestellung Messprodukt mit Zählzeitdefinition des LF
          description: Z60
        - value: ANGEBOT_AUF_BASIS_PREISBLATT
          name: Angebot auf Basis Preisblat
          description: Z33
        - value: INDIVIDUELLES_ANGEBOT
          name: Individuelles Angebot
          description: Z34
        - value: AENDERUNG_KONFIGURATION
          name: Änderung Konfiguration
          description: Z55
        - value: KANN_NICHT_ANGEBOTEN_WERDEN
          name: ''
          description: ''
        - value: NEUKONFIGURATION
          name: Neukonfiguration
          description: Z64
        - value: BEENDIGUNG_KONFIGURATION
          name: >-
            Beendigung Konfiguration aufgrund Überführung der Marktlokation zu
            ruhender Marktlokation
          description: Z66
        - value: AKTIVIERUNG_KONFIGURATION
          name: Aktivierung Konfiguration in der derzeit ruhenden Marktlokation
          description: Z67
      x-apidog-folder: ''
    Anfragekategorie:
      type: string
      title: Anfragekategorie
      description: Anfragekategorie
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
        - BESTELLUNG_ANGEBOT_AENDERUNG_TECHNIK_LOKATION
      x-apidog-enum:
        - value: PROZESSDATENBERICHT
          name: Prozessdatenbericht
          description: '7'
        - value: GERAETEUEBERNAHME
          name: Geräteübernahme
          description: Z10
        - value: WEITERVERPFLICHTUNG_BETRIEB_MELO
          name: Weiterverpflichtung zum Betrieb der Messlokation
          description: Z11
        - value: AENDERUNG_MELO
          name: ''
          description: ''
        - value: STAMMDATEN_MALO_ODER_MELO
          name: Stammdaten der Markt- oder Messlokation
          description: Z14
        - value: BILANZIERTE_MENGE_MEHR_MINDER_MENGEN
          name: Bilanzierte Menge (MMMA)
          description: Z23
        - value: ALLOKATIONSLISTE_MEHR_MINDER_MENGEN
          name: Allokationsliste (MMMA)
          description: Z24
        - value: ENERGIEMENGE_UND_LEISTUNGSMAXIMUM
          name: Energiemenge und Leistungsmaximum
          description: Z28
        - value: ABRECHNUNG_MESSSTELLENBETRIEB_MSB_AN_LF
          name: Abrechnung des Messstellenbetriebs vom MSB an den LF
          description: Z29
        - value: AENDERUNG_PROGNOSEGRUNDLAGE_GERAETEKONFIGURATION
          name: Änderung Prognosegrundlage
          description: Z30
        - value: AENDERUNG_GERAETEKONFIGURATION
          name: Änderung Gerätekonfiguration
          description: Z31
        - value: REKLAMATION_VON_WERTEN
          name: Reklamation von Werten
          description: Z34
        - value: LASTGANG_MALO_TRANCHE
          name: Lastgang Marktlokation, Tranche
          description: Z48
        - value: SPERRUNG
          name: Sperrung
          description: Z51
        - value: ENTSPERRUNG
          name: Entsperrung
          description: Z52
        - value: REKLAMATION_ZAEHLZEITDEFINITION
          name: ''
          description: ''
        - value: ZEITREIHEN_IM_RAHMEN_BILANZKREISABRECHNUNG
          name: Zeitreihen im Rahmen der Bilanzkreisabrechnung
          description: BK
        - value: GERAETEWECHSELABSICHT
          name: Gerätewechselabsicht
          description: Z13
        - value: AENDERUNG_KONZESSIONSABGABE
          name: ''
          description: ''
        - value: AENDERUNG_ZAEHLZEITDEFINITION
          name: ''
          description: ''
        - value: UEBERMITTLUNG_WERTE_AN_ESA
          name: Übermittlung von Werten an ESA
          description: Z57
        - value: AENDERUNG
          name: Änderung
          description: Z68
        - value: BILANZKREISZUORDNUNGSLISTE
          name: Bilanzkreiszuordnungsliste
          description: E40
        - value: CLEARINGLISTE
          name: Clearingliste
          description: Z05
        - value: NORMIERTES_PROFIL_PROFILSCHAR
          name: normiertes Profil/Profilschar
          description: Z19
        - value: REDISPATCH_EINZELZEITREIHE_AUSFALLARBEIT
          name: Redispatch Einzelzeitreihe Ausfallarbeit
          description: Z45
        - value: REKLAMATION_PROFIL_PROFILSCHAR
          name: Reklamation Profil/Profilschar
          description: Z58
        - value: STAMMDATEN_MALO
          name: Stammdaten der Marktlokation
          description: Z61
        - value: STAMMDATEN_MELO
          name: Stammdaten der Messlokation
          description: Z62
        - value: STAMMDATEN_TRANCHE
          name: ''
          description: ''
        - value: BEENDIGUNG_EINER_KONFIGURATION
          name: Beendigung einer Konfiguration
          description: Z72
        - value: BESTELLUNG_EINER_KONFIGURATION
          name: Bestellung einer Konfiguration
          description: Z73
        - value: BESTELLUNG_EINES_ANGEBOTS_EINER_KONFIGURATION
          name: Bestellung eines Angebots einer Konfiguration
          description: Z74
        - value: REKLAMATION_EINER_KONFIGURATION
          name: Reklamation einer Konfiguration
          description: Z76
        - value: >-
            BESTELLUNG_AENDERUNG_NETZENTGELTE_NETZORIENTIERTER_STEUERUNGSMOEGLICHKEIT
          name: ''
          description: ''
        - value: AENDERUNG_DER_TECHNIK_DER_LOKATION
          name: Änderung der Technik der Lokation
          description: Z12
        - value: AENDERUNG_INDIVIDUELLER_KONFIGURATION
          name: Änderung individueller Konfiguration
          description: Z56
        - value: BESTELLUNG_AENDERUNG_ABRECHNUNGSDATEN
          name: Bestellung Änderung Abrechnungsdaten
          description: Z91
        - value: EINRICHTUNG_KONFIGURATION_AUFGRUND_ZUORDNUNG_LF
          name: Einrichtung Konfiguration aufgrund Zuordnung LF
          description: Z92
        - value: REKLAMATION_DEFINITION
          name: Reklamation der Übersicht der Definitionen oder einer Definition
          description: Z55
        - value: BESTELLUNG_ANGEBOT_AENDERUNG_TECHNIK_LOKATION
          name: ''
          description: ''
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
    PI_17132:
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
                    eMailAdresse:
                      type: string
                      description: >-
                        E-Mail Adresse | 

                        <TipInfo>SG2.NAD+MS.SG5.CTA+IC.COM+[EM|FX|TE|AJ|AL]</TipInfo>
                    nachname:
                      type: string
                      description: |-
                        Nachname (Familienname) des Ansprechpartners | 
                        <TipInfo>SG2.NAD+MS.SG5.CTA+IC</TipInfo>
                  x-apidog-orders:
                    - eMailAdresse
                    - nachname
                  x-apidog-ignore-properties: []
                rollencodenummer:
                  type: string
                  description: |-
                    Gibt die Codenummer der Marktrolle an - MP ID
                    ORDERS NAD Z31 Übertragungsnetzbetreiber 
                    PI 17134
                    ORDERS NAD DEB Messstellenbetreiber
                    PI 17003 17134 17135
                    IFTSTA NAD DEB Messstellenbetreiber 
                    PI 21007 21015 21018 | 
                    <TipInfo>SG2.NAD+MS</TipInfo>
                rufnummern:
                  type: array
                  items:
                    type: object
                    properties:
                      nummerntyp: *ref_1
                      rufnummer:
                        type: string
                        description: >-
                          Rufnummer | 

                          <TipInfo>SG2.NAD+MS.SG5.CTA+IC.COM+[EM|FX|TE|AJ|AL]</TipInfo>
                    x-apidog-orders:
                      - nummerntyp
                      - rufnummer
                    x-apidog-ignore-properties: []
                rollencodetyp: *ref_0
              x-apidog-orders:
                - ansprechpartner
                - rollencodenummer
                - rufnummern
                - rollencodetyp
              required:
                - rollencodenummer
                - rollencodetyp
              x-apidog-ignore-properties: []
            empfaenger:
              type: object
              properties:
                rollencodetyp: *ref_0
                rollencodenummer:
                  type: string
                  description: |-
                    Gibt die Codenummer der Marktrolle an - MP ID
                    ORDERS NAD Z31 Übertragungsnetzbetreiber 
                    PI 17134
                    ORDERS NAD DEB Messstellenbetreiber
                    PI 17003 17134 17135
                    IFTSTA NAD DEB Messstellenbetreiber 
                    PI 21007 21015 21018 | 
                    <TipInfo>SG2.NAD+MR</TipInfo>
              x-apidog-orders:
                - rollencodetyp
                - rollencodenummer
              required:
                - rollencodetyp
                - rollencodenummer
              x-apidog-ignore-properties: []
            nachrichtendatum:
              type: string
              description: |-
                Erstellungdatum der EDIFact / DTM+137 | 
                <TipInfo>DTM+137</TipInfo>
              format: date-time
            nachrichtenreferenznummer:
              type: string
              description: |-
                EDIFact Referenz aus dem UNT Segment / UTILMD UNT+21 | 
                <TipInfo>UNH</TipInfo>
            pruefidentifikator:
              type: string
              description: >-
                Enthält den Prüfidentifikator aus der EDIFact Kommunikation /
                RFF+Z13 | 

                <TipInfo>SG1.RFF+Z13</TipInfo>
            dokumentennummer:
              type: string
              description: |-
                EDIFact Referenz aus dem BGM Segment / BGM | 
                <TipInfo>BGM+Z14</TipInfo>
          x-apidog-orders:
            - absender
            - empfaenger
            - nachrichtendatum
            - nachrichtenreferenznummer
            - pruefidentifikator
            - dokumentennummer
          required:
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
                  lokationsId:
                    type: string
                    description: |-
                      LokationsId | 
                      <TipInfo>SG2.NAD+DP.LOC+172</TipInfo>
                  anfragekategorie:
                    type: string
                    examples:
                      - STAMMDATEN_MALO_ODER_MELO
                    description: Festwert STAMMDATEN_MALO_ODER_MELO
                  anfragetyp:
                    type: string
                x-apidog-orders:
                  - lokationsId
                  - anfragekategorie
                  - anfragetyp
                required:
                  - lokationsId
                  - anfragekategorie
                x-apidog-ignore-properties: []
          x-apidog-orders:
            - ANFRAGE
          required:
            - ANFRAGE
          x-apidog-ignore-properties: []
      required:
        - transaktionsdaten
        - stammdaten
      description: 17132 - Geschäftsdatefrage [LF an NB/ MSB an NB] ORDERS AHB
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
