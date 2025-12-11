# Absenderdaten lesen

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /lesenMarktteilnehmerAbsender:
    get:
      summary: Absenderdaten lesen
      deprecated: true
      description: >-
        ** OBSOLET: Daten sind bereits im Event Container vorhanden **

        Lesen einen absender(marktteilnehmer) mit LokationsId  (Parameter1)  zum
        Zeitpunkt (Parameter2) | Read a sender (market participant)  (parameter
        1) at time (parameter 2)
      operationId: LESEN_MARKTTEILNEHMER_ABSENDER
      tags:
        - Schnittstellen/Obsolet
        - LESEN | READ
      parameters:
        - name: command
          in: query
          description: >-
            Name der Operation | Name of the operation (MACO APP interal
            assignment between process and interface)
          required: false
          schema:
            default: LESEN_MARKTTEILNEHMER_ABSENDER
            type: string
            examples:
              - SAP_LESEN_MARKTTEILNEHMER_ABSENDER
        - name: parameter1
          in: query
          description: ILN Nummer | ILN number
          required: true
          schema:
            type: string
            examples:
              - '9903790000002'
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
      responses:
        '200':
          description: >-
            Erfolgreiches Lesen der Kommunikationsdaten | Successful reading of
            communication data
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apidog-name: OK
        '400':
          description: Fehlerhafte Anfrage | Bad Request
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apidog-name: Bad Request
      security:
        - bearer: []
      x-apidog-folder: Schnittstellen/Obsolet
      x-apidog-status: obsolete
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-14017022-run
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
