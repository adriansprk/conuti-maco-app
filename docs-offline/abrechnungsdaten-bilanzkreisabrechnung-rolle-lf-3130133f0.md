# Abrechnungsdaten Bilanzkreisabrechnung (Rolle LF)

```mermaid
sequenceDiagram
  autonumber
 
  participant LF as LF
  participant NB as NB
  participant ÜNB as ÜNB  
 
 par immer, gegenüber LF durchführen
  NB ->> LF: Abrechnungsdaten Bilanzkreisabrechnung vom NB an LF (*1)
  LF ->> NB : Rückmeldung auf Abrechnungsdaten (*2)
  
 opt wenn LF anderen Inhalt der Abrechnungsdaten erwaret
 NB->>LF: Bearbeitungsstand zur Rückmeldung (*3)
 end
 
 and wenn Abrechnungsaten für ÜNB relevant, gegenüber ÜNB durchführen
 
 NB->> ÜNB: Abrechnungsdaten Bilanzkreisabrechnung vom NB an ÜNB (*4)
 ÜNB->> NB: Rückmeldung auf Abrechnungsdaten (*5)
 
 opt wenn ÜNB anderen Inhalt der Abrechnungsdaten erwartet
 NB->> ÜNB: Bearbeitungstand zur Rückmeldung (*6)
 end
end 

opt wenn sich Daten ändern, die für Ersatzwertbildung benötigt werden, gegenüber MSB durchführen
    NB ->> NB: ref Stammdatenänderung vom NB (verantwortlich) ausgehend (*7)
end

opt wenn es sich um eine Bilanzierung auf Basis von Viertelstundnwerten handelt
    NB->> NB: ref Stammdaten zur Bilanzkreistreue (*8)
end
  
 
```

*1 Prüfi: 55126, 55672
*2 Prüfi: 55156, 55673
*3 Prüfi: 21047
*4 Prüfi: 55613, 55674
*5 Prüfi: 55614, 55675
*6 Prüfi: 21047
*7 Prüfi: 55627, 
*8 Prüfi: 55670, 55628, 55629, 55630, 55632, 55173
