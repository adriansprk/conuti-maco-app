# INCIDENT_CLEARINGPROZESS



![LW24h mit Abhängigkeiten - INCIDENT_CLEARINGPROZESS.png](https://api.apidog.com/api/v1/projects/816353/resources/376723/image-preview)
<Steps>
  <Step title="Prozessauslöser - manueller Start">
    <Tabs>
      <Tab title="Übersicht">
        <Card title="G-INCIDENT_CLEARINGPROZESS">
          Der Bereinigungsprozess ermöglicht die Weiterverarbeitung von Prozessen im Fehlerfall. Er wird **manuell** über den Störungsmonitor zur Fehlerbereinigung gestartet. 
          Die laufende Prozessinstanzen zu einem BusinessKey wird beendet. Anhand der Auswahl im Störungsmonitor wird der Prozess entweder an entsprechender Stelle neugestartet oder mit ausgewähltem Status beendet. Der ursprüngliche BusinessKey wird beibehalten.
        </Card>
        <Card title="Trigger">
          Manueller Start durch Clearing/2nd-Level-Support bei festgestellten Prozessfehlern über den Störungsmonitor.
        </Card>
      </Tab>
      <Tab title="📄 Trigger">
        <Accordion title="Verarbeitung Nachricht abbrechen und Status 'abgebrochen' setzen" defaultOpen={false}>
          **prozessZustand:** canceln
Bricht die Verarbeitung der Nachricht endgültig ab. Der Verarbeitungsstatus **und** der fachliche Status werden auf abgebrochen gesetzt, sodass die Nachricht im weiteren Verlauf nicht mehr verarbeitet wird. Anschließend wird die Archivierung des Datakeepers über das Send-Event ${roleSystem}-${edifactVersion}-archivierungStarten angestoßen.
**Wann nutzen:** Wenn die Nachricht nicht weiterverarbeitet werden soll oder kann — z. B. weil sie fachlich nicht weiter relevant ist, eine doppelte Übermittlung vorliegt, eine Bearbeitung in aktueller Prozessversion nicht möglich ist oder eine inhaltliche Klärung mit dem Marktpartner ergeben hat, dass keine Verarbeitung notwendig ist.
                       
         
        </Accordion>
          
                  <Accordion title="Verarbeitung Nachricht abbrechen und Status 'erfolgreich' setzen" defaultOpen={false}>
          **prozessZustand:** posBeenden
Bricht die Verarbeitung der Nachricht endgültig ab. Der Verarbeitungsstatus wird auf erfolgreich gesetzt und der fachliche Status auf abgebrochen, sodass die Nachricht im weiteren Verlauf nicht mehr verarbeitet wird. Anschließend wird die Archivierung des Datakeepers über das Send-Event ${roleSystem}-${edifactVersion}-archivierungStarten angestoßen.
**Wann nutzen:** Wenn die Nachricht nicht weiterverarbeitet werden soll oder kann — z. B. weil sie fachlich nicht weiter relevant ist, eine doppelte Übermittlung vorliegt, eine Bearbeitung in aktueller Prozessversion nicht möglich ist oder eine inhaltliche Klärung mit dem Marktpartner ergeben hat, dass keine Verarbeitung notwendig ist.
                       
         
        </Accordion>
<Accordion title="Nachrichteneingang mit Aperak neu starten" defaultOpen={false}>
          **prozessZustand:** neustartenMitAperak
Startet den Nachrichteneingang erneut und versendet dabei wieder eine Aperak-Rückmeldung an den Marktpartner. Der pruefidentifikator wird aus dem Datakeeper gelesen, das ediEmpfangsDatum wird auf das aktuelle Datum gesetzt. Anschließend wird das Send-Event ${roleSystem}-${edifactVersion}-neustartenMitAperak ausgelöst.
**Wann nutzen:** Wenn die Originalverarbeitung vor Durchführung der Aperak-Prüfungen fehlgeschlagen ist und der Marktpartner noch eine entsprechende Rückmeldung erhalten muss.
         
        </Accordion>
<Accordion title="Nachrichteneingang ohne Aperak neu starten" defaultOpen={false}>
          **prozessZustand:** neustartenOhneAperak
Startet den Nachrichteneingang erneut, ohne dabei eine Aperak-Rückmeldung an den Marktpartner zu senden. Der pruefidentifikator wird aus dem Datakeeper gelesen, das ediEmpfangsDatum wird auf das aktuelle Datum gesetzt. Anschließend wird das Send-Event ${roleSystem}-${edifactVersion}-neustartenOhneAperak ausgelöst.
**Wann nutzen:** Wenn die Verarbeitung innerhalb der App wiederholt werden muss, dem Marktpartner aber bereits zuvor eine Aperak gesendet wurde (oder bewusst keine erneute Rückmeldung erfolgen soll, um Duplikate zu vermeiden).
         
        </Accordion>
<Accordion title="Nachrichtausgang mit EDI-Versand neu starten" defaultOpen={false}>
          **prozessZustand:** neustartenMitVersand
Startet den Nachrichtenausgang erneut inklusive EDI-Versand an den Marktpartner. Der processIdentifier wird aus dem Datakeeper gelesen, anschließend wird das Send-Event ${roleSystem}-${edifactVersion}-neustartenMitVersand ausgelöst.
**Wann nutzen:** Wenn eine ausgehende Nachricht noch vor Versand der Edifact auf Fehler gelaufen ist. Nach Fehlerbehebung kann der Prozess so neugestartet und die Edifact korrekt aufgebaut und versendet werden.
         
        </Accordion>
<Accordion title="Nachrichtausgang ohne EDI-Versand neu starten" defaultOpen={false}>
         **prozessZustand:** neustartenOhneVersand
Startet den Nachrichtenausgang erneut, ohne dabei eine EDI an den Marktpartner zu versenden. Der processIdentifier wird aus dem Datakeeper gelesen, anschließend wird das Send-Event ${roleSystem}-${edifactVersion}-neustartenOhneVersand ausgelöst.
**Wann nutzen:** Wenn die ausgehende Nachricht nicht korrekt an die Backend-Verarbeitung(Schnittstelle) übergeben werden konnte, der Marktpartner die Nachricht aber bereits korrekt erhalten hat (kein erneuter Versand gewünscht).
         
        </Accordion>
<Accordion title="Eventeingang neu starten" defaultOpen={false}>
  **prozessZustand:** neuStartenEvent
Startet den Eventeingang erneut. Der eventName wird aus den INBOUND-Daten ($.zusatzdaten.eventname) gelesen, anschließend wird das Send-Event ${roleSystem}-${edifactVersion}-neuStartenEvent ausgelöst.
**Wann nutzen:** Kommt es bereits bei der Verarbeitung eines Events zu Fehlern im Prozess, kann der Prozess nach Korrektur etwaiger Daten erneut gestartet werden. So kann die Nachricht ohne neues Event aus dem Backend an den Nachrichtenausgang übergeben und der Edifact-Versand ermöglicht werden.
         
        </Accordion>
<Accordion title="Fristenausgang neu starten" defaultOpen={false}>
   **prozessZustand:** neustartenFristenAusgang
Startet den Fristenausgang erneut. Es werden keine zusätzlichen Daten aus dem Datakeeper gelesen — das Send-Event ${roleSystem}-${edifactVersion}-neustartenFristenAusgang wird direkt ausgelöst.
**Wann nutzen:** Bei Fehlern in der Fristberechnung kann der Prozess nach Korrektur neu in den Fristenprozess übergeben werden um die Verarbeitung der Antwortnachrichten auch im Fehlerfall zu gewährleisten.
         
        </Accordion>
      </Tab>
<Tab title="📄 Eingangsparameter">
        <Accordion title="Erforderliche Prozessvariablen" defaultOpen={false}>
          | Variable | Typ | Beschreibung |
          |---|---|---|
          | `businessKey` | String | Eindeutige Geschäftsreferenz des zu bereinigenden Prozesses |
          | `prozessZustand` | String | Steuert den Bereinigungs-Pfad (siehe Step "Bereinigungsentscheidung") |
          | `roleSystem` | String | Marktpartner-Rolle (z. B. LF, NB, MSB) |
          | `edifactVersion` | String | EDIFACT-Version |
        </Accordion>
      </Tab>
    </Tabs>
  </Step>


  
  <Step title="Prozessende">
    <Tabs>
      <Tab title="Übersicht">
        <Card title="Bereinigungsprozess abgeschlossen">
          Nach abbruch der aktuellen Prozessinstanz und Start der getroffenen Auswahl zur Prozessbereinigung ist der Bereinigungsprozess beendet. Die Umsetzung der getroffenen Auswahl erfolgt im jeweiligen Steuerungsprozess wie dem Nachrichteneingang oder -ausgang
        </Card>
      </Tab>
    </Tabs>
  </Step>
</Steps>
