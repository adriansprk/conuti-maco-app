# Lieferbeginn (Rolle NB)


```mermaid
sequenceDiagram
  autonumber
  
  participant NB as NB
  participant LFN as LFN
  participant LFZ as LFZ
  participant LFA as LFA
  
  LFN ->> NB: Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche (*1)

  opt wenn Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche erforderlich
  
    NB ->> LFN : Information über existierende Zuordnung (*2)

    NB ->> LFA : Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche (*3)

    LFA ->> NB : Antwort auf Anfrage zur Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche (*4)    
  end

  alt wenn Voraussetzungen erfüllt sind
  
  NB ->> LFN : Zuordnung des LFN zur Marktlokation bzw. Tranche (*5)
  
  else
  
      NB ->> LFN : Ablehnung der Anmeldung einer Zuordnung des LFN zur Marktlokation bzw. Tranche (*6) 
  end
  
  opt bei Zuordnung des LFN (Durchführung unverzüglich)
  
      par immer, gegeüber LFN durchführen
      
          opt bei einer verbrauchenden Marktlokation
          
              NB ->> NB: ref Abrechnungsdaten Netznutzungsabrechnung (*7)
          end
          
          NB ->> NB : ref Abrechnungsdaten Bilanzkreisabrechnung (*8)
          NB ->> NB : ref Stammdatenänderung vom NB (verantwortlich) ausgehend (*9)
          
          and wenn Anfrage zur Beendiung der Zuordnung des LFA zur Marktlokation bzw. Tranche versandt wurde, gegeüber LFA durchführen  
          
          NB ->> LFA : Beendigung der Zuordnung des LFA zur Marktlokation bzw. Tranche (*10)
          
          opt bei einer verbrauchenden Marktlokation und wenn mit dem LFA vereinbart wurde, dass die Netznutzungsabrechnung über diesen abgewickelt wird
          
          NB ->> NB : ref Abrechnungsdaten Netznutzungsabrechnung (*11)
          
          end
          
          NB ->> NB : ref Abrechnungsdaten Bilanzkreisabrechnung (*12)
          
          and wenn Zuordnungszeitraum des LFN zeitlich über Zuordnungsbeginn des LFZ andauert (überholende Zuordnung), gegenüber LFZ durchführen
          
          NB ->> LFZ : Aufhebung der Zuordnung des LFZ zur Marktlokation bzw. Tranche (*13)
          
          opt bei einer verbrauchenden Marktlokation und wenn mit dem LFZ vereinbart wurde, dass die Netznutzungsabrechnung über diesen abgewickelt wird
          
              NB ->> NB : ref Abrechnungsdaten Netznutzungsabrechnung (*14)
              
          end
          
          NB ->> NB : ref Abrechnungsdaten Bilanzkreisabrechnung (*15)
          
          end
  end
  
  opt bei Zuordnung des LFN (Durchführung abhängig vom Zuordnungsbeginn) 
  
      NB ->> NB : ref Übermittlung der Berechnungsformel (*16)
      
      NB ->> NB : ref Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche (*17)
      
      opt bei einer verbrauchenden Marktlokation
      
      opt wenn E/G erforderlich
      
          NB ->> NB : ref Beginn der Ersatz- /Grundversorgung (*18)
          
      end
      
      opt bei einer gesperrten Marktlokation 
          
          NB ->> NB : ref Wiederherstellung der Anschlussnutzung bei Lieferbeginn (*19)
      end
      end
      
      opt bei einer erzeugenden Marktlokation bzw. einer Tranche und wenn eine 100% LF-Zuordnung hergestellt werden muss
      
          NB ->> NB : ref Herstellung einer 100 % LF-Zuordnung zu einer erzeugenden Marktlokation (*20)
      end
  end  
  

```

*1 Prüfi: 55001
*2 Prüfi: 55036
*3 Prüfi: 55010
*4 Prüfi: 55011
*5 Prüfi: 55002
*6 Prüfi: 55003
*7 Prüfi: 55218
*8 Prüfi: 55126
*9 Prüfi: 55615, 55620, 55175, 55225, 55616, 55617, 55618, 55619, 55691
*10 Prüfi: 55037
*11 Prüfi: 55218
*12 Prüfi: 55126
*13 Prüfi: 55038
*14 Prüfi: 55218
*15 Prüfi: 55126
*16 Prüfi: 25001
*17 Prüfi: 17134
*18 Prüfi: 55013
*19 Prüfi: 21040, 21039
*20 Prüfi: 55607
