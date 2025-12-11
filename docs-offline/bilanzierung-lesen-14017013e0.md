# Bilanzierung lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getAccountingBasic:
    get:
      summary: Bilanzierung lesen
      deprecated: false
      description: >-
        Lesen einer Bilanzierung mittels LokationsId (Parameter1) zum Zeitpunkt
        (Parameter3)
      operationId: LESEN_BILANZIERUNG_BASIS
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: 'LokationsId '
          required: true
          schema:
            type: string
            default: '74018657187'
            examples:
              - '74018657187'
        - name: parameter2
          in: query
          description: LokationsTyp
          required: true
          schema:
            type: string
            default: MALO
            enum:
              - MALO
              - MELO
              - NELO
              - TECHNISCHE_RESSOURCE
              - STEUERBARE_RESOURCE
              - TRANCHE
            examples:
              - MALO
        - name: parameter3
          in: query
          description: Datum (Gültig ab) oder Stichtag, wenn parameter4 nicht gesetzt
          required: true
          schema:
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            type: string
            examples:
              - '2024-06-28T12:18:00Z'
        - name: parameter4
          in: query
          description: 'Datum (Gültig bis) '
          required: true
          schema:
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            type: string
            examples:
              - '2024-06-28T12:18:00Z'
        - name: command
          in: query
          description: >-
            Entspricht der operationId dieser Schnittstelle. Diese Operation Id
            entspricht dem Command im Camunda Konnektor Prozess. Wenn das
            Backend einen generischen Endpunkt bereitstellt, kann dieses Command
            gentutzt werden um zu definieren welche Operation ausgeführt werden
            soll.
          required: false
          example: SAP_LESEN_BILANZIERUNG_BASIS
          schema:
            type: string
      responses:
        '200':
          description: Erfolgreiches Lesen der Bilanzierung
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Bilanzierung'
              example:
                stammdaten:
                  BILANZIERUNG:
                    - boTyp: BILANZIERUNG
                      versionStruktur: '1'
                      marktlokationsId: '50754496000'
                      gueltigkeitszeitraum:
                        zeitraumId: null
                        startdatum: null
                        enddatum: null
                      datenqualitaet: null
                      lastprofile:
                        - bezeichnung: XYZ
                          profilschar: null
                          verfahren: SYNTHETISCH
                          einspeisung: false
                          tagesparameter:
                            klimazone: null
                            temperaturmessstelle: null
                            dienstanbieter: null
                            herausgeber: null
                          profilart: ART_STANDARDLASTPROFIL
                          herausgeber: NB
                          referenzprofilbezeichnung: XYZ
                      lastprofileBilanzierungsbeteiligter:
                        - bezeichnung: ZYX
                          profilschar: null
                          verfahren: SYNTHETISCH
                          einspeisung: false
                          tagesparameter:
                            klimazone: null
                            temperaturmessstelle: null
                            dienstanbieter: null
                            herausgeber: null
                          profilart: ART_STANDARDLASTPROFIL
                          herausgeber: NB
                      bilanzierungsbeginn: '0001-01-01T00:00:00Z'
                      bilanzierungsende: '2025-10-31T23:00:00Z'
                      bilanzkreis: 11Y0-0000-0076-N
                      jahresverbrauchsprognose:
                        wert: 2300
                        einheit: KWH
                      vorjahresverbrauch:
                        wert: 2500
                        einheit: KWH
                      temperaturarbeit:
                        wert: null
                        einheit: null
                      kundenwert:
                        wert: 2550
                        einheit: KWH
                      verbrauchsaufteilung:
                        wert: null
                        einheit: null
                      zeitreihentyp: SLS
                      aggregationsverantwortung: VNB
                      prognosegrundlage: PROFILE
                      detailsPrognosegrundlage:
                        - SLP_SEP
                      wahlrechtPrognosegrundlage: DURCH_LF
                      fallgruppenzuordnung: null
                      prioritaet: '1'
                      grundWahlrechtPrognosegrundlage: DURCH_LF
                      abwicklungsmodell: MODELL_1_BILANZIERUNG_AN_MARKTLOKATION
                      datenDerBeteiligtenMarktrolle:
                        - marktlokationsId: '50754496000'
                          lastprofile:
                            - bezeichnung: H0
                              profilschar: null
                              verfahren: SYNTHETISCH
                              tagesparameter:
                                klimazone: null
                                temperaturmessstelle: null
                                dienstanbieter: null
                                herausgeber: null
                              einspeisung: false
                              profilart: ART_STANDARDLASTPROFIL
                              herausgeber: NB
                          jahresverbrauchsprognose:
                            wert: 2300
                            einheit: KWH
                          temperaturarbeit:
                            wert: null
                            einheit: null
                          bilanzkreis: 11Y0-0000-0076-N
                          bilanzkreisAn: 11Y0-0000-0076-N
                          bilanzkreisVon: 11Y0-0000-0077-N
                          zeitreihentyp: SLS
                          aggregationsverantwortung: VNB
                          prognosegrundlage: PROFILE
                          detailsPrognosegrundlage:
                            - SLP_SEP
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
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017013-run
components:
  schemas:
    Bilanzierung:
      title: Bilanzierung
      type: object
      properties:
        boTyp:
          $ref: '#/components/schemas/BOTyp'
          default: BILANZIERUNG
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        marktlokationsId:
          type: string
          description: >-
            Für welche Marktlokation gelten diese Bilanzierungsdaten.
            Referenzierung auf eine ID einer Marktlokation LOC Z16

            RFF Z18

            PI 55690 55060 55043 55168 55169 55238 55239 55074 55075 55076 55065
            55066 55195 55196 55201 55202 
        aggregationsverantwortung:
          $ref: '#/components/schemas/Aggregationsverantwortung'
          description: |-
            Aggregationsverantwortung, wem die Bilanzierung zugeordnet ist. 
            CCI 6 
            PI 55043 55168 55169 55195 55196 55223 55224 
        zeitreihentyp:
          type: string
          description: |
            Zeitreihentyp 
            Summenzeitreihentyp Z21
            CCI 15 Z21 
            PI 55670 55671 55074 55075 55076 55065 55066 55196
            MSCONS Zeitreihentyp
        prognosegrundlage:
          $ref: '#/components/schemas/Prognosegrundlage'
          description: >-
            Prognosegrundlage, aufgrund dieser Information wird das
            Bilanzierungsverfahren, welches in den Prozessen erwähnt wird,
            abgeleitet. 

            PI 55013 55613 55614 55126 55156 55674 55675 55672 55673 55628 55634
            55035 55095 55060 55043 55168 55169 55195 55196

            CAV Z38 

            ORDERS

            PI 17120

            Gas UTILMD Bereits ausgetauschte Prognosegrundlage

            ZB0 Prognose auf Basis von Werten gültig

            ZB1 Prognose auf Basis von Profilen gültig

            CCI ZB0

            PI 44139 44142
        bilanzierungsbeginn:
          type: string
          format: date-time
          description: >-
            Beginn der Zuordnung einer MaLo, Tranche zum Bilanzkreis. 

            DTM 158

            55238 55239 55062 55064 55065 55066 55071 55195 55196 55223 55224
            55197 55199 55203 55204 55205 55209 55210 55211
        bilanzierungsende:
          type: string
          format: date-time
          description: >-
            Beendigung der Zuordnung einer MaLo, Tranche zum Bilanzkreis.

            DTM 159

            55240 55241 55242 55243 55063 55064 55065 55066 55072 55195 55196
            55223 55224 55198 55200 55206 55207 55208 55212 55213 55214
        bilanzkreis:
          type: string
          description: >-
            Bilanzkreis bzw. das Konto, auf dem die Bilanzierung durchgeführt
            wird.

            CCI Z19

            PI 55613 55614 55126 55156 55674 55675 55672 55673 55670 55671 55074
            55075 55076 55065 55066 55195 55196
        fallgruppenzuordnung:
          $ref: '#/components/schemas/Fallgruppenzuordnung'
          description: >-
            Fallgruppenzuordnung nach GABi Gas

            GABi- SLP-Kunden analytisches Verfahren - Exit SLPana

            GABi- SLP-Kunden synthetisches Verfahren - Exit SLPsyn

            CCI Z17

            PI 44123 44156 44157 44001 44002 44013 44014 44019 44020 44021 44035
            44103 44104
        temperaturarbeit: &ref_0
          $ref: '#/components/schemas/Menge'
          description: >-
            Kundenwert TLP, Angabe der spezifischen Arbeit für eine
            tagesparameterabhängige Marktlokation als Zahlenwert, angepassten
            elektrischen Arbeit einer tagesparameterabhängigen Marktlokationon.
            Schließt auch gemeinsame Messung ein - SLP und TLP-.

            QTY Z10

            PI 55672 55673 55628 55634 55035 55095 55060 55065 55066

            QTY 265

            PI 55013 55126 55156 55672 55673 55628 55634 55035 55095 55060 55043
            55168 55169 55065 55066

            QTY Z08

            PI 55013 55126 55156 55628 55634 55035 55095 55060 55043 55168 55169
            55065 55066
        jahresverbrauchsprognose: *ref_0
        kundenwert: *ref_0
        verbrauchsaufteilung: *ref_0
        wahlrechtPrognosegrundlage: &ref_1
          $ref: '#/components/schemas/WahlrechtPrognosegrundlage'
          description: >-
            Wahlrecht der Prognosegrundlage (true = Wahlrecht beim Lieferanten
            vorhanden)
        grundWahlrechtPrognosegrundlage: *ref_1
        abwicklungsmodell:
          $ref: '#/components/schemas/Abwicklungsmodell'
          description: >-
            Abwicklungsmodell, aufgrund dieser Information wird für die
            Bilanzierung abgeleitet, ob die Malo mit dem zugeordneten
            Bilanzkreis im Modell 1 ZE9 bilanziert wird oder die Energiemenge
            der Malo als NGZ im Modell 2 ZF0 in ein benachbartes
            Bilanzierungsgebiet übergeben wird.

            CAV ZA2

            PI 55628 55634 55043 55168 55169 
        vorjahresverbrauch: *ref_0
        datenqualitaet:
          $ref: '#/components/schemas/Datenqualitaet'
          description: Datenqualität
        gueltigkeitszeitraum:
          $ref: '#/components/schemas/Zeitraum'
          description: Gültigkeitszeitraum
        lastprofile:
          type: array
          items: &ref_2
            $ref: '#/components/schemas/Lastprofil'
          description: |-
            Normiertes Profil  - Profilbezeichnung
            CCI Z02 
        lastprofileBilanzierungsbeteiligter:
          type: array
          items: *ref_2
          description: Lastprofile des Bilanzierungsbeteiligten
        detailsPrognosegrundlage:
          type: array
          items:
            $ref: '#/components/schemas/Profiltyp'
          description: >-
            Prognosegrundlage - dient zur genaueren Wertspezifizierung des
            Merkmals im vorangegangenen Segments Prognosegrundlage. 

            CAV E02 

            PI 55013 55613 55614 55126 55156 55672 55673 55628 55634 55035 55095
            55060 55043 55168 55169 55195 55196
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - marktlokationsId
        - aggregationsverantwortung
        - zeitreihentyp
        - prognosegrundlage
        - bilanzierungsbeginn
        - bilanzierungsende
        - bilanzkreis
        - fallgruppenzuordnung
        - temperaturarbeit
        - jahresverbrauchsprognose
        - kundenwert
        - verbrauchsaufteilung
        - wahlrechtPrognosegrundlage
        - grundWahlrechtPrognosegrundlage
        - abwicklungsmodell
        - vorjahresverbrauch
        - datenqualitaet
        - gueltigkeitszeitraum
        - lastprofile
        - lastprofileBilanzierungsbeteiligter
        - detailsPrognosegrundlage
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Profiltyp:
      type: string
      title: Profiltyp
      description: Profiltyp
      enum:
        - SLP_SEP
        - TLP_TEP
        - TEP
      x-apidog-enum:
        - value: SLP_SEP
          name: SLP/SEP
          description: E02
        - value: TLP_TEP
          name: TLP/TEP
          description: E14
        - value: TEP
          name: TEP mit Referenzmessung
          description: Z36
      x-apidog-folder: ''
    Lastprofil:
      title: Lastprofil
      type: object
      properties:
        bezeichnung:
          type: string
          description: >-
            Bezeichnung des Profils. Es dürften nur Codes aus der gültigen Liste
            der Profildefinitionen des jeweiligen NB und zugehörigem
            Bilanzierungsgebiet eingetragen werden. 

            CAV ABC

            PI 55613 55614 55126 55156 55672 55673 55628 55634 55035 55095 55043
            55168 55169 55065 55066 55073 55195 55196 55223 55224 

            MSCONS LOC Z04 
        verfahren:
          $ref: '#/components/schemas/Profilverfahren'
          description: Verfahren - spezifischen Eigenschaften
        profilart:
          $ref: '#/components/schemas/Profilart'
          description: >-
            Standardlastprofil

            CCI Z02

            PI 55613 55614 55126 55156 55628 55634 55035 55043 55168 55169 55065
            55066 55073 55195 55196 55223 55224

            ORDERS PI 17201
        profilschar:
          type: string
          description: |-
            Code für die Profilschar, Bezeichnung der Profilschar.
            CAV COD
            PI 55126 55156 55672 55673 55035 55095 55073 
            MSCONS LOC Z06
            PI 13011
        einspeisung:
          type: boolean
          description: >-
            Standardeinspeiseprofil 

            CCI Z04

            PI 55672 55673 55628 55634 55095 55043 55168 55169 55065 55066 55073
            55224

            ORDERS PI 17201

            Z05 tagesparameterabhängiges Einspeiseprofil

            PI 55672 55673 55628 55634 55095 55043 55169 55065 55066 55073

            ORDERS PI 17201
        herausgeber:
          type: string
          description: |-
            Herausgeber des Lastprofils
            89 Vergeben vom Händler (hier Netzbetreiber)
            293 DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)
        tagesparameter:
          $ref: '#/components/schemas/Tagesparameter'
          description: >-
            Klimazone / Temperaturmessstelle - Angabe der Temperaturmessstelle
            werden die ID und der Anbieter aus der EDI@Energy-Codeliste
            angegeben.
        referenzprofilbezeichnung:
          type: string
          description: >-
            Code des Referenzprofils

            CAV COD

            PI 55672 55673 55628 55634 55095 55043 55168 55169 55065 55066
            55073 
      x-apidog-orders:
        - bezeichnung
        - verfahren
        - profilart
        - profilschar
        - einspeisung
        - herausgeber
        - tagesparameter
        - referenzprofilbezeichnung
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Tagesparameter:
      title: Tagesparameter
      type: object
      properties:
        klimazone:
          type: string
          description: |-
            Klimazone des Tagesparameters (derzeit ist Tagesparameter)
            CCI ZA0
            PI 55126 55156 55672 55673 55035 55095 55043 55168 55169 55073
        temperaturmessstelle:
          type: string
          description: >-
            Temperaturmessstelle Messstelle des Tagesparameters (derzeit ist nur
            die Temperatur ein erlaubter Tagesparameter)

            CCI Z99

            PI 55126 55156 55672 55673 55035 55095 55043 55168 55169 55073
        dienstanbieter:
          type: string
          description: Dienstanbieter auf Basis der EDI@Energy Codeliste
        herausgeber:
          $ref: '#/components/schemas/Herausgeber'
          description: |-
            Herausgeber der ID
            PI 55126 55156 55672 55673 55035 55095 55043 55168 55169 55073
      x-apidog-orders:
        - klimazone
        - temperaturmessstelle
        - dienstanbieter
        - herausgeber
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Herausgeber:
      type: string
      title: Herausgeber
      description: Herausgeber
      enum:
        - NB
        - BDEW
        - TUM
      x-apidog-enum:
        - value: NB
          name: Vergeben vom Händler (hier Netzbetreiber)
          description: '89'
        - value: BDEW
          name: DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)
          description: '293'
        - value: TUM
          name: ''
          description: ''
      x-apidog-folder: ''
    Profilart:
      type: string
      title: Profilart
      description: Profilart
      enum:
        - ART_STANDARDLASTPROFIL
        - ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL
        - ART_LASTPROFIL
      x-apidog-enum:
        - value: ART_STANDARDLASTPROFIL
          name: Standardlastprofil
          description: Z02
        - value: ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL
          name: tagesparameterabhängiges Lastprofil
          description: Z03
        - value: ART_LASTPROFIL
          name: ''
          description: ''
      x-apidog-folder: ''
    Profilverfahren:
      type: string
      title: Profilverfahren
      description: Profilverfahren
      enum:
        - SYNTHETISCH
        - ANALYTISCH
      x-apidog-enum:
        - value: SYNTHETISCH
          name: synthetisches Verfahren
          description: E01
        - value: ANALYTISCH
          name: analytisches Verfahren
          description: Z10
      x-apidog-folder: ''
    Zeitraum:
      title: Zeitraum
      type: object
      properties:
        zeiteinheit: &ref_3
          $ref: '#/components/schemas/Zeiteinheit'
          description: nicht in Benutzung
        dauer:
          type: integer
          description: Zeitspanne, Wert
        startdatum:
          type: string
          format: date-time
          description: |-
            Datum aus 
            DTM Z25 Verwendung der Daten ab 
            DTM 163 Verarbeitung, Beginndatum/-zeit
            DTM 155 Rechnungsperiode, Beginndatum
            DTM Z42 vorläufiger Abrechnungszeitraum Beginn
        enddatum:
          type: string
          format: date-time
          description: |-
            Datum aus 
            DTM Z26 Verwendung der Daten bis 
            DTM164 Verarbeitung, Endedatum/-zeit
            DTM 156 Rechnungsperiode, Endedatum
            DTM Z43 vorläufiger Abrechnungszeitraum Ende
        einheit: *ref_3
        ableseZeitraum:
          type: string
          description: |-
            Turnusablesung des NB
            DTM 752
            PI 44113 44140 44142 44043 44168 44169 44060 
        abrechnungsZeitraum:
          type: string
          description: |-
            Termin, zu dem die Netznutzungsabrechnung des NB erfolgt
            DTM Z21
            PI 44112 44139 44142 44002 44013 44014 44035
        zeitraumText:
          type: string
          description: ZeitraumText
        zeitraumId:
          type: integer
          description: |-
            Referenz auf Zeitraum-ID
            RFF Z46
            PI 25001
      x-apidog-orders:
        - zeiteinheit
        - dauer
        - startdatum
        - enddatum
        - einheit
        - ableseZeitraum
        - abrechnungsZeitraum
        - zeitraumText
        - zeitraumId
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zeiteinheit:
      type: string
      title: Zeiteinheit
      description: Zeiteinheit
      enum:
        - SEKUNDE
        - MINUTE
        - STUNDE
        - VIERTEL_STUNDE
        - TAG
        - WOCHE
        - MONAT
        - QUARTAL
        - HALBJAHR
        - JAHR
      x-apidog-enum:
        - value: SEKUNDE
          name: ''
          description: ''
        - value: MINUTE
          name: ''
          description: ''
        - value: STUNDE
          name: ''
          description: ''
        - value: VIERTEL_STUNDE
          name: ''
          description: ''
        - value: TAG
          name: Tag
          description: '804'
        - value: WOCHE
          name: Woche
          description: '803'
        - value: MONAT
          name: Monat
          description: '802'
        - value: QUARTAL
          name: ''
          description: ''
        - value: HALBJAHR
          name: ''
          description: ''
        - value: JAHR
          name: ''
          description: ''
      x-apidog-folder: ''
    Datenqualitaet:
      type: string
      title: Datenqualitaet
      description: Datenqualitaet
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
      x-apidog-enum:
        - value: ERWARTETE_DATEN
          name: ''
          description: abhängig vom BO
        - value: IM_SYSTEM_VORHANDENE_DATEN
          name: ''
          description: abhängig vom BO
        - value: INFORMATIVE_DATEN
          name: ''
          description: abhängig vom BO
        - value: GUELTIGE_DATEN
          name: ''
          description: abhängig vom BO
        - value: KEINE_DATEN
          name: ''
          description: abhängig vom BO
        - value: IM_SYSTEM_KEINE_DATEN_VORHANDEN
          name: ''
          description: abhängig vom BO
        - value: KEINE_DATEN_ERWARTET
          name: ''
          description: abhängig vom BO
        - value: DIFFERENZ_DATEN
          name: ''
          description: abhängig vom BO
        - value: DIFFERENZ_ERWARTETE_DATEN
          name: ''
          description: abhängig vom BO
        - value: DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN
          name: ''
          description: abhängig vom BO
      x-apidog-folder: ''
    Abwicklungsmodell:
      type: string
      title: Abwicklungsmodell
      description: Abwicklungsmodell
      enum:
        - MODELL_1_BILANZIERUNG_AN_MARKTLOKATION
        - MODELL_2_BILANZIERUNG_IM_BILANZIERUNGSGEBIET
      x-apidog-enum:
        - value: MODELL_1_BILANZIERUNG_AN_MARKTLOKATION
          name: Modell 1 "Bilanzierung an der Marktlokation"
          description: ZE9
        - value: MODELL_2_BILANZIERUNG_IM_BILANZIERUNGSGEBIET
          name: Modell 2 "Bilanzierung im Bilanzierungsgebiet (BG) des LPB"
          description: ZF0
      x-apidog-folder: ''
    WahlrechtPrognosegrundlage:
      title: WahlrechtPrognosegrundlage
      type: string
      enum:
        - DURCH_LF
        - DURCH_LF_NICHT_GEGEBEN
        - NICHT_WEGEN_GROSSEN_VERBRAUCHS
        - NICHT_WEGEN_EIGENVERBRAUCH
        - NICHT_WEGEN_TAGES_VERBRAUCH
        - NICHT_WEGEN_ENWG
      description: WahlrechtPrognosegrundlage
      x-apidog-folder: ''
    Menge:
      title: Menge
      type: object
      properties:
        wert:
          type: number
          format: float
          description: Wert Mengenangabe
        einheit:
          $ref: '#/components/schemas/Mengeneinheit'
          description: Mengeneinheit
      x-apidog-orders:
        - wert
        - einheit
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Mengeneinheit:
      type: string
      title: Mengeneinheit
      description: >-
        Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden
        können
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
      x-apidog-enum:
        - value: W
          name: ''
          description: ''
        - value: WH
          name: ''
          description: ''
        - value: KW
          name: ''
          description: ''
        - value: KWH
          name: Kilowattstunde
          description: KWH
        - value: KVARH
          name: ''
          description: ''
        - value: MW
          name: ''
          description: ''
        - value: MWH
          name: ''
          description: ''
        - value: STUECK
          name: Stück
          description: H87
        - value: KUBIKMETER
          name: ''
          description: ''
        - value: STUNDE
          name: ''
          description: ''
        - value: TAG
          name: Tag
          description: ZD8
        - value: MONAT
          name: Monat
          description: MON
        - value: JAHR
          name: Jahr
          description: ANN
        - value: PROZENT
          name: Prozent
          description: P1
        - value: ANZAHL
          name: ''
          description: ''
        - value: VAR
          name: ''
          description: ''
        - value: KVAR
          name: ''
          description: ''
        - value: VARH
          name: ''
          description: ''
        - value: KWHK
          name: ''
          description: ''
        - value: Z16
          name: kWh/K (Kilowatt-Stunde/Kelvin)
          description: Z16
        - value: KWT
          name: Kilowatt
          description: ''
      x-apidog-folder: ''
    Fallgruppenzuordnung:
      type: string
      title: Fallgruppenzuordnung
      description: Fallgruppenzuordnung
      enum:
        - GABI_RLMmT
        - GABI_RLMoT
        - GABI_RLMNEV
      x-apidog-enum:
        - value: GABI_RLMmT
          name: RLM-Kunde in Tagesregime - Exit
          description: GABi-RLMmT
        - value: GABI_RLMoT
          name: GABi-RLMoT
          description: RLM-Kunde im Stundenregime - Exit
        - value: GABI_RLMNEV
          name: >-
            Nominierungsersatzverfahren - Exit (Hinweis: Dieser Code darf nur
            für Liefermonate vor dem 01.10.2016 genutzt werden)
          description: GABi-RLMNEV
      x-apidog-folder: ''
    Prognosegrundlage:
      type: string
      title: Prognosegrundlage
      description: Prognosegrundlage
      enum:
        - WERTE
        - PROFILE
      x-apidog-enum:
        - value: WERTE
          name: Prognose auf Basis von Werten
          description: ZC0/Z39
        - value: PROFILE
          name: Prognose auf Basis von Profilen
          description: ZA6/Z38
      x-apidog-folder: ''
    Aggregationsverantwortung:
      type: string
      title: Aggregationsverantwortung
      description: Aggregationsverantwortung
      enum:
        - UENB
        - VNB
      x-apidog-enum:
        - value: UENB
          name: ÜNB
          description: ZA9
        - value: VNB
          name: NB
          description: ZA8
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
