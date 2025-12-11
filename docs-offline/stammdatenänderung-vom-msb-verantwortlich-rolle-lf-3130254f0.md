# Stammdatenänderung vom MSB (verantwortlich) (Rolle LF)

```mermaid
sequenceDiagram
  autonumber
  
  participant LF as LF
  participant MSB as MSB
  participant NB as NB
  participant weiterer MSB as weiterer MSB
  participant ÜNB as ÜNB  
 
 
 par wenn Änderung für NB relevant
  MSB ->> NB: Änderung vom MSB an NB (*1)
  NB ->> MSB : Rückmeldung auf Änderung (*2)

  opt wenn NB anderen Inhalt erwartet
    MSB ->> NB: Bearbeitungsstand zur Rückmeldung (*3)    
  end
   
 and wenn Änderung für LF relevant

    MSB ->> LF: Änderung vom MSB an LF (*4)
    LF ->> MSB: Rückmeldung auf Änderung (*5)
    
    opt wenn LF anderen Inhalt erwartet
        MSB ->> LF: Bearbeitungsstand zur Rückmeldung (*6)
    end
    
 and wenn Änderung für weiteren MSB relevant   
 
     MSB ->> weiterer MSB: Änderung vom MSB an weiteren MSB (*8)
     weiterer MSB ->> MSB: Rückmeldung auf Änderung (*9)
     
    opt wenn wenn weiterer MSB anderen Inhalt erwartet
        MSB ->> weiterer MSB: Bearbeitungsstand zur Rückmeldung (*10)
    end
    
    opt wenn durch Änderung Werteübermittlung erforderlich wird
        weiterer MSB ->> weiterer MSB: ref Aufbereitung und Übermittlung von Werten vom MSB der Messlokation (*11)
    end
    
  and wenn Änderung für ÜNB relevant
  
    MSB ->> ÜNB: Änderung vom MSB an ÜNB (*12)
    ÜNB ->> MSB: Rückmeldung auf Änderung (*13)
    
    opt wenn ÜNB anderen Inhalt erwartet
        MSB ->> ÜNB: Bearbeitungsstand zur Rückmeldung (*14)
    end
    
    opt wenn durch Änderung Übermittlung von Werten erforderlich wird 
        alt bei einer Übermittlung von Werten nach Typ 1
        MSB ->> MSB: ref Aufbereitung und Übermittlung von Werten vom MSB der Messlokation (*15)
        else
        MSB ->> MSB: ref Übermittlung von Werten nach Typ 2 vom MSB an NB oder LF (*16)
        end
    end
  end

```

*1 Prüfi: 55639, 55640, 55642, 55641, 55643, 55557
*2 Prüfi: 55644, 55645, 55647, 55646, 55648, 55559
*3 Prüfi: 21047
*4 Prüfi: 55649, 55650, 55652, 55651, 55653
*5 Prüfi: 55654, 55655, 55657, 55656, 55658
*6 Prüfi: 21047
*7 Prüfi: 13017, 13018
*8 Prüfi: 55659, 55660, 55662, 55661, 55663
*9 Prüfi: 55664, 55665, 55667, 55666, 55669
*10 Prüfi: 21047
*11 Prüfi: 13017, 13018
*12 Prüfi: 55684, 55686
*13 Prüfi: 55685, 55687
*14 Prüfi: 21047
*15 Prüfi: 13017, 13018
*16 Prüfi: 13027
