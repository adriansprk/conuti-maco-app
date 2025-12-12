# Stammdatenänderung 55109 - Praktisches Beispiel

## Szenario: Adressänderung eines Kunden

**Anwendungsfall**: Ein Kunde hat umgezogen und die neue Adresse muss dem DSO (Netzbetreiber) gemeldet werden.

---

## 1. Trigger-Request (Outbound → Conuti API)

**Endpoint**: `POST https://api.macoapp.de/inbound`  
**Event**: `START_VERSAND_SDAE`  
**Prüfidentifikator**: `55109`

```json
{
  "stammdaten": {
    "MARKTLOKATION": [
      {
        "boTyp": "MARKTLOKATION",
        "versionStruktur": "1",
        "marktlokationsId": "50074561188",
        "sparte": "STROM",
        "datenqualitaet": "GUELTIGE_DATEN",
        "gueltigkeitszeitraum": {
          "zeitraumId": 1
        }
      }
    ],
    "ENERGIELIEFERVERTRAG": [
      {
        "boTyp": "VERTRAG",
        "versionStruktur": "1",
        "vertragsart": "ENERGIELIEFERVERTRAG",
        "sparte": "STROM",
        "lokationsId": "50074561188",
        "lokationsTyp": "MALO",
        "vertragspartner2": [
          {
            "boTyp": "GESCHAEFTSPARTNER",
            "versionStruktur": "1",
            "anrede": "Herr",
            "name1": "Schmidt",
            "name2": "Thomas",
            "geschaeftspartnerrolle": ["KUNDE"],
            "externeReferenzen": [
              {
                "exRefName": "Kundennummer beim Lieferanten",
                "exRefWert": "KUNDE-2024-12345"
              }
            ]
          }
        ],
        "korrespondenzpartner": {
          "boTyp": "GESCHAEFTSPARTNER",
          "versionStruktur": "1",
          "anrede": "Herr",
          "name1": "Schmidt",
          "name2": "Thomas",
          "partneradresse": {
            "strasse": "Musterstraße",
            "hausnummer": "42",
            "postleitzahl": "10115",
            "ort": "Berlin",
            "ortsteil": "Mitte",
            "landescode": "DE"
          }
        },
        "datenqualitaet": "GUELTIGE_DATEN",
        "gueltigkeitszeitraum": {
          "zeitraumId": 1
        }
      }
    ],
    "NETZNUTZUNGSVERTRAG": [
      {
        "boTyp": "VERTRAG",
        "versionStruktur": "1",
        "vertragsart": "NETZNUTZUNGSVERTRAG",
        "sparte": "STROM",
        "lokationsId": "50074561188",
        "lokationsTyp": "MALO",
        "vertragskonditionen": {
          "haushaltskunde": true
        }
      }
    ],
    "VERWENDUNGSZEITRAUM": [
      {
        "boTyp": "VERWENDUNGSZEITRAUM",
        "versionStruktur": "1",
        "zeitraumId": 1,
        "verwendungAb": "2024-12-01T00:00:00Z",
        "datenqualitaet": "GUELTIGE_DATEN"
      }
    ]
  },
  "transaktionsdaten": {
    "sparte": "STROM",
    "transaktionsgrund": "ZE6",
    "pruefidentifikator": "55109",
    "absender": {
      "boTyp": "MARKTTEILNEHMER",
      "versionStruktur": "1",
      "rollencodenummer": "9903790000002",
      "rollencodetyp": "BDEW",
      "ansprechpartner": {
        "boTyp": "ANSPRECHPARTNER",
        "versionStruktur": "1",
        "nachname": "Müller",
        "eMailAdresse": "support@lieferant.de"
      }
    },
    "empfaenger": {
      "boTyp": "MARKTTEILNEHMER",
      "versionStruktur": "1",
      "rollencodenummer": "9900321000005",
      "rollencodetyp": "BDEW"
    },
    "nachrichtendatum": "2024-11-15T10:30:00Z",
    "kategorie": "STAMMDATEN_MALO"
  },
  "zusatzdaten": {
    "prozessId": "55077-2024-11-15-001",
    "eventname": "START_VERSAND_SDAE"
  }
}
```

