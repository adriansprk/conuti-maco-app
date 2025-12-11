# Zuordnungsemächtigung lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /getAllocationAuthorization:
    get:
      summary: Zuordnungsemächtigung lesen
      deprecated: false
      description: Ermitteln ob eine Zuordnungsermächtigung vorhanden ist
      operationId: LESEN_PROZESSDATEN_ZUORDNUNGERMAECHTIGUNG
      tags:
        - Schnittstellen/Prozessdaten lesen (Backend)
        - LESEN | READ
      parameters:
        - name: parameter1
          in: query
          description: MarktlokationsId
          required: true
          example: ''
          schema:
            type: string
            minLength: 11
            maxLength: 11
            pattern: \d{11}
            examples:
              - '50858721423'
        - name: parameter2
          in: query
          description: Rollencodenummer (ILN) des Lieferanten
          required: true
          example: ''
          schema:
            type: string
            pattern: \{d13}
            minLength: 13
            maxLength: 13
            examples:
              - '9979052000006'
        - name: parameter3
          in: query
          description: Einzugsdatum
          required: true
          schema:
            type: string
            format: date-time
            examples:
              - '2024-06-28T12:18:00Z'
            pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$
        - name: parameter4
          in: query
          description: Bilanzkreis aus der Anmeldung
          required: true
          schema:
            type: string
        - name: command
          in: query
          description: >-
            Entspricht der operationId dieser Schnittstelle. Diese Operation Id
            entspricht dem Command im Camunda Konnektor Prozess. Wenn das
            Backend einen generischen Endpunkt bereitstellt, kann dieses Command
            gentutzt werden um zu definieren welche Operation ausgeführt werden
            soll.
          required: true
          example: LESEN_PROZESSDATEN_ZUORDNUNGSERMAECHTIGUNG
          schema:
            type: string
      responses:
        '200':
          description: 'Erfolgreiches Lesen der Zuordnungsermächtigung '
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Zuordnungserm%C3%A4chtigung'
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
      x-apidog-folder: Schnittstellen/Prozessdaten lesen (Backend)
      x-apidog-status: developing
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14665842-run
components:
  schemas:
    Zuordnungsermächtigung:
      type: object
      properties:
        ermaechtigungVorhanden:
          type: boolean
          description: Wenn die Zuordnungermächtigung vorhanden ist, dann true, sonst false
      x-apidog-orders:
        - ermaechtigungVorhanden
      required:
        - ermaechtigungVorhanden
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
