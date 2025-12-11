# Konzeption Umsetzung Ermittlung SAP

## **Primäre Trefferkriterien**
### 1.a [vollständige Adressprüfung]
-           Die zu prüfende Adresse der Marktlokation besteht aus **Straße, Hausnummer/Hausnummernergänzung, PLZ, Ort und Ländercode**.
-          Bei Marktlokationen ohne zugeordnete Adressdaten kann zudem über das Tupel bestehend aus **Gemarkung, Flurnummer und Flurstücknummer** identifiziert werden.
-          Es kann auch eine Identifizierung über **geographische Koordinaten** erfolgen.
Bei der Adressprüfung gelten die folgenden Regeln:
-          Die Zeichenketten „straße“, „str.“ oder „strasse“ am Ende eines Straßennamens werden durch einen Stern „*“ ersetzt, um damit alle Straßen zu finden, deren Name mit den links vom Stern stehenden Buchstaben beginnen. Der Stern gilt somit als Platzhalter.

![Pic1.png](https://api.apidog.com/api/v1/projects/816353/resources/352717/image-preview)

-          Diakritische Zeichen sind zu ignorieren.
          
![Pic2.png](https://api.apidog.com/api/v1/projects/816353/resources/352718/image-preview)
-           Interpunktionszeichen sind zu ignorieren, indem die Adressen interpretiert werden, als wären diese Zeichen nicht vorhanden
          
![Pic3.png](https://api.apidog.com/api/v1/projects/816353/resources/352719/image-preview)
          
-           Leerzeichen sind zu ignorieren.
-           Groß- und Kleinschreibung sind zu ignorieren.
          
#### SAP-Prüfungslogik
          Suche alle Anschlußobjekte mit Strasse und PLZ  Selektion aller MaLo-ID, die diesen zugeordnet sind 
          
### 1.b [Adressprüfung]
-           Die zu prüfende Adresse der Marktlokation besteht aus Straße und PLZ.
-           Bei Marktlokationen ohne zugeordnete Adressdaten kann zudem über das Flurstücknummer identifiziert werden.
-           Es kann auch eine Identifizierung über geographische Koordinaten erfolgen.

Bei der Adressprüfung gelten die gleichen Regeln wie in [1a](#1a-vollständige-adressprüfung)

### 2.a [vollständige Namensprüfung]
Der zu prüfende Name besteht bei **natürlichen Personen aus dem Vor- und Nachnamen**. Bei **juristischen Personen aus dem Namen der Firma**.
Mindestens folgende Gegebenheiten sollten abgefangen werden:
-           Identifikation durch Vertauschen von Vor- und Nachnamen
-           Identifikation aus dem String "Vor- und Nachname" gegen jeweils Vor- und Nachname in beide Richtungen (z.B. für Kunden, die im Vor- und Nachnamen jeweils einen kompletten Namen eingetragen haben (Wohngemeinschaften))
-           Angabe der Firmenbezeichnung wird gegen Vor- und Nachnamen sowie dem kompletten String aus "Vor- und Nachname" verglichen.
Bei der Namensprüfung gelten die folgenden Regeln:

![Pic4.png](https://api.apidog.com/api/v1/projects/816353/resources/352720/image-preview)
- Diakritische Zeichen sind zu ignorieren
          
### 2.b [Namensprüfung]
Der zu prüfende Name besteht bei **natürlichen Personen Nachnamen**. Bei **juristischen Personen aus dem Namen der Firma**.
Es gelten alle weiteren Gegebenheiten und Prüfungen der vollständigen Namensprüfung ( vgl. [2a](#2a-vollständige-namensprüfung) )
          
### 3. [Gerätenummernprüfung]
Die Prüfung ist für jede angegebene Gerätenummer durchzuführen. 
Es sind alle Geräte vom Typ kME, mME und Smart-Meter-Gateways mit der übergebenen Gerätenummer zu suchen. 
Dabei sind führende Nullen gemäß der Beschreibung im Dokument Allgemeine Festlegungen zu ignorieren. 
Zusätzlich sind schließende Nullen ebenfalls zu ignorieren. 
Eine Identifizierung soll auch erfolgen, wenn ein Marktpartner einen Zähler/Gateway sendet, der bereits im Rahmen eines Gerätewechsels innerhalb der letzten 36 Monate ausgetauscht wurde (Ausnahme Netzbetreiberwechsel).
Die Übereinstimmung einer Gerätenummer liegt vor, wenn alle Zeichen in genannter Reihenfolge mit der aufgebrachten Nummer auf dem Gerät identisch sind. 
Gegebenenfalls im System vorhandene Prä- und Suffixe sind zu ignorieren.

#### SAP-Prüfungslogik
Suche über EGERR ( GERAET ) nach alle EQUNR -> ETDZ nach allen LOGIKZW -> EASTL nach allen ANLAGE -> EUIINSTLN -> EUITRANS (UISTRUTYP = „MA“ ) 
&
Suche über EQUI ( SERGE evtl. GERNR ) nach alle EQUNR -> ETDZ nach allen LOGIKZW -> EASTL nach allen ANLAGE -> EUIINSTLN -> EUITRANS (UISTRUTYP = „MA“ ) 

### 4. [MaLo-ID-Prüfung]
Die Übereinstimmung der MaLo-ID liegt vor, wenn die vollständige, 11-stellige Zeichenkette übereinstimmt.

#### SAP-Prüfungslogik
Lesen aller Malo-IDs über EUITRANS ( UISTRUTYP = „MA“ ) INNERJOIN  EUIINSTLN INNERJOIN EANL ( ANLART < > „TRAN“ ) zum Selektionsdatum.

### 5. [MeLo-ID-Prüfung]
Die Prüfung ist für jede angegebene MeLo-ID durchzuführen. Die Übereinstimmung der MeLo-ID liegt vor, wenn die vollständige 33-stellige Zeichenkette übereinstimmt.
#### SAP-Prüfungslogik
Lesen aller Malo-IDs über EUITRANS ( UISTRUTYP = „ME“ ) INNERJOIN  EUIINSTLN zum Selektionsdatum 
### 6. [Tranchen-ID-Prüfung]
Die Prüfung ist für jede angegebene Tranchen-ID durchzuführen. Die Übereinstimmung der Tranchen-ID liegt vor, wenn die vollständige 11-stellige Zeichenkette übereinstimmt.
#### SAP-Prüfungslogik
Lesen aller Malo-IDs über EUITRANS ( UISTRUTYP = „MA“ ) INNERJOIN  EUIINSTLN INNERJOIN EANL ( ANLART = „TRAN“ ) zum Selektionsdatum 

### 7. [Kundennummer-Prüfung]
Übermittelt wird die Kundennummer des LFA. Die Übereinstimmung der Kundennummer liegt vor, wenn die Zeichenkette der Kundennummer, wie sie dem Kunden mitgeteilt wurde übereinstimmt.
#### SAP-Prüfungslogik
Klärung, wo diese Nummer liegt, danach Selektion über GP -> EVER ( Feld Anlage ) -> EUIINSTLN -> EUITRANS (EXT_UI bei UISTRUTYP = „MA“) 

## Sekundäre Trefferkriterien
### 8. [Vollständige Adress-Prüfung] 
Ermittlung, ob ermittelte Malo alle Adressidentifizierungsparameter erfüllt ( vgl. [1b. primäre Trefferkriterien](#1b-adressprüfung) )

### 9. [Vollständige Namen-Prüfung] 
Ermittlung, ob ermittelte Malo alle Namensidentifizierungsparameter erfüllt ( vgl. [2b. primäre Trefferkriterien](#2b-namensprüfung) )


### 10. [nimmt an Mako teil]
Ermittlung, ob ermittelte Malo an der Mako teilnimmt

### 11. [stillgelegt]
Ermittlung, ob ermittelte Malo stillgelegt ist.

### 12. [eigenes Netzgebiet]
Ermittlung, ob ermittelte Malo zum Selektionszeitpunkt einem Netz zugeordnet ist, welches durch eine Serviceanbieter mit Kennzeichen „eigener Service“ versorgt wird.

### 13. [eigenes Netzgebiet < 3 KJ]
Ermittlung, ob ermittelte Malo zum innerhalb der letzten 3 KJ einem Netz zugeordnet ist oder war, welches durch eine Serviceanbieter mit Kennzeichen „eigener Service“ versorgt wird.

## Rückgabestruktur (Beispiel)

![Pic5.png](https://api.apidog.com/api/v1/projects/816353/resources/352721/image-preview)

```json
{
  "maloIdentDaten": [
    {
      "lokationsId": "74018657187",
      "trefferMaloid": true,
      "trefferTrancheId": false,
      "trefferAdresse1": true,
      "trefferKundennummer": false,
      "trefferName": false,
      "trefferGeraetenummer": false,
      "trefferMeloid": false,
      "trefferAdresse2": true,
      "trefferMakorelevant": true,
      "trefferStillgelegt": false,
      "trefferNetzgebiet": true,
      "trefferNetzgebiet3KJ": true
    }
  ]
}
```
