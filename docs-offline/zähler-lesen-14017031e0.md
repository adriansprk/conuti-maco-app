# Zähler lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getCounterBasic:
    get:
      summary: Zähler lesen
      deprecated: false
      description: >-
        Lesen einer Zaehlers mittels LokationsId (Parameter1) und lokationsTyp
        (Parameter2 - default MELO) zum Zeitpunkt (Parameter3) | Reading a
        tranche using location ID (Parameter1) at the time (Parameter2)
      operationId: LESEN_ZAEHLER_BASIS
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: LokationsId | Location ID
          required: true
          schema:
            type: string
            default: '74018657187'
            examples:
              - '74018657187'
        - name: parameter2
          in: query
          description: LokationsTyp | Location type
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
          description: Datum (Gültig ab) | Date (Valid from)
          required: true
          schema:
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            type: string
            examples:
              - '2024-06-28T12:18:00Z'
        - name: parameter4
          in: query
          description: Datum (Gültig bis) | Date (Valid until)
          required: true
          schema:
            format: date-time
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
            type: string
            examples:
              - '2024-06-28T12:18:00Z'
      responses:
        '200':
          description: Erfolgreiches Lesen des Zaehlers | Successful reading of the meter
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Zaehler'
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
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017031-run
components:
  schemas:
    Zaehler:
      title: Zaehler
      type: object
      properties:
        boTyp: &ref_5
          $ref: '#/components/schemas/BOTyp'
          default: ZAEHLER
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        zaehlernummer:
          type: string
          description: >-
            Nummer des Gerätes 

            CAV Z30

            PI 55600 55601 55643 55648 55653 55658 55663 55669 55553 55555 55035
            55095 55060 55194 55039 55040 55042 55043 55168 55169 55074 55075
            55076 

            RFF MG Gerätenummer des Zählers

            PI 55643 55648 55653 55658 55663 55669 55060 55043 55168 55169 55074
            55075 55076

            QUOTES RFF Z09 Gerätenummer 

            PI 15001

            MSCONS RFF MG 

            PI 13017 13002
        sparte:
          $ref: '#/components/schemas/Sparte'
          description: Strom oder Gas
        zaehlerauspraegung:
          $ref: '#/components/schemas/Zaehlerauspraegung'
          description: >-
            Energierichtung

            CAV ERZ

            PI 55643 55648 55653 55658 55663 55669 55043 55168 55169 55074 55075
            55076

            QUOTES PI 15001
        zaehlertyp:
          $ref: '#/components/schemas/Zaehlertyp'
          description: >-
            Wertspezifizierung des Zählers - Zähleinrichtung

            CAV AHZ

            PI 55643 55648 55653 55658 55663 55669 55035 55095 55060 55043 55168
            55169 55074 55075 55076

            QUOTES

            PI 15001

            UTILMD Gas 
        tarifart:
          $ref: '#/components/schemas/Tarifart'
          description: >-
            Tarifanzahl, Registeranzahl - Es wird die Information des
            tatsächlich verbauten Gerätes angegeben.

            CAV ETZ

            PI 55643 55648 55653 55658 55663 55669 55043 55168 55169 55074 55075
            55076

            QUOTES PI 15001
        zaehlerkonstante:
          type: number
          format: float
          description: Zählerkonstante auf dem Zähler.
        eichungBis:
          type: string
          format: date-time
          description: |-
            Eichgültigkeit - Bis zu diesem Datum ist der Zähler geeicht.
            DTM Z04
            PI 15001
        zaehlerhersteller:
          $ref: '#/components/schemas/Geschaeftspartner'
          description: Der Hersteller des Zählers. Details Geschaeftspartner
        gateway:
          type: string
          description: >-
            Zuordnung der Zähleinrichtung zu dem Smartmeter-Gateway worüber die
            Kommunikation erfolgt.

            RFF Z14

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55035 55095 55060
            55043 55168 55169 55074 55075 55076
        fernschaltung:
          $ref: '#/components/schemas/Fernschaltung'
          description: >-
            Fernschaltung der Zähleinrichtung, liefert die Information, ob die
            Funktion zur Fernschaltung vorhanden ist. Die

            Fernschaltung gibt die Möglichkeit den Energiefluss durch die
            Zähleinrichtung zu unterbrechen bzw. die Unterbrechung

            aufzuheben.

            CAV Z58

            PI 55643 55648 55653 55658 55663 55669 55043 55168 55169 55074 55075
            55076
        messwerterfassung:
          $ref: '#/components/schemas/Messwerterfassung'
          description: |-
            Technische Möglichkeit - Messwerterfassung an der Zähleinrichtung
            CAV AMR 
            PI 55643 55648 55663 55669 55035 55095 55060 55043 55168 55169
            QUOTES PI 15001
        zaehlertypspezifikation:
          $ref: '#/components/schemas/ZaehlertypSpezifikation'
          description: >-
            Zählertyp

            PI 55643 55648 55653 55658 55663 55669 55035 55095 55060 55043 55168
            55169 

            QUOTES PI 15001
        befestigungsart:
          $ref: '#/components/schemas/Befestigungsart'
          description: |-
            Befestigungsart Zähleinrichtung
            CAV BKE
            PI 55643 55648 55663 55669 55043 55168 55169
            QUOTES PI 15001
        zaehlergroesse: &ref_0
          $ref: '#/components/schemas/Geraetemerkmal'
          description: |-
            Zähleinrichtung/Zählergröße (Gas)
            PI 15001
        mengenumwertertyp:
          $ref: '#/components/schemas/Mengenumwertertyp'
          description: nicht in Benutzung
        volumenerfassung: &ref_3
          $ref: '#/components/schemas/Volumenerfassung'
          description: |-
            Art der Volumenerfassung 
            CAV ZC0
            PI 44116 44148 44149 44043 44168 44169 44060 
        serialnummer:
          type: string
          description: |-
            Herstellernummer - Serialnummer
            GIN BN
            PI 15001
        geraetemerkmal: *ref_0
        herstellungsdatum:
          type: string
          format: date-time
          description: |-
            Produktions-/Herstellungsdatum
            DTM 94
            PI 15001
        baujahr:
          type: string
          description: |-
            Baujahr/Jahr des in Verkehrs bringens
            DTM Z03
            PI 15001
        messlokationsId:
          type: string
          description: >-
            Referenzierung auf eine ID einer Messlokation, der die
            Zähleinrichtung zugeordnet ist.

            RFF Z19

            PI 55035 55095 55060 55040 55043 55168 55169 55074 55075 55076 
        marktlokationsId:
          type: string
          description: |-
            Referenz auf die ID einer Marktlokation pro Zähler einer Melo.
            RFF Z18
            PI 55043 55168 55169 55074 55075 55076
        geraete:
          type: array
          items:
            $ref: '#/components/schemas/Geraet'
          description: Liste der Geräte, die zu diesem Zähler gehören.
        zaehlwerke:
          type: array
          items:
            $ref: '#/components/schemas/Zaehlwerk'
          description: Die Zählwerke des Zählers.
        datenqualitaet:
          $ref: '#/components/schemas/Datenqualitaet'
          description: |-
            Leitet Segmentengruppe ein
            SEQ Z03 Zähleinrichtungsdaten
            SEQ ZA3 Erwartete Zähleinrichtungsdaten
            SEQ ZA4 Im System vorhandene Zähleinrichtungsdaten
            SEQ ZF5 Informative Zähleinrichtungsdaten
            SEQ Z20 OBIS-Daten der Zähleinrichtung
            SEQ ZA5 Erwartete OBIS-Daten der Zähleinrichtung
            SEQ ZA6 Im System vorhandene OBIS-Daten der Zähleinrichtung
            SEQ ZF6 Informative OBIS-Daten der Zähleinrichtung
            SEQ Z04 Wandlerdaten
            SEQ ZB9 Erwartete Wandlerdaten
            SEQ ZC0 Im System vorhandene Wandlerdaten
            SEQ ZF7 Informative Wandlerdaten
            SEQ Z05 Kommunikationseinrichtungsdaten
            SEQ ZB7 Erwartete Kommunikationseinrichtungsdaten
            SEQ ZB8 Im System vorhandene Kommunikationseinrichtungsdaten
            SEQ ZF8 Informative Kommunikationseinrichtungsdaten
            SEQ Z06 Daten der technischen Steuereinrichtung
            SEQ ZC1 Erwartete Daten der technischen Steuereinrichtung
            SEQ ZC2 Im System vorhandene Daten der technischen Steuereinrichtung
            SEQ ZF9 Informative Daten der technischen Steuereinrichtung
            SEQ Z13 Smartmeter-Gateway
            SEQ ZC3 Erwartetes Smartmeter-Gateway
            SEQ ZC4 Im System vorhandenes Smartmeter-Gateway
            SEQ ZG0 Informative Smartmeter-Gateway
            SEQ Z14 Steuerbox
            SEQ ZH3 Erwartete Daten der Steuerbox
            SEQ ZH4 Im System vorhandene Daten der Steuerbox
        gueltigkeitszeitraum:
          $ref: '#/components/schemas/Zeitraum'
          description: Referenz auf Zeitraum-ID
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - zaehlernummer
        - sparte
        - zaehlerauspraegung
        - zaehlertyp
        - tarifart
        - zaehlerkonstante
        - eichungBis
        - zaehlerhersteller
        - gateway
        - fernschaltung
        - messwerterfassung
        - zaehlertypspezifikation
        - befestigungsart
        - zaehlergroesse
        - mengenumwertertyp
        - volumenerfassung
        - serialnummer
        - geraetemerkmal
        - herstellungsdatum
        - baujahr
        - messlokationsId
        - marktlokationsId
        - geraete
        - zaehlwerke
        - datenqualitaet
        - gueltigkeitszeitraum
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Zaehler.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zeitraum:
      title: Zeitraum
      type: object
      properties:
        zeiteinheit: &ref_1
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
        einheit: *ref_1
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
    Zaehlwerk:
      title: Zaehlwerk
      type: object
      properties:
        zaehlwerkId:
          type: string
          description: >-
            Identifikation des Zählwerks (Registers) innerhalb des Zählers.
            Oftmals eine laufende Nummer hinter der

            Zählernummer. Z.B. 47110815_1
        bezeichnung:
          type: string
          description: >-
            Bezeichnung des Zählwerks auf dem Gerät, dient zur Identifizierung
            und Beschreibung der lokalen Kennzeichnung auf dem Gerät (z. B. HT
            oder NT)

            CCI Z63

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55168 55169
        richtung:
          $ref: '#/components/schemas/Energierichtung'
          description: >-
            Die Energierichtung, Einspeisung oder Ausspeisung. Details
            Energierichtung
        obisKennzahl:
          type: string
          description: >-
            Produktidentifikation bei Austausch von Daten der Energiemengen
            werden gewährleistet durch OBIS Kennzahlen.

            PIA 5 OBIS-Kennzahl der Netzlokation

            PI 55639 55644 55649 55654 55659 55664 55060 55043 55168 55169

            PIA 5 OBIS-Kennzahl der Marktlokation

            PI 55684 55685 55640 55645 55650 55655 55660 55665 55553 55555 55035
            55095 55060 55043 55168 55169 55239 55074 55075 55076 55195 55196 

            RFF Z10 Referenz auf die OBIS-Kennzahl der Marktlokation

            PI 55616 55622 

            PIA 5 OBIS-Daten der Marktlokation der beteiligten Marktrolle

            PI 55196

            PIA 5 OBIS-Kennzahl der Tranche

            PI 55686 55687 55642 55647 55652 55657 55662 55667 55095 55074 55075
            55076 55195 55196

            PIA 5 OBIS-Kennzahl der Zähleinrichtung /Smartmeter-Gateway

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55035 55095 55060
            55043 55168 55169 55074 55075 55076
        wandlerfaktor:
          type: number
          format: float
          description: >-
            Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um
            zum eigentlichen Verbrauch im Zeitraum zu

            kommen.
        einheit:
          $ref: '#/components/schemas/Mengeneinheit'
          description: Die Einheit der gemessenen Größe, z.B. kWh. Details Mengeneinheit
        schwachlastfaehig: &ref_2
          $ref: '#/components/schemas/Schwachlastfaehig'
          description: >-
            Schwachlastfähigkeit, die Beschreibung der Schwachlastfähigkeit wird
            für die Konzessionsabgabe genutzt. 

            CCI Z10

            PI 55643 55648 55653 55658 55663 55669
        verbrauchsart:
          type: array
          items:
            $ref: '#/components/schemas/Verbrauchsart'
          description: >-
            Angabe für welchen Verwendungszweck die Stromentnahme an der
            OBIS-Kennzahl der Marktlokation erfolgt. Definiert den
            Verwendungszweck des Stroms: 

            CAV Z64

            PI 55616 55622 55035 
        unterbrechbarkeit:
          $ref: '#/components/schemas/Unterbrechbarkeit'
          description: >-
            Unterbrechbarkeit Marktlokation, Angabe, ob eine Unterbrechung der
            Verbrauchseinrichtung durch den Netzbetreiber möglich ist.

            CAV Z62

            PI 55616 55622 55035
        waermenutzung:
          $ref: '#/components/schemas/Waermenutzung'
          description: >-
            Wärmenutzung Marktlokation, im Falle der Wärmenutzung wird eine
            genauere Angabe über die Wärmenutzung definiert.

            CAV Z56

            PI 55616 55622 55617 55623 55629 55635 55035 55060 55043 55168 55169
        konzessionsabgabe:
          $ref: '#/components/schemas/Konzessionsabgabe'
          description: |-
            Konzessionsabgabedaten
            CCI Z08
            PI 44112 44139 44142 44001 44002 44013 44014 44035
        steuerbefreit:
          type: boolean
          description: Steuerbefreit
        vorkommastelle:
          type: integer
          description: >-
            Angabe der Vorkommastelle des Zählwerks

            CAV Wert

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55043 55168 55169
            55074 55075 55076
        nachkommastelle:
          type: integer
          description: >-
            Angabe der Nachkommastelle des Zählwerks

            CAV Wert

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55043 55168 55169
            55074 55075 55076
        abrechnungsrelevant:
          type: boolean
          description: Abrechnungsrelevant
        anzahlAblesungen:
          type: integer
          description: Anzahl Ablesungen
        zaehlzeiten:
          $ref: '#/components/schemas/Zaehlzeitregister'
          description: Zugeordnete Zählzeitdefinition
        konfiguration:
          type: string
          description: >-
            Angabe der Konfigurations-ID

            RFF AGK

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55035 55095 55060
            55043 55168 55169 55074 55075 55076
        messprodukt:
          type: string
          description: |-
            Erforderliches Messprodukt Z11 der Malo/ Tranche/ Melo
            PIA 5
            PI 55043 55168 55169 
            Messprodukt der Tranche
            PI 55060 55043 55168 55169 
            Messprodukt der Messlokation
            PI 55060 55043 55168 55169
            Erforderliches Produkt der Marktlokation ORDERS 
            PI 17123 17121 17134
            Erforderliches Produkt der Tranche ORDERS 
            PI 17121 17134 
            Erforderliches Produkt der Messlokation ORDERS 
            PI 17121 17118 17003 17134 17135
            Erforderliches Produkt der Netzlokation ORDERS
            PI 17121 17003
        wertegranularitaet:
          $ref: '#/components/schemas/Wertegranularitaet'
          description: >-
            Mit der Wertegranularität wird angegeben in welchem Intervall Werte
            der im PIA+5 genannten OBIS-Kennzahl im Markt

            bereitgestellt werden. ZD9 Jährlich ZE8 Halbjährlich ZE9
            Quartalsweise ZB7 Monatlich

            CCI ZE4

            PI 55640 55645 55650 55655 55660 55665 55643 55648 55653 55658 55663
            55669 55553 55555 55035 55095 55060 55043 55168 55169 55074 55075
            55076
        notwendigkeitZweiteMessung:
          $ref: '#/components/schemas/NotwendigkeitZweiteMessung'
          description: >-
            Weitere Beschreibung erforderliches Messprodukt, Notwendigkeit einer
            zweiten Messung vorhanden oder nicht vorhanden. Der Wert dient dem
            MSB zur Ermittlung, Plausibilisierung oder auch Ersatzwertbildung an
            der Melo. 

            CAV ZC9

            PI 55060 55043 55168 55169

            ORDERS PI 17121 17118
        werteuebermittlungVerwendungszweck:
          $ref: '#/components/schemas/WerteuebermittlungVerwendungszweck'
          description: >-
            Werteübermitlung an den NB aufgrund weiterem Verwendungszweck
            vorhanden oder nicht vorhanden. Das wird benötigt, da noch nicht
            alle Berechnungsformeln für Abrechnungszwecke ausgetauscht werden
            können.  

            CCI Z88

            PI 55060 55043 55168 55169

            ORDERS PI 17121 17118
        artEMobilitaet:
          $ref: '#/components/schemas/ArtEmobilitaet'
          description: >-
            Art der E-Mobilität, im Falle der E-Mobilität wird eine genauere
            Angabe über die Art definitiert. 

            CAV Z87

            PI 55616 55622 55617 55623 55629 55635 55035 55060 55043 55168 55169
        konfigurationsprodukt:
          type: string
          description: Konfigurationsprodukt
        keinKonfigurationsprodukt:
          type: boolean
          description: Kein Konfigurationsprodukt
        leistungskurvendefinition:
          type: string
          description: Leistungskurvendefinition
        verwendungszwecke:
          type: array
          items:
            $ref: '#/components/schemas/Verwendungszweck'
          description: Verwendungungszweck der Werte Marktlokation, Tranche
      x-apidog-orders:
        - zaehlwerkId
        - bezeichnung
        - richtung
        - obisKennzahl
        - wandlerfaktor
        - einheit
        - schwachlastfaehig
        - verbrauchsart
        - unterbrechbarkeit
        - waermenutzung
        - konzessionsabgabe
        - steuerbefreit
        - vorkommastelle
        - nachkommastelle
        - abrechnungsrelevant
        - anzahlAblesungen
        - zaehlzeiten
        - konfiguration
        - messprodukt
        - wertegranularitaet
        - notwendigkeitZweiteMessung
        - werteuebermittlungVerwendungszweck
        - artEMobilitaet
        - konfigurationsprodukt
        - keinKonfigurationsprodukt
        - leistungskurvendefinition
        - verwendungszwecke
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Verwendungszweck:
      title: Verwendungszweck
      type: object
      properties:
        marktrolle:
          $ref: '#/components/schemas/Marktrolle'
          description: >-
            Identifizierung der Marktrolle

            CCI ZA8

            PI 55639 55644 55659 55664 55043 55168 55169 55649 55654 55684 55685
            55686 55687 55660 55665 55662 55667 

            ORDERS PI 17121 17134
        zweck:
          type: array
          items:
            $ref: '#/components/schemas/VerwendungszweckValue'
          description: >-
            Verwendungszweck der Werte

            CAV Z47

            PI 55639 55644 55659 55664 55043 55168 55169 55649 55654 55640 55645
            55660 55665 55650 55655 

            PI 55684 55685 55686 55687 55662 55667 

            ORDERS

            PI 17121 17134
      x-apidog-orders:
        - marktrolle
        - zweck
      description: .
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    VerwendungszweckValue:
      type: string
      title: VerwendungszweckValue
      description: VerwendungszweckValue
      enum:
        - NETZNUTZUNGSABRECHNUNG
        - BILANZKREISABRECHNUNG
        - MEHRMINDERMENGENABRECHNUNG
        - ENDKUNDENABRECHNUNG
        - UEBERMITTLUNG_AN_DAS_HKNR
        - BLINDARBEITSABRECHNUNG
        - ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS
        - BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG
        - ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR
      x-apidog-enum:
        - value: NETZNUTZUNGSABRECHNUNG
          name: Netznutzungsabrechnung
          description: Z84
        - value: BILANZKREISABRECHNUNG
          name: Bilanzkreisabrechnung
          description: Z85
        - value: MEHRMINDERMENGENABRECHNUNG
          name: Mehrmindermengenabrechnung
          description: Z86
        - value: ENDKUNDENABRECHNUNG
          name: Endkundenabrechnung
          description: Z47
        - value: UEBERMITTLUNG_AN_DAS_HKNR
          name: Übermitlung an das HKNR
          description: Z92
        - value: BLINDARBEITSABRECHNUNG
          name: ''
          description: ''
        - value: ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS
          name: Zur Ermitlung der Ausgeglichenheit von Bilanzkreisen
          description: ZB5
        - value: BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG
          name: Blindarbeitabrechnung / Betriebsführung
          description: ZD1
        - value: ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR
          name: Es liegt kein Verwendungszweck vor
          description: ZE1
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
    ArtEmobilitaet:
      type: string
      title: ArtEmobilitaet
      description: ArtEmobilitaet
      enum:
        - WB
        - LS
        - LP
      x-apidog-enum:
        - value: WB
          name: Wallbox
          description: ZE6
        - value: LS
          name: E-Mobilitätsladesäule
          description: Z87
        - value: LP
          name: Ladepark
          description: ZE7
      x-apidog-folder: ''
    WerteuebermittlungVerwendungszweck:
      type: string
      title: WerteuebermittlungVerwendungszweck
      description: Werteübermitlung an den NB aufgrund weiterem Verwendungszweck
      enum:
        - VORHANDEN
        - NICHT_VORHANDEN
      x-apidog-enum:
        - value: VORHANDEN
          name: vorhanden
          description: Z06
        - value: NICHT_VORHANDEN
          name: nicht vorhanden
          description: Z07
      x-apidog-folder: ''
    NotwendigkeitZweiteMessung:
      type: string
      title: NotwendigkeitZweiteMessung
      description: NotwendigkeitZweiteMessung
      enum:
        - VORHANDEN
        - NICHT_VORHANDEN
      x-apidog-enum:
        - value: VORHANDEN
          name: vorhanden
          description: Z06
        - value: NICHT_VORHANDEN
          name: nicht vorhanden
          description: Z07
      x-apidog-folder: ''
    Wertegranularitaet:
      type: string
      title: Wertegranularitaet
      description: Wertegranularitaet
      enum:
        - JAEHRLICH
        - HALBJAEHRLICH
        - QUARTALSWEISE
        - MONATLICH
      x-apidog-enum:
        - value: JAEHRLICH
          name: Jährlich
          description: ZD9
        - value: HALBJAEHRLICH
          name: Halbjährlich
          description: ZE8
        - value: QUARTALSWEISE
          name: Quartalsweise
          description: ZE9
        - value: MONATLICH
          name: Monatlich
          description: ZB7
      x-apidog-folder: ''
    Zaehlzeitregister:
      title: Zaehlzeitregister
      type: object
      properties:
        register:
          type: string
          description: >-
            Code des Zählzeitregisters

            CCI Z38 

            PI 55218 55220 55640 55645 55650 55655 55660 55665 55643 55648 55653
            55658 55663 55669 55553 55555 55035 55060 55043 55168 55169 

            UTILTS CCI Z38

            PI 25004
        zaehlzeitDefinition:
          type: string
          description: >-
            Code der Zählzeitdefinition

            CCI Z39

            PI 55218 55220 55035 55640 55645 55650 55655 55660 55665 55643 55648
            55653 55658 55663 55669 55553 55555 55060 55043 55168 55169

            CCI Z41 Keine Zählzeit für Messprodukt erforderlich

            PI 55060 55043 55168 55169

            Z39 Code der Zählzeitdefinition ORDERS

            Z41 Keine Zählzeit für Messprodukt erforderlich ORDERS

            CCI Z39

            PI 17123 17121 17118 17134 17135

            UTILTS RFF Z27

            PI 25004
        schwachlastfaehig: *ref_2
      x-apidog-orders:
        - register
        - zaehlzeitDefinition
        - schwachlastfaehig
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Konzessionsabgabe:
      title: Konzessionsabgabe
      type: object
      properties:
        satz:
          $ref: '#/components/schemas/AbgabeArt'
          description: |-
            Gruppen der KAV
            CAV KAS
        kosten:
          type: number
          format: float
          description: Konzessionsabgabe in Euro/kWh
        kategorie:
          type: string
          description: >-
            Gebührenkategorie der Konzessionsabgabe - Übermittlung von
            zusätzlichen Informationen
      x-apidog-orders:
        - satz
        - kosten
        - kategorie
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    AbgabeArt:
      type: string
      title: AbgabeArt
      description: Art der Konzessionsabgabe
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
      x-apidog-enum:
        - value: KAS
          name: >-
            für alle konzessionsvertraglichen Sonderregelungen, die nicht in die
            Systematik der KAV eingegliedert sind
          description: KAS
        - value: SA
          name: >-
            Sondervertragskunden < 1 kV nach § 2 (7) und > 1 kV, Preis nach § 2
            (3) (für Strom 0,11 ct/ kWh und für Gas 0,03 ct/kWh)
          description: SA
        - value: SAS
          name: >-
            Kennzeichnung, dass ein abweichender Preis für Sondervertragskunden
            vorliegt
          description: SAS
        - value: TA
          name: >-
            Tarifkunden, für Strom § 2. (2) 1b HT bzw. ET (hohe KA) und für Gas
            § 2 (2) 2b
          description: TA
        - value: TAS
          name: Kennzeichnung, dass ein abweichender Preis für Tarifkunden vorliegt
          description: TAS
        - value: TK
          name: >-
            für Gas nach KAV § 2 (2) 2a bei ausschließlicher Nutzung zum Kochen
            und Warmwassererzeugung
          description: TK
        - value: TKS
          name: >-
            Kennzeichnung, wenn nach KAV § 2 (2) 2a ein anderer Preis zu
            verwenden ist
          description: TKS
        - value: TS
          name: ''
          description: ''
        - value: TSS
          name: ''
          description: ''
      x-apidog-folder: ''
    Waermenutzung:
      type: string
      title: Waermenutzung
      description: Waermenutzung
      enum:
        - SPEICHERHEIZUNG
        - WAERMEPUMPE
        - DIREKTHEIZUNG
        - WAERMEPUMPE_WAERME_KAELTE
        - WAERMEPUMPE_KAELTE
        - WAERMEPUMPE_WAERME
      x-apidog-enum:
        - value: SPEICHERHEIZUNG
          name: Speicherheizung
          description: Z56
        - value: WAERMEPUMPE
          name: Wärmepumpe (unspezifiziert)
          description: Z57
        - value: DIREKTHEIZUNG
          name: Direktheizung
          description: Z61
        - value: WAERMEPUMPE_WAERME_KAELTE
          name: Wärmepumpe (Wärme und Kälte)
          description: ZV5
        - value: WAERMEPUMPE_KAELTE
          name: Wärmepumpe (Kälte)
          description: ZV6
        - value: WAERMEPUMPE_WAERME
          name: Wärmepumpe (Wärme)
          description: ZV7
      x-apidog-folder: ''
    Unterbrechbarkeit:
      type: string
      title: Unterbrechbarkeit
      description: Unterbrechbarkeit
      enum:
        - UV
        - NUV
      x-apidog-enum:
        - value: UV
          name: unterbrechbare Verbrauchseinrichtung
          description: Z62
        - value: NUV
          name: nicht-unterbrechbare Verbrauchseinrichtung
          description: Z63
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
    Schwachlastfaehig:
      type: string
      title: Schwachlastfaehig
      description: Schwachlastfaehig
      enum:
        - SCHWACHLASTFAEHIG
        - NICHT_SCHWACHLASTFAEHIG
      x-apidog-enum:
        - value: SCHWACHLASTFAEHIG
          name: Schwachlast fähig
          description: Z60
        - value: NICHT_SCHWACHLASTFAEHIG
          name: Nicht-Schwachlast fähig
          description: Z59
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
    Energierichtung:
      type: string
      title: Energierichtung
      description: Spezifiziert die Energierichtung einer Markt- und/oder Messlokation
      enum:
        - AUSSP
        - EINSP
      x-apidog-enum:
        - value: AUSSP
          name: Verbrauch
          description: 'Z07 / Z71 '
        - value: EINSP
          name: Erzeugung
          description: 'Z06 / Z72 '
      x-apidog-folder: ''
    Geraet:
      title: Geraet
      type: object
      properties:
        geraetetyp: &ref_4
          $ref: '#/components/schemas/Geraetetyp'
        bezeichnung:
          type: string
          description: Bezeichnung des Gerätes
        geraetenummer:
          type: string
          description: >-
            Angabe der Referenz auf die Gerätenummer des Zählers /
            Smartmeter-Gateway / Wandler

            RFF Z14 Smartmeter-Gateway

            PI 55643 55648 55653 55658 55663 55669 55043 55168 55169 55074 55075
            55076 

            CAV Z30 Gerätenummer

            55643 55648 55653 55658 55663 55669 55060 55043 55168 55169 55074
            55075 55076 

            ORDERS RFF Z09  

            PI 17101 17126 17009 
        geraetereferenz:
          type: string
          description: Gäaetereferenz
        geraeteeigenschaften:
          $ref: '#/components/schemas/Geraeteeigenschaften'
          description: Festlegung der Eigenschaften des Gerätes. Z.B. Wandler MS/NS.
        volumenerfassung: *ref_3
        weitereGeraetenummern:
          type: array
          items:
            type: string
          description: weitere Gäaetenummern
      x-apidog-orders:
        - geraetetyp
        - bezeichnung
        - geraetenummer
        - geraetereferenz
        - geraeteeigenschaften
        - volumenerfassung
        - weitereGeraetenummern
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Geraeteeigenschaften:
      title: Geraeteeigenschaften
      type: object
      properties:
        geraetetyp: *ref_4
        geraetemerkmal: *ref_0
        faktor:
          type: number
          format: float
          description: >-
            Wandlerfaktor - Angabe der Wandlerkonstante

            PI 55643 55648 55653 55658 55663 55669 55060 55043 55168 55169 55074
            55075 55076 

            QUOTES PI 15001
      x-apidog-orders:
        - geraetetyp
        - geraetemerkmal
        - faktor
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Geraetetyp:
      type: string
      title: Geraetetyp
      description: Auflistung möglicher abzurechnender Gerätetypen
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
      x-apidog-enum:
        - value: WECHSELSTROMZAEHLER
          name: analoger Wechselstromzähler
          description: WSZ
        - value: DREHSTROMZAEHLER
          name: analoger Haushaltszähler (Drehstrom)
          description: AHZ
        - value: ZWEIRICHTUNGSZAEHLER
          name: ''
          description: ''
        - value: RLM_ZAEHLER
          name: Lastgangzähler
          description: LAZ
        - value: IMS_ZAEHLER
          name: ''
          description: ''
        - value: BALGENGASZAEHLER
          name: Balgengaszähler
          description: BGZ
        - value: MAXIMUMZAEHLER
          name: Maximumzähler
          description: MAZ
        - value: MULTIPLEXANLAGE
          name: ''
          description: ''
        - value: PAUSCHALANLAGE
          name: ''
          description: ''
        - value: VERSTAERKERANLAGE
          name: ''
          description: ''
        - value: SUMMATIONSGERAET
          name: ''
          description: ''
        - value: IMPULSGEBER
          name: ''
          description: ''
        - value: EDL_21_ZAEHLERAUFSATZ
          name: ''
          description: ''
        - value: VIER_QUADRANTEN_LASTGANGZAEHLER
          name: ''
          description: ''
        - value: MENGENUMWERTER
          name: Mengenumwerter
          description: Z64
        - value: STROMWANDLER
          name: ''
          description: ''
        - value: SPANNUNGSWANDLER
          name: ''
          description: ''
        - value: DATENLOGGER
          name: ''
          description: ''
        - value: KOMMUNIKATIONSANSCHLUSS
          name: ''
          description: ''
        - value: MODEM
          name: ''
          description: ''
        - value: TELEKOMMUNIKATIONSEINRICHTUNG
          name: ''
          description: ''
        - value: KOMMUNIKATIONSEINRICHTUNG
          name: Kommunikationseinrichtung
          description: Z26
        - value: DREHKOLBENGASZAEHLER
          name: Drehkolbengaszähler
          description: DKZ
        - value: TURBINENRADGASZAEHLER
          name: Turbinenradgaszähler
          description: TRZ
        - value: ULTRASCHALLZAEHLER
          name: Ultraschallgaszähler
          description: UGZ
        - value: WIRBELGASZAEHLER
          name: Wirbelgaszähler
          description: WGZ
        - value: MODERNE_MESSEINRICHTUNG
          name: moderne Messeinrichtung nach MsbG
          description: MME
        - value: ELEKTRONISCHER_HAUSHALTSZAEHLER
          name: elektronischer Haushaltszähler
          description: EHZ
        - value: STEUEREINRICHTUNG
          name: ''
          description: ''
        - value: TECHNISCHESTEUEREINRICHTUNG
          name: Technische Steuereinrichtung
          description: Z27
        - value: TARIFSCHALTGERAET
          name: ''
          description: ''
        - value: RUNDSTEUEREMPFAENGER
          name: ''
          description: ''
        - value: OPTIONALE_ZUS_ZAEHLEINRICHTUNG
          name: Zähleinrichtung
          description: ZD4
        - value: MESSWANDLERSATZ_IMS_MME
          name: ''
          description: ''
        - value: KOMBIMESSWANDLER_IMS_MME
          name: ''
          description: ''
        - value: TARIFSCHALTGERAET_IMS_MME
          name: ''
          description: ''
        - value: RUNDSTEUEREMPFAENGER_IMS_MME
          name: ''
          description: ''
        - value: TEMPERATUR_KOMPENSATION
          name: ''
          description: ''
        - value: HOECHSTBELASTUNGS_ANZEIGER
          name: ''
          description: ''
        - value: SONSTIGES_GERAET
          name: Individuelle Abstimmung (Sonderausstattung)
          description: IVA
        - value: SMARTMETERGATEWAY
          name: Smartmeter-Gateway
          description: Z75
        - value: STEUERBOX
          name: Steuerbox
          description: Z76
        - value: BLOCKSTROMWANDLER
          name: ''
          description: ''
        - value: KOMBIMESSWANDLER
          name: ''
          description: ''
        - value: MODEM_GSM
          name: ''
          description: ''
        - value: ETHERNET_KOM
          name: ''
          description: ''
        - value: PLC_COM
          name: ''
          description: ''
        - value: MODEM_FESTNETZ
          name: ''
          description: ''
        - value: DSL_KOM
          name: ''
          description: ''
        - value: LTE_KOM
          name: ''
          description: ''
        - value: DICHTEMENGENUMWERTER
          name: ''
          description: ''
        - value: TEMPERATURMENGENUMWERTER
          name: ''
          description: ''
        - value: ZUSTANDSMENGENUMWERTER
          name: ''
          description: ''
        - value: MESSDATENREGISTRIERGERAET
          name: Messdatenregistriergerät
          description: MRG
        - value: WANDLER
          name: Wandler
          description: Z25
      x-apidog-folder: ''
    Volumenerfassung:
      type: string
      title: Volumenerfassung
      description: Art der Volumenerfassung
      enum:
        - HOCHFREQUENZSONDE
        - KENNLINIENKORREKTUR
        - SCHLEICHMENGENUNTERDRUECKUNG
      x-apidog-enum:
        - value: HOCHFREQUENZSONDE
          name: Hochfrequenzsonde
          description: Z16
        - value: KENNLINIENKORREKTUR
          name: Kennlinienkorrektur
          description: Z17
        - value: SCHLEICHMENGENUNTERDRUECKUNG
          name: Schleichmengenunterdrückung
          description: Z18
      x-apidog-folder: ''
    Mengenumwertertyp:
      title: Mengenumwertertyp
      type: string
      enum:
        - DICHTEMENGENUMWERTER
        - TEMPERATURMENGENUMWERTER
        - ZUSTANDSMENGENUMWERTER
      description: Mengenumwertertyp
      x-apidog-folder: ''
    Geraetemerkmal:
      type: string
      title: Geraetemerkmal
      description: Geraetemerkmal
      enum:
        - EINTARIF
        - ZWEITARIF
        - MEHRTARIF
        - GAS_G2P5
        - GAS_G4
        - GAS_G6
        - GAS_G10
        - GAS_G16
        - GAS_G25
        - GAS_G40
        - GAS_G65
        - GAS_G100
        - GAS_G160
        - GAS_G250
        - GAS_G350
        - GAS_G400
        - GAS_G4000
        - GAS_G650
        - GAS_G6500
        - GAS_G1000
        - GAS_G10000
        - GAS_G12500
        - GAS_G1600
        - GAS_G16000
        - GAS_G2500
        - IMPULSGEBER_G4_G100
        - IMPULSGEBER_G100
        - MODEM_GSM
        - MODEM_GPRS
        - MODEM_FUNK
        - MODEM_GSM_O_LG
        - MODEM_GSM_M_LG
        - MODEM_FESTNETZ
        - MODEM_GPRS_M_LG
        - PLC_COM
        - ETHERNET_KOM
        - DSL_KOM
        - LTE_KOM
        - RUNDSTEUEREMPFAENGER
        - TARIFSCHALTGERAET
        - ZUSTANDS_MU
        - TEMPERATUR_MU
        - KOMPAKT_MU
        - SYSTEM_MU
        - UNBESTIMMT
        - WASSER_MWZW
        - WASSER_WZWW
        - WASSER_WZ01
        - WASSER_WZ02
        - WASSER_WZ03
        - WASSER_WZ04
        - WASSER_WZ05
        - WASSER_WZ06
        - WASSER_WZ07
        - WASSER_WZ08
        - WASSER_WZ09
        - WASSER_WZ10
        - WASSER_VWZ04
        - WASSER_VWZ05
        - WASSER_VWZ06
        - WASSER_VWZ07
        - WASSER_VWZ10
        - DICHTEMENGENUMWERTER
        - TEMPERATURMENGENUMWERTER
        - ZUSTANDSMENGENUMWERTER
        - BLOCKSTROMWANDLER
        - MESSWANDLERSATZ_IMS_MME
        - KOMBIMESSWANDLER
        - SPANNUNGSWANDLER
      x-apidog-enum:
        - value: EINTARIF
          name: ''
          description: ''
        - value: ZWEITARIF
          name: ''
          description: ''
        - value: MEHRTARIF
          name: ''
          description: ''
        - value: GAS_G2P5
          name: Gaszähler G2.5
          description: G2.5
        - value: GAS_G4
          name: Gaszähler G4
          description: G4
        - value: GAS_G6
          name: Gaszähler G6
          description: G6
        - value: GAS_G10
          name: Gaszähler G10
          description: G10
        - value: GAS_G16
          name: Gaszähler G16
          description: G16
        - value: GAS_G25
          name: Gaszähler G25
          description: G25
        - value: GAS_G40
          name: Gaszähler G40
          description: G40
        - value: GAS_G65
          name: Gaszähler G65
          description: G65
        - value: GAS_G100
          name: Gaszähler G100
          description: G100
        - value: GAS_G160
          name: Gaszähler G160
          description: G160
        - value: GAS_G250
          name: Gaszähler G250
          description: G250
        - value: GAS_G350
          name: Gaszähler G350
          description: G350
        - value: GAS_G400
          name: Gaszähler G400
          description: G400
        - value: GAS_G4000
          name: Gaszähler G4000
          description: G4000
        - value: GAS_G650
          name: Gaszähler G650
          description: G650
        - value: GAS_G6500
          name: Gaszähler G6500
          description: G6500
        - value: GAS_G1000
          name: Gaszähler G1000
          description: G1000
        - value: GAS_G10000
          name: Gaszähler G10000
          description: G10000
        - value: GAS_G12500
          name: Gaszähler G12500
          description: G12500
        - value: GAS_G1600
          name: Gaszähler G1600
          description: G1600
        - value: GAS_G16000
          name: Gaszähler G16000
          description: G16000
        - value: GAS_G2500
          name: Gaszähler G2500
          description: G2500
        - value: IMPULSGEBER_G4_G100
          name: ''
          description: ''
        - value: IMPULSGEBER_G100
          name: ''
          description: ''
        - value: MODEM_GSM
          name: GSM/GPRS/UMTS-Kom.-Einr.
          description: GSM
        - value: MODEM_GPRS
          name: ''
          description: ''
        - value: MODEM_FUNK
          name: ''
          description: ''
        - value: MODEM_GSM_O_LG
          name: ''
          description: ''
        - value: MODEM_GSM_M_LG
          name: ''
          description: ''
        - value: MODEM_FESTNETZ
          name: Festnetz-Kom.-Einricht. TAE
          description: PST
        - value: MODEM_GPRS_M_LG
          name: ''
          description: ''
        - value: PLC_COM
          name: PLC-Kom.-Einrichtung
          description: PLC
        - value: ETHERNET_KOM
          name: Ethernet-Kom.-Einricht. LAN/WLAN
          description: ETH
        - value: DSL_KOM
          name: DSL-Kom.Einr.
          description: DSL
        - value: LTE_KOM
          name: LTE-Kom.-Einr.
          description: LTE
        - value: RUNDSTEUEREMPFAENGER
          name: Rundsteuerempfänger
          description: RSU
        - value: TARIFSCHALTGERAET
          name: Tarifschaltuhr
          description: TSU
        - value: ZUSTANDS_MU
          name: ''
          description: ''
        - value: TEMPERATUR_MU
          name: ''
          description: ''
        - value: KOMPAKT_MU
          name: ''
          description: ''
        - value: SYSTEM_MU
          name: ''
          description: ''
        - value: UNBESTIMMT
          name: ''
          description: ''
        - value: WASSER_MWZW
          name: ''
          description: ''
        - value: WASSER_WZWW
          name: ''
          description: ''
        - value: WASSER_WZ01
          name: ''
          description: ''
        - value: WASSER_WZ02
          name: ''
          description: ''
        - value: WASSER_WZ03
          name: ''
          description: ''
        - value: WASSER_WZ04
          name: ''
          description: ''
        - value: WASSER_WZ05
          name: ''
          description: ''
        - value: WASSER_WZ06
          name: ''
          description: ''
        - value: WASSER_WZ07
          name: ''
          description: ''
        - value: WASSER_WZ08
          name: ''
          description: ''
        - value: WASSER_WZ09
          name: ''
          description: ''
        - value: WASSER_WZ10
          name: ''
          description: ''
        - value: WASSER_VWZ04
          name: ''
          description: ''
        - value: WASSER_VWZ05
          name: ''
          description: ''
        - value: WASSER_VWZ06
          name: ''
          description: ''
        - value: WASSER_VWZ07
          name: ''
          description: ''
        - value: WASSER_VWZ10
          name: ''
          description: ''
        - value: DICHTEMENGENUMWERTER
          name: Dichtemengenumwerter
          description: DMU
        - value: TEMPERATURMENGENUMWERTER
          name: Temperaturmengenumwerter
          description: TMU
        - value: ZUSTANDSMENGENUMWERTER
          name: Zustandsmengenumwerter
          description: ZMU
        - value: BLOCKSTROMWANDLER
          name: Blockstromwandler
          description: MBW
        - value: MESSWANDLERSATZ_IMS_MME
          name: Messwandlersatz Strom
          description: MIW
        - value: KOMBIMESSWANDLER
          name: Kombimesswandlersatz (Strom und Spannung)
          description: MPW
        - value: SPANNUNGSWANDLER
          name: Messwandlersatz Spannung
          description: MUW
      x-apidog-folder: ''
    Befestigungsart:
      type: string
      title: Befestigungsart
      description: Befestigungsart von Zählern
      enum:
        - STECKTECHNIK
        - DREIPUNKT
        - HUTSCHIENE
        - EINSTUTZEN
        - ZWEISTUTZEN
      x-apidog-enum:
        - value: STECKTECHNIK
          name: Stecktechnik (Befestigungs- und Kontaktierungseinrichtung)
          description: BKE
        - value: DREIPUNKT
          name: 3-Dreipunktaufhängung
          description: DPA
        - value: HUTSCHIENE
          name: Hutschiene
          description: HUT
        - value: EINSTUTZEN
          name: Einstutzen-Zähler
          description: Z31
        - value: ZWEISTUTZEN
          name: Zweistutzen-Zähler
          description: Z32
      x-apidog-folder: ''
    ZaehlertypSpezifikation:
      type: string
      title: ZaehlertypSpezifikation
      description: ZaehlertypSpezifikation
      enum:
        - EDL40
        - EDL21
        - SONSTIGER_EHZ
        - MME_STANDARD
        - MME_MEDA
      x-apidog-enum:
        - value: EDL40
          name: EDL40
          description: Z01
        - value: EDL21
          name: EDL21
          description: Z02
        - value: SONSTIGER_EHZ
          name: sonstiger EHZ
          description: Z03
        - value: MME_STANDARD
          name: Standard
          description: Z04
        - value: MME_MEDA
          name: MeDa-Zähler
          description: Z05
      x-apidog-folder: ''
    Messwerterfassung:
      type: string
      title: Messwerterfassung
      description: Die Messwerterfassung des Zählers
      enum:
        - FERNAUSLESBAR
        - MANUELL_AUSGELESENE
      x-apidog-enum:
        - value: FERNAUSLESBAR
          name: fernauslesbare Zähler
          description: AMR
        - value: MANUELL_AUSGELESENE
          name: manuell ausgelesene Zähler
          description: MMR
      x-apidog-folder: ''
    Fernschaltung:
      type: string
      title: Fernschaltung
      description: Fernschaltung
      enum:
        - VORHANDEN
        - NICHT_VORHANDEN
      x-apidog-enum:
        - value: VORHANDEN
          name: vorhanden
          description: Z06
        - value: NICHT_VORHANDEN
          name: nicht vorhanden
          description: Z07
      x-apidog-folder: ''
    Geschaeftspartner:
      title: Geschaeftspartner
      type: object
      properties:
        boTyp: *ref_5
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        anrede:
          type: string
          description: |-
            Die Anrede für den GePa, Z.B. Herr.
            Z04 Korrespondenzanschrift des Kunden des Lieferanten
            PI 55001 55600 55601 55013 55014 55043 55168 55169
        name1:
          type: string
          description: >-
            Erster Teil des Namens. Hier kann der Firmenname oder bei
            Privatpersonen beispielsweise der Nachname dargestellt werden.
            Beispiele: Yellow Strom GmbH oder Hagen
        name2:
          type: string
          description: >-
            Zweiter Teil des Namens. Hier kann der eine Erweiterung zum
            Firmennamen oder bei Privatpersonen beispielsweise der Vorname
            dargestellt werden. Beispiele: Bereich Süd oder Nina
        name3:
          type: string
          description: >-
            Dritter Teil des Namens. Hier können weitere Ergänzungen zum
            Firmennamen oder bei Privatpersonen Zusätze zum  Namen dargestellt
            werden. Beispiele: und Afrika oder Sängerin
        name4:
          type: string
          description: Name 4
        umsatzsteuerId:
          type: string
          description: 'Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825'
        glaeubigerId:
          type: string
          description: >-
            Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird- Z.B. DE
            47116789
        emailAdresse:
          type: string
          description: email Adresse
        website:
          type: string
          description: 'Internetseite des Marktpartners. Beispiel: www.mp-energie.de'
        gewerbekennzeichnung:
          type: boolean
          description: >-
            Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
            (gewerbeKennzeichnung = true)

            oder eine Privatperson handelt. (gewerbeKennzeichnung = false)

            Z01 Struktur von Personennamen

            Z02 Struktur der Firmenbezeichnung
        hrnummer:
          type: string
          description: Handelsregisternummer des Geschäftspartners
        amtsgericht:
          type: string
          description: >-
            Amtsgericht bzw Handelsregistergericht, das die
            Handelsregisternummer herausgegeben hat
        partneradresse:
          $ref: '#/components/schemas/Adresse'
          description: Adresse des Geschäftspartners, an der sich der Hauptsitz befindet.
        externeKundenummerLieferant:
          type: string
          description: externeKundenummerLieferant
        externeReferenzen:
          type: array
          items:
            $ref: '#/components/schemas/ExterneReferenz'
          description: >-
            Hier können IDs anderer Systeme hinterlegt werden (z.B. eine
            SAP-GP-Nummer) (Details siehe ExterneReferenz)
        geschaeftspartnerrolle:
          type: array
          items:
            $ref: '#/components/schemas/Geschaeftspartnerrolle'
          description: |-
            Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde).
            NAD Z09 ORDERS
            PI 17101 17003
            NAD Kunde des Messstellenbetreibers ORDERS
            PI 17126
        kontaktweg:
          type: array
          items:
            $ref: '#/components/schemas/Kontaktart'
          description: Bevorzugter Kontaktweg des Geschäftspartners.
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - anrede
        - name1
        - name2
        - name3
        - name4
        - umsatzsteuerId
        - glaeubigerId
        - emailAdresse
        - website
        - gewerbekennzeichnung
        - hrnummer
        - amtsgericht
        - partneradresse
        - externeKundenummerLieferant
        - externeReferenzen
        - geschaeftspartnerrolle
        - kontaktweg
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Geschaeftspartner.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Kontaktart:
      title: Kontaktart
      type: string
      enum:
        - ANSCHREIBEN
        - TELEFONAT
        - FAX
        - E_MAIL
        - SMS
      description: >-
        Gibt an, auf welchem Weg die Person oder der Geschäftspartner
        kontaktiert werden kann
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
    ExterneReferenz:
      title: ExterneReferenz
      type: object
      properties:
        exRefName:
          type: string
          enum:
            - Kundennummer beim Lieferanten
            - Kundennummer beim Altlieferanten
          description: >-
            Bezeichnung der externen Referenz, Kundennummer beim Lieferanten,
            bezieht sich auf das vorangegangene NAD Segment

            RFF AVC

            PI 55109 55137 

            RFF AVC Kundennummer beim Lieferanten ORDERS

            PI 17101
        exRefWert:
          type: string
          description: >-
            Kundennummer beim Altieferanten - Angabe von Referenzen für
            Rückmeldungen und Anfragen

            PI 55109 55137 

            ORDERS PI 17101
      x-apidog-orders:
        - exRefName
        - exRefWert
      x-apidog-ignore-properties: []
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
    Tarifart:
      type: string
      title: Tarifart
      description: Tarifart
      enum:
        - EINTARIF
        - ZWEITARIF
        - MEHRTARIF
        - SMART_METER
        - LEISTUNGSGEMESSEN
      x-apidog-enum:
        - value: EINTARIF
          name: Eintarif
          description: ETZ
        - value: ZWEITARIF
          name: Zweitarif
          description: ZTZ
        - value: MEHRTARIF
          name: Mehrtarif
          description: NTZ
        - value: SMART_METER
          name: ''
          description: ''
        - value: LEISTUNGSGEMESSEN
          name: ''
          description: ''
      x-apidog-folder: ''
    Zaehlertyp:
      type: string
      title: Zaehlertyp
      description: Zaehlertyp
      enum:
        - DREHSTROMZAEHLER
        - BALGENGASZAEHLER
        - DREHKOLBENZAEHLER
        - SMARTMETER
        - LEISTUNGSZAEHLER
        - MAXIMUMZAEHLER
        - TURBINENRADGASZAEHLER
        - ULTRASCHALLGASZAEHLER
        - WECHSELSTROMZAEHLER
        - WIRBELGASZAEHLER
        - MESSDATENREGISTRIERGERAET
        - ELEKTRONISCHERHAUSHALTSZAEHLER
        - SONDERAUSSTATTUNG
        - WASSERZAEHLER
        - MODERNEMESSEINRICHTUNG
      x-apidog-enum:
        - value: DREHSTROMZAEHLER
          name: analoger Haushaltszähler (Drehstrom)
          description: AHZ
        - value: BALGENGASZAEHLER
          name: Balgengaszähler
          description: BGZ
        - value: DREHKOLBENZAEHLER
          name: Drehkolbengaszähler
          description: DKZ
        - value: SMARTMETER
          name: ''
          description: ''
        - value: LEISTUNGSZAEHLER
          name: Lastgangzähler
          description: LAZ
        - value: MAXIMUMZAEHLER
          name: Maximumzähler
          description: MAZ
        - value: TURBINENRADGASZAEHLER
          name: Turbinenradgaszähler
          description: TRZ
        - value: ULTRASCHALLGASZAEHLER
          name: Ultraschallgaszähler
          description: UGZ
        - value: WECHSELSTROMZAEHLER
          name: analoger Wechselstromzähler
          description: WSZ
        - value: WIRBELGASZAEHLER
          name: Wirbelgaszähler
          description: WGZ
        - value: MESSDATENREGISTRIERGERAET
          name: Messdatenregistriergerät
          description: MRG
        - value: ELEKTRONISCHERHAUSHALTSZAEHLER
          name: elektronischer Haushaltszähler
          description: EHZ
        - value: SONDERAUSSTATTUNG
          name: Individuelle Abstimmung (Sonderausstatung)
          description: IVA
        - value: WASSERZAEHLER
          name: ''
          description: ''
        - value: MODERNEMESSEINRICHTUNG
          name: moderne Messeinrichtung nach MsbG
          description: MME
      x-apidog-folder: ''
    Zaehlerauspraegung:
      type: string
      title: Zaehlerauspraegung
      description: Zaehlerauspraegung
      enum:
        - EINRICHTUNGSZAEHLER
        - ZWEIRICHTUNGSZAEHLER
      x-apidog-enum:
        - value: EINRICHTUNGSZAEHLER
          name: Einrichtungszähler
          description: ERZ
        - value: ZWEIRICHTUNGSZAEHLER
          name: Zweirichtungszähler
          description: ZRZ
      x-apidog-folder: ''
    Sparte:
      type: string
      title: Sparte
      description: Division
      enum:
        - STROM
        - GAS
        - FERNWAERME
        - NAHWAERME
        - WASSER
        - ABWASSER
      x-apidog-enum:
        - value: STROM
          name: Sparte Strom
          description: Represents electricity as the utility division
        - value: GAS
          name: Sparte Gas
          description: Represents natural gas as the utility division
        - value: FERNWAERME
          name: Sparte Fernwärme
          description: Represents district heating as the utility division
        - value: NAHWAERME
          name: Sparte Nahwärme
          description: Represents local heating as the utility division
        - value: WASSER
          name: Sparte Wasser
          description: Represents water supply as the utility division
        - value: ABWASSER
          name: Sparte Abwasser
          description: Represents wastewater services as the utility division
      examples:
        - STROM
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
