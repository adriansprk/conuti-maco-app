# Avis lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getAvisBasic:
    get:
      summary: Avis lesen
      deprecated: false
      description: |
        Lesen des Avises mittels Avisnummer (Parameter1) 
      operationId: LESEN_AVIS_BASIS
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: avisNummer | avis Number
          required: true
          example: '{{avisNummer}}'
          schema:
            type: string
            examples:
              - '123456'
        - name: command
          in: query
          description: >-
            Entspricht der operationId dieser Schnittstelle. Diese Operation Id
            entspricht dem Command im Camunda Konnektor Prozess. Wenn das
            Backend einen generischen Endpunkt bereitstellt, kann dieses Command
            gentutzt werden um zu definieren welche Operation ausgeführt werden
            soll.
          required: false
          example: SAP_LESEN_AVIS_BASIS
          schema:
            type: string
      responses:
        '200':
          description: 'Erfolgreiches Lesen des Avises '
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Avis'
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
        '422':
          description: Nicht verarbeitbare Anfrage | Unprocessable Request
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
      x-apidog-folder: Schnittstellen/BO4E Lesen (Backend)
      x-apidog-status: developing
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017011-run
components:
  schemas:
    Avis:
      title: Avis
      type: object
      properties:
        boTyp:
          $ref: '#/components/schemas/BOTyp'
          default: AVIS
          examples:
            - AVIS
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
          x-apidog-mock: '1'
        avisNummer:
          type: string
          description: Zahlungsavisnummer vergeben vom Absender des Dokuments.
          x-apidog-mock: '{{$string.numeric}}'
        avisTyp:
          $ref: '#/components/schemas/AvisTyp'
          description: |-
            Gibt den Typ des Avis an, Typ und Funktion einer Nachricht
            BGM 481
            PI 33002 33003 33004 33001
        zuZahlen: &ref_0
          $ref: '#/components/schemas/Betrag'
          description: Summenbetrag
        positionen:
          type: array
          items:
            $ref: '#/components/schemas/Avisposition'
          description: >-
            Avispositionen - Angaben zu den Dokumenten

            380 Handelsrechnung

            389 Selbst ausgestellte Rechnung (engl.: "Selfbilled invoice")

            457 Storno einer Belastung

            Z25 Storno für selbst ausgestellte Rechnung (Gutschrift im
            Gutschriftsverfahren)

            DOC 380

            PI 33001 33002 33003 33004
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - avisNummer
        - avisTyp
        - zuZahlen
        - positionen
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Avisposition:
      title: Avisposition
      type: object
      properties:
        rechnungsNummer:
          type: string
          description: 'Dokumentennummer '
        rechnungsDatum:
          type: string
          format: date-time
          description: |-
            Rechnungsdatum
            DTM 137
            PI 33001 33002 33003 33004
        istStorno:
          type: boolean
          description: >-
            Storno

            457 Storno einer Belastung.

            Z25 Storno für selbst ausgestellte Rechnung (Gutschrift im
            Gutschriftsverfahren)
        istSelbstausgestellt:
          type: boolean
          description: |-
            Selbst ausgestellte Rechnung
            389 Selbst ausgestellte Rechnung (engl.: "Selfbilled invoice")
        gesamtBrutto: *ref_0
        zuZahlen: *ref_0
        referenz:
          type: string
          description: |-
            Referenznummer auf COMDIS
            RFF ACW
            PI 33002 33003 33004
        abweichung:
          type: array
          items: &ref_1
            $ref: '#/components/schemas/Abweichung'
          description: |-
            Abweichungsgrund, alle erkannten Ablehnungsgründe
            ATJ 
            PI 33002 33003
        positionen:
          type: array
          items:
            $ref: '#/components/schemas/Rueckmeldungsposition'
          description: |-
            Identifikation der Zeile - Position im Dokument
            DLI 1
            PI 33004
      x-apidog-orders:
        - rechnungsNummer
        - rechnungsDatum
        - istStorno
        - istSelbstausgestellt
        - gesamtBrutto
        - zuZahlen
        - referenz
        - abweichung
        - positionen
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Rueckmeldungsposition:
      title: Rueckmeldungsposition
      type: object
      properties:
        positionsnummer:
          type: integer
          description: Positionsnummer
        abweichung:
          type: array
          items: *ref_1
          description: Abweichung
      x-apidog-orders:
        - positionsnummer
        - abweichung
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Abweichung:
      title: Abweichung
      type: object
      properties:
        abweichungsgrund:
          $ref: '#/components/schemas/Abweichungsgrund'
          description: nicht in Benutzung
        abweichungsgrundBemerkung:
          type: string
          description: Bemerkung zum Abweichungsgrund
        zugehoerigeRechnung:
          type: string
          description: |-
            Angabe der Rechnungsnummer - Zugehörige Rechnung
            RFF AFL
            PI 31010 33003 
        zugehoerigeBestellung:
          type: string
          description: Angabe der Bestellungsnummer, auf die sich diese Abweichung bezieht
        abweichungsgrundCode:
          type: string
          description: Code des Abweichungsgrundes, Codes aus den EBDs
        abweichungsgrundCodeliste:
          type: string
          description: Codeliste oder EBD
        fehlendePositionen1:
          type: string
          description: |-
            fehlende Positionsnummer eines Angebotes 1
            FTX Z16
            PI 33003
        fehlendePositionen2:
          type: string
          description: fehlende Positionsnummer eines Angebotes 2
        fehlendePositionen3:
          type: string
          description: fehlende Positionsnummer eines Angebotes 3
        fehlendePositionen4:
          type: string
          description: fehlende Positionsnummer eines Angebotes 4
        fehlendePositionen5:
          type: string
          description: fehlende Positionsnummer eines Angebotes 5
        abweichungsgrundBemerkung1:
          type: string
          description: |-
            Information über Abweichung 1
            FTX ABO 
            PI 33002 33003 
        abweichungsgrundBemerkung2:
          type: string
          description: Information über Abweichung 2
        abweichungsgrundBemerkung3:
          type: string
          description: Information über Abweichung 3
        abweichungsgrundBemerkung4:
          type: string
          description: Information über Abweichung 4
        abweichungsgrundBemerkung5:
          type: string
          description: Information über Abweichung 5
        referenz:
          type: string
          description: |-
            Referenznummer einer vorangegangenen Nachricht
            RFF ACW
            PI 33004
        abschlagsrechnungen:
          type: array
          items:
            type: string
          description: |-
            Enthaltene Abschlagsrechnungen - Rechnungsnummer
            FTX Z14
            PI 33003
      x-apidog-orders:
        - abweichungsgrund
        - abweichungsgrundBemerkung
        - zugehoerigeRechnung
        - zugehoerigeBestellung
        - abweichungsgrundCode
        - abweichungsgrundCodeliste
        - fehlendePositionen1
        - fehlendePositionen2
        - fehlendePositionen3
        - fehlendePositionen4
        - fehlendePositionen5
        - abweichungsgrundBemerkung1
        - abweichungsgrundBemerkung2
        - abweichungsgrundBemerkung3
        - abweichungsgrundBemerkung4
        - abweichungsgrundBemerkung5
        - referenz
        - abschlagsrechnungen
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Abweichungsgrund:
      title: Abweichungsgrund
      type: string
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
        - ZEITINTERVALL_DER_BILANZIERTEN_MENGE_INKONSISTENT
        - >-
          RECHNUNGSEMPFAENGER_WIDERSPRICHT_DER_STEUERRECHTLICHEN_EINSCHAETZUNG_DES_RECHNUNGSSTELLERS
        - ANGEGEBENE_QUOTES_AN_MARKTLOKATION_NICHT_VORHANDEN
        - RECHNUNGSABWICKLUNG_NICHT_VEREINBART
        - COMDIS_WIRD_ABGELEHNT
      description: Abweichungsgrund
      x-apidog-folder: ''
    Betrag:
      title: Betrag
      type: object
      properties:
        wert:
          type: number
          format: float
          description: |-
            Geforderter Rechnungsbetrag
            MOA 9
            PI 29001
            REMADV 
            PI 33001 33002 33003 33004
            MOA 12
            PI 33001 33002 33003 33004
            INVOIC MOA 203/77/113/9
          x-apidog-mock: '{{$string.numeric}}'
        waehrung:
          type: string
          description: |-
            Währungsangaben der Rechnung, Referenzwährung Euro, Geldbetrag
            EUR Euro
            CUX 2 EUR 
            PI 29001
            REMADV
            PI 33001 33002 33003 33004
            QUOTES
            PI 15001 15002 15003
          x-apidog-mock: EUR
      x-apidog-orders:
        - wert
        - waehrung
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    AvisTyp:
      type: string
      title: AvisTyp
      description: AvisTyp
      enum:
        - ABGELEHNTE_FORDERUNG
        - ZAHLUNGSAVIS
      x-apidog-enum:
        - value: ABGELEHNTE_FORDERUNG
          name: Abgelehnte Forderung (Nicht-Zahlungsavis)
          description: '239'
        - value: ZAHLUNGSAVIS
          name: Zahlungsavis
          description: '481'
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
