# Stammdatenänderung vom Netzbetreiber (verantwortlich) (Rolle LF)

```mermaid
sequenceDiagram
  autonumber
  participant LF as LF
  participant NB as NB  
  participant MSB as MSB
  participant ÜNB as ÜNB
 
 par wenn Änderung für LF relevant
  NB ->> LF: Änderung vom NB an LF (*1)
  LF ->> NB : Rückmeldung auf Änderung (*2)

  opt wenn LF anderen Inhalt erwartet
    NB ->> LF: Bearbeitungsstand zur Rückmeldung (*3)    
  end
   
 and wenn Änderung für MSB relevant

    NB ->> MSB: Änderung vom NB an MSB (*4)
    MSB ->> NB: Rückmeldung auf Änderung (*5)
    
    opt wenn MSB anderen Inhalt erwartet
        NB ->> MSB: Bearbeitungsstand zur Rückmeldung (*6)
    end
    opt wenn durch Änderung Werteübermittlung erforderlich wird
        MSB ->> MSB: ref Aufbereitung und Übermittlung von Werten vom MSB der Messlokation (*7)
    end
  and wenn Änderung für ÜNB relevant
      NB ->> ÜNB: Änderung vom NB an ÜNB (*8)
    ÜNB ->> NB: Rückmeldung auf Änderung (*9)
        opt wenn ÜNB anderen Inhalt erwartet
        NB ->> ÜNB: Bearbeitungsstand zur Rückmeldung (*10)
    end
  end

```

*1 Prüfi: 55615, 55616, 55619, 55617, 55618, 55620, 55225, 55175
*2 Prüfi: 55621, 55622, 55625, 55623, 55624, 55626, 55227, 55180
*3 Prüfi: 21047
*4 Prüfi: 55627, 55628, 55629, 55630, 55632, 55173
*5 Prüfi: 55633, 55634, 55635, 55636, 55638, 55177
*6 Prüfi: 21047
*7 Prüfi: 13017, 13018
*8 Prüfi: 55688
*9 Prüfi: 55689
*10 Prüfi: 21047

