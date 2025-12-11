# Beginn der Ersatz-/Grundversorgung (Rolle NB)

```mermaid
sequenceDiagram
  autonumber
  
  participant NB as NB
  participant LF as LF
   
    
NB ->> LF : Ankündigung der Zuordnung des E/G zur Marktlokation (*1)
LF ->> NB : Antwort auf Ankündigung der Zuordnung des E/G zur Marktlokation (*2)

opt wenn Antwort auf Ankündigung der Zuordnung des E/G zur Marktlokation nicht fristgerecht eingeht

    NB ->> LF : Zuordnung des E/G zur Marktlokation aufgrund fehlender Antwort (*3)
    
end

opt bei Zuordnung des E/G

    NB ->> NB : ref Übermittlung der Berechnungsformel (*4)
    
    NB ->> NB : ref Abrechnungsdaten Netznutzungsabrechnung (*5)
    
    NB ->> NB : ref Abrechnungsdaten Bilanzkreisabrechnung (*6)
    
    NB ->> NB : ref Stammdatenänderung vom NB (verantwortlich) ausgehend (*7)
    
    NB ->> NB : ref Einrichtung der Konfigurationen aufgrund einer Zuordnung eines LF zu einer Marktlokation bzw. Tranche (*8)
    
end

    
```

*1 Prüfi: 55013
*2 Prüfi: 55014, 55015
*3 Prüfi: 55013
*4 Prüfi: 25001
*5 Prüfi: 55218
*6 Prüfi: 55126
*7 Prüfi: 55615, 55620, 55175, 55225, 55616, 55617, 55618, 55619, 55691
*8 Prüfi: 17134

