# Malo-Ident (Rolle NB)


```mermaid
sequenceDiagram
autonumber
  participant NB as NB
  participant LF as LF
  
  LF ->> NB: Anfrage MaLo-ID der Marktlokation (/maloId/request/v1)
  alt
  NB ->> LF: neg Rückmeldung auf Anfrage (/maloId/dataForMarketLocationNegative/v1)
  else
  NB ->> LF: pos Rückmeldung auf Anfrage (/maloId/dataForMarketLocationPositive/v1)
  end

```