---

## 2. Weitere Beispiele für verschiedene Änderungen

### Beispiel 2: Änderung der Kundendaten (Name)

```json
{
  "stammdaten": {
    "MARKTLOKATION": [
      {
        "boTyp": "MARKTLOKATION",
        "versionStruktur": "1",
        "marktlokationsId": "50074561188",
        "sparte": "STROM",
        "datenqualitaet": "DIFFERENZ_DATEN"
      }
    ],
    "ENERGIELIEFERVERTRAG": [
      {
        "boTyp": "VERTRAG",
        "versionStruktur": "1",
        "vertragsart": "ENERGIELIEFERVERTRAG",
        "sparte": "STROM",
        "lokationsId": "50074561188",
        "lokationsTyp": "MALO",
        "vertragspartner2": [
          {
            "boTyp": "GESCHAEFTSPARTNER",
            "versionStruktur": "1",
            "anrede": "Frau",
            "name1": "Schmidt-Müller",
            "name2": "Anna",
            "geschaeftspartnerrolle": ["KUNDE"],
            "externeReferenzen": [
              {
                "exRefName": "Kundennummer beim Lieferanten",
                "exRefWert": "KUNDE-2024-12345"
              }
            ]
          }
        ],
        "datenqualitaet": "DIFFERENZ_DATEN"
      }
    ]
  },
  "transaktionsdaten": {
    "sparte": "STROM",
    "transaktionsgrund": "ZE6",
    "pruefidentifikator": "55109",
    "absender": {
      "rollencodenummer": "9903790000002",
      "rollencodetyp": "BDEW"
    },
    "empfaenger": {
      "rollencodenummer": "9900321000005",
      "rollencodetyp": "BDEW"
    },
    "nachrichtendatum": "2024-11-15T10:30:00Z",
    "kategorie": "STAMMDATEN_MALO"
  },
  "zusatzdaten": {
    "prozessId": "55077-2024-11-15-002",
    "eventname": "START_VERSAND_SDAE"
  }
}
```

### Beispiel 3: Änderung Haushaltskunde-Status

```json
{
  "stammdaten": {
    "MARKTLOKATION": [
      {
        "boTyp": "MARKTLOKATION",
        "versionStruktur": "1",
        "marktlokationsId": "50074561188",
        "sparte": "STROM",
        "datenqualitaet": "GUELTIGE_DATEN"
      }
    ],
    "NETZNUTZUNGSVERTRAG": [
      {
        "boTyp": "VERTRAG",
        "versionStruktur": "1",
        "vertragsart": "NETZNUTZUNGSVERTRAG",
        "sparte": "STROM",
        "lokationsId": "50074561188",
        "lokationsTyp": "MALO",
        "vertragskonditionen": {
          "haushaltskunde": false
        },
        "datenqualitaet": "DIFFERENZ_DATEN"
      }
    ]
  },
  "transaktionsdaten": {
    "sparte": "STROM",
    "transaktionsgrund": "ZE6",
    "pruefidentifikator": "55109",
    "absender": {
      "rollencodenummer": "9903790000002",
      "rollencodetyp": "BDEW"
    },
    "empfaenger": {
      "rollencodenummer": "9900321000005",
      "rollencodetyp": "BDEW"
    },
    "nachrichtendatum": "2024-11-15T10:30:00Z",
    "kategorie": "STAMMDATEN_MALO"
  },
  "zusatzdaten": {
    "prozessId": "55077-2024-11-15-003",
    "eventname": "START_VERSAND_SDAE"
  }
}
```

### Beispiel 4: EnFG-Daten (Erneuerbare-Energien-Gesetz)

