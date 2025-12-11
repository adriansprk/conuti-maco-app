# Lastgangs einer Lokation lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getEnergyAmountLoadCurve:
    get:
      summary: Lastgangs einer Lokation lesen
      deprecated: false
      description: >-
        Lesen eines Lastgangs einer Lokation (Parameter1) mit LokationsTyp
        (parameter2) zum Start- und Endezeitpunkt (Parameter3/Parameter4) und
        einer OBIS Kennzahl (Parameter4 optional)
      operationId: LESEN_ENERGIEMENGE_LASTGANG
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
          description: 'LokationsTyp '
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
        - name: parameter5
          in: query
          description: OBIS Kennzahl
          required: true
          schema:
            type: string
            examples:
              - '123456789'
        - name: parameter6
          in: query
          description: >-
            abrechnungsrevant? [true/false = default null) Wenn Parameter null
            ist, soll dieser in der Abfage ignoriert werden, wenn true soll
            explizit geprüft werden ob Lastgang abrechnungsrelevant ist, wenn
            false soll explizit geprüft werden ob nicht Lastgang NICHT
            abrechnungsrelevant ist
          required: true
          schema:
            type: boolean
            default: null
            examples:
              - null
        - name: parameter7
          in: query
          description: >-
            bilanzierungsrelevant) [true/false = default null) WennParameter
            null ist, soll dieser in der Abfage ignoriert werden, wenn true soll
            explizit geprüft werden ob Lastgang bilanzierungsrelevant ist, wenn
            false soll explizit geprüft werden ob nicht Lastgang NICHT
            bilanzierungsrelevant ist
          required: true
          schema:
            type: boolean
            default: null
            examples:
              - null
        - name: command
          in: query
          description: >-
            Entspricht der operationId dieser Schnittstelle. Diese Operation Id
            entspricht dem Command im Camunda Konnektor Prozess. Wenn das
            Backend einen generischen Endpunkt bereitstellt, kann dieses Command
            gentutzt werden um zu definieren welche Operation ausgeführt werden
            soll.
          required: false
          example: SAP_LESEN_ENERGIEMENGE_LASTGANG
          schema:
            type: string
        - name: Authorization
          in: header
          description: ''
          required: false
          example: Bearer {{accessToken}}
          schema:
            type: string
      responses:
        '200':
          description: >-
            Erfolgreiches Lesen des Lastgangs | Successful reading of the load
            profile
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Energiemenge'
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017016-run
components:
  schemas:
    Energiemenge:
      title: Energiemenge
      type: object
      properties:
        boTyp:
          $ref: '#/components/schemas/BOTyp'
          default: ENERGIEMENGE
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        lokationsId:
          type: string
          description: >-
            Angabe der Identifikation, für den die Daten gelten

            LOC 172

            PI 13017 13019 13016 13015 13028 13002 13009 13018 13025 13008 13003
            13023 13020 13022 13021 13007 13013 13014 13027 13006
        lokationsTyp:
          $ref: '#/components/schemas/Lokationstyp'
          description: Gibt an, ob es sich um eine Markt- oder Messlokation handelt.
        fertigstellungsdatum:
          type: string
          format: date-time
          description: >-
            eindeutige Versionsnummer - Fertigstellungsdatum/-zeit

            DTM 293

            PI 13010 13011 13012 13003 13023 13005 13026 13020 13022 13021 13007
            13013
        startdatum:
          type: string
          format: date-time
          description: >
            Beginn-Zeitpunkt des Übertragungszeitraumes

            DTM 163

            PI 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010 13012
            13003 13023 13005 13026 13020 13022 13021 13007 13014 13027 
        enddatum:
          type: string
          format: date-time
          description: >-
            Ende-Zeitpunkt des Übertragungszeitraumes

            DTM 164

            PI 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010 13012
            13003 13023 13005 13026 13020 13022 13021 13007 13014 13027 
        bilanzierungsdatum:
          type: string
          format: date-time
          description: |-
            Bilanzierungsmonat
            DTM 492
            PI 13003 13023 13020 13013
        beginndatum:
          type: string
          format: date-time
          description: |-
            Gültigkeit, Beginndatum Profilschar 
            DTM 157
            PI 13011
        referenzStammdatenmeldungMsb:
          type: string
          description: |-
            Referenz auf vorherige Stammdatenmeldung des MSB
            RFF Z30
            PI 13002
        konfiguration:
          type: string
          description: |-
            Konfigurations-ID
            RFF AGK
            PI 13017 13019 
        energieverbrauch:
          type: array
          items:
            $ref: '#/components/schemas/Verbrauch'
          description: Gibt den Verbrauch in einer Zeiteinheit an.
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - lokationsId
        - lokationsTyp
        - fertigstellungsdatum
        - startdatum
        - enddatum
        - bilanzierungsdatum
        - beginndatum
        - referenzStammdatenmeldungMsb
        - konfiguration
        - energieverbrauch
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Energiemenge.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Verbrauch:
      title: Verbrauch
      type: object
      properties:
        startdatum:
          type: string
          format: date-time
          description: >-
            Beginn Messperiode

            DTM 163

            PI 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010 13012
            13003 13023 13005 13026 13020 13022 13021 13007 13014 13027 
        enddatum:
          type: string
          format: date-time
          description: >-
            Ende Messperiode

            DTM 164

            PI 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010 13012
            13003 13023 13005 13026 13020 13022 13021 13007 13014 13027 
        wertermittlungsverfahren:
          $ref: '#/components/schemas/Wertermittlungsverfahren'
          description: Messwert oder Prognosewert - bezieht sich auf die Statusangabe
        messwertstatus:
          $ref: '#/components/schemas/Messwertstatus'
          description: >-
            Statusangaben

            PI 13017 13019 13016 13015 13002 13009 13018 13025 13008 13003 13022
            13021 13007 13027 13010 13011 13012 13003 13023 13005 13026 13020
            13013 13014 13028 
        obiskennzahl:
          type: string
          description: >-
            Produktidentifikation unter Verwendung des OBIS-Kennzeichens

            PIA 5

            SRW OBIS-Kennzahl

            PI 13017 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010
            13011 13012 13003 13005 13007 13027

            Z02 BDEW OBIS-ähnliche Kennzahl

            PI 13016 13011 13013 13014

            Z08 Medium

            PI 13023 13026 13020 13022 13021 
        wert:
          type: number
          format: float
          description: |-
            Energiemenge, Mengenangabe MSCONS
            QTY 136 Erreichte Menge in dem Zeitintervall
            PI 21045
        einheit:
          $ref: '#/components/schemas/Mengeneinheit'
          description: |-
            Maßeinheit
            PI 13021 13023 13026 13020 13022
        type:
          $ref: '#/components/schemas/Verbrauchsmengetyp'
          description: nicht in Benutzung
        tarifstufe:
          $ref: '#/components/schemas/Tarifstufe'
          description: nicht in Benutzung
        nutzungszeitpunkt:
          type: string
          format: date-time
          description: |-
            Nutzungszeitpunkt - eindeutige Zählerstandszuordnung
            DTM 7
            PI 13017 13002 13027 
        ausfuehrungszeitpunkt:
          type: string
          format: date-time
          description: |-
            Ausführungs- / Änderungszeitpunkt - Konstruktionsänderungsdatum
            DTM 60
            PI 13017 13002
        position:
          type: integer
          description: >-
            Positionsdaten -  zeigt den Beginn eines Positionsteils, Hochzählung

            LIN 1

            PI 13017 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010
            13011 13012 13003 13023 13005 13026 13020 13022 13021 13007 13013
            13014 13027
        ablesedatum:
          type: string
          format: date-time
          description: |-
            Ablesedatum
            DTM 9
            PI 13017 13002 
        leistungsperiode:
          type: string
          description: |-
            Leistungsperiode
            DTM 306
            PI 13016 13015 13013
        statuszusatzinformationen:
          type: array
          items:
            $ref: '#/components/schemas/StatusZusatzInformation'
          description: Plausibilisierungshinweis
      x-apidog-orders:
        - startdatum
        - enddatum
        - wertermittlungsverfahren
        - messwertstatus
        - obiskennzahl
        - wert
        - einheit
        - type
        - tarifstufe
        - nutzungszeitpunkt
        - ausfuehrungszeitpunkt
        - position
        - ablesedatum
        - leistungsperiode
        - statuszusatzinformationen
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    StatusZusatzInformation:
      title: StatusZusatzInformation
      type: object
      properties:
        art:
          $ref: '#/components/schemas/StatusArt'
          description: |-
            Z33 Plausibilisierungshinweis
            STS Z33
        status:
          $ref: '#/components/schemas/Status'
          description: |-
            Statusanlaß
            STS Z34
            PI 13017 13019 13016 13002 13009 13018 13025 13008 13002 13007
      x-apidog-orders:
        - art
        - status
      description: .
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Status:
      type: string
      title: Status
      description: Status
      enum:
        - KUNDENSELBSTABLESUNG
        - LEERSTAND
        - REALER_ZAEHLERUEBERLAUF_GEPRUEFT
        - PLAUSIBEL_WG_KONTROLLABLESUNG
        - PLAUSIBEL_WG_KUNDENHINWEIS
        - AUSTAUSCH_DES_ERSATZWERTES
        - RECHENWERT
        - BASIS_MME
        - VERGLEICHSMESSUNG_GEEICHT
        - VERGLEICHSMESSUNG_NICHT_GEEICHT
        - MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN
        - MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN
        - INTERPOLATION
        - HALTEWERT
        - BILANZIERUNG_NETZABSCHNITT
        - HISTORISCHE_MESSWERTE
        - STATISTISCHE_METHODE
        - AUFTEILUNG
        - VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS
        - UMGANGS_UND_KORREKTURMENGEN
        - ANGABEN_MESSLOKATION
        - KEIN_ZUGANG
        - KOMMUNIKATIONSSTOERUNG
        - NETZAUSFALL
        - SPANNUNGSAUSFALL
        - STATUS_GERAETEWECHSEL
        - KALIBRIERUNG
        - GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN
        - MESSEINRICHTUNG_GESTOERT_DEFEKT
        - UNSICHERHEIT_MESSUNG
        - BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK
        - MENGENUMWERTUNG_VOLLSTAENDIG
        - UHRZEIT_GESTELLT_SYNCHRONISATION
        - MESSWERT_UNPLAUSIBEL
        - FALSCHER_WANDLERFAKTOR
        - FEHLERHAFTE_ABLESUNG
        - AENDERUNG_DER_BERECHNUNG
        - UMBAU_DER_MESSLOKATION
        - DATENBEARBEITUNGSFEHLER
        - BRENNWERTKORREKTUR
        - Z_ZAHL_KORREKTUR
        - STOERUNG_DEFEKT_MESSEINRICHTUNG
        - AENDERUNG_TARIFSCHALTZEITEN
        - TARIFSCHALTGERAET_DEFEKT
        - IMPULSWERTIGKEIT_NICHT_AUSREICHEND
        - ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL
        - ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL
        - WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET
        - GESTOERTE_WERTE
        - WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN
        - KONSISTENZ_UND_SYNCHRONPRUEFUNG
        - GRUND_ANGABEN_MESSLOKATION
        - >-
          ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR
        - UMSTELLUNG_GASQUALITAET
        - >-
          ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
        - >-
          ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
        - >-
          ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
        - >-
          ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
        - GESCHEITERT
        - AUSGEBAUT
      x-apidog-enum:
        - value: KUNDENSELBSTABLESUNG
          name: Kundenselbstablesung
          description: Z83
        - value: LEERSTAND
          name: Leerstand
          description: Z84
        - value: REALER_ZAEHLERUEBERLAUF_GEPRUEFT
          name: Realer Zählerüberlauf geprüf
          description: Z85
        - value: PLAUSIBEL_WG_KONTROLLABLESUNG
          name: Plausibel wg. Kontrollablesung
          description: Z86
        - value: PLAUSIBEL_WG_KUNDENHINWEIS
          name: Plausibel wg. Kundenhinweis
          description: Z87
        - value: AUSTAUSCH_DES_ERSATZWERTES
          name: Austausch des Ersatzwertes
          description: ZC3
        - value: RECHENWERT
          name: Rechenwert
          description: ZR5
        - value: BASIS_MME
          name: Wert auf Basis der modernen Messeinrichtung
          description: ZS2
        - value: VERGLEICHSMESSUNG_GEEICHT
          name: Vergleichsmessung (geeicht)
          description: Z88
        - value: VERGLEICHSMESSUNG_NICHT_GEEICHT
          name: Vergleichsmessung (nicht geeicht)
          description: Z89
        - value: MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN
          name: Messwertnachbildung aus geeichten Werten
          description: Z90
        - value: MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN
          name: Messwertnachbildung aus nicht geeichten Werten
          description: Z91
        - value: INTERPOLATION
          name: Interpolation
          description: Z92
        - value: HALTEWERT
          name: Haltewert
          description: Z93
        - value: BILANZIERUNG_NETZABSCHNITT
          name: Bilanzierung Netzabschnit
          description: Z94
        - value: HISTORISCHE_MESSWERTE
          name: Historische Messwerte
          description: Z95
        - value: STATISTISCHE_METHODE
          name: Statistische Methode
          description: ZJ2
        - value: AUFTEILUNG
          name: Aufteilung
          description: ZQ8
        - value: VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS
          name: Verwendung von Werten des Störmengenzählwerks
          description: ZQ9
        - value: UMGANGS_UND_KORREKTURMENGEN
          name: Umgangs- und Korrekturmengen
          description: ZR0
        - value: ANGABEN_MESSLOKATION
          name: Ersatzwertbildungsverfahren gemäß Angaben auf Ebene der Messlokation
          description: ZS0
        - value: KEIN_ZUGANG
          name: kein Zugang
          description: Z74
        - value: KOMMUNIKATIONSSTOERUNG
          name: Kommunikationsstörung
          description: Z75
        - value: NETZAUSFALL
          name: Netzausfall
          description: Z76
        - value: SPANNUNGSAUSFALL
          name: Spannungsausfall
          description: Z77
        - value: STATUS_GERAETEWECHSEL
          name: Gerätewechsel
          description: Z78
        - value: KALIBRIERUNG
          name: Kalibrierung
          description: Z79
        - value: GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN
          name: Gerät arbeitet außerhalb der Betriebsbedingungen
          description: Z80
        - value: MESSEINRICHTUNG_GESTOERT_DEFEKT
          name: Messeinrichtung gestört/defekt
          description: Z81
        - value: UNSICHERHEIT_MESSUNG
          name: Unsicherheit Messung
          description: Z82
        - value: BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK
          name: Berücksichtigung Störmengenzählwerk
          description: Z98
        - value: MENGENUMWERTUNG_VOLLSTAENDIG
          name: Mengenumwertung unvollständig
          description: Z99
        - value: UHRZEIT_GESTELLT_SYNCHRONISATION
          name: Uhrzeit gestellt /Synchronisation
          description: ZA0
        - value: MESSWERT_UNPLAUSIBEL
          name: Messwert unplausibel
          description: ZA1
        - value: FALSCHER_WANDLERFAKTOR
          name: Falscher Wandlerfaktor
          description: ZA3
        - value: FEHLERHAFTE_ABLESUNG
          name: Fehlerhafte Ablesung
          description: ZA4
        - value: AENDERUNG_DER_BERECHNUNG
          name: Änderung der Berechnung
          description: ZA5
        - value: UMBAU_DER_MESSLOKATION
          name: Umbau der Messlokation
          description: ZA6
        - value: DATENBEARBEITUNGSFEHLER
          name: Datenbearbeitungsfehler
          description: ZA7
        - value: BRENNWERTKORREKTUR
          name: Brennwertkorrektur
          description: ZA8
        - value: Z_ZAHL_KORREKTUR
          name: Z-Zahl-Korrektur
          description: ZA9
        - value: STOERUNG_DEFEKT_MESSEINRICHTUNG
          name: Störung / Defekt Messeinrichtung
          description: ZB0
        - value: AENDERUNG_TARIFSCHALTZEITEN
          name: Änderung Tarifschaltzeiten
          description: ZB9
        - value: TARIFSCHALTGERAET_DEFEKT
          name: Tarifschaltgerät defekt
          description: ZC2
        - value: IMPULSWERTIGKEIT_NICHT_AUSREICHEND
          name: Impulswertigkeit nicht ausreichend
          description: ZC4
        - value: ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL
          name: Energiemenge in ungemessenem Zeitintervall
          description: ZJ8
        - value: ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL
          name: Energiemenge aus dem ungepairten Zeitintervall
          description: ZJ9
        - value: WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET
          name: Wartungsarbeiten an geeichtem Messgerät
          description: ZR1
        - value: GESTOERTE_WERTE
          name: gestörte Werte
          description: ZR2
        - value: WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN
          name: Wartungsarbeiten an eichrechtskonformen Messgeräten
          description: ZR3
        - value: KONSISTENZ_UND_SYNCHRONPRUEFUNG
          name: Konsistenz- und Synchronprüfung
          description: ZR4
        - value: GRUND_ANGABEN_MESSLOKATION
          name: Grund der Ersatzwertbildung gemäß Angaben auf Ebene der Messlokation
          description: ZS9
        - value: >-
            ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR
          name: >-
            Anforderung in die Vergangenheit, zum angeforderten Zeitpunkt liegt
            kein Wert vor
          description: ZT8
        - value: UMSTELLUNG_GASQUALITAET
          name: Umstellung Gasqualität
          description: ZG3
        - value: >-
            ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
          name: >-
            Zählerstand zum Beginn der angegebenen Energiemenge vorhanden und
            kommuniziert
          description: Z36
        - value: >-
            ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
          name: >-
            Zählerstand zum Ende der angegebenen Energiemenge vorhanden und
            kommuniziert
          description: Z37
        - value: >-
            ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
          name: >-
            Zählerstand zum Beginn der angegebenen Energiemenge nicht vorhanden
            da Mengenabgrenzung
          description: Z38
        - value: >-
            ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
          name: >-
            Zählerstand zum Ende der angegebenen Energiemenge nicht vorhanden da
            Mengenabgrenzung
          description: Z39
        - value: GESCHEITERT
          name: ''
          description: ''
        - value: AUSGEBAUT
          name: ''
          description: ''
      x-apidog-folder: ''
    StatusArt:
      type: string
      title: StatusArt
      description: StatusArt
      enum:
        - PLAUSIBILISIERUNGSHINWEIS
        - ERSATZWERTBILDUNGSVERFAHREN
        - KORREKTURGRUND
        - GRUND_ERSATZWERTBILDUNGSVERFAHREN
        - GASQUALITAET
        - MESSKLASSIFIZIERUNG
      x-apidog-enum:
        - value: PLAUSIBILISIERUNGSHINWEIS
          name: Plausibilisierungshinweis
          description: Z33
        - value: ERSATZWERTBILDUNGSVERFAHREN
          name: Ersatzwertbildungsverfahren
          description: Z32
        - value: KORREKTURGRUND
          name: Korrekturgrund
          description: Z34
        - value: GRUND_ERSATZWERTBILDUNGSVERFAHREN
          name: Grund der Ersatzwertbildung
          description: Z40
        - value: GASQUALITAET
          name: Gasqualität
          description: Z31
        - value: MESSKLASSIFIZIERUNG
          name: Messklassifizierung
          description: '10'
      x-apidog-folder: ''
    Tarifstufe:
      type: string
      title: Tarifstufe
      description: Tarifstufe
      enum:
        - TARIFSTUFE_0
        - TARIFSTUFE_1
        - TARIFSTUFE_2
        - TARIFSTUFE_3
        - TARIFSTUFE_4
        - TARIFSTUFE_5
        - TARIFSTUFE_6
        - TARIFSTUFE_7
        - TARIFSTUFE_8
        - TARIFSTUFE_9
      x-apidog-enum:
        - value: TARIFSTUFE_0
          name: Tarifstufe 0
          description: Z20
        - value: TARIFSTUFE_1
          name: Tarifstufe 1
          description: Z21
        - value: TARIFSTUFE_2
          name: Tarifstufe 2
          description: Z22
        - value: TARIFSTUFE_3
          name: Tarifstufe 3
          description: Z23
        - value: TARIFSTUFE_4
          name: Tarifstufe 4
          description: Z24
        - value: TARIFSTUFE_5
          name: Tarifstufe 5
          description: Z25
        - value: TARIFSTUFE_6
          name: Tarifstufe 6
          description: Z26
        - value: TARIFSTUFE_7
          name: Tarifstufe 7
          description: Z27
        - value: TARIFSTUFE_8
          name: Tarifstufe 8
          description: Z28
        - value: TARIFSTUFE_9
          name: Tarifstufe 9
          description: Z29
      x-apidog-folder: ''
    Verbrauchsmengetyp:
      title: Verbrauchsmengetyp
      type: string
      enum:
        - ARBEITLEISTUNGTAGESPARAMETERABHMALO
        - VERANSCHLAGTEJAHRESMENGE
        - TUMKUNDENWERT
      description: Verbrauchsmengetyp
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
    Messwertstatus:
      type: string
      title: Messwertstatus
      description: Der Status eines Zählerstandes
      enum:
        - ABGELESEN
        - ERSATZWERT
        - VORSCHLAGSWERT
        - NICHT_VERWENDBAR
        - PROGNOSEWERT
        - ENERGIEMENGESUMMIERT
        - VOLAEUFIGERWERT
        - FEHLT
        - ANGABE_FUER_LIEFERSCHEIN
        - GRUNDLAGE_POG_ERMITTLUNG
      x-apidog-enum:
        - value: ABGELESEN
          name: Wahrer Wert
          description: '220'
        - value: ERSATZWERT
          name: Ersatzwert
          description: '67'
        - value: VORSCHLAGSWERT
          name: Vorschlagswert
          description: '201'
        - value: NICHT_VERWENDBAR
          name: Nicht verwendbarer Wert
          description: '20'
        - value: PROGNOSEWERT
          name: Prognosewert
          description: '187'
        - value: ENERGIEMENGESUMMIERT
          name: Energiemenge summiert (Summenwert, Bilanzsumme)
          description: '79'
        - value: VOLAEUFIGERWERT
          name: Vorläufiger Wert
          description: Z18
        - value: FEHLT
          name: Fehlender Wert
          description: Z30
        - value: ANGABE_FUER_LIEFERSCHEIN
          name: Angabe für Lieferschein
          description: Z31
        - value: GRUNDLAGE_POG_ERMITTLUNG
          name: Grundlage POG-Ermittlung
          description: Z47
      x-apidog-folder: ''
    Wertermittlungsverfahren:
      title: Wertermittlungsverfahren
      type: string
      enum:
        - PROGNOSE
        - MESSUNG
      description: Wertermittlungsverfahren
      x-apidog-folder: ''
    Lokationstyp:
      type: string
      title: Lokationstyp
      description: Gibt an, ob es sich um eine Markt- oder Messlokation handelt
      enum:
        - MALO
        - MELO
        - NELO
        - TECHNISCHE_RESSOURCE
      x-apidog-enum:
        - value: MALO
          name: Marktlokation
          description: Z18
        - value: MELO
          name: Messlokation
          description: Z19
        - value: NELO
          name: Netzlokation
          description: Z32
        - value: TECHNISCHE_RESSOURCE
          name: Technische Ressource
          description: Z37
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
