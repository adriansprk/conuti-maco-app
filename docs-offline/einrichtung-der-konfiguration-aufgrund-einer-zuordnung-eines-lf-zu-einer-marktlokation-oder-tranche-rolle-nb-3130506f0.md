# Einrichtung der Konfiguration aufgrund einer Zuordnung eines LF zu einer Marktlokation oder Tranche (Rolle NB)

```mermaid
sequenceDiagram
  autonumber
  
  
  participant NB as NB
  participant MSB as MSB
  participant weiterer MSB as weiterer MSB
  
 
 NB ->> MSB : Einrichtung der Konfigurationen (*1)
   
 opt wenn weiterer MSB betroffen
     MSB ->> weiterer MSB : Einrichtung der Konfigurationen (*2)
     
     alt wenn durch Einrichtung der Konfigurationen Stammdatenänderung erforderlich wird
     
         weiterer MSB ->> weiterer MSB : ref Stammdatenänderung vom MSB (verantwortlich) ausgehend (*3)
     else 
     
         weiterer MSB ->> weiterer MSB : ref Aufbereitung und Übermittlung von Werten vom MSB der Messlokation (*4)
     end
 end
 
 alt wenn durch Einrichtung der Konfigurationen Stammdatenänderung erforderlich wird
     
     MSB ->> MSB : ref Stammdatenänderung vom MSB (verantwortlich) ausgehend (*5)
     
     else
     
     MSB ->> MSB : ref Aufbereitung und Übermittlung von Werten vom MSB der Messlokation (*6)
 end
 
```

*1 Prüfi: 17134
*2 Prüfi: 17135
*3 Prüfi: 55659, 55553, 55660, 55661, 55662, 55663, 
*4 Prüfi: 13017, 13018
*5 Prüfi: 55557, 55553, 55639, 55640, 55641, 55642, 55643, 55653
*6 Prüfi: 21047
*7 Prüfi: 13017, 13018

