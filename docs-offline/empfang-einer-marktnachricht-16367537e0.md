# Empfang einer Marktnachricht

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /receive:
    post:
      summary: Empfang einer Marktnachricht
      deprecated: false
      description: >+
        ## 📬 Beschreibung


        Empfang von Marktnachrichten als Rohdaten (EDIFACT, IDOC XML) für die
        weitere Verarbeitung im **Market Communications Service (MCS)**.


        Über **Query-Parameter** können optionale Verarbeitungseinstellungen
        gesteuert werden, z.B.:

        - Auswahl des Eingangs-Channels

        - Bestimmung des zuständigen Service

        - Priorisierung der Nachricht

        - Angabe von Metainformationen, wie Absender, Empfänger, Betreff,
        Dateiname


        **Unterstützte Content-Types für den Payload:**

        - `application/octet-stream` – Binärdaten (klassisches EDIFACT oder
        andere Formate)

        - `text/xml` – XML-Daten (z.B. IDOC XML)

        - `text/plain` – EDIFACT-Nachrichten im Textformat


        **Hinweis:**  

        Es erfolgt keine Vorvalidierung der Daten am Endpoint – der Fokus liegt
        auf schnellem, flexiblem Intake verschiedenster Formate. Die Nachricht
        wird in die Eingangs Quue gelegt und 

      operationId: receive
      tags:
        - Schnittstellen/MCS Eingang (MACO APP)
      parameters:
        - name: channel
          in: query
          description: >-
            Initialer Nachrichten-Channel in dem die eingehende Nachricht
            behandlet wird. Default ist INBOUND_CHANNEL_ERROR - wenn dieser
            gesetzt ist, wird die Ermittlung des korrekten Kanals für die
            Verarbeitung anhannd der Payload durchgeführt. Default :
            INBOUND_CHANNEL_ERROR
          required: false
          example: INBOUND_CHANNEL_ERROR
          schema:
            type: string
        - name: service
          in: query
          description: >-
            Service ID, der zum Empfang der Nachricht zugeordnet ist. Dieser
            kann u.a. genutzt werden um den initialen Nachrichten-Channel
            festzulegen. Default: ‘default_http’ 
          required: false
          example: REST_SERVICE
          schema:
            type: string
            default: default_http
        - name: mailto
          in: query
          description: >-
            Empfänger Mailadresse der Nachricht kann übergeben werden, sofern
            sie für die weitere Verarbeitung relevant ist und während der
            Verarbeitung nicht ermittelt wird. Im Default sollte der Wert nicht
            gefüllt werden.
          required: false
          example: edi@marktpartner.de
          schema:
            type: string
            format: email
        - name: mailfrom
          in: query
          description: >-
            Absender Mailadresse der Nachricht kann übergeben werden, sofern sie
            für die weitere Verarbeitung relevant ist und während der
            Verarbeitung nicht ermittelt wird. Im Default sollte der Wert nicht
            gefüllt werden.
          required: false
          example: edi@marktpartner.de
          schema:
            type: string
            format: email
        - name: filename
          in: query
          description: >-
            Setzt die Mail-Betreff und Name des Anhangs , sofern sie für die
            weitere Verarbeitung relevant ist und während der Verarbeitung nicht
            ermittelt wird. Im Default sollte der Wert nicht gefüllt werden.
          required: false
          example: APERAK__9900683000008_9903854000005_20250515_BC57064B5A2B70
          schema:
            type: string
        - name: encoding
          in: query
          description: Definiert das Encoding des Request-Bodys / der Nachricht
          required: false
          example: ISO-8859-1
          schema:
            type: string
            default: System-Standard-Encoding
            examples:
              - ISO-8859-1
        - name: prio
          in: query
          description: >-
            Setzt die Priorität mit der die Nachricht in die Queue gegeben wird.
            Default: low
          required: false
          example: medium
          schema:
            type: string
            enum:
              - low
              - medium
              - high
              - ultra
        - name: activeuser
          in: query
          description: "Persistiert den ‘activeuser’ des Requests in die Status-Historie. Kein Default.\t"
          required: false
          schema:
            type: string
        - name: freeText
          in: query
          description: >-
            Speichert in Kombination mit der Angabe des ‘activeuser’ eine
            Freitext-Nachricht des Versandgrunds in die Statushistorie. Kein
            Default.
          required: false
          schema:
            type: string
        - name: alternativeId
          in: query
          description: >-
            Speichert eine alternative ID  in den Kontext zur Laufzeit der
            Nachrichtenverarbeitung. Hier kann der BusinessKey übergeben
            werden, 
          required: false
          schema:
            type: string
            format: uuid
        - name: suppress_errors
          in: query
          description: >-
            Speichert den Wert der Eigenschaft B3P_SUPPRESS_SYNC_ERRORS in den
            Kontext zur Laufzeit der Nachrichtenverarbeitung. Kein Default.
          required: false
          example: 'true'
          schema:
            type: boolean
        - name: isBinary
          in: query
          description: >-
            Wenn angegeben wird die Nachricht auch gleich im B3P_CURRENT_PAYLOAD
            zur Laufzeit gespeichert. Default: Keine Angabe.
          required: false
          example: 'true'
          schema:
            type: boolean
        - name: sync
          in: query
          description: >-
            Wenn gesetzt wird die Nachricht in einen eigenem Thread verarbeitet.
            Default: Keine Angabe.
          required: false
          example: 'true'
          schema:
            type: boolean
        - name: sfc
          in: query
          description: >-
            Wenn gesetzt werden die Format-Erkennung und Channel-Distributionen
            in der Nachrichtenverarbeitung übersprungen. Default: Keine Angabe.
          required: false
          example: 'true'
          schema:
            type: boolean
        - name: responseType
          in: query
          description: >-
            Definiert, was bei der erfolgreichen Nachrichtenübergabe als Antwort
            zurückgegeben werden soll. Aktuell wird nur der Wert ‘messageIds’
            unterstützt. In diesem Fall werden die IDs der erstellten
            Nachrichten kommasepariert zurückgegeben. Default: es wird keine
            Antwort zurückgegeben.
          required: false
          example: messageIds
          schema:
            type: string
            enum:
              - messageIds
      requestBody:
        content:
          application/octet-stream:
            schema:
              type: string
              format: binary
            example: file://C:\Users\conut\Downloads\edifact.txt
      responses:
        '200':
          description: OK – Nachricht erfolgreich angenommen. Rückgabe vom businessKey
          content:
            text/plain:
              schema:
                type: string
                description: Komma‐separierte Message-IDs (bei responseType=messageIds)
          headers: {}
          x-apidog-name: OK
        '204':
          description: No Content – Nachricht erfolgreich angenommen (ohne ResponseBody)
          headers: {}
          x-apidog-name: No Content
        '400':
          description: Bad Request – Ungültige Parameter
          headers: {}
          x-apidog-name: Bad Request
        '500':
          description: Internal Server Error – Serverfehler bei Verarbeitung
          headers: {}
          x-apidog-name: Server Error
      security:
        - bearer: []
      x-apidog-folder: Schnittstellen/MCS Eingang (MACO APP)
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-16367537-run
components:
  schemas: {}
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
