# Lieferende NB -> LF (Rolle LF)

```mermaid
sequenceDiagram
  autonumber
  
  participant LF as LF
  participant NB as NB
  participant LFZ as LFZ
  participant MSB as MSB
  participant MSBZ as MSBZ
  

opt wenn es sich nicht um eine Stilllegung einer Marktlokation handelt oder wenn im Fall der Stilllegung einer Marktlokation die Zuordnung des LF zur Marktlokation bzw. Tranche nicht bereits zum Zuordnungsende beendet wurde

NB ->> LF: Ankündigung der Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche (*1)
LF ->> NB: Antwort auf Ankündigung der Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche (*2)

    opt wenn Antwort auf Ankündigung der Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche nicht fristgerecht eingeht
    NB ->> LF: Beendigung der Zuordnung des LF zur Marktlokation bzw. Tranche aufgrund fehlender Antwort (*3)
    end
    
    
opt bei Beendigung der Zuordnung des LF (Durchführung unverzüglich)
    
    opt bei einer verbrauchenden Marktlokation und wenn mit dem LF vereinbart wurde, dass die Netznutzungsabrechnung über diesen abgewickelt wird
    NB ->> NB: ref Abrechnungsdaten Netznutzungsabrechnung (*4)
    end
    
NB ->> NB: ref Abrechnungsdaten Bilanzkreisabrechnung (*5)
end

opt bei Beendigung der Zuordnung des LF (Durchführung abhängig vom Zuordnungsende)

    opt bei einer verbrauchenden Marklokation und E/G erforderlich
    NB ->> NB: ref Beginn der Ersatz- /Grundversorgung (*6)
    end
    
    opt bei einer erzeugenden Marktlikation bzw. einer Tranche und wenn eine 100% LF-Zuordnung hergestellt werden muss
    NB ->> NB: ref Herstellung einer 100% LF-Zuordnung zu einer erzeugenden Marktlokation (*7)
    end
end

opt im Fall der Stilllegung einer Marktlokation

    par gegenüber LFZ durchführen
    NB ->> LFZ: Aufhebung der Zuordnung des LFZ zur Marktlokation bzw. Tranche (*8)
    
        opt bei einer verbrauchenden Marktlokation und wenn mit dem LFZ vereinbart wurde, dass die Netznutzungsabrechnung über diesen abgewickelt wird
        NB ->> NB: ref Abrechnungsdaten Netznutzungsabrechung (*9)
        end
        
    NB ->> NB: ref Abrechnungsdaten Bilanzkreisabrechnung (*10)
    
    and gegenüber MSB durchführen
    
    NB ->> MSB: Beendigung der Zuordnung des MSB zur Marktlokation bzw. Messlokation (*11)
    MSB ->> MSB: ref Aufbereitung und Übermittlung von Werten vom MSB der Messlokation (*12)
    
    and gegenüber MSBZ durchführen
    
    NB ->> MSBZ: Aufhebung der Zuordnung des MSBZ zur Marktlokation bzw. Messlokation (*13)
    
    and wenn das Lokationsbündel nicht stillgelegt wird, gegenüber den Marktpartnern der weiterhin aktiven Lokationen durchführen, wenn nicht bereits druchgeführt
    
    NB ->> NB: ref Stammdatenänderung vom NB (verantwortlich) ausgehend (*1)
    
    end
end

end

    
```

*1 Prüfi: 55007
*2 Prüfi: 55008, 55009
*3 Prüfi: 55037
*4 Prüfi: 55218
*5 Prüfi: 55126
*6 Prüfi: 55013
*7 Prüfi: 55607
*8 Prüfi: 55038
*9 Prüfi: 55218
*10 Prüfi: 55126
*11 Prüfi: 55611
*12 Prüfi: 13017, 13018
*13 Prüfi: 55611
*8 Prüfi: 55615, 55627, 55616, 55628, 55619, 55617, 55629, 55618, 55630, 55620, 55632, 55225, 55175, 55173
