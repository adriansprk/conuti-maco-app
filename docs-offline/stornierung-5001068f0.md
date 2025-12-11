# Anfrage nach Stornierung

```mermaid
sequenceDiagram
autonumber

  participant NB
  participant Beteiligte aus Ursprungsnachricht
 
  NB ->> Beteiligte aus Ursprungsnachricht: Anfrage nach Stornierung (*1)
  
  Beteiligte aus Ursprungsnachricht ->> NB: Antwort auf Stornierung (*2)
  
```

*1 Prüfi: 55022
*2 Prüfi: 55023, 55024