```json
{
  "stammdaten": {
    "MARKTLOKATION": [
      {
        "boTyp": "MARKTLOKATION",
        "versionStruktur": "1",
        "marktlokationsId": "50074561188",
        "sparte": "STROM",
        "datenqualitaet": "GUELTIGE_DATEN"
      }
    ],
    "ENERGIELIEFERVERTRAG": [
      {
        "boTyp": "VERTRAG",
        "versionStruktur": "1",
        "vertragsart": "ENERGIELIEFERVERTRAG",
        "sparte": "STROM",
        "lokationsId": "50074561188",
        "lokationsTyp": "MALO",
        "enFG": [
          {
            "grundlageVerringerungUmlagen": "ERFUELLT_VORAUSSETZUNG_NACH_ENFG",
            "grund": [
              "ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN"
            ]
          }
        ],
        "datenqualitaet": "GUELTIGE_DATEN"
      }
    ]
  },
  "transaktionsdaten": {
    "sparte": "STROM",
    "transaktionsgrund": "ZE6",
    "pruefidentifikator": "55109",
    "absender": {
      "rollencodenummer": "9903790000002",
      "rollencodetyp": "BDEW"
    },
    "empfaenger": {
      "rollencodenummer": "9900321000005",
      "rollencodetyp": "BDEW"
    },
    "nachrichtendatum": "2024-11-15T10:30:00Z",
    "kategorie": "STAMMDATEN_MALO"
  },
  "zusatzdaten": {
    "prozessId": "55077-2024-11-15-004",
    "eventname": "START_VERSAND_SDAE"
  }
}
```

---

## 3. Wichtige Felder erklärt

### Datenqualität (`datenqualitaet`)
- `GUELTIGE_DATEN`: Neue/aktuelle Daten
- `DIFFERENZ_DATEN`: Geänderte Daten (wichtig für Änderungen!)
- `ERWARTETE_DATEN`: Erwartete Daten
- `KEINE_DATEN`: Keine Daten vorhanden

### Transaktionsgrund (`transaktionsgrund`)
- `ZE6`: Stammdatenänderung vom Lieferanten
- Weitere mögliche Werte je nach Kontext

### Kategorie (`kategorie`)
- `STAMMDATEN_MALO`: Stammdaten Marktlokation
- `STAMMDATEN_MELO`: Stammdaten Messlokation
- `STAMMDATEN_TRANCHE`: Stammdaten Tranche
- `AENDERUNG`: Allgemeine Änderung

### EnFG-Gründe (`enFG.grund`)
Mögliche Werte für Abweichungsgründe:
- `ENFG_ELEKTRISCH_ANGETRIEBENE_WAERMEPUMPEN`
- `ENFG_ERNEUERBARE_ENERGIEN_GESETZ`
- Weitere EnFG-spezifische Gründe

---

## 4. Erwartete Antworten vom DSO

Nach dem Versand der Stammdatenänderung können folgende Antworten eintreffen:

### Erfolg (55110)
```json
{
  "pruefidentifikator": "55110",
  "transaktionsdaten": {
    "vorgangsnummer": "55077-2024-11-15-001"
  }
}
```

### Ablehnung (55111)
```json
{
  "pruefidentifikator": "55111",
  "transaktionsdaten": {
    "vorgangsnummer": "55077-2024-11-15-001",
    "freitext": "Ablehnungsgrund..."
  }
}
```

---

## 5. Backend-Implementierung

