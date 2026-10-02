# Fehlercodes


Übersicht der Schnittstellen Fehlercodes.  

## Antwortcodes  

Die MACO APP verwendet standardmäßige HTTP-Codes, um den Erfolg oder Misserfolg Ihrer Anfragen anzuzeigen.  

- **2xx** HTTP-Codes stehen für erfolgreiche Anfragen.  
- **4xx** HTTP-Codes stehen für fehlerhafte Anfragen seitens des Nutzers.  
- **5xx** HTTP-Codes deuten auf ein Problem mit den MACO APP-Servern hin.  

### Statuscodes  

| Statuscode | Beschreibung |
|------------|-------------|
| **200** | Erfolgreiche Anfrage. |
| **4xx** | Client-Fehler, siehe Fehlercodes. |
| **5xx** | Fehler auf den MACO APP-Servern. |

## Fehler-Schema  

MACO APP verwendet HTTP-Standardcodes zur Anzeige von Erfolgen oder Fehlern. Die folgenden Fehlercodes können auftreten:  

| Statuscode | Typ                  | Beschreibung                                                                 |
|------------|----------------------|------------------------------------------------------------------------------|
| **400**    | `malformed`          | Die Anfrage enthält Syntaxfehler, z. B. ein nicht lesbares JSON-Format.     |
| **401**    | `unauthenticated`    | Die Anfrage enthält keine gültigen Zugangsdaten.                            |
| **403**    | `permissionDenied`   | Der authentifizierte Benutzer hat keine Berechtigung für diese Anfrage.     |
| **404**    | `notFound`           | Die angeforderte Ressource existiert nicht.                                 |
| **409**    | `conflict`           | Die Anfrage steht in Konflikt mit einer anderen Anfrage.                    |
| **422**    | `invalid`            | Die Anfrage enthält ungültige Parameter.                                    |
| **429**    | `rateLimited`        | Zu viele Anfragen in kurzer Zeit – der Client wurde vorübergehend geblockt.|
| **500**    | `internal`           | Ein unerwarteter Fehler ist aufgetreten, das Ergebnis ist unbekannt.        |
| **501**    | `notImplemented`     | Die angeforderte Operation wird nicht unterstützt oder ist nicht implementiert. |
| **502**    | `badGateway`         | Der Server hat eine ungültige Antwort vom Upstream-Server erhalten.         |
| **503**    | `unavailable`        | Der Service ist momentan nicht verfügbar (z. B. Wartung oder Überlastung).  |
| **504**    | `timeout`            | Der Server hat vom Upstream-Server keine rechtzeitige Antwort erhalten.     |
| **505**    | `httpVersionNotSupported` | Die HTTP-Version der Anfrage wird vom Server nicht unterstützt.       |


## Fehlerbehandlung  

Wenn ein Fehler auftritt, enthält die Antwort zusätzliche Informationen über das Problem.  

 
 

