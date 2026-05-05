# Abmeldeanfrage NB -> LFA (Rolle NB)

```mermaid
sequenceDiagram
  autonumber
  
  participant NB as NB
  participant LFA as LFA
  participant LFN as LFN
  participant LFZ as LFZ
  link LFN: Dashboard @ https://dashboard.contoso.com/alice

  LFN ->>+NB: Anmeldung verb. MaLo (*1)
  LFN ->>+NB : Anmeldung erz. MaLo (*2)

  opt Existierende Zuordnung
    NB ->> LFN: Existierende Zuordnung (*3)

    NB ->> LFA: Anfrage zur Beendigung der Zuordnung (*4)

    alt Bestätigung der Beendigung
        LFA ->> NB: Bestätigung Beendigung der Zuordnung (*5)
    else Ablehnung der Beendigung
        LFA ->> NB: Ablehnung Beendigung der Zuordnung (*6)
    end
  end

  alt Bestätigung der Anmeldung
  NB ->> LFN: Bestätigung Anmeldung verb. MaLo (*7)
  NB ->> LFN: Bestätigung Anmeldung erz. MaLo (*8)

  else Ablehnung der Anmeldung
    NB ->> LFN: Ablehnung Anmeldung verb. MaLo (*9)
    NB ->> LFN: Ablehnung Anmeldung erz. MaLo (*10)
  end

  NB ->> LFA: Beendigung der Zuordnung (*11)

  NB ->> LFZ: Aufhebung einer zuk. Zuordnung (*12)

```

*1 Prüfi: 55001
*2 Prüfi: 55077
*3 Prüfi: 55036
*4 Prüfi: 55010
*5 Prüfi: 55011
*6 Prüfi: 55012
*7 Prüfi: 55002
*8 Prüfi: 55078
*9 Prüfi: 55003
*10 Prüfi: 55080
*11 Prüfi: 55037
*12 Prüfi: 55038