### Schritt 1: Trigger-Request senden
```python
import requests

def send_stammdatenaenderung(marktlokations_id, aenderungen):
    """
    Sendet Stammdatenänderung an DSO
    
    Args:
        marktlokations_id: ID der Marktlokation
        aenderungen: Dict mit geänderten Daten
    """
    payload = {
        "stammdaten": {
            "MARKTLOKATION": [{
                "boTyp": "MARKTLOKATION",
                "versionStruktur": "1",
                "marktlokationsId": marktlokations_id,
                "sparte": "STROM",
                "datenqualitaet": "DIFFERENZ_DATEN"
            }],
            "ENERGIELIEFERVERTRAG": [{
                "boTyp": "VERTRAG",
                "versionStruktur": "1",
                "vertragsart": "ENERGIELIEFERVERTRAG",
                "sparte": "STROM",
                "lokationsId": marktlokations_id,
                "lokationsTyp": "MALO",
                **aenderungen
            }]
        },
        "transaktionsdaten": {
            "sparte": "STROM",
            "transaktionsgrund": "ZE6",
            "pruefidentifikator": "55109",
            "absender": {
                "rollencodenummer": "9903790000002",
                "rollencodetyp": "BDEW"
            },
            "empfaenger": {
                "rollencodenummer": "9900321000005",
                "rollencodetyp": "BDEW"
            },
            "nachrichtendatum": "2024-11-15T10:30:00Z",
            "kategorie": "STAMMDATEN_MALO"
        },
        "zusatzdaten": {
            "prozessId": f"55109-{marktlokations_id}-{timestamp}",
            "eventname": "START_VERSAND_SDAE"
        }
    }
    
    response = requests.post(
        "https://api.macoapp.de/inbound",
        json=payload,
        headers={"Authorization": "Bearer YOUR_TOKEN"}
    )
    return response.json()
```

### Schritt 2: Webhook-Handler für Antworten
```python
@app.post("/webhook/stammdatenaenderung")
def handle_stammdatenaenderung_response(data: dict):
    """
    Empfängt Antworten vom DSO (55110, 55111)
    """
    pruefi = data.get("transaktionsdaten", {}).get("pruefidentifikator")
    prozess_id = data.get("zusatzdaten", {}).get("prozessId")
    
    if pruefi == "55110":
        # Erfolg - Stammdatenänderung akzeptiert
        update_process_status(prozess_id, "SUCCESS")
    elif pruefi == "55111":
        # Ablehnung - Stammdatenänderung abgelehnt
        freitext = data.get("transaktionsdaten", {}).get("freitext", "")
        update_process_status(prozess_id, "REJECTED", reason=freitext)
    
    return {"status": "ok"}
```

---

## 6. Checkliste für die Implementierung

- [ ] Marktlokations-ID vorhanden
- [ ] Geänderte Daten identifiziert
- [ ] `datenqualitaet` auf `DIFFERENZ_DATEN` gesetzt (bei Änderungen)
- [ ] `pruefidentifikator` = `55109` gesetzt
- [ ] `eventname` = `START_VERSAND_SDAE` gesetzt
- [ ] Eindeutige `prozessId` generiert
- [ ] Webhook-Handler für Antworten (55110/55111) implementiert
- [ ] Prozessdaten im Backend gespeichert

---

## 7. Häufige Fehler vermeiden

1. **Falsche Datenqualität**: Bei Änderungen `DIFFERENZ_DATEN` verwenden, nicht `GUELTIGE_DATEN`
2. **Fehlende Marktlokations-ID**: Immer `marktlokationsId` angeben
3. **Falscher Prüfidentifikator**: Muss `55109` sein für LF → NB
4. **Fehlende Prozess-ID**: `prozessId` ist erforderlich für die Zuordnung der Antwort
5. **Falsche Rollencodetypen**: Absender = LF, Empfänger = NB (beide BDEW)

---

## Weitere Informationen

- **Schema**: `maco-api-documentation/macoapp-schreiben/components/requestBodies/PIs/PI_55109.yml`
- **Dokumentation**: `docs-offline/stammdatenänderung-vom-lieferanten-verantwortlich-15239974e0.md`
- **Trigger-Schema**: `maco-api-documentation/_build/macoapp-trigger.min.json` → `START_VERSAND_SDAE`
