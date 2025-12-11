# Anfrage nach Stornierung

```mermaid
sequenceDiagram
autonumber

  participant MSB
  participant Beteiligte aus Ursprungsnachricht
 
  MSB ->> Beteiligte aus Ursprungsnachricht: Anfrage nach Stornierung (*1)
  
  Beteiligte aus Ursprungsnachricht ->> MSB: Antwort auf Stornierung (*2)
  
```

*1 Prüfi: 55022
*2 Prüfi: 55023, 55024
