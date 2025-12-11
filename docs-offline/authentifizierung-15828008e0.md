# Authentifizierung

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /auth-token-url:
    post:
      summary: Authentifizierung
      deprecated: false
      description: >
        # Authentifizierung via MACO APP OAuth (Service-Login für
        Trigger-Schnittstellen)


        Für den Zugriff auf ausgewählte **Trigger-Schnittstellen** der MACO APP
        erfolgt die Authentifizierung über einen **OAuth-basierten Login**.
        Dieses Verfahren ist ausschließlich für **Services** vorgesehen – also
        für Systeme, die automatisiert mit der MACO APP kommunizieren, nicht für
        interaktive Benutzeranmeldung.


        Nach erfolgreicher Anmeldung steht dir ein **Access Token** zur
        Verfügung, mit dem du in freigeschalteten Umgebungen Requests direkt
        über die API-Dokumentation testen kannst.


        ---


        ## Ziel


        Du möchtest:


        - deinen Service gegenüber der MACO APP authentifizieren,

        - ein Access Token automatisiert abrufen,

        - dieses Token in API-Requests verwenden,

        - und freigegebene Schnittstellen über die Doku testen.


        Genau dafür ist dieser Loginflow gedacht.


        ---


        ## Voraussetzungen


        Folgende Umgebungsvariablen müssen in Apidog (bzw. im Testtool deiner
        Wahl) definiert werden:


        | Variable         |
        Beschreibung                                              |

        |------------------|-----------------------------------------------------------|

        | `username`       | Technischer Benutzername
        (Service-Account)               |

        | `password`       | Passwort für den
        Service-Account                          |

        | `authTokenUrl`   | Token-Endpunkt der MACO APP
        OAuth-Anmeldung               |

        | `clientId`       | Die zugewiesene
        Client-ID                                 |

        | `clientSecret`   | (Optional) Das Secret, falls für deinen Client
        erforderlich |


        **Wichtig:**  

        Diese Werte sind **abhängig von der Umgebung** (z. B. Test, Staging,
        Produktion) und werden dir beim Onboarding durch das MACO APP Team
        individuell bereitgestellt. Verwende ausschließlich die dir zugewiesenen
        Zugangsdaten.


        ---


        ## Login und Token-Nutzung


        ### 1. Login-Request erstellen


        Erzeuge einen POST-Request auf `{{authTokenUrl}}`  

        Setze den Content-Type auf: `application/x-www-form-urlencoded`


        ### 2. Body-Parameter setzen


        Verwende folgende Felder im Body des Requests:


        ```

        grant_type=password

        client_id={{clientId}}

        client_secret={{clientSecret}}  // falls notwendig

        username={{username}}

        password={{password}}

        ```


        ### 3. Access Token speichern


        Das Antwortfeld `access_token` enthält deinen Token.  

        Speichere diesen als Umgebungsvariable `accessToken`, damit du ihn in
        weiteren Requests nutzen kannst.


        ### 4. Token verwenden


        Füge in jedem weiteren Request diesen Header ein:


        ```

        Authorization: Bearer {{accessToken}}

        ```


        ---


        ## Ablaufdiagramm


        ```mermaid

        graph TD
            A[Service sendet Login-Request] --> B[Access Token wird ausgestellt]
            B --> C[Token in Apidog speichern]
            C --> D[Requests an Trigger-Schnittstellen senden]
        ```


        ---


        ## Anwendung über die API-Doku


        Sobald dein Token gespeichert ist, kannst du damit in freigeschalteten
        Umgebungen direkt über die **MACO APP API-Dokumentation** Anfragen
        ausführen – z. B. zum Auslösen von Prozessen oder Testen von
        Integrationen.


        Die verfügbaren Endpunkte variieren je nach Umgebung und Berechtigungen.


        ---


        ## Sicherheit beachten


        - Der Token ist zeitlich begrenzt gültig (i. d. R. 5–15 Minuten).

        - Bei Bedarf kann zusätzlich ein Refresh Token verwendet werden.

        - Nutze ausschließlich HTTPS.

        - Tokens dürfen nicht in Logs oder öffentlich zugänglichen Systemen
        gespeichert werden.


        ---


        ## Zusammenfassung


        Mit diesem Setup kannst du:


        - deinen Service automatisiert gegen die MACO APP authentifizieren,

        - Trigger-Schnittstellen nutzen,

        - Token-Handling zentral verwalten,

        - und Anfragen direkt über die API-Dokumentation testen.


        ---


        Falls du noch Fragen zur Nutzung in speziellen Umgebungen oder zu
        erweiterten OAuth-Szenarien hast (z. B. Mandantenkontexte,
        Rollenmapping, Claim-Handling):  

        Wende dich gern an das Architektur-Team.
      operationId: login
      tags:
        - Schnittstellen/Trigger (MACO APP)
      parameters:
        - name: Content-Type
          in: header
          description: ''
          required: true
          example: application/x-www-form-urlencoded
          schema:
            type: string
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                username:
                  description: Benutzername
                  example: '{{username}}'
                  type: string
                password:
                  description: Passwort
                  example: '{{password}}'
                  type: string
                client_id:
                  description: Cleint Id
                  example: '{{client-id}}'
                  type: string
                client_secret:
                  example: '{{client-secret}}'
                  type: string
                grant_type:
                  example: password
                  type: string
              required:
                - username
                - password
                - client_id
                - client_secret
                - grant_type
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apidog-name: Success
      security: []
      x-apidog-folder: Schnittstellen/Trigger (MACO APP)
      x-apidog-status: developing
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-15828008-run
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
