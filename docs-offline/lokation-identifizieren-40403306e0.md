# Lokation identifizieren

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /identifyLocation:
    post:
      summary: Lokation identifizieren
      deprecated: false
      description: >+
        Identifiziert zu einem definierten Stichtag **alle** zugehörigen
        **Marktlokationen (MaLo)**

        bzw. **Messlokationen (MeLo)** anhand übergebener
        Identifikationsmerkmale.


        ### Fachlicher Zweck


        Der Aufrufer kennt die gesuchten Lokationen nicht (oder nicht sicher)
        über ihre ID, sondern

        nur über andere Merkmale — z. B. eine Adresse, eine Zählernummer oder
        eine Kundenreferenz.

        Die Methode löst diese Merkmale im Backend gegen den Datenbestand auf
        und liefert die

        zugeordneten Lokationen im gewünschten Lokationstyp zurück.


        Da die übergebenen Merkmale fachlich nicht zwingend eindeutig sind (eine
        Lokationsadresse

        kann z. B. für ein ganzes Gebäude mehrere Messlokationen umfassen),
        liefert die Methode

        grundsätzlich eine **Trefferliste**. Eine Treffermenge größer 1 ist ein
        reguläres fachliches

        Ergebnis und kein Fehlerfall.x


        ### Identifikationsmerkmale (`stammdaten`)


        Es kann ein einzelnes Merkmal oder eine beliebige Kombination übergeben
        werden. Alle

        übergebenen Merkmale werden UND-verknüpft ausgewertet — je mehr Merkmale
        gesetzt sind,

        desto stärker wird die Treffermenge eingegrenzt:


        | Container | Merkmale |

        |---|---|

        | `MARKTLOKATION` | Marktlokations-ID, Energierichtung,
        Lokationsadresse, Katasterinformation, Geokoordinaten |

        | `MESSLOKATION` | Messlokations-ID, Messadresse |

        | `TRANCHE` | Tranchen-ID |

        | `ZAEHLER` | Zählernummer |

        | `ENERGIELIEFERVERTRAG` | Vertragsart, Vertragspartner inkl. externer
        Referenzen (Kunden-/Vertragskontonummern) |

        | `NETZNUTZUNGSVERTRAG` | Vertragsart, Sparte, Vertragszeitraum,
        Vertragskonditionen |


        Identifikationsmerkmal und gewünschter Rückgabetyp sind unabhängig
        voneinander: So können

        über eine Zählernummer die zugehörigen Marktlokationen oder über eine
        Marktlokations-ID die

        zugehörigen Messlokationen ermittelt werden.


        ### Zeitlicher Bezug (`transaktionsdaten.ausfuehrungsdatum`)


        Die Identifikation erfolgt **stichtagsbezogen**: Ausgewertet wird
        ausschließlich der

        Datenstand, der zum angegebenen Zeitpunkt gültig ist. Anfragen mit
        identischen Merkmalen,

        aber unterschiedlichem Ausführungsdatum können daher bewusst zu
        unterschiedlichen

        Ergebnissen führen (z. B. nach Gerätewechsel, Adressänderung oder
        Lieferantenwechsel).


        Der Zeitpunkt wird in UTC übergeben und muss umgerechnet einem
        Tagesbeginn (00:00 Uhr)

        gesetzlicher deutscher Zeit entsprechen.


        ### Steuerung des Ergebnisses (`zusatzdaten`)


        | Feld | Pflicht | Wertebereich | Default | Bedeutung |

        |---|---|---|---|---|

        | `lokationsTyp` | ja | `MALO` \| `MELO` | — | Typ der zurückzugebenden
        Lokationen — `MALO` → Marktlokationen, `MELO` → Messlokationen |


        Die Mengensteuerung liegt **nicht** im Body, sondern in HTTP-Headern
        (siehe nächster

        Abschnitt). Der Body transportiert ausschließlich Fachdaten.


        ### Begrenzung und Blättern (HTTP-Header)


        Die Schnittstelle ist so ausgelegt, dass sie **im Normalfall ohne
        Paginierung auskommt**:

        Ohne die beiden Anfrage-Header wird die vollständige Treffermenge einer
        üblichen

        Identifikationsanfrage in einem einzigen Aufruf beantwortet. Blättern
        ist der Ausnahmefall

        für ungewöhnlich unscharfe Anfragen — nicht der Regelweg.


        **Anfrage-Header** (beide optional):


        | Header | Wertebereich | Default | Bedeutung |

        |---|---|---|---|

        | `Treffer-Max-Anzahl` | 1 … 500 | 20 | Maximale Anzahl der in einer
        Antwort gelieferten Lokationen (Seitengröße) |

        | `Treffer-Offset` | 0 … 10000 | 0 | Anzahl der zu überspringenden
        Treffer — nur für das Nachladen weiterer Seiten |


        **Antwort-Header** (immer gesetzt):


        | Header | Bedeutung |

        |---|---|

        | `Treffer-Offset` | Der tatsächlich angewendete Versatz (Echo des
        Requests bzw. `0`) |

        | `Treffer-Anzahl` | Anzahl der in **dieser Antwort** gelieferten
        Lokationen (= Länge des Arrays) |

        | `Treffer-Gesamtanzahl` | Anzahl **aller** zum Stichtag passenden
        Lokationen, unabhängig von Offset und Seitengröße |

        | `Treffer-Weitere-Vorhanden` | `true`, wenn hinter dieser Seite weitere
        Treffer liegen (`Treffer-Offset + Treffer-Anzahl <
        Treffer-Gesamtanzahl`) |


        - **Seitengröße:** `Treffer-Max-Anzahl` begrenzt die Anzahl gelieferter
        Lokationen. Der
          Default von 20 deckt eindeutige und nahezu eindeutige Anfragen (Zählernummer,
          Kundenreferenz, vollständige Adresse) vollständig ab; eine Kürzung tritt bei unscharfen
          Merkmalen auf, etwa einer Adresse ohne Hausnummer oder einem Mehrfamilienhaus.
        - **Harter Server-Cap:** Der Maximalwert von **500** ist serverseitig
        festgelegt und kann
          vom Aufrufer nicht überschritten werden. Werte außerhalb der zulässigen Bereiche sowie
          nicht-numerische Header-Werte werden mit `400 Bad Request` abgelehnt — sie werden
          **nicht** stillschweigend auf den Cap gekappt.
        - **Versatz:** `Treffer-Offset` überspringt die ersten n Treffer der
        sortierten
          Gesamtmenge. Die nächste Seite wird angefordert mit
          `Treffer-Offset_neu = Treffer-Offset + Treffer-Anzahl`. `0` entspricht dem Weglassen des
          Headers.
        - **Immer `200 OK`:** Auch die gekürzte Antwort wird mit 200
        beantwortet, nicht mit
          `206 Partial Content`. `Range`/`Content-Range` kommen bewusst nicht zum Einsatz:
          Range-Handling ist laut RFC 9110 ausschließlich für `GET` definiert und muss bei `POST`
          ignoriert werden.
        - **Deterministische Sortierung:** Die Gesamtmenge wird vor dem Anwenden
        von Offset und
          Seitengröße stabil aufsteigend nach der Lokations-ID sortiert. Nur dadurch sind Seiten
          überschneidungs- und lückenfrei.
        - **Kein Snapshot:** Es gibt keinen Cursor und keine serverseitige
        Ergebniskonservierung.
          Seiten sind konsistent, solange sich der zum Stichtag gültige Datenbestand zwischen den
          Aufrufen nicht ändert. Bei sehr großen Treffermengen ist die fachlich bessere Reaktion,
          die Identifikationsmerkmale zu verfeinern, statt über viele Seiten zu blättern.


        ### Ergebnis


        Der Antwort-Body ist ein **flaches Array auf Root-Ebene** mit 0 … n
        ermittelten

        Lokationen — kein umgebender Container. Die Einträge entsprechen
        unverändert dem

        bisherigen Einzelergebnis (Marktlokation bzw. Messlokation, gesteuert
        über

        `lokationsTyp`); eine Gruppierung nach Containertypen wie im Request
        gibt es nicht.

        Sämtliche Metadaten liegen in den Antwort-Headern.


        ```http

        HTTP/1.1 200 OK

        Content-Type: application/json

        Treffer-Offset: 0

        Treffer-Anzahl: 2

        Treffer-Gesamtanzahl: 2

        Treffer-Weitere-Vorhanden: false


        [
          { "boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50754496000" },
          { "boTyp": "MARKTLOKATION", "versionStruktur": "1", "marktlokationsId": "50754497001" }
        ]

        ```


        Fallunterscheidung:


        - **Kein Treffer** → leeres Array `[]`, `Treffer-Anzahl: 0`,
          `Treffer-Gesamtanzahl: 0`, `Treffer-Weitere-Vorhanden: false`. Dies ist ein gültiges
          fachliches Ergebnis und keine technische Störung (kein Fehler-Response, HTTP 200).
        - **Genau ein Treffer** → Array mit einem Element. Es gibt keinen
        abweichenden Sonderfall
          für die eindeutige Zuordnung.
        - **Mehrere Treffer** → alle passenden Lokationen bis zur Seitengröße.
        Mehrdeutigkeit führt
          ausdrücklich **nicht** mehr zu einem leeren Ergebnis; die Auflösung obliegt dem Aufrufer.
        - **Weitere Seiten vorhanden** → `Treffer-Weitere-Vorhanden: true`. Der
        Aufrufer kann die
          Merkmale verfeinern oder die Folgeseite mit
          `Treffer-Offset = Treffer-Offset + Treffer-Anzahl` abrufen. Auch dies ist kein
          Fehler-Response.
        - **`Treffer-Offset` hinter dem Ende der Treffermenge** → leeres Array
        bei gefülltem
          `Treffer-Gesamtanzahl`, `Treffer-Weitere-Vorhanden: false`, HTTP 200.




      operationId: IDENTIFIZIEREN_LOKATION_BASIS
      tags:
        - Schnittstellen/BO4E Lesen (Backend)
        - LESEN | READ
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                stammdaten:
                  type: object
                  properties:
                    MARKTLOKATION:
                      type: array
                      items:
                        type: object
                        properties:
                          boTyp:
                            type: string
                          versionStruktur:
                            type: string
                          marktlokationsId:
                            type: string
                          energierichtung:
                            type: string
                          lokationsadresse:
                            type: object
                            properties:
                              postleitzahl:
                                type: string
                              ort:
                                type: string
                              strasse:
                                type: string
                              hausnummer:
                                type: string
                              postfach:
                                type: string
                              adresszusatz:
                                type: string
                              coErgaenzung:
                                type: string
                              landescode:
                                type: string
                              ortsteil:
                                type: string
                              zusatzInformation:
                                type: object
                                properties:
                                  zusatz1:
                                    type: string
                                  zusatz2:
                                    type: string
                                  zusatz3:
                                    type: string
                                  zusatz4:
                                    type: string
                                  zusatz5:
                                    type: string
                                required:
                                  - zusatz1
                                  - zusatz2
                                  - zusatz3
                                  - zusatz4
                                  - zusatz5
                                x-apidog-orders:
                                  - zusatz1
                                  - zusatz2
                                  - zusatz3
                                  - zusatz4
                                  - zusatz5
                                x-apidog-ignore-properties: []
                            required:
                              - postleitzahl
                              - ort
                              - strasse
                              - hausnummer
                              - postfach
                              - adresszusatz
                              - coErgaenzung
                              - landescode
                              - ortsteil
                              - zusatzInformation
                            x-apidog-orders:
                              - postleitzahl
                              - ort
                              - strasse
                              - hausnummer
                              - postfach
                              - adresszusatz
                              - coErgaenzung
                              - landescode
                              - ortsteil
                              - zusatzInformation
                            x-apidog-ignore-properties: []
                          katasterinformation:
                            type: object
                            properties:
                              gemarkung_flur:
                                type: string
                              flurstueck:
                                type: string
                              flurstueckNummer:
                                type: string
                            required:
                              - gemarkung_flur
                              - flurstueck
                              - flurstueckNummer
                            x-apidog-orders:
                              - gemarkung_flur
                              - flurstueck
                              - flurstueckNummer
                            x-apidog-ignore-properties: []
                          geokoordinaten:
                            type: object
                            properties:
                              breitengrad:
                                type: string
                              laengengrad:
                                type: string
                              ostwert:
                                type: string
                              nordwert:
                                type: string
                              zone:
                                type: string
                              hochwert:
                                type: string
                              rechtswert:
                                type: string
                            required:
                              - breitengrad
                              - laengengrad
                              - ostwert
                              - nordwert
                              - zone
                              - hochwert
                              - rechtswert
                            x-apidog-orders:
                              - breitengrad
                              - laengengrad
                              - ostwert
                              - nordwert
                              - zone
                              - hochwert
                              - rechtswert
                            x-apidog-ignore-properties: []
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                          - marktlokationsId
                          - energierichtung
                          - lokationsadresse
                          - katasterinformation
                          - geokoordinaten
                        x-apidog-ignore-properties: []
                    TRANCHE:
                      type: array
                      items:
                        type: object
                        properties:
                          boTyp:
                            type: string
                          versionStruktur:
                            type: string
                          tranchenId:
                            type: string
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                          - tranchenId
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                    MESSLOKATION:
                      type: array
                      items:
                        type: object
                        properties:
                          boTyp:
                            type: string
                          versionStruktur:
                            type: string
                          messlokationsId:
                            type: string
                          messadresse:
                            type: object
                            properties:
                              postleitzahl:
                                type: string
                              ort:
                                type: string
                              strasse:
                                type: string
                              hausnummer:
                                type: string
                              postfach:
                                type: string
                              adresszusatz:
                                type: string
                              coErgaenzung:
                                type: string
                              gewerbekennzeichnung:
                                type: boolean
                              landescode:
                                type: string
                              ortsteil:
                                type: string
                              zusatzInformation:
                                type: object
                                properties:
                                  zusatz1:
                                    type: string
                                  zusatz2:
                                    type: string
                                  zusatz3:
                                    type: string
                                  zusatz4:
                                    type: string
                                  zusatz5:
                                    type: string
                                required:
                                  - zusatz1
                                  - zusatz2
                                  - zusatz3
                                  - zusatz4
                                  - zusatz5
                                x-apidog-orders:
                                  - zusatz1
                                  - zusatz2
                                  - zusatz3
                                  - zusatz4
                                  - zusatz5
                                x-apidog-ignore-properties: []
                            required:
                              - postleitzahl
                              - ort
                              - strasse
                              - hausnummer
                              - postfach
                              - adresszusatz
                              - coErgaenzung
                              - gewerbekennzeichnung
                              - landescode
                              - ortsteil
                              - zusatzInformation
                            x-apidog-orders:
                              - postleitzahl
                              - ort
                              - strasse
                              - hausnummer
                              - postfach
                              - adresszusatz
                              - coErgaenzung
                              - gewerbekennzeichnung
                              - landescode
                              - ortsteil
                              - zusatzInformation
                            x-apidog-ignore-properties: []
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                          - messlokationsId
                          - messadresse
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                    ZAEHLER:
                      type: array
                      items:
                        type: object
                        properties:
                          boTyp:
                            type: string
                          versionStruktur:
                            type: string
                          zaehlernummer:
                            type: string
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                          - zaehlernummer
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                    ENERGIELIEFERVERTRAG:
                      type: array
                      items:
                        type: object
                        properties:
                          boTyp:
                            type: string
                          versionStruktur:
                            type: string
                          vertragsart:
                            type: string
                          vertragspartner2:
                            type: array
                            items:
                              type: object
                              properties:
                                boTyp:
                                  type: string
                                versionStruktur:
                                  type: string
                                anrede:
                                  type: string
                                name1:
                                  type: string
                                name2:
                                  type: string
                                gewerbekennzeichnung:
                                  type: boolean
                                geschaeftspartnerrolle:
                                  type: array
                                  items:
                                    type: string
                                externeReferenzen:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      exRefName:
                                        type: string
                                      exRefWert:
                                        type: string
                                    required:
                                      - exRefName
                                      - exRefWert
                                    x-apidog-orders:
                                      - exRefName
                                      - exRefWert
                                    x-apidog-ignore-properties: []
                              x-apidog-orders:
                                - boTyp
                                - versionStruktur
                                - anrede
                                - name1
                                - name2
                                - gewerbekennzeichnung
                                - geschaeftspartnerrolle
                                - externeReferenzen
                              required:
                                - boTyp
                                - versionStruktur
                              x-apidog-ignore-properties: []
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                          - vertragsart
                          - vertragspartner2
                        x-apidog-ignore-properties: []
                    NETZNUTZUNGSVERTRAG:
                      type: array
                      items:
                        type: object
                        properties:
                          boTyp:
                            type: string
                          versionStruktur:
                            type: string
                          vertragsart:
                            type: string
                          sparte:
                            type: string
                          vertragsbeginn:
                            type: string
                          vertragsende:
                            type: string
                          vertragskonditionen:
                            type: object
                            properties:
                              haushaltskunde:
                                type: boolean
                            required:
                              - haushaltskunde
                            x-apidog-orders:
                              - haushaltskunde
                            x-apidog-ignore-properties: []
                        x-apidog-orders:
                          - boTyp
                          - versionStruktur
                          - vertragsart
                          - sparte
                          - vertragsbeginn
                          - vertragsende
                          - vertragskonditionen
                        required:
                          - boTyp
                          - versionStruktur
                        x-apidog-ignore-properties: []
                  x-apidog-orders:
                    - MARKTLOKATION
                    - TRANCHE
                    - MESSLOKATION
                    - ZAEHLER
                    - ENERGIELIEFERVERTRAG
                    - NETZNUTZUNGSVERTRAG
                  description: >-
                    Informationscontainer für Stammdaten, die zur
                    Identifizierung genutzt werden
                  x-apidog-ignore-properties: []
                transaktionsdaten:
                  type: object
                  description: |
                    Informationscontainer für Daten zum Vorgang 
                  properties:
                    ausfuehrungsdatum:
                      type: string
                      pattern: >-
                        20(\\d{2}(\\-(0[13578]|1[02])\\-(0[1-9]|[12]\\d|3[01])|\\-02\\-(0[1-9]|1\\d|2[0-8])|\\-(0[469]|11)\\-(0[1-9]|[12]\\d|30))|([02468][048]|[13579][26])\\-02\\-(29))T([01]\\d|2[0-3]):[0-5]\\d:[0-5]\\dZ
                      description: >
                        Zeitpunkt zu dem die Identifikation stattfinden soll in
                        angegeben in Zeitzone UTC. (umgerechnet muss dieser
                        Zeitpunkt ein Tagesbeginn 00:00 Uhr gesetzlicher
                        deutscher Zeit sein) | Format YYYY-MM-DD'T'HH:mm:ss'Z' |
                        Mapping auf identificationDateTime
                      examples:
                        - '2023-08-02T22:00:00Z'
                  required:
                    - ausfuehrungsdatum
                  x-apidog-orders:
                    - ausfuehrungsdatum
                  x-apidog-ignore-properties: []
                zusatzdaten:
                  type: object
                  properties:
                    lokationsTyp:
                      type: string
                      title: Lokationstyp
                      description: >-
                        Gibt an, ob eine Markt- oder Messlokation
                        zurückgeliefert werden soll
                      enum:
                        - MALO
                        - MELO
                      x-apidog-enum:
                        - value: MALO
                          name: Marktlokation
                          description: Marktlokation
                        - value: MELO
                          name: Messlokation
                          description: Messlokation
                  x-apidog-orders:
                    - lokationsTyp
                  x-apidog-refs: {}
                  required:
                    - lokationsTyp
                  description: >-
                    Informationscontainer für Daten zum gewünschten
                    Rückgabeformatt 
                  x-apidog-ignore-properties: []
              required:
                - stammdaten
                - transaktionsdaten
                - zusatzdaten
              x-apidog-orders:
                - stammdaten
                - transaktionsdaten
                - zusatzdaten
              x-apidog-ignore-properties: []
            example:
              stammdaten:
                MARKTLOKATION:
                  - boTyp: MARKTLOKATION
                    versionStruktur: '1'
                    marktlokationsId: '90131677420'
                    energierichtung: EINSP
                    lokationsadresse:
                      postleitzahl: aliquip tempor amet
                      ort: commodo in Excepteur eu dolor
                      strasse: laborum minim proident
                      hausnummer: '50'
                      postfach: quis aliqua
                      adresszusatz: veniam in ea
                      coErgaenzung: id est adipisicing tempor
                      landescode: UK
                      ortsteil: dolore ad esse
                      zusatzInformation:
                        zusatz1: Lorem id Duis anim
                        zusatz2: aliqua laborum minim cillum deserunt
                        zusatz3: proident
                        zusatz4: consectetur sit
                        zusatz5: consequat reprehenderit qui pariatur nulla
                  - boTyp: MARKTLOKATION
                    versionStruktur: '1'
                    marktlokationsId: '03308573585'
                    energierichtung: AUSSP
                    lokationsadresse:
                      postleitzahl: Ut ex enim cupidatat aliquip
                      ort: Duis ea ex sed
                      strasse: elit consequat aliquip
                      hausnummer: '96'
                      postfach: minim Duis fugiat ut
                      adresszusatz: consectetur pariatur officia
                      coErgaenzung: reprehenderit mollit irure
                      landescode: GL
                      ortsteil: eu id
                      zusatzInformation:
                        zusatz1: exercitation
                        zusatz2: elit ad dolor veniam
                        zusatz3: Ut ullamco Duis laboris
                        zusatz4: Ut est non ex
                        zusatz5: irure in deserunt culpa
                TRANCHE:
                  - boTyp: TRANCHE
                    versionStruktur: '1'
                    tranchenId: '25753438709'
                MESSLOKATION:
                  - boTyp: MESSLOKATION
                    versionStruktur: '1'
                    messlokationsId: DE89771071027XDWTLEH0Q9J3J02PYZXW
                    messadresse:
                      postleitzahl: <string>
                      ort: <string>
                      strasse: <string>
                      hausnummer: <string>
                      postfach: <string>
                      adresszusatz: <string>
                      coErgaenzung: <string>
                      gewerbekennzeichnung: true
                      landescode: DE
                      ortsteil: <string>
                      zusatzInformation:
                        zusatz1: <string>
                        zusatz2: <string>
                        zusatz3: <string>
                        zusatz4: <string>
                        zusatz5: <string>
      responses:
        '200':
          description: >-
            Erfolgreiches Lesen der Marktlokation | Successful reading of the
            market location
          content:
            application/json:
              schema:
                type: array
                title: IdentifizierteLokationen
                description: >
                  Ergebnis der Lokationsidentifikation: flaches Array mit 0..n
                  ermittelten Markt- oder Messlokationen des über
                  zusatzdaten.lokationsTyp angeforderten Typs. Trefferanzahl und
                  Paginierung liegen in den Antwort-Headern (Treffer-Offset,
                  Treffer-Anzahl, Treffer-Gesamtanzahl,
                  Treffer-Weitere-Vorhanden). Ein leeres Array ist ein gültiges
                  fachliches Ergebnis.
                minItems: 0
                maxItems: 50
                items:
                  oneOf:
                    - $ref: '#/components/schemas/Marktlokation'
                    - $ref: '#/components/schemas/Messlokation'
                  description: 'Ermittelte Messlokation oder Marktlokation. '
                  discriminator:
                    propertyName: boTyp
                    mapping:
                      MARKTLOKATION: '#/definitions/5241973'
                      MESSLOKATION: '#/definitions/5241975'
              examples:
                '1':
                  summary: EIne Marktlokation
                  value:
                    - boTyp: MARKTLOKATION
                      versionStruktur: '1'
                      marktlokationsId: '50754496000'
                      marktlokationsTyp:
                        - typ: STANDARD_MARKTLOKATION
                          gueltigAb: '2023-08-01T22:00:00Z'
                          gueltigBis: '2027-08-01T22:00:00Z'
                      zukuenftigerMeldepunkt: null
                      sparte: STROM
                      gueltigkeitszeitraum:
                        zeitraumId: null
                        startdatum: null
                        enddatum: null
                      rollencodenummer: '9906464000001'
                      inbetriebnahmedatum: '2023-08-01T22:00:00Z'
                      datenqualitaet: null
                      energierichtung: AUSSP
                      bilanzierungsmethode: SLP
                      verbrauchsart:
                        - KL
                      unterbrechbar: false
                      netzebene: NSP
                      umspannung: null
                      netzbetreiberCodeNr: '9900683000008'
                      gebietTyp: VERSORGUNGSGEBIET
                      netzgebietNr: '12345'
                      bilanzierungsgebiet: 11YR00000004025V
                      grundversorgerCodeNr: '9900683000008'
                      endkunde:
                        boTyp: GESCHAEFTSPARTNER
                        versionStruktur: '1'
                        anrede: Herr
                        name1: Haiko
                        name2: Fisch
                        name3: null
                        gewerbekennzeichnung: false
                        hrnummer: null
                        amtsgericht: null
                        kontaktweg:
                          - TELEFONAT
                          - E_MAIL
                        umsatzsteuerId: null
                        glaeubigerId: null
                        eMailAdresse: hai.fisch@web.de
                        website: null
                        partneradresse:
                          postleitzahl: '65189'
                          ort: Wiesbaden
                          strasse: Korallenweg
                          hausnummer: '10'
                          postfach: null
                          adresszusatz: Wohnung 1
                          coErgaenzung: null
                          landescode: DE
                          ortsteil: Riff
                      lokationsadresse:
                        postleitzahl: '65189'
                        ort: Wiesbaden
                        strasse: Korallenweg
                        hausnummer: '10'
                        postfach: null
                        adresszusatz: Wohnung 1
                        coErgaenzung: null
                        landescode: DE
                        ortsteil: Riff
                        zusatzInformation:
                          zusatz1: null
                          zusatz2: null
                          zusatz3: null
                          zusatz4: null
                          zusatz5: null
                      katasteradresse:
                        gemarkung_flur: '1'
                        flurstueck: '1'
                        flurstueckNummer: '1'
                      geokoordinaten:
                        breitengrad: '50.0782'
                        laengengrad: '8.2397'
                        ostwert: null
                        nordwert: null
                        zone: UTMZone32
                        hochwert: null
                        rechtswert: null
                      marktrollen:
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-07-01T04:00:00Z'
                          marktrolle: MSB
                          gewerbekennzeichnung: true
                          rollencodenummer: '9906464000001'
                          rollencodetyp: BDEW
                          weiterverpflichtet: false
                          messstellenbetreiberEigenschaft: GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: NB
                          gewerbekennzeichnung: true
                          rollencodenummer: '9900683000008'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: LF
                          gewerbekennzeichnung: true
                          rollencodenummer: '9904000000005'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: UENB
                          gewerbekennzeichnung: true
                          rollencodenummer: '4033872000058'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: BIKO
                          gewerbekennzeichnung: true
                          rollencodenummer: '4033872000027'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: BKV
                          gewerbekennzeichnung: true
                          rollencodenummer: '4033872000034'
                          rollencodetyp: BDEW
                      regelzone: '1'
                      marktgebiet: '1234'
                      zeitreihentyp: SLS
                      zaehlwerke:
                        - zaehlwerkId: '1'
                          bezeichnung: HT
                          richtung: AUSSP
                          obisKennzahl: 1-1:1.9.0
                          wandlerfaktor: 1
                          einheit: KWH
                          schwachlastfaehig: NICHT_SCHWACHLASTFAEHIG
                          verwendungszwecke:
                            - marktrolle: NB
                              zweck:
                                - NETZNUTZUNGSABRECHNUNG
                          verbrauchsart:
                            - KL
                          unterbrechbarkeit: NUV
                          waermenutzung: null
                          konzessionsabgabe:
                            satz: TA
                            kosten: 0
                            kategorie: '1'
                          steuerbefreit: false
                          vorkommastelle: 7
                          nachkommastelle: 3
                          abrechnungsrelevant: true
                          anzahlAblesungen: 1
                          zaehlzeiten:
                            zaehlzeitDefinition: null
                            register: null
                            schwachlastfaehig: null
                          leistungskurvendefinition: null
                          konfiguration: null
                          messprodukt: '9991000000044'
                          wertegranularitaet: JAEHRLICH
                          notwendigkeitZweiteMessung: NICHT_VORHANDEN
                          werteuebermittlungVerwendungszweck: NICHT_VORHANDEN
                          artEMobilitaet: null
                      zaehlwerkeBeteiligteMarktrolle:
                        - NB
                      verbrauchsmenge:
                        - startdatum: '2024-08-01T22:00:00Z'
                          enddatum: '2025-08-01T22:00:00Z'
                          wertermittlungsverfahren: PROGNOSE
                          messwertstatus: PROGNOSEWERT
                          statuszusatzinformationen:
                            - art: PLAUSIBILISIERUNGSHINWEIS
                              status: KUNDENSELBSTABLESUNG
                          obiskennzahl: 1-1:1.9.0
                          wert: 2500
                          einheit: KWH
                      zugehoerigeMesslokationen:
                        - messlokationsId: DE0009697056900614312080040415111
                          arithmetik: ADDITION
                          gueltigSeit: '2023-08-01T22:00:00Z'
                          gueltigBis: '2027-08-01T22:00:00Z'
                      messtechnischeEinordnung: IMS
                      netznutzungsabrechnungsdaten:
                        - artikelId: '1'
                          artikelIdTyp: ARTIKELID
                          anzahl: 1
                          gemeinderabatt: null
                          zuschlag: null
                          abschlag: null
                          singulaereBetriebsmittel:
                            wert: null
                            einheit: null
                          preisSingulaereBetriebsmittel:
                            wert: null
                            einheit: null
                            bezugswert: null
                            status: null
                          abrechnungBlindarbeit: null
                          zahlerBlindarbeit: null
                          zahlerBlindarbeitLf: null
                          zaehlzeiten:
                            zaehlzeitDefinition: null
                            register: null
                      messstellenbetriebsabrechnungsdaten:
                        - messstellenbetriebsabrechnung: true
                          artikelId: '1'
                          artikelIdTyp: ARTIKELID
                          anzahl: 1
                          zuschlag: null
                          abschlag: null
                      sperrstatus: ENTSPERRT
                      referenzMarktlokationsId: '50754496000'
                      energieherkunft:
                        - erzeugungsart: null
                          anteilProzent: null
                      versorgungsart: null
                      eigentuemer:
                        boTyp: GESCHAEFTSPARTNER
                        versionStruktur: '1'
                        anrede: Herr
                        name1: Haiko
                        name2: Fisch
                        name3: null
                        gewerbekennzeichnung: false
                        geschaeftspartnerrolle:
                          - EIGENTUEMER
                        hrnummer: null
                        amtsgericht: null
                        kontaktweg:
                          - TELEFONAT
                          - E_MAIL
                        umsatzsteuerId: null
                        glaeubigerId: null
                        eMailAdresse: hai.fisch@web.de
                        website: null
                        partneradresse:
                          postleitzahl: '65189'
                          ort: Wiesbaden
                          strasse: Korallenweg
                          hausnummer: '10'
                          postfach: null
                          adresszusatz: Wohnung 1
                          coErgaenzung: null
                          landescode: DE
                          ortsteil: Riff
                      hausverwalter:
                        boTyp: GESCHAEFTSPARTNER
                        versionStruktur: '1'
                        anrede: Herr
                        name1: Haiko
                        name2: Fisch
                        name3: null
                        gewerbekennzeichnung: false
                        geschaeftspartnerrolle:
                          - HAUSVERWALTER
                        hrnummer: null
                        amtsgericht: null
                        kontaktweg:
                          - TELEFONAT
                          - E_MAIL
                        umsatzsteuerId: null
                        glaeubigerId: null
                        eMailAdresse: hai.fisch@web.de
                        website: null
                        partneradresse:
                          postleitzahl: '65189'
                          ort: Wiesbaden
                          strasse: Korallenweg
                          hausnummer: '10'
                          postfach: null
                          adresszusatz: Wohnung 1
                          coErgaenzung: null
                          landescode: DE
                          ortsteil: Riff
                      verguetungEmpfaenger: null
                      statusErzeugendeMalo: null
                      fernsteuerbarkeit: TECHNISCH_NICHT_FERNSTEUERBAR
                      foerderungsLand: null
                      redispatch: false
                      lokationszuordnung: null
                      modulNetzentgelte: null
                      produktdatenRelevanteRolle: LF
                      konfigurationsprodukt: null
                      leistungskurvendefinition: null
                      beteiligterMarktpartner:
                        boTyp: MARKTTEILNEHMER
                        versionStruktur: '1'
                        marktrolle: NB
                        gewerbekennzeichnung: true
                        rollencodenummer: '9900683000008'
                        rollencodetyp: BDEW
                      erforderlichesProduktpaket:
                        - produktpaketId: 1
                          produkt:
                            - produktCode: '9991000002008'
                              codeProdukteigenschaft: '9991000002115'
                              wertedetails: null
                          umsetzungsgradvorgabe: ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
                          priorisierung: PRIORITAET1
                      datenDerBeteiligtenMarktrolle: null
                      paketId: null
                '2':
                  summary: Mehrere Marktlokationen
                  value:
                    - boTyp: MARKTLOKATION
                      versionStruktur: '1'
                      marktlokationsId: '50754496000'
                      marktlokationsTyp:
                        - typ: STANDARD_MARKTLOKATION
                          gueltigAb: '2023-08-01T22:00:00Z'
                          gueltigBis: '2027-08-01T22:00:00Z'
                      zukuenftigerMeldepunkt: null
                      sparte: STROM
                      gueltigkeitszeitraum:
                        zeitraumId: null
                        startdatum: null
                        enddatum: null
                      rollencodenummer: '9906464000001'
                      inbetriebnahmedatum: '2023-08-01T22:00:00Z'
                      datenqualitaet: null
                      energierichtung: AUSSP
                      bilanzierungsmethode: SLP
                      verbrauchsart:
                        - KL
                      unterbrechbar: false
                      netzebene: NSP
                      umspannung: null
                      netzbetreiberCodeNr: '9900683000008'
                      gebietTyp: VERSORGUNGSGEBIET
                      netzgebietNr: '12345'
                      bilanzierungsgebiet: 11YR00000004025V
                      grundversorgerCodeNr: '9900683000008'
                      endkunde:
                        boTyp: GESCHAEFTSPARTNER
                        versionStruktur: '1'
                        anrede: Herr
                        name1: Haiko
                        name2: Fisch
                        name3: null
                        gewerbekennzeichnung: false
                        hrnummer: null
                        amtsgericht: null
                        kontaktweg:
                          - TELEFONAT
                          - E_MAIL
                        umsatzsteuerId: null
                        glaeubigerId: null
                        eMailAdresse: hai.fisch@web.de
                        website: null
                        partneradresse:
                          postleitzahl: '65189'
                          ort: Wiesbaden
                          strasse: Korallenweg
                          hausnummer: '10'
                          postfach: null
                          adresszusatz: Wohnung 1
                          coErgaenzung: null
                          landescode: DE
                          ortsteil: Riff
                      lokationsadresse:
                        postleitzahl: '65189'
                        ort: Wiesbaden
                        strasse: Korallenweg
                        hausnummer: '10'
                        postfach: null
                        adresszusatz: Wohnung 1
                        coErgaenzung: null
                        landescode: DE
                        ortsteil: Riff
                        zusatzInformation:
                          zusatz1: null
                          zusatz2: null
                          zusatz3: null
                          zusatz4: null
                          zusatz5: null
                      katasteradresse:
                        gemarkung_flur: '1'
                        flurstueck: '1'
                        flurstueckNummer: '1'
                      geokoordinaten:
                        breitengrad: '50.0782'
                        laengengrad: '8.2397'
                        ostwert: null
                        nordwert: null
                        zone: UTMZone32
                        hochwert: null
                        rechtswert: null
                      marktrollen:
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-07-01T04:00:00Z'
                          marktrolle: MSB
                          gewerbekennzeichnung: true
                          rollencodenummer: '9906464000001'
                          rollencodetyp: BDEW
                          weiterverpflichtet: false
                          messstellenbetreiberEigenschaft: GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: NB
                          gewerbekennzeichnung: true
                          rollencodenummer: '9900683000008'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: LF
                          gewerbekennzeichnung: true
                          rollencodenummer: '9904000000005'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: UENB
                          gewerbekennzeichnung: true
                          rollencodenummer: '4033872000058'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: BIKO
                          gewerbekennzeichnung: true
                          rollencodenummer: '4033872000027'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: BKV
                          gewerbekennzeichnung: true
                          rollencodenummer: '4033872000034'
                          rollencodetyp: BDEW
                      regelzone: '1'
                      marktgebiet: '1234'
                      zeitreihentyp: SLS
                      zaehlwerke:
                        - zaehlwerkId: '1'
                          bezeichnung: HT
                          richtung: AUSSP
                          obisKennzahl: 1-1:1.9.0
                          wandlerfaktor: 1
                          einheit: KWH
                          schwachlastfaehig: NICHT_SCHWACHLASTFAEHIG
                          verwendungszwecke:
                            - marktrolle: NB
                              zweck:
                                - NETZNUTZUNGSABRECHNUNG
                          verbrauchsart:
                            - KL
                          unterbrechbarkeit: NUV
                          waermenutzung: null
                          konzessionsabgabe:
                            satz: TA
                            kosten: 0
                            kategorie: '1'
                          steuerbefreit: false
                          vorkommastelle: 7
                          nachkommastelle: 3
                          abrechnungsrelevant: true
                          anzahlAblesungen: 1
                          zaehlzeiten:
                            zaehlzeitDefinition: null
                            register: null
                            schwachlastfaehig: null
                          leistungskurvendefinition: null
                          konfiguration: null
                          messprodukt: '9991000000044'
                          wertegranularitaet: JAEHRLICH
                          notwendigkeitZweiteMessung: NICHT_VORHANDEN
                          werteuebermittlungVerwendungszweck: NICHT_VORHANDEN
                          artEMobilitaet: null
                      zaehlwerkeBeteiligteMarktrolle:
                        - NB
                      verbrauchsmenge:
                        - startdatum: '2024-08-01T22:00:00Z'
                          enddatum: '2025-08-01T22:00:00Z'
                          wertermittlungsverfahren: PROGNOSE
                          messwertstatus: PROGNOSEWERT
                          statuszusatzinformationen:
                            - art: PLAUSIBILISIERUNGSHINWEIS
                              status: KUNDENSELBSTABLESUNG
                          obiskennzahl: 1-1:1.9.0
                          wert: 2500
                          einheit: KWH
                      zugehoerigeMesslokationen:
                        - messlokationsId: DE0009697056900614312080040415111
                          arithmetik: ADDITION
                          gueltigSeit: '2023-08-01T22:00:00Z'
                          gueltigBis: '2027-08-01T22:00:00Z'
                      messtechnischeEinordnung: IMS
                      netznutzungsabrechnungsdaten:
                        - artikelId: '1'
                          artikelIdTyp: ARTIKELID
                          anzahl: 1
                          gemeinderabatt: null
                          zuschlag: null
                          abschlag: null
                          singulaereBetriebsmittel:
                            wert: null
                            einheit: null
                          preisSingulaereBetriebsmittel:
                            wert: null
                            einheit: null
                            bezugswert: null
                            status: null
                          abrechnungBlindarbeit: null
                          zahlerBlindarbeit: null
                          zahlerBlindarbeitLf: null
                          zaehlzeiten:
                            zaehlzeitDefinition: null
                            register: null
                      messstellenbetriebsabrechnungsdaten:
                        - messstellenbetriebsabrechnung: true
                          artikelId: '1'
                          artikelIdTyp: ARTIKELID
                          anzahl: 1
                          zuschlag: null
                          abschlag: null
                      sperrstatus: ENTSPERRT
                      referenzMarktlokationsId: '50754496000'
                      energieherkunft:
                        - erzeugungsart: null
                          anteilProzent: null
                      versorgungsart: null
                      eigentuemer:
                        boTyp: GESCHAEFTSPARTNER
                        versionStruktur: '1'
                        anrede: Herr
                        name1: Haiko
                        name2: Fisch
                        name3: null
                        gewerbekennzeichnung: false
                        geschaeftspartnerrolle:
                          - EIGENTUEMER
                        hrnummer: null
                        amtsgericht: null
                        kontaktweg:
                          - TELEFONAT
                          - E_MAIL
                        umsatzsteuerId: null
                        glaeubigerId: null
                        eMailAdresse: hai.fisch@web.de
                        website: null
                        partneradresse:
                          postleitzahl: '65189'
                          ort: Wiesbaden
                          strasse: Korallenweg
                          hausnummer: '10'
                          postfach: null
                          adresszusatz: Wohnung 1
                          coErgaenzung: null
                          landescode: DE
                          ortsteil: Riff
                      hausverwalter:
                        boTyp: GESCHAEFTSPARTNER
                        versionStruktur: '1'
                        anrede: Herr
                        name1: Haiko
                        name2: Fisch
                        name3: null
                        gewerbekennzeichnung: false
                        geschaeftspartnerrolle:
                          - HAUSVERWALTER
                        hrnummer: null
                        amtsgericht: null
                        kontaktweg:
                          - TELEFONAT
                          - E_MAIL
                        umsatzsteuerId: null
                        glaeubigerId: null
                        eMailAdresse: hai.fisch@web.de
                        website: null
                        partneradresse:
                          postleitzahl: '65189'
                          ort: Wiesbaden
                          strasse: Korallenweg
                          hausnummer: '10'
                          postfach: null
                          adresszusatz: Wohnung 1
                          coErgaenzung: null
                          landescode: DE
                          ortsteil: Riff
                      verguetungEmpfaenger: null
                      statusErzeugendeMalo: null
                      fernsteuerbarkeit: TECHNISCH_NICHT_FERNSTEUERBAR
                      foerderungsLand: null
                      redispatch: false
                      lokationszuordnung: null
                      modulNetzentgelte: null
                      produktdatenRelevanteRolle: LF
                      konfigurationsprodukt: null
                      leistungskurvendefinition: null
                      beteiligterMarktpartner:
                        boTyp: MARKTTEILNEHMER
                        versionStruktur: '1'
                        marktrolle: NB
                        gewerbekennzeichnung: true
                        rollencodenummer: '9900683000008'
                        rollencodetyp: BDEW
                      erforderlichesProduktpaket:
                        - produktpaketId: 1
                          produkt:
                            - produktCode: '9991000002008'
                              codeProdukteigenschaft: '9991000002115'
                              wertedetails: null
                          umsetzungsgradvorgabe: ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
                          priorisierung: PRIORITAET1
                      datenDerBeteiligtenMarktrolle: null
                      paketId: null
                    - boTyp: MARKTLOKATION
                      versionStruktur: '1'
                      marktlokationsId: '50754497001'
                      marktlokationsTyp:
                        - typ: STANDARD_MARKTLOKATION
                          gueltigAb: '2023-08-01T22:00:00Z'
                          gueltigBis: '2027-08-01T22:00:00Z'
                      zukuenftigerMeldepunkt: null
                      sparte: STROM
                      gueltigkeitszeitraum:
                        zeitraumId: null
                        startdatum: null
                        enddatum: null
                      rollencodenummer: '9906464000001'
                      inbetriebnahmedatum: '2023-08-01T22:00:00Z'
                      datenqualitaet: null
                      energierichtung: AUSSP
                      bilanzierungsmethode: SLP
                      verbrauchsart:
                        - KL
                      unterbrechbar: false
                      netzebene: NSP
                      umspannung: null
                      netzbetreiberCodeNr: '9900683000008'
                      gebietTyp: VERSORGUNGSGEBIET
                      netzgebietNr: '12345'
                      bilanzierungsgebiet: 11YR00000004025V
                      grundversorgerCodeNr: '9900683000008'
                      endkunde:
                        boTyp: GESCHAEFTSPARTNER
                        versionStruktur: '1'
                        anrede: Frau
                        name1: Marina
                        name2: Welle
                        name3: null
                        gewerbekennzeichnung: false
                        hrnummer: null
                        amtsgericht: null
                        kontaktweg:
                          - TELEFONAT
                          - E_MAIL
                        umsatzsteuerId: null
                        glaeubigerId: null
                        eMailAdresse: marina.welle@web.de
                        website: null
                        partneradresse:
                          postleitzahl: '65189'
                          ort: Wiesbaden
                          strasse: Korallenweg
                          hausnummer: '10'
                          postfach: null
                          adresszusatz: Wohnung 2
                          coErgaenzung: null
                          landescode: DE
                          ortsteil: Riff
                      lokationsadresse:
                        postleitzahl: '65189'
                        ort: Wiesbaden
                        strasse: Korallenweg
                        hausnummer: '10'
                        postfach: null
                        adresszusatz: Wohnung 2
                        coErgaenzung: null
                        landescode: DE
                        ortsteil: Riff
                        zusatzInformation:
                          zusatz1: null
                          zusatz2: null
                          zusatz3: null
                          zusatz4: null
                          zusatz5: null
                      katasteradresse:
                        gemarkung_flur: '1'
                        flurstueck: '1'
                        flurstueckNummer: '1'
                      geokoordinaten:
                        breitengrad: '50.0782'
                        laengengrad: '8.2397'
                        ostwert: null
                        nordwert: null
                        zone: UTMZone32
                        hochwert: null
                        rechtswert: null
                      marktrollen:
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-07-01T04:00:00Z'
                          marktrolle: MSB
                          gewerbekennzeichnung: true
                          rollencodenummer: '9906464000001'
                          rollencodetyp: BDEW
                          weiterverpflichtet: false
                          messstellenbetreiberEigenschaft: GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: NB
                          gewerbekennzeichnung: true
                          rollencodenummer: '9900683000008'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: LF
                          gewerbekennzeichnung: true
                          rollencodenummer: '9904000000005'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: UENB
                          gewerbekennzeichnung: true
                          rollencodenummer: '4033872000058'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: BIKO
                          gewerbekennzeichnung: true
                          rollencodenummer: '4033872000027'
                          rollencodetyp: BDEW
                        - boTyp: MARKTTEILNEHMER
                          versionStruktur: '1'
                          gueltigkeitszeitraum:
                            zeitraumId: 1
                            startdatum: '2022-12-31T23:00:00Z'
                            enddatum: '2027-12-31T23:00:00Z'
                          marktrolle: BKV
                          gewerbekennzeichnung: true
                          rollencodenummer: '4033872000034'
                          rollencodetyp: BDEW
                      regelzone: '1'
                      marktgebiet: '1234'
                      zeitreihentyp: SLS
                      zaehlwerke:
                        - zaehlwerkId: '1'
                          bezeichnung: HT
                          richtung: AUSSP
                          obisKennzahl: 1-1:1.9.0
                          wandlerfaktor: 1
                          einheit: KWH
                          schwachlastfaehig: NICHT_SCHWACHLASTFAEHIG
                          verwendungszwecke:
                            - marktrolle: NB
                              zweck:
                                - NETZNUTZUNGSABRECHNUNG
                          verbrauchsart:
                            - KL
                          unterbrechbarkeit: NUV
                          waermenutzung: null
                          konzessionsabgabe:
                            satz: TA
                            kosten: 0
                            kategorie: '1'
                          steuerbefreit: false
                          vorkommastelle: 7
                          nachkommastelle: 3
                          abrechnungsrelevant: true
                          anzahlAblesungen: 1
                          zaehlzeiten:
                            zaehlzeitDefinition: null
                            register: null
                            schwachlastfaehig: null
                          leistungskurvendefinition: null
                          konfiguration: null
                          messprodukt: '9991000000044'
                          wertegranularitaet: JAEHRLICH
                          notwendigkeitZweiteMessung: NICHT_VORHANDEN
                          werteuebermittlungVerwendungszweck: NICHT_VORHANDEN
                          artEMobilitaet: null
                      zaehlwerkeBeteiligteMarktrolle:
                        - NB
                      verbrauchsmenge:
                        - startdatum: '2024-08-01T22:00:00Z'
                          enddatum: '2025-08-01T22:00:00Z'
                          wertermittlungsverfahren: PROGNOSE
                          messwertstatus: PROGNOSEWERT
                          statuszusatzinformationen:
                            - art: PLAUSIBILISIERUNGSHINWEIS
                              status: KUNDENSELBSTABLESUNG
                          obiskennzahl: 1-1:1.9.0
                          wert: 1800
                          einheit: KWH
                      zugehoerigeMesslokationen:
                        - messlokationsId: DE0009697056900614312080040415222
                          arithmetik: ADDITION
                          gueltigSeit: '2023-08-01T22:00:00Z'
                          gueltigBis: '2027-08-01T22:00:00Z'
                      messtechnischeEinordnung: IMS
                      netznutzungsabrechnungsdaten:
                        - artikelId: '1'
                          artikelIdTyp: ARTIKELID
                          anzahl: 1
                          gemeinderabatt: null
                          zuschlag: null
                          abschlag: null
                          singulaereBetriebsmittel:
                            wert: null
                            einheit: null
                          preisSingulaereBetriebsmittel:
                            wert: null
                            einheit: null
                            bezugswert: null
                            status: null
                          abrechnungBlindarbeit: null
                          zahlerBlindarbeit: null
                          zahlerBlindarbeitLf: null
                          zaehlzeiten:
                            zaehlzeitDefinition: null
                            register: null
                      messstellenbetriebsabrechnungsdaten:
                        - messstellenbetriebsabrechnung: true
                          artikelId: '1'
                          artikelIdTyp: ARTIKELID
                          anzahl: 1
                          zuschlag: null
                          abschlag: null
                      sperrstatus: ENTSPERRT
                      referenzMarktlokationsId: '50754497001'
                      energieherkunft:
                        - erzeugungsart: null
                          anteilProzent: null
                      versorgungsart: null
                      eigentuemer:
                        boTyp: GESCHAEFTSPARTNER
                        versionStruktur: '1'
                        anrede: Herr
                        name1: Haiko
                        name2: Fisch
                        name3: null
                        gewerbekennzeichnung: false
                        geschaeftspartnerrolle:
                          - EIGENTUEMER
                        hrnummer: null
                        amtsgericht: null
                        kontaktweg:
                          - TELEFONAT
                          - E_MAIL
                        umsatzsteuerId: null
                        glaeubigerId: null
                        eMailAdresse: hai.fisch@web.de
                        website: null
                        partneradresse:
                          postleitzahl: '65189'
                          ort: Wiesbaden
                          strasse: Korallenweg
                          hausnummer: '10'
                          postfach: null
                          adresszusatz: Wohnung 1
                          coErgaenzung: null
                          landescode: DE
                          ortsteil: Riff
                      hausverwalter:
                        boTyp: GESCHAEFTSPARTNER
                        versionStruktur: '1'
                        anrede: Herr
                        name1: Haiko
                        name2: Fisch
                        name3: null
                        gewerbekennzeichnung: false
                        geschaeftspartnerrolle:
                          - HAUSVERWALTER
                        hrnummer: null
                        amtsgericht: null
                        kontaktweg:
                          - TELEFONAT
                          - E_MAIL
                        umsatzsteuerId: null
                        glaeubigerId: null
                        eMailAdresse: hai.fisch@web.de
                        website: null
                        partneradresse:
                          postleitzahl: '65189'
                          ort: Wiesbaden
                          strasse: Korallenweg
                          hausnummer: '10'
                          postfach: null
                          adresszusatz: Wohnung 1
                          coErgaenzung: null
                          landescode: DE
                          ortsteil: Riff
                      verguetungEmpfaenger: null
                      statusErzeugendeMalo: null
                      fernsteuerbarkeit: TECHNISCH_NICHT_FERNSTEUERBAR
                      foerderungsLand: null
                      redispatch: false
                      lokationszuordnung: null
                      modulNetzentgelte: null
                      produktdatenRelevanteRolle: LF
                      konfigurationsprodukt: null
                      leistungskurvendefinition: null
                      beteiligterMarktpartner:
                        boTyp: MARKTTEILNEHMER
                        versionStruktur: '1'
                        marktrolle: NB
                        gewerbekennzeichnung: true
                        rollencodenummer: '9900683000008'
                        rollencodetyp: BDEW
                      erforderlichesProduktpaket:
                        - produktpaketId: 1
                          produkt:
                            - produktCode: '9991000002008'
                              codeProdukteigenschaft: '9991000002115'
                              wertedetails: null
                          umsetzungsgradvorgabe: ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
                          priorisierung: PRIORITAET1
                      datenDerBeteiligtenMarktrolle: null
                      paketId: null
          headers: {}
          x-apidog-name: OK
        '400':
          description: Fehlerhafte Anfrage | Bad Request
          content:
            application/json:
              schema:
                type: object
                properties: {}
                x-apidog-orders: []
                x-apidog-ignore-properties: []
          headers: {}
          x-apidog-name: Bad Request
      security:
        - bearer: []
      x-apidog-folder: Schnittstellen/BO4E Lesen (Backend)
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/816353/apis/api-40403306-run
components:
  schemas:
    Messlokation:
      title: Messlokation
      type: object
      properties:
        boTyp: &ref_6
          $ref: '#/components/schemas/BOTyp'
          default: MESSLOKATION
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        messlokationsId:
          type: string
          description: >-
            Angabe der ID der Messlokation,  für die die Stammdaten gelten. Die
            ID dient der eindeutigen Identifikation einer Messlokation und wird
            spätestens bei der Bestätigung vom NB mitgeliefert.

            LOC Z17

            PI 55002 55078 55600 55602 55601 55603 55013 55607 55611 55620 55626
            55632 55638 55175 55180 55173 55177 55690 55643 55648 55653 55658
            55663 55669 55035 55095 55060 55039 55040 55041 55042 55043 55044
            55168 55169 55170 55051 55052 55053 55074 55075 55076

            RFF Z19

            PI 55002 55078 55602 55603 55013 55607 55690 55035 55095 55060 55194
            55043 55168 55169 

            RFF Z46

            PI 55643 55648 55663 55669 

            ORDERS RFF Z19 

            PI 17121 17134

            IFTSTA LOC 172

            PI 21000 21001 21002 21003 21004 21005 21007 21009 21010 21011 21012
            21013 21015 21018 21024 21025 21026 21027 21036 21028 21029 21030
            21031 21033 

            QUOTES LOC 172 

            PI 15001 15003 15004

            INVOIC LOC 172 

            PI 31003 31009 31004 
        sparte: &ref_11
          $ref: '#/components/schemas/Sparte'
          description: Strom oder Gas
        energierichtung: &ref_2
          $ref: '#/components/schemas/Energierichtung'
          description: nicht in Benutzung
        netzebenemessung: &ref_14
          $ref: '#/components/schemas/Netzebene'
          description: >-
            Spannungsebene der Messlokation, in welcher Spannungsebene liegt die
            Melo. 

            CAV E03 

            PI 55643 55648 55653 55658 55663 55669 55060 55043 55168 55169
        messgebietNr:
          type: string
          description: Die Nummer des Messgebietes in der ene't-Datenbank.
        grundzustaendigerMSBCodeNr:
          type: string
          description: >-
            Codenummer des grundzuständigen Messstellenbetreibers, der für diese
            Messlokation zuständig ist.( Dieser ist immer dann
            Messstellenbetreiber, wenn kein anderer MSB die Einrichtungen an der
            Messlokation betreibt.)
        messadresse: &ref_7
          $ref: '#/components/schemas/Adresse'
          description: >-
            Messlokationsadresse

            Z03 Messlokationsadresse

            Z43 Erwartete Messlokationsadresse

            Z44 Im System vorhandene Messlokationsadresse

            Z64 Informative Messlokakaonsadresse

            NAD Z03

            PI 55643 55648 55663 55669 55060 55194 55039 55040 55042 55043 55168
            55169 55168 55169

            ORDERS NAD Z03 Messlokationsadresse 

            PI 17126 17104

            INVOIC NAD DP Adresse der Leistungserbringung 

            PI 31001 31002 31003 31009 31004 31005 31006 31011
        bilanzierungsmethode: &ref_12
          $ref: '#/components/schemas/Bilanzierungsmethode'
          description: Bilanzierungsmethode
        abrechnungmessstellenbetriebnna:
          type: boolean
          description: >-
            Dieser Wert ist true, falls die Abrechnungs des Messstellenbetriebs
            die Netznutzungsabrechnung enthält. false

            andernfalls
        gasqualitaet: &ref_15
          $ref: '#/components/schemas/Gasqualitaet'
          description: >-
            Gasqualität

            CCI Y02

            PI 44112 44113 44139 44140 44142 44002 44013 44014 44035 44043 44168
            44169 44060
        verlustfaktor:
          type: number
          format: float
          description: Verlustfaktor für EDIFACT mapping
        betriebszustand:
          $ref: '#/components/schemas/Betriebszustand'
          description: >-
            Betriebszustand der Messlokation, hier wird der vorläufige
            Betriebszustand einer Melo dem MSB mitgeteilt.

            CCI Z32

            PI 55632 55638 55043 55168 55169
        ablesekartenempfaenger: &ref_16
          $ref: '#/components/schemas/Geschaeftspartner'
          description: |-
            Name und Adresse für die Ablesekarte
            Z05 Name und Adresse für die Ablesekarte
            Z45 Erwarteter Name und Adresse für die Ablesekarte
            Z46 Im System vorhandener Name und Adresse für die Ablesekarte
            PI 55643 55648 55653 55658 55663 55669 55042 55043 55168 55169
        referenzMarktlokationsId:
          type: string
          description: |-
            Referenzierung auf eine ID der zugeordneten Marktlokationen
            RFF Z16
            PI 55043 55168 55169
            RFF Z18
            PI 55043 55168 55169
        verwendungsumfang:
          $ref: '#/components/schemas/Verwendungsumfang'
          description: |-
            Verwendungsumfang 
            CCI Z01
            PI 55043 55168 55169
        zukuenftigerMeldepunkt:
          type: boolean
          description: zukuenftigerMeldepunkt
        lokationszuordnung: &ref_17
          $ref: '#/components/schemas/Lokationszuordnung'
          description: nicht in Benutzung
        beteiligterMarktpartner: &ref_0
          $ref: '#/components/schemas/Marktteilnehmer'
          description: >-
            Beteiligter Marktpartner MP-ID

            NAD VY

            PI 55003 55080 55604 55605 55010 55036 55691 55692 55075 55076 55067
            55071 55072
        geraete:
          type: array
          items:
            $ref: '#/components/schemas/Geraet'
          description: Liste der Geräte, die zu diesem Zähler gehören.
        messdienstleistung:
          type: array
          items:
            $ref: '#/components/schemas/Dienstleistung'
          description: Liste der Messdienstleistungen, die zu dieser Messstelle gehört.
        messlokationszaehler:
          type: array
          items:
            type: string
          description: Zähler, die zu dieser Messlokation gehören. Details
        zaehlwerke:
          type: array
          items: &ref_20
            $ref: '#/components/schemas/Zaehlwerk'
          description: Die Zählwerke des Zählers.
        marktrollen:
          type: array
          items: *ref_0
          description: Zugeordnete Marktpartner
        datenqualitaet: &ref_18
          $ref: '#/components/schemas/Datenqualitaet'
          description: |-
            Einleitung Segmentengruppe
            SEQ Z18 Daten der Messlokation 
            Z18 Daten der Messlokation
            ZG6 Erwartete Daten der Messlokation
            ZG7 Im System vorhandene Daten der Messlokation
            ZF3 Informative Daten der Messlokation
            Z19 Erforderliches Produkt der Messlokation
            ZF4 Informative Erforderliches Produkt der Messlokation
        gueltigkeitszeitraum: &ref_19
          $ref: '#/components/schemas/Zeitraum'
          description: Referenz auf Zeitraum-ID
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - messlokationsId
        - sparte
        - energierichtung
        - netzebenemessung
        - messgebietNr
        - grundzustaendigerMSBCodeNr
        - messadresse
        - bilanzierungsmethode
        - abrechnungmessstellenbetriebnna
        - gasqualitaet
        - verlustfaktor
        - betriebszustand
        - ablesekartenempfaenger
        - referenzMarktlokationsId
        - verwendungsumfang
        - zukuenftigerMeldepunkt
        - lokationszuordnung
        - beteiligterMarktpartner
        - geraete
        - messdienstleistung
        - messlokationszaehler
        - zaehlwerke
        - marktrollen
        - datenqualitaet
        - gueltigkeitszeitraum
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Messlokation.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zeitraum:
      title: Zeitraum
      type: object
      properties:
        zeiteinheit: &ref_1
          $ref: '#/components/schemas/Zeiteinheit'
          description: nicht in Benutzung
        dauer:
          type: integer
          description: Zeitspanne, Wert
        startdatum:
          type: string
          format: date-time
          description: |-
            Datum aus 
            DTM Z25 Verwendung der Daten ab 
            DTM 163 Verarbeitung, Beginndatum/-zeit
            DTM 155 Rechnungsperiode, Beginndatum
            DTM Z42 vorläufiger Abrechnungszeitraum Beginn
        enddatum:
          type: string
          format: date-time
          description: |-
            Datum aus 
            DTM Z26 Verwendung der Daten bis 
            DTM164 Verarbeitung, Endedatum/-zeit
            DTM 156 Rechnungsperiode, Endedatum
            DTM Z43 vorläufiger Abrechnungszeitraum Ende
        einheit: *ref_1
        ableseZeitraum:
          type: string
          description: |-
            Turnusablesung des NB
            DTM 752
            PI 44113 44140 44142 44043 44168 44169 44060 
        abrechnungsZeitraum:
          type: string
          description: |-
            Termin, zu dem die Netznutzungsabrechnung des NB erfolgt
            DTM Z21
            PI 44112 44139 44142 44002 44013 44014 44035
        zeitraumText:
          type: string
          description: ZeitraumText
          x-apidog-mock: "DTM+Z01:03MQ:Z01'\r\nNachfolgend noch einige Beispiele zur Übermittlung der Kündigungsfrist in der\r\nKommunikation von LF zu LF:\r\nBeispiel 1:\r\nDTM+Z01:30TM:Z01'\r\nDies entspricht der Kündigungsfrist von 30 Tagen zum Monatsende.\r\nBeispiel 2:\r\nDTM+Z01:03MJ:Z01'\r\nDies entspricht der Kündigungsfrist von 3 Monaten zum Jahresende. Somit hat die Kündigung\r\n3 Monate vor dem 31.12. zu erfolgen.\r\nBeispiel 3:\r\nDTM+Z01:01MQ:Z01'\r\nDies entspricht der Kündigungsfrist von 1 Monat zum Quartalsende.\r\nBeispiel 4:\r\nDTM+Z01:01MM:Z01'\r\nDies entspricht der Kündigungsfrist von 1 Monat zum Monatsende.\r\nBeispiel 5:\r\nDTM+Z01:01MT:Z01'\r\nDTM+Z10:201211152300?+00:303'\r\nDies entspricht der Kündigungsfrist von 1 Monat zum 16.11.2012 00:00 Uhr.\r\nBeispiel 6:\r\nDTM+Z01:02WT:Z01'\r\nDTM+Z10:1120:106'\r\nDies entspricht der Kündigungsfrist von 2 Wochen zum 20. eines Monats 00:00 Uhr ab\r\nNovember.\r\nBeispiel 7:\r\nDTM+Z01:14TR:Z01'\r\nDies entspricht einer rollierenden Kündigungsfrist von 14 Tagen in der Zukunft."
        zeitraumId:
          type: integer
          description: |-
            Referenz auf Zeitraum-ID
            RFF Z46
            PI 25001
      x-apidog-orders:
        - zeiteinheit
        - dauer
        - startdatum
        - enddatum
        - einheit
        - ableseZeitraum
        - abrechnungsZeitraum
        - zeitraumText
        - zeitraumId
      required:
        - enddatum
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zeiteinheit:
      type: string
      title: Zeiteinheit
      description: Zeiteinheit
      enum:
        - SEKUNDE
        - MINUTE
        - STUNDE
        - VIERTEL_STUNDE
        - TAG
        - WOCHE
        - MONAT
        - QUARTAL
        - HALBJAHR
        - JAHR
      x-apidog-enum:
        - value: SEKUNDE
          name: ''
          description: ''
        - value: MINUTE
          name: ''
          description: ''
        - value: STUNDE
          name: ''
          description: ''
        - value: VIERTEL_STUNDE
          name: ''
          description: ''
        - value: TAG
          name: Tag
          description: '804'
        - value: WOCHE
          name: Woche
          description: '803'
        - value: MONAT
          name: Monat
          description: '802'
        - value: QUARTAL
          name: ''
          description: ''
        - value: HALBJAHR
          name: ''
          description: ''
        - value: JAHR
          name: ''
          description: ''
      x-apidog-folder: ''
    Datenqualitaet:
      type: string
      title: Datenqualitaet
      description: Datenqualitaet
      enum:
        - ERWARTETE_DATEN
        - IM_SYSTEM_VORHANDENE_DATEN
        - INFORMATIVE_DATEN
        - GUELTIGE_DATEN
        - KEINE_DATEN
        - IM_SYSTEM_KEINE_DATEN_VORHANDEN
        - KEINE_DATEN_ERWARTET
        - DIFFERENZ_DATEN
        - DIFFERENZ_ERWARTETE_DATEN
        - DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN
      x-apidog-enum:
        - value: ERWARTETE_DATEN
          name: ''
          description: abhängig vom BO
        - value: IM_SYSTEM_VORHANDENE_DATEN
          name: ''
          description: abhängig vom BO
        - value: INFORMATIVE_DATEN
          name: ''
          description: abhängig vom BO
        - value: GUELTIGE_DATEN
          name: ''
          description: abhängig vom BO
        - value: KEINE_DATEN
          name: ''
          description: abhängig vom BO
        - value: IM_SYSTEM_KEINE_DATEN_VORHANDEN
          name: ''
          description: abhängig vom BO
        - value: KEINE_DATEN_ERWARTET
          name: ''
          description: abhängig vom BO
        - value: DIFFERENZ_DATEN
          name: ''
          description: abhängig vom BO
        - value: DIFFERENZ_ERWARTETE_DATEN
          name: ''
          description: abhängig vom BO
        - value: DIFFERENZ_IM_SYSTEM_VORHANDENE_DATEN
          name: ''
          description: abhängig vom BO
      x-apidog-folder: ''
    Zaehlwerk:
      title: Zaehlwerk
      type: object
      properties:
        zaehlwerkId:
          type: string
          description: >-
            Identifikation des Zählwerks (Registers) innerhalb des Zählers.
            Oftmals eine laufende Nummer hinter der

            Zählernummer. Z.B. 47110815_1
        bezeichnung:
          type: string
          description: >-
            Bezeichnung des Zählwerks auf dem Gerät, dient zur Identifizierung
            und Beschreibung der lokalen Kennzeichnung auf dem Gerät (z. B. HT
            oder NT)

            CCI Z63

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55168 55169
        richtung: *ref_2
        obisKennzahl:
          type: string
          description: >-
            Produktidentifikation bei Austausch von Daten der Energiemengen
            werden gewährleistet durch OBIS Kennzahlen.

            PIA 5 OBIS-Kennzahl der Netzlokation

            PI 55639 55644 55649 55654 55659 55664 55060 55043 55168 55169

            PIA 5 OBIS-Kennzahl der Marktlokation

            PI 55684 55685 55640 55645 55650 55655 55660 55665 55553 55555 55035
            55095 55060 55043 55168 55169 55239 55074 55075 55076 55195 55196 

            RFF Z10 Referenz auf die OBIS-Kennzahl der Marktlokation

            PI 55616 55622 

            PIA 5 OBIS-Daten der Marktlokation der beteiligten Marktrolle

            PI 55196

            PIA 5 OBIS-Kennzahl der Tranche

            PI 55686 55687 55642 55647 55652 55657 55662 55667 55095 55074 55075
            55076 55195 55196

            PIA 5 OBIS-Kennzahl der Zähleinrichtung /Smartmeter-Gateway

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55035 55095 55060
            55043 55168 55169 55074 55075 55076
        wandlerfaktor:
          type: number
          format: float
          description: >-
            Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um
            zum eigentlichen Verbrauch im Zeitraum zu

            kommen.
        einheit: &ref_24
          $ref: '#/components/schemas/Mengeneinheit'
          description: Die Einheit der gemessenen Größe, z.B. kWh. Details Mengeneinheit
        schwachlastfaehig: &ref_3
          $ref: '#/components/schemas/Schwachlastfaehig'
          description: >-
            Schwachlastfähigkeit, die Beschreibung der Schwachlastfähigkeit wird
            für die Konzessionsabgabe genutzt. 

            CCI Z10

            PI 55643 55648 55653 55658 55663 55669
        verbrauchsart:
          type: array
          items: &ref_13
            $ref: '#/components/schemas/Verbrauchsart'
          description: >-
            Angabe für welchen Verwendungszweck die Stromentnahme an der
            OBIS-Kennzahl der Marktlokation erfolgt. Definiert den
            Verwendungszweck des Stroms: 

            CAV Z64

            PI 55616 55622 55035 
        unterbrechbarkeit:
          $ref: '#/components/schemas/Unterbrechbarkeit'
          description: >-
            Unterbrechbarkeit Marktlokation, Angabe, ob eine Unterbrechung der
            Verbrauchseinrichtung durch den Netzbetreiber möglich ist.

            CAV Z62

            PI 55616 55622 55035
        waermenutzung:
          $ref: '#/components/schemas/Waermenutzung'
          description: >-
            Wärmenutzung Marktlokation, im Falle der Wärmenutzung wird eine
            genauere Angabe über die Wärmenutzung definiert.

            CAV Z56

            PI 55616 55622 55617 55623 55629 55635 55035 55060 55043 55168 55169
        konzessionsabgabe:
          $ref: '#/components/schemas/Konzessionsabgabe'
          description: |-
            Konzessionsabgabedaten
            CCI Z08
            PI 44112 44139 44142 44001 44002 44013 44014 44035
        steuerbefreit:
          type: boolean
          description: Steuerbefreit
        vorkommastelle:
          type: integer
          description: >-
            Angabe der Vorkommastelle des Zählwerks

            CAV Wert

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55043 55168 55169
            55074 55075 55076
        nachkommastelle:
          type: integer
          description: >-
            Angabe der Nachkommastelle des Zählwerks

            CAV Wert

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55043 55168 55169
            55074 55075 55076
        abrechnungsrelevant:
          type: boolean
          description: Abrechnungsrelevant
        anzahlAblesungen:
          type: integer
          description: Anzahl Ablesungen
        zaehlzeiten: &ref_23
          $ref: '#/components/schemas/Zaehlzeitregister'
          description: Zugeordnete Zählzeitdefinition
        konfiguration:
          type: string
          description: >-
            Angabe der Konfigurations-ID

            RFF AGK

            PI 55643 55648 55653 55658 55663 55669 55553 55555 55035 55095 55060
            55043 55168 55169 55074 55075 55076
        messprodukt:
          type: string
          description: |-
            Erforderliches Messprodukt Z11 der Malo/ Tranche/ Melo
            PIA 5
            PI 55043 55168 55169 
            Messprodukt der Tranche
            PI 55060 55043 55168 55169 
            Messprodukt der Messlokation
            PI 55060 55043 55168 55169
            Erforderliches Produkt der Marktlokation ORDERS 
            PI 17123 17121 17134
            Erforderliches Produkt der Tranche ORDERS 
            PI 17121 17134 
            Erforderliches Produkt der Messlokation ORDERS 
            PI 17121 17118 17003 17134 17135
            Erforderliches Produkt der Netzlokation ORDERS
            PI 17121 17003
        wertegranularitaet:
          $ref: '#/components/schemas/Wertegranularitaet'
          description: >-
            Mit der Wertegranularität wird angegeben in welchem Intervall Werte
            der im PIA+5 genannten OBIS-Kennzahl im Markt

            bereitgestellt werden. ZD9 Jährlich ZE8 Halbjährlich ZE9
            Quartalsweise ZB7 Monatlich

            CCI ZE4

            PI 55640 55645 55650 55655 55660 55665 55643 55648 55653 55658 55663
            55669 55553 55555 55035 55095 55060 55043 55168 55169 55074 55075
            55076
        notwendigkeitZweiteMessung:
          $ref: '#/components/schemas/NotwendigkeitZweiteMessung'
          description: >-
            Weitere Beschreibung erforderliches Messprodukt, Notwendigkeit einer
            zweiten Messung vorhanden oder nicht vorhanden. Der Wert dient dem
            MSB zur Ermittlung, Plausibilisierung oder auch Ersatzwertbildung an
            der Melo. 

            CAV ZC9

            PI 55060 55043 55168 55169

            ORDERS PI 17121 17118
        werteuebermittlungVerwendungszweck:
          $ref: '#/components/schemas/WerteuebermittlungVerwendungszweck'
          description: >-
            Werteübermitlung an den NB aufgrund weiterem Verwendungszweck
            vorhanden oder nicht vorhanden. Das wird benötigt, da noch nicht
            alle Berechnungsformeln für Abrechnungszwecke ausgetauscht werden
            können.  

            CCI Z88

            PI 55060 55043 55168 55169

            ORDERS PI 17121 17118
        artEMobilitaet:
          $ref: '#/components/schemas/ArtEmobilitaet'
          description: >-
            Art der E-Mobilität, im Falle der E-Mobilität wird eine genauere
            Angabe über die Art definitiert. 

            CAV Z87

            PI 55616 55622 55617 55623 55629 55635 55035 55060 55043 55168 55169
        konfigurationsprodukt:
          type: string
          description: Konfigurationsprodukt
        keinKonfigurationsprodukt:
          type: boolean
          description: Kein Konfigurationsprodukt
        leistungskurvendefinition:
          type: string
          description: Leistungskurvendefinition
        verwendungszwecke:
          type: array
          items:
            $ref: '#/components/schemas/Verwendungszweck'
          description: Verwendungungszweck der Werte Marktlokation, Tranche
        verwendungszweckNB:
          type: string
          description: Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck NB
        verwendungszweckLF:
          type: string
          description: Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck LF
        verwendungszweckUENB:
          type: string
          description: Codes gemäß Codeliste der Verwendungszwecke Verwendungszweck ÜNB
        keinProdukt:
          type: boolean
          description: 'CCI+11++ZF6: keinProdukt zugeordnet'
      x-apidog-orders:
        - zaehlwerkId
        - bezeichnung
        - richtung
        - obisKennzahl
        - wandlerfaktor
        - einheit
        - schwachlastfaehig
        - verbrauchsart
        - unterbrechbarkeit
        - waermenutzung
        - konzessionsabgabe
        - steuerbefreit
        - vorkommastelle
        - nachkommastelle
        - abrechnungsrelevant
        - anzahlAblesungen
        - zaehlzeiten
        - konfiguration
        - messprodukt
        - wertegranularitaet
        - notwendigkeitZweiteMessung
        - werteuebermittlungVerwendungszweck
        - artEMobilitaet
        - konfigurationsprodukt
        - keinKonfigurationsprodukt
        - leistungskurvendefinition
        - verwendungszwecke
        - verwendungszweckNB
        - verwendungszweckLF
        - verwendungszweckUENB
        - keinProdukt
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Verwendungszweck:
      title: Verwendungszweck
      type: object
      properties:
        marktrolle: &ref_8
          $ref: '#/components/schemas/Marktrolle'
          description: >-
            Identifizierung der Marktrolle

            CCI ZA8

            PI 55639 55644 55659 55664 55043 55168 55169 55649 55654 55684 55685
            55686 55687 55660 55665 55662 55667 

            ORDERS PI 17121 17134
        zweck:
          type: array
          items:
            $ref: '#/components/schemas/VerwendungszweckValue'
          description: >-
            Verwendungszweck der Werte

            CAV Z47

            PI 55639 55644 55659 55664 55043 55168 55169 55649 55654 55640 55645
            55660 55665 55650 55655 

            PI 55684 55685 55686 55687 55662 55667 

            ORDERS

            PI 17121 17134
      x-apidog-orders:
        - marktrolle
        - zweck
      description: .
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    VerwendungszweckValue:
      type: string
      title: VerwendungszweckValue
      description: VerwendungszweckValue
      enum:
        - NETZNUTZUNGSABRECHNUNG
        - BILANZKREISABRECHNUNG
        - MEHRMINDERMENGENABRECHNUNG
        - ENDKUNDENABRECHNUNG
        - UEBERMITTLUNG_AN_DAS_HKNR
        - BLINDARBEITSABRECHNUNG
        - ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS
        - BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG
        - ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR
      x-apidog-enum:
        - value: NETZNUTZUNGSABRECHNUNG
          name: Netznutzungsabrechnung
          description: Z84
        - value: BILANZKREISABRECHNUNG
          name: Bilanzkreisabrechnung
          description: Z85
        - value: MEHRMINDERMENGENABRECHNUNG
          name: Mehrmindermengenabrechnung
          description: Z86
        - value: ENDKUNDENABRECHNUNG
          name: Endkundenabrechnung
          description: Z47
        - value: UEBERMITTLUNG_AN_DAS_HKNR
          name: Übermitlung an das HKNR
          description: Z92
        - value: BLINDARBEITSABRECHNUNG
          name: ''
          description: ''
        - value: ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS
          name: Zur Ermitlung der Ausgeglichenheit von Bilanzkreisen
          description: ZB5
        - value: BLINDARBEITABRECHNUNG_BETRIEBSFUEHRUNG
          name: Blindarbeitabrechnung / Betriebsführung
          description: ZD1
        - value: ES_LIEGT_KEIN_VERWENDUNGSZWECK_VOR
          name: Es liegt kein Verwendungszweck vor
          description: ZE1
      x-apidog-folder: ''
    Marktrolle:
      type: string
      title: Marktrolle
      description: Diese Rollen kann ein Marktteilnehmer einnehmen
      enum:
        - NB
        - LF
        - MSB
        - MSBA
        - GMSB
        - MDL
        - DL
        - BKV
        - UENB
        - KUNDE-SELBST-NN
        - MGV
        - EIV
        - RB
        - KUNDE
        - INTERESSENT
        - KN
        - UBA
        - BIKO
        - ESA
      x-apidog-enum:
        - value: NB
          name: Netzbetreiber
          description: Z88
        - value: LF
          name: Lieferant
          description: Z89
        - value: MSB
          name: Messstellenbetreiber
          description: Z91
        - value: MSBA
          name: Messstellenbetreiber Alt
          description: ZB4
        - value: GMSB
          name: Grundzuständiger Messstellenbetreiber
          description: ZF0
        - value: MDL
          name: ''
          description: ''
        - value: DL
          name: ''
          description: ''
        - value: BKV
          name: ''
          description: ''
        - value: UENB
          name: Übertragungsnetzbetreiber
          description: Z90
        - value: KUNDE-SELBST-NN
          name: ''
          description: ''
        - value: MGV
          name: ''
          description: ''
        - value: EIV
          name: ''
          description: ''
        - value: RB
          name: ''
          description: ''
        - value: KUNDE
          name: ''
          description: ''
        - value: INTERESSENT
          name: ''
          description: ''
        - value: KN
          name: ''
          description: ''
        - value: UBA
          name: ''
          description: ''
        - value: BIKO
          name: ''
          description: ''
        - value: ESA
          name: ''
          description: ''
      x-apidog-folder: ''
    ArtEmobilitaet:
      type: string
      title: ArtEmobilitaet
      description: ArtEmobilitaet
      enum:
        - WB
        - LS
        - LP
      x-apidog-enum:
        - value: WB
          name: Wallbox
          description: ZE6
        - value: LS
          name: E-Mobilitätsladesäule
          description: Z87
        - value: LP
          name: Ladepark
          description: ZE7
      x-apidog-folder: ''
    WerteuebermittlungVerwendungszweck:
      type: string
      title: WerteuebermittlungVerwendungszweck
      description: Werteübermitlung an den NB aufgrund weiterem Verwendungszweck
      enum:
        - VORHANDEN
        - NICHT_VORHANDEN
      x-apidog-enum:
        - value: VORHANDEN
          name: vorhanden
          description: Z06
        - value: NICHT_VORHANDEN
          name: nicht vorhanden
          description: Z07
      x-apidog-folder: ''
    NotwendigkeitZweiteMessung:
      type: string
      title: NotwendigkeitZweiteMessung
      description: NotwendigkeitZweiteMessung
      enum:
        - VORHANDEN
        - NICHT_VORHANDEN
      x-apidog-enum:
        - value: VORHANDEN
          name: vorhanden
          description: Z06
        - value: NICHT_VORHANDEN
          name: nicht vorhanden
          description: Z07
      x-apidog-folder: ''
    Wertegranularitaet:
      type: string
      title: Wertegranularitaet
      description: Wertegranularitaet
      enum:
        - JAEHRLICH
        - HALBJAEHRLICH
        - QUARTALSWEISE
        - MONATLICH
      x-apidog-enum:
        - value: JAEHRLICH
          name: Jährlich
          description: ZD9
        - value: HALBJAEHRLICH
          name: Halbjährlich
          description: ZE8
        - value: QUARTALSWEISE
          name: Quartalsweise
          description: ZE9
        - value: MONATLICH
          name: Monatlich
          description: ZB7
      x-apidog-folder: ''
    Zaehlzeitregister:
      title: Zaehlzeitregister
      type: object
      properties:
        register:
          type: string
          description: >-
            Code des Zählzeitregisters

            CCI Z38 

            PI 55218 55220 55640 55645 55650 55655 55660 55665 55643 55648 55653
            55658 55663 55669 55553 55555 55035 55060 55043 55168 55169 

            UTILTS CCI Z38

            PI 25004
        zaehlzeitDefinition:
          type: string
          description: >-
            Code der Zählzeitdefinition

            CCI Z39

            PI 55218 55220 55035 55640 55645 55650 55655 55660 55665 55643 55648
            55653 55658 55663 55669 55553 55555 55060 55043 55168 55169

            CCI Z41 Keine Zählzeit für Messprodukt erforderlich

            PI 55060 55043 55168 55169

            Z39 Code der Zählzeitdefinition ORDERS

            Z41 Keine Zählzeit für Messprodukt erforderlich ORDERS

            CCI Z39

            PI 17123 17121 17118 17134 17135

            UTILTS RFF Z27

            PI 25004
        schwachlastfaehig: *ref_3
      x-apidog-orders:
        - register
        - zaehlzeitDefinition
        - schwachlastfaehig
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Konzessionsabgabe:
      title: Konzessionsabgabe
      type: object
      properties:
        satz:
          $ref: '#/components/schemas/AbgabeArt'
          description: |-
            Gruppen der KAV
            CAV KAS
        kosten:
          type: number
          format: float
          description: Konzessionsabgabe in Euro/kWh
        kategorie:
          type: string
          description: >-
            Gebührenkategorie der Konzessionsabgabe - Übermittlung von
            zusätzlichen Informationen
      x-apidog-orders:
        - satz
        - kosten
        - kategorie
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    AbgabeArt:
      type: string
      title: AbgabeArt
      description: Art der Konzessionsabgabe
      enum:
        - KAS
        - SA
        - SAS
        - TA
        - TAS
        - TK
        - TKS
        - TS
        - TSS
      x-apidog-enum:
        - value: KAS
          name: >-
            für alle konzessionsvertraglichen Sonderregelungen, die nicht in die
            Systematik der KAV eingegliedert sind
          description: KAS
        - value: SA
          name: >-
            Sondervertragskunden < 1 kV nach § 2 (7) und > 1 kV, Preis nach § 2
            (3) (für Strom 0,11 ct/ kWh und für Gas 0,03 ct/kWh)
          description: SA
        - value: SAS
          name: >-
            Kennzeichnung, dass ein abweichender Preis für Sondervertragskunden
            vorliegt
          description: SAS
        - value: TA
          name: >-
            Tarifkunden, für Strom § 2. (2) 1b HT bzw. ET (hohe KA) und für Gas
            § 2 (2) 2b
          description: TA
        - value: TAS
          name: Kennzeichnung, dass ein abweichender Preis für Tarifkunden vorliegt
          description: TAS
        - value: TK
          name: >-
            für Gas nach KAV § 2 (2) 2a bei ausschließlicher Nutzung zum Kochen
            und Warmwassererzeugung
          description: TK
        - value: TKS
          name: >-
            Kennzeichnung, wenn nach KAV § 2 (2) 2a ein anderer Preis zu
            verwenden ist
          description: TKS
        - value: TS
          name: ''
          description: ''
        - value: TSS
          name: ''
          description: ''
      x-apidog-folder: ''
    Waermenutzung:
      type: string
      title: Waermenutzung
      description: Waermenutzung
      enum:
        - SPEICHERHEIZUNG
        - WAERMEPUMPE
        - DIREKTHEIZUNG
        - WAERMEPUMPE_WAERME_KAELTE
        - WAERMEPUMPE_KAELTE
        - WAERMEPUMPE_WAERME
      x-apidog-enum:
        - value: SPEICHERHEIZUNG
          name: Speicherheizung
          description: Z56
        - value: WAERMEPUMPE
          name: Wärmepumpe (unspezifiziert)
          description: Z57
        - value: DIREKTHEIZUNG
          name: Direktheizung
          description: Z61
        - value: WAERMEPUMPE_WAERME_KAELTE
          name: Wärmepumpe (Wärme und Kälte)
          description: ZV5
        - value: WAERMEPUMPE_KAELTE
          name: Wärmepumpe (Kälte)
          description: ZV6
        - value: WAERMEPUMPE_WAERME
          name: Wärmepumpe (Wärme)
          description: ZV7
      x-apidog-folder: ''
    Unterbrechbarkeit:
      type: string
      title: Unterbrechbarkeit
      description: Unterbrechbarkeit
      enum:
        - UV
        - NUV
      x-apidog-enum:
        - value: UV
          name: unterbrechbare Verbrauchseinrichtung
          description: Z62
        - value: NUV
          name: nicht-unterbrechbare Verbrauchseinrichtung
          description: Z63
      x-apidog-folder: ''
    Verbrauchsart:
      type: string
      title: Verbrauchsart
      description: Verbrauchsart
      enum:
        - KL
        - W
        - EMOB
        - SB
        - SW
        - WK
      x-apidog-enum:
        - value: KL
          name: Kraft/Licht
          description: Z64
        - value: W
          name: ''
          description: ''
        - value: EMOB
          name: E-Mobilität
          description: ZE5
        - value: SB
          name: Straßenbeleuchtung
          description: ZA8
        - value: SW
          name: Steuerung Wärmeabgabe
          description: ZB3
        - value: WK
          name: Wärme/Kälte
          description: Z65
      x-apidog-folder: ''
    Schwachlastfaehig:
      type: string
      title: Schwachlastfaehig
      description: Schwachlastfaehig
      enum:
        - SCHWACHLASTFAEHIG
        - NICHT_SCHWACHLASTFAEHIG
      x-apidog-enum:
        - value: SCHWACHLASTFAEHIG
          name: Schwachlast fähig
          description: Z60
        - value: NICHT_SCHWACHLASTFAEHIG
          name: Nicht-Schwachlast fähig
          description: Z59
      x-apidog-folder: ''
    Mengeneinheit:
      type: string
      title: Mengeneinheit
      description: >-
        Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden
        können
      enum:
        - W
        - WH
        - KW
        - KWH
        - KVARH
        - MW
        - MWH
        - STUECK
        - KUBIKMETER
        - STUNDE
        - TAG
        - MONAT
        - JAHR
        - PROZENT
        - ANZAHL
        - VAR
        - KVAR
        - VARH
        - KWHK
        - Z16
        - KWT
      x-apidog-enum:
        - value: W
          name: ''
          description: ''
        - value: WH
          name: ''
          description: ''
        - value: KW
          name: ''
          description: ''
        - value: KWH
          name: Kilowattstunde
          description: KWH
        - value: KVARH
          name: ''
          description: ''
        - value: MW
          name: ''
          description: ''
        - value: MWH
          name: ''
          description: ''
        - value: STUECK
          name: Stück
          description: H87
        - value: KUBIKMETER
          name: ''
          description: ''
        - value: STUNDE
          name: ''
          description: ''
        - value: TAG
          name: Tag
          description: ZD8
        - value: MONAT
          name: Monat
          description: MON
        - value: JAHR
          name: Jahr
          description: ANN
        - value: PROZENT
          name: Prozent
          description: P1
        - value: ANZAHL
          name: ''
          description: ''
        - value: VAR
          name: ''
          description: ''
        - value: KVAR
          name: ''
          description: ''
        - value: VARH
          name: ''
          description: ''
        - value: KWHK
          name: ''
          description: ''
        - value: Z16
          name: kWh/K (Kilowatt-Stunde/Kelvin)
          description: Z16
        - value: KWT
          name: Kilowatt
          description: ''
      x-apidog-folder: ''
    Dienstleistung:
      title: Dienstleistung
      type: object
      properties:
        dienstleistungstyp:
          $ref: '#/components/schemas/Dienstleistungstyp'
          description: Eindeutige Nummer der Dienstleistung. Details Dienstleistungstyp
        bezeichnung:
          type: string
          description: Bezeichnung der Dienstleistung.
      x-apidog-orders:
        - dienstleistungstyp
        - bezeichnung
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Dienstleistungstyp:
      title: Dienstleistungstyp
      type: string
      enum:
        - DATENBEREITSTELLUNG_TAEGLICH
        - DATENBEREITSTELLUNG_WOECHENTLICH
        - DATENBEREITSTELLUNG_MONATLICH
        - DATENBEREITSTELLUNG_JAEHRLICH
        - DATENBEREITSTELLUNG_HISTORISCHE_LG
        - DATENBEREITSTELLUNG_STUENDLICH
        - DATENBEREITSTELLUNG_VIERTELJAEHRLICH
        - DATENBEREITSTELLUNG_HALBJAEHRLICH
        - DATENBEREITSTELLUNG_MONATLICH_ZUSAETZLICH
        - DATENBEREITSTELLUNG_EINMALIG
        - AUSLESUNG_2X_TAEGLICH_FERNAUSLESUNG
        - AUSLESUNG_TAEGLICH_FERNAUSLESUNG
        - AUSLESUNG_LGK_MANUELL_MSB
        - AUSLESUNG_MONATLICH_SLP_FERNAUSLESUNG
        - AUSLESUNG_JAEHRLICH_SLP_FERNAUSLESUNG
        - AUSLESUNG_MDE_SLP
        - ABLESUNG_MONATLICH_SLP
        - ABLESUNG_VIERTELJAEHRLICH_SLP
        - ABLESUNG_HALBJAEHRLICH_SLP
        - ABLESUNG_JAEHRLICH_SLP
        - AUSLESUNG_SLP_FERNAUSLESUNG
        - ABLESUNG_SLP_ZUSAETZLICH_MSB
        - ABLESUNG_SLP_ZUSAETZLICH_KUNDE
        - AUSLESUNG_LGK_FERNAUSLESUNG_ZUSAETZLICH_MSB
        - AUSLESUNG_MOATLICH_FERNAUSLESUNG
        - AUSLESUNG_STUENDLICH_FERNAUSLESUNG
        - ABLESUNG_MONATLICH_LGK
        - AUSLESUNG_TEMERATURMENGENUMWERTER
        - AUSLESUNG_ZUSTANDSMENGENUMWERTER
        - AUSLESUNG_SYSTEMMENGENUMWERTER
        - AUSLESUNG_VORGANG_SLP
        - AUSLESUUNG_KOMPAKTMENGENUMWERTER
        - AUSLESUNG_MDE_LGK
        - SPERRUNG_SLP
        - ENTSPERRUNG_SLP
        - SPERRUNG_RLM
        - ENTSPERRUNG_RLM
        - MAHNKOSTEN
        - INKASSOKOSTEN
      description: Auflistung möglicher abzurechnender Dienstleistungen
      x-apidog-folder: ''
    Geraet:
      title: Geraet
      type: object
      properties:
        geraetetyp: &ref_4
          $ref: '#/components/schemas/Geraetetyp'
        bezeichnung:
          type: string
          description: Bezeichnung des Gerätes
        geraetenummer:
          type: string
          description: >-
            Angabe der Referenz auf die Gerätenummer des Zählers /
            Smartmeter-Gateway / Wandler

            RFF Z14 Smartmeter-Gateway

            PI 55643 55648 55653 55658 55663 55669 55043 55168 55169 55074 55075
            55076 

            CAV Z30 Gerätenummer

            55643 55648 55653 55658 55663 55669 55060 55043 55168 55169 55074
            55075 55076 

            ORDERS RFF Z09  

            PI 17101 17126 17009 
        geraetereferenz:
          type: string
          description: Gäaetereferenz
        geraeteeigenschaften:
          $ref: '#/components/schemas/Geraeteeigenschaften'
          description: Festlegung der Eigenschaften des Gerätes. Z.B. Wandler MS/NS.
        volumenerfassung: &ref_5
          $ref: '#/components/schemas/Volumenerfassung'
          description: Art der Volumenerfassung
        weitereGeraetenummern:
          type: array
          items:
            type: string
          description: weitere Gäaetenummern
      x-apidog-orders:
        - geraetetyp
        - bezeichnung
        - geraetenummer
        - geraetereferenz
        - geraeteeigenschaften
        - volumenerfassung
        - weitereGeraetenummern
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Volumenerfassung:
      type: string
      title: Volumenerfassung
      description: Art der Volumenerfassung
      enum:
        - HOCHFREQUENZSONDE
        - KENNLINIENKORREKTUR
        - SCHLEICHMENGENUNTERDRUECKUNG
      x-apidog-enum:
        - value: HOCHFREQUENZSONDE
          name: Hochfrequenzsonde
          description: Z16
        - value: KENNLINIENKORREKTUR
          name: Kennlinienkorrektur
          description: Z17
        - value: SCHLEICHMENGENUNTERDRUECKUNG
          name: Schleichmengenunterdrückung
          description: Z18
      x-apidog-folder: ''
    Geraeteeigenschaften:
      title: Geraeteeigenschaften
      type: object
      properties:
        geraetetyp: *ref_4
        geraetemerkmal:
          $ref: '#/components/schemas/Geraetemerkmal'
          description: >-
            Wandlertyp und Faktor

            CAV MIW

            PI 55643 55648 55653 55658 55663 55669 55060 55043 55168 55169 55074
            55075 55076 

            QUOTES PI 15001
        faktor:
          type: number
          format: float
          description: >-
            Wandlerfaktor - Angabe der Wandlerkonstante

            PI 55643 55648 55653 55658 55663 55669 55060 55043 55168 55169 55074
            55075 55076 

            QUOTES PI 15001
        serialnummer:
          type: string
        herstellungsdatum:
          type: string
        baujahr:
          type: string
        eichungBis:
          type: string
        volumenerfassung: *ref_5
        firmwareVersion:
          type: string
          description: Firmware-Version
        herstellerTypbezeichnung:
          type: string
          description: Hersteller-Typbezeichnung
        simKartenNummer:
          type: string
          description: SIM-Kartennummer
        modemKennungIMSI:
          type: string
          description: Modem-Kennung (IMSI)
        tkProvider:
          type: string
          description: Telekommunikationsanbieter
        ipVersion:
          type: string
          description: IP-Version
      x-apidog-orders:
        - geraetetyp
        - geraetemerkmal
        - faktor
        - serialnummer
        - herstellungsdatum
        - baujahr
        - eichungBis
        - volumenerfassung
        - firmwareVersion
        - herstellerTypbezeichnung
        - simKartenNummer
        - modemKennungIMSI
        - tkProvider
        - ipVersion
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Geraetemerkmal:
      type: string
      title: Geraetemerkmal
      description: Geraetemerkmal
      enum:
        - EINTARIF
        - ZWEITARIF
        - MEHRTARIF
        - GAS_G2P5
        - GAS_G4
        - GAS_G6
        - GAS_G10
        - GAS_G16
        - GAS_G25
        - GAS_G40
        - GAS_G65
        - GAS_G100
        - GAS_G160
        - GAS_G250
        - GAS_G350
        - GAS_G400
        - GAS_G4000
        - GAS_G650
        - GAS_G6500
        - GAS_G1000
        - GAS_G10000
        - GAS_G12500
        - GAS_G1600
        - GAS_G16000
        - GAS_G2500
        - IMPULSGEBER_G4_G100
        - IMPULSGEBER_G100
        - MODEM_GSM
        - MODEM_GPRS
        - MODEM_FUNK
        - MODEM_GSM_O_LG
        - MODEM_GSM_M_LG
        - MODEM_FESTNETZ
        - MODEM_GPRS_M_LG
        - PLC_COM
        - ETHERNET_KOM
        - DSL_KOM
        - LTE_KOM
        - RUNDSTEUEREMPFAENGER
        - TARIFSCHALTGERAET
        - ZUSTANDS_MU
        - TEMPERATUR_MU
        - KOMPAKT_MU
        - SYSTEM_MU
        - UNBESTIMMT
        - WASSER_MWZW
        - WASSER_WZWW
        - WASSER_WZ01
        - WASSER_WZ02
        - WASSER_WZ03
        - WASSER_WZ04
        - WASSER_WZ05
        - WASSER_WZ06
        - WASSER_WZ07
        - WASSER_WZ08
        - WASSER_WZ09
        - WASSER_WZ10
        - WASSER_VWZ04
        - WASSER_VWZ05
        - WASSER_VWZ06
        - WASSER_VWZ07
        - WASSER_VWZ10
        - DICHTEMENGENUMWERTER
        - TEMPERATURMENGENUMWERTER
        - ZUSTANDSMENGENUMWERTER
        - BLOCKSTROMWANDLER
        - MESSWANDLERSATZ_IMS_MME
        - KOMBIMESSWANDLER
        - SPANNUNGSWANDLER
      x-apidog-enum:
        - value: EINTARIF
          name: ''
          description: ''
        - value: ZWEITARIF
          name: ''
          description: ''
        - value: MEHRTARIF
          name: ''
          description: ''
        - value: GAS_G2P5
          name: Gaszähler G2.5
          description: G2.5
        - value: GAS_G4
          name: Gaszähler G4
          description: G4
        - value: GAS_G6
          name: Gaszähler G6
          description: G6
        - value: GAS_G10
          name: Gaszähler G10
          description: G10
        - value: GAS_G16
          name: Gaszähler G16
          description: G16
        - value: GAS_G25
          name: Gaszähler G25
          description: G25
        - value: GAS_G40
          name: Gaszähler G40
          description: G40
        - value: GAS_G65
          name: Gaszähler G65
          description: G65
        - value: GAS_G100
          name: Gaszähler G100
          description: G100
        - value: GAS_G160
          name: Gaszähler G160
          description: G160
        - value: GAS_G250
          name: Gaszähler G250
          description: G250
        - value: GAS_G350
          name: Gaszähler G350
          description: G350
        - value: GAS_G400
          name: Gaszähler G400
          description: G400
        - value: GAS_G4000
          name: Gaszähler G4000
          description: G4000
        - value: GAS_G650
          name: Gaszähler G650
          description: G650
        - value: GAS_G6500
          name: Gaszähler G6500
          description: G6500
        - value: GAS_G1000
          name: Gaszähler G1000
          description: G1000
        - value: GAS_G10000
          name: Gaszähler G10000
          description: G10000
        - value: GAS_G12500
          name: Gaszähler G12500
          description: G12500
        - value: GAS_G1600
          name: Gaszähler G1600
          description: G1600
        - value: GAS_G16000
          name: Gaszähler G16000
          description: G16000
        - value: GAS_G2500
          name: Gaszähler G2500
          description: G2500
        - value: IMPULSGEBER_G4_G100
          name: ''
          description: ''
        - value: IMPULSGEBER_G100
          name: ''
          description: ''
        - value: MODEM_GSM
          name: GSM/GPRS/UMTS-Kom.-Einr.
          description: GSM
        - value: MODEM_GPRS
          name: ''
          description: ''
        - value: MODEM_FUNK
          name: ''
          description: ''
        - value: MODEM_GSM_O_LG
          name: ''
          description: ''
        - value: MODEM_GSM_M_LG
          name: ''
          description: ''
        - value: MODEM_FESTNETZ
          name: Festnetz-Kom.-Einricht. TAE
          description: PST
        - value: MODEM_GPRS_M_LG
          name: ''
          description: ''
        - value: PLC_COM
          name: PLC-Kom.-Einrichtung
          description: PLC
        - value: ETHERNET_KOM
          name: Ethernet-Kom.-Einricht. LAN/WLAN
          description: ETH
        - value: DSL_KOM
          name: DSL-Kom.Einr.
          description: DSL
        - value: LTE_KOM
          name: LTE-Kom.-Einr.
          description: LTE
        - value: RUNDSTEUEREMPFAENGER
          name: Rundsteuerempfänger
          description: RSU
        - value: TARIFSCHALTGERAET
          name: Tarifschaltuhr
          description: TSU
        - value: ZUSTANDS_MU
          name: ''
          description: ''
        - value: TEMPERATUR_MU
          name: ''
          description: ''
        - value: KOMPAKT_MU
          name: ''
          description: ''
        - value: SYSTEM_MU
          name: ''
          description: ''
        - value: UNBESTIMMT
          name: ''
          description: ''
        - value: WASSER_MWZW
          name: ''
          description: ''
        - value: WASSER_WZWW
          name: ''
          description: ''
        - value: WASSER_WZ01
          name: ''
          description: ''
        - value: WASSER_WZ02
          name: ''
          description: ''
        - value: WASSER_WZ03
          name: ''
          description: ''
        - value: WASSER_WZ04
          name: ''
          description: ''
        - value: WASSER_WZ05
          name: ''
          description: ''
        - value: WASSER_WZ06
          name: ''
          description: ''
        - value: WASSER_WZ07
          name: ''
          description: ''
        - value: WASSER_WZ08
          name: ''
          description: ''
        - value: WASSER_WZ09
          name: ''
          description: ''
        - value: WASSER_WZ10
          name: ''
          description: ''
        - value: WASSER_VWZ04
          name: ''
          description: ''
        - value: WASSER_VWZ05
          name: ''
          description: ''
        - value: WASSER_VWZ06
          name: ''
          description: ''
        - value: WASSER_VWZ07
          name: ''
          description: ''
        - value: WASSER_VWZ10
          name: ''
          description: ''
        - value: DICHTEMENGENUMWERTER
          name: Dichtemengenumwerter
          description: DMU
        - value: TEMPERATURMENGENUMWERTER
          name: Temperaturmengenumwerter
          description: TMU
        - value: ZUSTANDSMENGENUMWERTER
          name: Zustandsmengenumwerter
          description: ZMU
        - value: BLOCKSTROMWANDLER
          name: Blockstromwandler
          description: MBW
        - value: MESSWANDLERSATZ_IMS_MME
          name: Messwandlersatz Strom
          description: MIW
        - value: KOMBIMESSWANDLER
          name: Kombimesswandlersatz (Strom und Spannung)
          description: MPW
        - value: SPANNUNGSWANDLER
          name: Messwandlersatz Spannung
          description: MUW
      x-apidog-folder: ''
    Geraetetyp:
      type: string
      title: Geraetetyp
      description: Auflistung möglicher abzurechnender Gerätetypen
      enum:
        - WECHSELSTROMZAEHLER
        - DREHSTROMZAEHLER
        - ZWEIRICHTUNGSZAEHLER
        - RLM_ZAEHLER
        - IMS_ZAEHLER
        - BALGENGASZAEHLER
        - MAXIMUMZAEHLER
        - MULTIPLEXANLAGE
        - PAUSCHALANLAGE
        - VERSTAERKERANLAGE
        - SUMMATIONSGERAET
        - IMPULSGEBER
        - EDL_21_ZAEHLERAUFSATZ
        - VIER_QUADRANTEN_LASTGANGZAEHLER
        - MENGENUMWERTER
        - STROMWANDLER
        - SPANNUNGSWANDLER
        - DATENLOGGER
        - KOMMUNIKATIONSANSCHLUSS
        - MODEM
        - TELEKOMMUNIKATIONSEINRICHTUNG
        - KOMMUNIKATIONSEINRICHTUNG
        - DREHKOLBENGASZAEHLER
        - TURBINENRADGASZAEHLER
        - ULTRASCHALLZAEHLER
        - WIRBELGASZAEHLER
        - MODERNE_MESSEINRICHTUNG
        - ELEKTRONISCHER_HAUSHALTSZAEHLER
        - STEUEREINRICHTUNG
        - TECHNISCHESTEUEREINRICHTUNG
        - TARIFSCHALTGERAET
        - RUNDSTEUEREMPFAENGER
        - OPTIONALE_ZUS_ZAEHLEINRICHTUNG
        - MESSWANDLERSATZ_IMS_MME
        - KOMBIMESSWANDLER_IMS_MME
        - TARIFSCHALTGERAET_IMS_MME
        - RUNDSTEUEREMPFAENGER_IMS_MME
        - TEMPERATUR_KOMPENSATION
        - HOECHSTBELASTUNGS_ANZEIGER
        - SONSTIGES_GERAET
        - SMARTMETERGATEWAY
        - STEUERBOX
        - BLOCKSTROMWANDLER
        - KOMBIMESSWANDLER
        - MODEM_GSM
        - ETHERNET_KOM
        - PLC_COM
        - MODEM_FESTNETZ
        - DSL_KOM
        - LTE_KOM
        - DICHTEMENGENUMWERTER
        - TEMPERATURMENGENUMWERTER
        - ZUSTANDSMENGENUMWERTER
        - MESSDATENREGISTRIERGERAET
        - WANDLER
        - BEFESTIGUNGSEINRICHTUNG
      x-apidog-enum:
        - value: WECHSELSTROMZAEHLER
          name: analoger Wechselstromzähler
          description: WSZ
        - value: DREHSTROMZAEHLER
          name: analoger Haushaltszähler (Drehstrom)
          description: AHZ
        - value: ZWEIRICHTUNGSZAEHLER
          name: ''
          description: ''
        - value: RLM_ZAEHLER
          name: Lastgangzähler
          description: LAZ
        - value: IMS_ZAEHLER
          name: ''
          description: ''
        - value: BALGENGASZAEHLER
          name: Balgengaszähler
          description: BGZ
        - value: MAXIMUMZAEHLER
          name: Maximumzähler
          description: MAZ
        - value: MULTIPLEXANLAGE
          name: ''
          description: ''
        - value: PAUSCHALANLAGE
          name: ''
          description: ''
        - value: VERSTAERKERANLAGE
          name: ''
          description: ''
        - value: SUMMATIONSGERAET
          name: ''
          description: ''
        - value: IMPULSGEBER
          name: ''
          description: ''
        - value: EDL_21_ZAEHLERAUFSATZ
          name: ''
          description: ''
        - value: VIER_QUADRANTEN_LASTGANGZAEHLER
          name: ''
          description: ''
        - value: MENGENUMWERTER
          name: Mengenumwerter
          description: Z64
        - value: STROMWANDLER
          name: ''
          description: ''
        - value: SPANNUNGSWANDLER
          name: ''
          description: ''
        - value: DATENLOGGER
          name: ''
          description: ''
        - value: KOMMUNIKATIONSANSCHLUSS
          name: ''
          description: ''
        - value: MODEM
          name: ''
          description: ''
        - value: TELEKOMMUNIKATIONSEINRICHTUNG
          name: ''
          description: ''
        - value: KOMMUNIKATIONSEINRICHTUNG
          name: Kommunikationseinrichtung
          description: Z26
        - value: DREHKOLBENGASZAEHLER
          name: Drehkolbengaszähler
          description: DKZ
        - value: TURBINENRADGASZAEHLER
          name: Turbinenradgaszähler
          description: TRZ
        - value: ULTRASCHALLZAEHLER
          name: Ultraschallgaszähler
          description: UGZ
        - value: WIRBELGASZAEHLER
          name: Wirbelgaszähler
          description: WGZ
        - value: MODERNE_MESSEINRICHTUNG
          name: moderne Messeinrichtung nach MsbG
          description: MME
        - value: ELEKTRONISCHER_HAUSHALTSZAEHLER
          name: elektronischer Haushaltszähler
          description: EHZ
        - value: STEUEREINRICHTUNG
          name: ''
          description: ''
        - value: TECHNISCHESTEUEREINRICHTUNG
          name: Technische Steuereinrichtung
          description: Z27
        - value: TARIFSCHALTGERAET
          name: ''
          description: ''
        - value: RUNDSTEUEREMPFAENGER
          name: ''
          description: ''
        - value: OPTIONALE_ZUS_ZAEHLEINRICHTUNG
          name: Zähleinrichtung
          description: ZD4
        - value: MESSWANDLERSATZ_IMS_MME
          name: ''
          description: ''
        - value: KOMBIMESSWANDLER_IMS_MME
          name: ''
          description: ''
        - value: TARIFSCHALTGERAET_IMS_MME
          name: ''
          description: ''
        - value: RUNDSTEUEREMPFAENGER_IMS_MME
          name: ''
          description: ''
        - value: TEMPERATUR_KOMPENSATION
          name: ''
          description: ''
        - value: HOECHSTBELASTUNGS_ANZEIGER
          name: ''
          description: ''
        - value: SONSTIGES_GERAET
          name: Individuelle Abstimmung (Sonderausstattung)
          description: IVA
        - value: SMARTMETERGATEWAY
          name: Smartmeter-Gateway
          description: Z75
        - value: STEUERBOX
          name: Steuerbox
          description: Z76
        - value: BLOCKSTROMWANDLER
          name: ''
          description: ''
        - value: KOMBIMESSWANDLER
          name: ''
          description: ''
        - value: MODEM_GSM
          name: ''
          description: ''
        - value: ETHERNET_KOM
          name: ''
          description: ''
        - value: PLC_COM
          name: ''
          description: ''
        - value: MODEM_FESTNETZ
          name: ''
          description: ''
        - value: DSL_KOM
          name: ''
          description: ''
        - value: LTE_KOM
          name: ''
          description: ''
        - value: DICHTEMENGENUMWERTER
          name: ''
          description: ''
        - value: TEMPERATURMENGENUMWERTER
          name: ''
          description: ''
        - value: ZUSTANDSMENGENUMWERTER
          name: ''
          description: ''
        - value: MESSDATENREGISTRIERGERAET
          name: Messdatenregistriergerät
          description: MRG
        - value: WANDLER
          name: Wandler
          description: Z25
        - value: BEFESTIGUNGSEINRICHTUNG
          name: ''
          description: ''
      x-apidog-folder: ''
    Marktteilnehmer:
      title: Marktteilnehmer
      type: object
      properties:
        boTyp: *ref_6
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        geschaeftspartnerrolle: &ref_9
          $ref: '#/components/schemas/Geschaeftspartnerrolle'
          description: Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde).
        anrede:
          type: string
          description: Anrede
        name1:
          type: string
          description: 'Erster Teil des Namens - Name des Unternehmens '
        name2:
          type: string
          description: Zweiter Teil des Namens
        name3:
          type: string
          description: Dritter Teil des Namens
        name4:
          type: string
          description: Vierter Teil des Namens
        partneradresse: *ref_7
        gewerbekennzeichnung:
          type: boolean
          description: >-
            Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
            (gewerbeKennzeichnung = true) oder eine Privatperson handelt.
            (gewerbeKennzeichnung = false)
        externeKundenummerLieferant:
          type: string
          description: externe Kundenummer Lieferant
        marktrolle: *ref_8
        rollencodenummer:
          type: string
          description: |-
            Gibt die Codenummer der Marktrolle an - MP ID
            ORDERS NAD Z31 Übertragungsnetzbetreiber 
            PI 17134
            ORDERS NAD DEB Messstellenbetreiber
            PI 17003 17134 17135
            IFTSTA NAD DEB Messstellenbetreiber 
            PI 21007 21015 21018
        rollencodetyp:
          $ref: '#/components/schemas/Rollencodetyp'
          description: >-
            Gibt den Typ des Codes an - Verantwortliche Stelle für die
            Codepflege

            9 GS1

            293 DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)

            332 DE, DVGW Service & Consult GmbH 
        umsatzsteuerId:
          type: string
          description: |-
            Umsatzsteuernummer
            RFF VA
            PI 37000 37001 37002 37005 37004 37003 37006
        steuernummer:
          type: string
          description: |-
            Steuernummer
            RFF FC
            PI 37000 37001 37002 37005 37004 37003 37006
        ansprechpartner: &ref_10
          $ref: '#/components/schemas/Ansprechpartner'
          description: |-
            Ansprechpartner innerhalb des im vorangegangenen NAD-Segment
            CTA IC 
        makoadresse:
          type: string
          description: >-
            Die 1:1-Kommunikationsadresse des Marktteilnehmers. Diese wird in
            der Marktkommunikation verwendet.
        downloadlinkZertifikat:
          type: string
          description: Downloadlink Zertifikat
        amtsgericht:
          type: string
          description: |-
            Amtsgericht - Angabe des Gerichtes
            FTX Z15
            PI 37000 37001 37002 37005 37004 37003 37006
        hrnummer:
          type: string
          description: Handelsregister-Nummer
        website:
          type: string
          description: |-
            Internetseite (URL) 
            FTX Z13
            PI 37000 37001 37002 37005 37004 37003 37006
        faxnummer:
          type: string
          description: |-
            Faxnummer des Unternehmens
            RFF Z25
            PI 37000 37001 37002 37005 37004 37003 37006
        kommunikationsrolle:
          $ref: '#/components/schemas/Kommunikationsrolle'
          description: Ansprechpartner für den Themenbereich
        weiterverpflichtet:
          type: boolean
          description: >-
            Art der Leistungserbringung

            Z19 Auf vertraglicher Grundlage gegenüber Anschlussnutzer /
            Anschlussnehmer

            Z20 In der Ausübung der Weiterverpflichtung durch den gMSB

            PI 55002 55078 55602 55603 55013 55616 55622 55628 55634 55690 55035
            55095 55060 55043 55168 55169
        kommunikationsparameter:
          $ref: '#/components/schemas/Kommunikationsparameter'
          description: nicht in Benutzung
        messstellenbetreiberEigenschaft:
          $ref: '#/components/schemas/MSBEigenschaft'
          description: >-
            Eigenschaft des Messstellenbetreiber an der Lokation

            CAV Z39

            PI 55002 55078 55602 55603 55013 55616 55622 55628 55634 55690 55035
            55095 55060 55043 55168 55169
        bankverbindung:
          type: array
          items:
            $ref: '#/components/schemas/Bankverbindung'
          description: |-
            Bankverbindung
            FII BK
            PI 37000 37001 37002 37005 37004 37003 37006
        erreichbarkeit:
          type: array
          items:
            $ref: '#/components/schemas/Erreichbarkeit'
          description: |-
            Erreichbarkeit des Unternehmens  an Werktagen
            CCI Z40
            PI 37000 37001 37002 37005 37004 37003 37006
        ipAdresse:
          type: string
          description: |-
            IP-Adresse des Absenders
            FTX Z27
        ipRange:
          $ref: '#/components/schemas/IpRange'
          description: |-
            IP-Range des Absenders
            FTX Z28
        zuordnungVon:
          type: string
          format: date-time
          description: Startdatum der Zuordnung des Marktteilnehmers
        zuordnungBis:
          type: string
          format: date-time
          description: Enddatum der Zuordnung des Marktteilnehmers
        bilanzkreis:
          type: string
          description: Bilanzkreis
        verwendungszweckBilanzkreis:
          $ref: '#/components/schemas/VerwendungszweckBilanzkreis'
          description: Verwendungszweck des Bilanzkreises
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - geschaeftspartnerrolle
        - anrede
        - name1
        - name2
        - name3
        - name4
        - partneradresse
        - gewerbekennzeichnung
        - externeKundenummerLieferant
        - marktrolle
        - rollencodenummer
        - rollencodetyp
        - umsatzsteuerId
        - steuernummer
        - ansprechpartner
        - makoadresse
        - downloadlinkZertifikat
        - amtsgericht
        - hrnummer
        - website
        - faxnummer
        - kommunikationsrolle
        - weiterverpflichtet
        - kommunikationsparameter
        - messstellenbetreiberEigenschaft
        - bankverbindung
        - erreichbarkeit
        - ipAdresse
        - ipRange
        - zuordnungVon
        - zuordnungBis
        - bilanzkreis
        - verwendungszweckBilanzkreis
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Marktteilnehmer.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    VerwendungszweckBilanzkreis:
      type: string
      title: VerwendungszweckBilanzkreis
      enum:
        - VERBRAUCHENDE_MARKTLOKATION
        - ERZEUGENDE_MARKTLOKATION_EEG
        - ERZEUGENDE_MARKTLOKATION_KWKG
        - SONSTIGE_ERZEUGENDE_MARKTLOKATION
      description: VerwendungszweckBilanzkreis
      x-apidog-folder: ''
    IpRange:
      title: IpRange
      type: object
      properties:
        untereGrenze:
          type: string
          description: untere Grenze der IP-Range des Absenders
        obereGrenze:
          type: string
          description: obere Grenze der IP-Range des Absenders
      x-apidog-orders:
        - untereGrenze
        - obereGrenze
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Erreichbarkeit:
      title: Erreichbarkeit
      type: object
      properties:
        verfuegbarkeit:
          $ref: '#/components/schemas/Verfuegbarkeit'
          description: |-
            Erreichbarkeit des Unternehmens an den Werktagen
            DTM Z36
            PI 37000 37001 37002 37005 37004 37003 37006
        zeit:
          type: string
          description: |-
            Zeit der Erreichbarkeit
            501 HHMMHHMM
      x-apidog-orders:
        - verfuegbarkeit
        - zeit
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Verfuegbarkeit:
      type: string
      title: Verfuegbarkeit
      description: Verfuegbarkeit
      enum:
        - MONTAG
        - DIENSTAG
        - MITTWOCH
        - DONNERSTAG
        - FREITAG
        - PAUSE
      x-apidog-enum:
        - value: MONTAG
          name: Verfügbarkeit Montag
          description: Z36
        - value: DIENSTAG
          name: Verfügbarkeit Dienstag
          description: Z37
        - value: MITTWOCH
          name: Verfügbarkeit Mittwoch
          description: Z38
        - value: DONNERSTAG
          name: Verfügbarkeit Donnerstag
          description: Z39
        - value: FREITAG
          name: Verfügbarkeit Freitag
          description: Z40
        - value: PAUSE
          name: Mittagspause (= Ausschluss der Verfügbarkeit)
          description: Z41
      x-apidog-folder: ''
    Bankverbindung:
      title: Bankverbindung
      type: object
      properties:
        verwendungszweck:
          $ref: '#/components/schemas/BankverbindungVerwendungszweck'
          description: nicht in Benutzung
        iban:
          type: string
          description: IBAN
        kontoinhaber:
          type: string
          description: Der Kontoinhaber
        bic:
          type: string
          description: BIC Code
        kreditinstitut:
          type: string
          description: Name des Kreditinstitut
      x-apidog-orders:
        - verwendungszweck
        - iban
        - kontoinhaber
        - bic
        - kreditinstitut
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    BankverbindungVerwendungszweck:
      title: BankverbindungVerwendungszweck
      type: string
      enum:
        - BV_ZAHLUNG_NNA
        - BV_ZAHLUNG_MMMA
        - BV_ZAHLUNG_MSB_ABRECHNNUNG
        - BV_ZAHLUNG_ENT_SPERREN_ABRECHNUNG
        - BV_SONSTIGE
      description: BankverbindungVerwendungszweck
      x-apidog-folder: ''
    MSBEigenschaft:
      type: string
      title: MSBEigenschaft
      description: MSBEigenschaft
      enum:
        - GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
        - WETTBEWERBLICHER_MESSSTELLENBETREIBER
        - AUFFANGMESSSTELLENBETREIBER
      x-apidog-enum:
        - value: GRUNDZUSTAENDIGER_MESSSTELLENBETREIBER
          name: Grundzuständiger Messstellenbetreiber
          description: Z39
        - value: WETTBEWERBLICHER_MESSSTELLENBETREIBER
          name: Wetbewerblicher Messstellenbetreiber
          description: Z40
        - value: AUFFANGMESSSTELLENBETREIBER
          name: Auffangmessstellenbetreiber
          description: Z41
      x-apidog-folder: ''
    Kommunikationsparameter:
      title: Kommunikationsparameter
      type: object
      properties:
        zieladresse:
          $ref: '#/components/schemas/Zieladresse'
          description: nicht in Benutzung
        zertifikatsAussteller:
          $ref: '#/components/schemas/ZertifikatsAussteller'
          description: nicht in Benutzung
        zertifikatsNutzer:
          $ref: '#/components/schemas/ZertifikatsNutzer'
          description: nicht in Benutzung
      x-apidog-orders:
        - zieladresse
        - zertifikatsAussteller
        - zertifikatsNutzer
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    ZertifikatsNutzer:
      title: ZertifikatsNutzer
      type: object
      properties:
        zertifikatsNutzer1:
          type: string
          description: Zertifikatsnutzer 1
        zertifikatsNutzer2:
          type: string
          description: Zertifikatsnutzer 2
        zertifikatsNutzer3:
          type: string
          description: Zertifikatsnutzer 3
        zertifikatsNutzer4:
          type: string
          description: Zertifikatsnutzer 4
        zertifikatsNutzer5:
          type: string
          description: Zertifikatsnutzer 5
      x-apidog-orders:
        - zertifikatsNutzer1
        - zertifikatsNutzer2
        - zertifikatsNutzer3
        - zertifikatsNutzer4
        - zertifikatsNutzer5
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    ZertifikatsAussteller:
      title: ZertifikatsAussteller
      type: object
      properties:
        zertifikatsAussteller1:
          type: string
          description: Zertifikats Aussteller 1
        zertifikatsAussteller2:
          type: string
          description: Zertifikats Aussteller 2
        zertifikatsAussteller3:
          type: string
          description: Zertifikats Aussteller 3
        zertifikatsAussteller4:
          type: string
          description: Zertifikats Aussteller 4
        zertifikatsAussteller5:
          type: string
          description: Zertifikats Aussteller 5
      x-apidog-orders:
        - zertifikatsAussteller1
        - zertifikatsAussteller2
        - zertifikatsAussteller3
        - zertifikatsAussteller4
        - zertifikatsAussteller5
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zieladresse:
      title: Zieladresse
      type: object
      properties:
        zieladresse1:
          type: string
          description: Zieladresse URI IPv4 für die Bereitstellung der Werte
        zieladresse2:
          type: string
          description: Zieladresse URI IPv6 für die Bereitstellung der Werte
        zieladresse3:
          type: string
          description: Zieladresse 3
        zieladresse4:
          type: string
          description: Zieladresse 4
        zieladresse5:
          type: string
          description: Zieladresse 5
      x-apidog-orders:
        - zieladresse1
        - zieladresse2
        - zieladresse3
        - zieladresse4
        - zieladresse5
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Kommunikationsrolle:
      type: string
      title: Kommunikationsrolle
      description: Kommunikationsrolle
      enum:
        - DATENAUSTAUSCH
        - RAHMENVERTRAEGE
        - KUENDIGUNGSPROZESSE
        - WECHSELPROZESSE
        - STAMMDATENPROZESSE
        - EINSPEISEPROZESSE
        - ABRECHNUNGSPROZESSE
        - MMMA_PROZESSE
        - BEWEGUNGSDATEN
        - ENT_SPERR_PROZESSE
        - BILANZIERUNGSPROZESSE
        - NETZANSCHLUSS_ANLAGEN
      x-apidog-enum:
        - value: DATENAUSTAUSCH
          name: Ansprechpartner Übertragungsweg / Datenaustausch
          description: Z10
        - value: RAHMENVERTRAEGE
          name: Ansprechpartner Rahmenverträge
          description: Z11
        - value: KUENDIGUNGSPROZESSE
          name: Ansprechpartner Kündigungsprozesse
          description: Z12
        - value: WECHSELPROZESSE
          name: Ansprechpartner Wechselprozesse
          description: Z13
        - value: STAMMDATENPROZESSE
          name: Ansprechpartner Stammdatenprozesse
          description: Z14
        - value: EINSPEISEPROZESSE
          name: Ansprechpartner Einspeiseprozesse
          description: Z16
        - value: ABRECHNUNGSPROZESSE
          name: Ansprechpartner Abrechnungsprozesse
          description: Z17
        - value: MMMA_PROZESSE
          name: Ansprechpartner MMMA-Prozesse
          description: Z18
        - value: BEWEGUNGSDATEN
          name: Ansprechpartner Bewegungsdaten
          description: Z19
        - value: ENT_SPERR_PROZESSE
          name: Ansprechpartner Sperr-/Entsperrprozesse
          description: Z20
        - value: BILANZIERUNGSPROZESSE
          name: Ansprechpartner Bilanzierungsprozesse / Bilanzkreismanagement
          description: Z21
        - value: NETZANSCHLUSS_ANLAGEN
          name: >-
            Ansprechpartner technischer Netzanschluss für Neuanlagen und
            Anlagenumbau
          description: Z33
      x-apidog-folder: ''
    Ansprechpartner:
      title: Ansprechpartner
      type: object
      properties:
        boTyp: *ref_6
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        nachname:
          type: string
          description: Nachname (Familienname) des Ansprechpartners
        eMailAdresse:
          type: string
          description: E-Mail Adresse
        rufnummern:
          type: array
          items:
            $ref: '#/components/schemas/Rufnummer'
          description: >-
            Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar
            ist.
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - nachname
        - eMailAdresse
        - rufnummern
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Ansprechpartner.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Rufnummer:
      title: Rufnummer
      type: object
      properties:
        nummerntyp:
          $ref: '#/components/schemas/Rufnummernart'
          description: |-
            Art des Kommunikationsmittels
            COM
        rufnummer:
          type: string
          description: Rufnummer
      x-apidog-orders:
        - nummerntyp
        - rufnummer
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Rufnummernart:
      type: string
      title: Rufnummernart
      description: Rufnummernart
      enum:
        - RUF_ZENTRALE
        - FAX_ZENTRALE
        - SAMMELRUF
        - SAMMELFAX
        - ABTEILUNGRUF
        - ABTEILUNGFAX
        - RUF_DURCHWAHL
        - FAX_DURCHWAHL
        - MOBIL_NUMMER
      x-apidog-enum:
        - value: RUF_ZENTRALE
          name: weiteres Telefon
          description: AJ
        - value: FAX_ZENTRALE
          name: ''
          description: ''
        - value: SAMMELRUF
          name: ''
          description: ''
        - value: SAMMELFAX
          name: ''
          description: ''
        - value: ABTEILUNGRUF
          name: ''
          description: ''
        - value: ABTEILUNGFAX
          name: ''
          description: ''
        - value: RUF_DURCHWAHL
          name: Telefon
          description: TE
        - value: FAX_DURCHWAHL
          name: Telefax
          description: FX
        - value: MOBIL_NUMMER
          name: Handy
          description: AL
      x-apidog-folder: ''
    Rollencodetyp:
      type: string
      title: Rollencodetyp
      description: Rollencodetyp
      enum:
        - BDEW
        - GS1
        - GLN
        - DVGW
      x-apidog-enum:
        - value: BDEW
          name: DE, BDEW (Bundesverband der Energie- und Wasserwirtschaft e.V.)
          description: '293'
        - value: GS1
          name: GS1
          description: '9'
        - value: GLN
          name: ''
          description: ''
        - value: DVGW
          name: DE, DVGW Service & Consult GmbH
          description: '332'
      x-apidog-folder: ''
    Geschaeftspartnerrolle:
      type: string
      title: Geschaeftspartnerrolle
      description: Geschaeftspartnerrolle
      enum:
        - KUNDE
        - LIEFERANT
        - DIENSTLEISTER
        - INTERESSENT
        - MARKTPARTNER
        - EIGENTUEMER
        - HAUSVERWALTER
        - KORRESPONDENZEMPFAENGER
        - ABLESEKARTENEMPFAENGER
      x-apidog-enum:
        - value: KUNDE
          name: ''
          description: ''
        - value: LIEFERANT
          name: ''
          description: ''
        - value: DIENSTLEISTER
          name: ''
          description: ''
        - value: INTERESSENT
          name: ''
          description: ''
        - value: MARKTPARTNER
          name: ''
          description: ''
        - value: EIGENTUEMER
          name: ''
          description: ''
        - value: HAUSVERWALTER
          name: ''
          description: ''
        - value: KORRESPONDENZEMPFAENGER
          name: ''
          description: ''
        - value: ABLESEKARTENEMPFAENGER
          name: ''
          description: ''
      x-apidog-folder: ''
    Lokationszuordnung:
      title: Lokationszuordnung
      type: string
      enum:
        - UNVERAENDERT
        - BEGINNT
        - ENDET
      description: Lokationszuordnung
      x-apidog-folder: ''
    Verwendungsumfang:
      type: string
      title: Verwendungsumfang
      description: Verwendungsumfang
      enum:
        - MESSLOKATION_PROZESSUAL_BEHANDELT
        - MESSLOKATION_LOKATIONSBUENDEL
      x-apidog-enum:
        - value: MESSLOKATION_PROZESSUAL_BEHANDELT
          name: ID der prozessual behandelten Messlokation
          description: Z82
        - value: MESSLOKATION_LOKATIONSBUENDEL
          name: ID der Messlokation im Loka�onsbündel
          description: Z81
      x-apidog-folder: ''
    Geschaeftspartner:
      title: Geschaeftspartner
      type: object
      properties:
        boTyp: *ref_6
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
        anrede:
          type: string
          description: |-
            Die Anrede für den GePa, Z.B. Herr.
            Z04 Korrespondenzanschrift des Kunden des Lieferanten
            PI 55001 55600 55601 55013 55014 55043 55168 55169
        name1:
          type: string
          description: >-
            Erster Teil des Namens. Hier kann der Firmenname oder bei
            Privatpersonen beispielsweise der Nachname dargestellt werden.
            Beispiele: Yellow Strom GmbH oder Hagen
        name2:
          type: string
          description: >-
            Zweiter Teil des Namens. Hier kann der eine Erweiterung zum
            Firmennamen oder bei Privatpersonen beispielsweise der Vorname
            dargestellt werden. Beispiele: Bereich Süd oder Nina
        name3:
          type: string
          description: >-
            Dritter Teil des Namens. Hier können weitere Ergänzungen zum
            Firmennamen oder bei Privatpersonen Zusätze zum  Namen dargestellt
            werden. Beispiele: und Afrika oder Sängerin
        name4:
          type: string
          description: Name 4
        umsatzsteuerId:
          type: string
          description: 'Die Umsatzsteuer-ID des Geschäftspartners. Beispiel: DE 813281825'
        glaeubigerId:
          type: string
          description: >-
            Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird- Z.B. DE
            47116789
        emailAdresse:
          type: string
          description: email Adresse
        website:
          type: string
          description: 'Internetseite des Marktpartners. Beispiel: www.mp-energie.de'
        gewerbekennzeichnung:
          type: boolean
          description: >-
            Kennzeichnung ob es sich um einen Gewerbe/Unternehmen
            (gewerbeKennzeichnung = true)

            oder eine Privatperson handelt. (gewerbeKennzeichnung = false)

            Z01 Struktur von Personennamen

            Z02 Struktur der Firmenbezeichnung
        hrnummer:
          type: string
          description: Handelsregisternummer des Geschäftspartners
        amtsgericht:
          type: string
          description: >-
            Amtsgericht bzw Handelsregistergericht, das die
            Handelsregisternummer herausgegeben hat
        partneradresse: *ref_7
        externeKundenummerLieferant:
          type: string
          description: externeKundenummerLieferant
        externeReferenzen:
          type: array
          items:
            $ref: '#/components/schemas/ExterneReferenz'
          description: >-
            Hier können IDs anderer Systeme hinterlegt werden (z.B. eine
            SAP-GP-Nummer) (Details siehe ExterneReferenz)
        geschaeftspartnerrolle:
          type: array
          items: *ref_9
          description: |-
            Rolle, die der Geschäftspartner hat (z.B. Interessent, Kunde).
            NAD Z09 ORDERS
            PI 17101 17003
            NAD Kunde des Messstellenbetreibers ORDERS
            PI 17126
        kontaktweg:
          type: array
          items:
            $ref: '#/components/schemas/Kontaktart'
          description: Bevorzugter Kontaktweg des Geschäftspartners.
        ansprechpartner: *ref_10
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - anrede
        - name1
        - name2
        - name3
        - name4
        - umsatzsteuerId
        - glaeubigerId
        - emailAdresse
        - website
        - gewerbekennzeichnung
        - hrnummer
        - amtsgericht
        - partneradresse
        - externeKundenummerLieferant
        - externeReferenzen
        - geschaeftspartnerrolle
        - kontaktweg
        - ansprechpartner
      examples:
        - $ref: >-
            https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/docs/examples/bo/Geschaeftspartner.json
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Kontaktart:
      title: Kontaktart
      type: string
      enum:
        - ANSCHREIBEN
        - TELEFONAT
        - FAX
        - E_MAIL
        - SMS
      description: >-
        Gibt an, auf welchem Weg die Person oder der Geschäftspartner
        kontaktiert werden kann
      x-apidog-folder: ''
    ExterneReferenz:
      title: ExterneReferenz
      type: object
      properties:
        exRefName:
          type: string
          enum:
            - Kundennummer beim Lieferanten
            - Kundennummer beim Altlieferanten
          description: >-
            Bezeichnung der externen Referenz, Kundennummer beim Lieferanten,
            bezieht sich auf das vorangegangene NAD Segment

            RFF AVC

            PI 55109 55137 

            RFF AVC Kundennummer beim Lieferanten ORDERS

            PI 17101
        exRefWert:
          type: string
          description: >-
            Kundennummer beim Altieferanten - Angabe von Referenzen für
            Rückmeldungen und Anfragen

            PI 55109 55137 

            ORDERS PI 17101
      x-apidog-orders:
        - exRefName
        - exRefWert
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Betriebszustand:
      type: string
      title: Betriebszustand
      description: Betriebszustand
      enum:
        - GESPERRT_NICHT_ENTSPERREN
        - GESPERRT
        - REGELBETRIEB
      x-apidog-enum:
        - value: GESPERRT_NICHT_ENTSPERREN
          name: Messlokation gesperrt und darf nicht entsperrt werden
          description: ZC1
        - value: GESPERRT
          name: Messlokation gesperrt und darf entsperrt werden
          description: ZC2
        - value: REGELBETRIEB
          name: Messlokation im Regelbetrieb
          description: ZC3
      x-apidog-folder: ''
    Gasqualitaet:
      type: string
      title: Gasqualitaet
      description: Unterscheidung für hoch- und niedrig-kalorisches Gas.
      enum:
        - H_GAS
        - L_GAS
      x-apidog-enum:
        - value: H_GAS
          name: H-Gas
          description: Y04
        - value: L_GAS
          name: L-Gas
          description: Y05
      x-apidog-folder: ''
    Bilanzierungsmethode:
      title: Bilanzierungsmethode
      type: string
      enum:
        - RLM
        - SLP
        - TLP_GEMEINSAM
        - TLP_GETRENNT
        - PAUSCHAL
        - IMS
      description: >-
        Mit dieser Aufzählung kann zwischen den Bilanzierungsmethoden bzw.
        -grundlagen unterschieden werden.
      x-apidog-folder: ''
    Adresse:
      title: Adresse
      type: object
      properties:
        postleitzahl:
          type: string
          description: Postleitzahl
        ort:
          type: string
          description: Ort
        strasse:
          type: string
          description: Strasse
        hausnummer:
          type: string
          description: Hausnummer und Ergänzung
        postfach:
          type: string
          description: Postfach
        adresszusatz:
          type: string
          description: Adresszusatz
        coErgaenzung:
          type: string
          description: coErgaenzung
        landescode:
          $ref: '#/components/schemas/Landescode'
          description: Landescode
        ortsteil:
          type: string
          description: Ortsteil
        zusatzInformation:
          $ref: '#/components/schemas/AdresszusatzInformation'
          description: Zusatzinformation zur Identifizierung, Zeile für Name und Anschrift
      x-apidog-orders:
        - postleitzahl
        - ort
        - strasse
        - hausnummer
        - postfach
        - adresszusatz
        - coErgaenzung
        - landescode
        - ortsteil
        - zusatzInformation
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    AdresszusatzInformation:
      title: AdresszusatzInformation
      type: object
      properties:
        zusatz1:
          type: string
          description: Adresszusatz 1
        zusatz2:
          type: string
          description: Adresszusatz 2
        zusatz3:
          type: string
          description: Adresszusatz 3
        zusatz4:
          type: string
          description: Adresszusatz 4
        zusatz5:
          type: string
          description: Adresszusatz 5
      x-apidog-orders:
        - zusatz1
        - zusatz2
        - zusatz3
        - zusatz4
        - zusatz5
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Landescode:
      title: Landescode
      type: string
      enum:
        - AC
        - AD
        - AE
        - AF
        - AG
        - AI
        - AL
        - AM
        - AN
        - AO
        - AQ
        - AR
        - AS
        - AT
        - AU
        - AW
        - AX
        - AZ
        - BA
        - BB
        - BD
        - BE
        - BF
        - BG
        - BH
        - BI
        - BJ
        - BL
        - BM
        - BN
        - BO
        - BQ
        - BR
        - BS
        - BT
        - BU
        - BV
        - BW
        - BY
        - BZ
        - CA
        - CC
        - CD
        - CF
        - CG
        - CH
        - CI
        - CK
        - CL
        - CM
        - CN
        - CO
        - CP
        - CR
        - CS
        - CU
        - CV
        - CW
        - CX
        - CY
        - CZ
        - DE
        - DG
        - DJ
        - DK
        - DM
        - DO
        - DZ
        - EA
        - EC
        - EE
        - EG
        - EH
        - ER
        - ES
        - ET
        - EU
        - FI
        - FJ
        - FK
        - FM
        - FO
        - FR
        - FX
        - GA
        - GB
        - GD
        - GE
        - GF
        - GG
        - GH
        - GI
        - GL
        - GM
        - GN
        - GP
        - GQ
        - GR
        - GS
        - GT
        - GU
        - GW
        - GY
        - HK
        - HM
        - HN
        - HR
        - HT
        - HU
        - IC
        - ID
        - IE
        - IL
        - IM
        - IN
        - IO
        - IQ
        - IR
        - IS
        - IT
        - JE
        - JM
        - JO
        - JP
        - KE
        - KG
        - KH
        - KI
        - KM
        - KN
        - KP
        - KR
        - KW
        - KY
        - KZ
        - LA
        - LB
        - LC
        - LI
        - LK
        - LR
        - LS
        - LT
        - LU
        - LV
        - LY
        - MA
        - MC
        - MD
        - ME
        - MF
        - MG
        - MH
        - MK
        - ML
        - MM
        - MN
        - MO
        - MP
        - MQ
        - MR
        - MS
        - MT
        - MU
        - MV
        - MW
        - MX
        - MY
        - MZ
        - NA
        - NC
        - NE
        - NF
        - NG
        - NI
        - NL
        - 'NO'
        - NP
        - NR
        - NT
        - NU
        - NZ
        - OM
        - PA
        - PE
        - PF
        - PG
        - PH
        - PK
        - PL
        - PM
        - PN
        - PR
        - PS
        - PT
        - PW
        - PY
        - QA
        - RE
        - RO
        - RS
        - RU
        - RW
        - SA
        - SB
        - SC
        - SD
        - SE
        - SF
        - SG
        - SH
        - SI
        - SJ
        - SK
        - SL
        - SM
        - SN
        - SO
        - SR
        - SS
        - ST
        - SU
        - SV
        - SX
        - SY
        - SZ
        - TA
        - TC
        - TD
        - TF
        - TG
        - TJ
        - TK
        - TL
        - TM
        - TN
        - TO
        - TP
        - TR
        - TT
        - TV
        - TW
        - TZ
        - UA
        - UG
        - UK
        - UM
        - US
        - UY
        - UZ
        - VA
        - VC
        - VE
        - VG
        - VI
        - VN
        - VU
        - WF
        - WS
        - XK
        - YE
        - YT
        - YU
        - ZA
        - ZM
        - ZR
        - ZW
      description: Der ISO-Landescode als Enumeration
      x-apidog-folder: ''
    Netzebene:
      type: string
      title: Netzebene
      description: Netzebene
      enum:
        - NSP
        - MSP
        - HSP
        - HSS
        - MSP_NSP_UMSP
        - HSP_MSP_UMSP
        - HSS_HSP_UMSP
        - HD
        - MD
        - ND
      x-apidog-enum:
        - value: NSP
          name: Niederspannung
          description: E06
        - value: MSP
          name: Mittelspannung
          description: E05
        - value: HSP
          name: Hochspannung
          description: E04
        - value: HSS
          name: Höchstspannung
          description: E03
        - value: MSP_NSP_UMSP
          name: MS/NS Umspannung
          description: E09
        - value: HSP_MSP_UMSP
          name: HS/MS Umspannung
          description: E08
        - value: HSS_HSP_UMSP
          name: Hös/HS Umspannung
          description: E07
        - value: HD
          name: Hochdruck
          description: Y01
        - value: MD
          name: Mitteldruck
          description: Y02
        - value: ND
          name: Niederdruck
          description: Y03
      x-apidog-folder: ''
    Energierichtung:
      type: string
      title: Energierichtung
      description: Spezifiziert die Energierichtung einer Markt- und/oder Messlokation
      enum:
        - AUSSP
        - EINSP
      x-apidog-enum:
        - value: AUSSP
          name: Verbrauch
          description: 'Z07 / Z71 '
        - value: EINSP
          name: Erzeugung
          description: 'Z06 / Z72 '
      x-apidog-folder: ''
    Sparte:
      type: string
      title: Sparte
      description: Division
      enum:
        - STROM
        - GAS
        - FERNWAERME
        - NAHWAERME
        - WASSER
        - ABWASSER
      x-apidog-enum:
        - value: STROM
          name: Sparte Strom
          description: Represents electricity as the utility division
        - value: GAS
          name: Sparte Gas
          description: Represents natural gas as the utility division
        - value: FERNWAERME
          name: Sparte Fernwärme
          description: Represents district heating as the utility division
        - value: NAHWAERME
          name: Sparte Nahwärme
          description: Represents local heating as the utility division
        - value: WASSER
          name: Sparte Wasser
          description: Represents water supply as the utility division
        - value: ABWASSER
          name: Sparte Abwasser
          description: Represents wastewater services as the utility division
      examples:
        - STROM
      x-apidog-folder: ''
    BOTyp:
      title: BOTyp
      type: string
      description: Typ des BO
      enum:
        - ANSPRECHPARTNER
        - AVIS
        - ENERGIEMENGE
        - GESCHAEFTSOBJEKT
        - GESCHAEFTSPARTNER
        - MARKTLOKATION
        - MARKTTEILNEHMER
        - MESSLOKATION
        - ZAEHLER
        - KOSTEN
        - TARIF
        - PREISBLATT
        - PREISBLATTNETZNUTZUNG
        - PREISBLATTMESSUNG
        - PREISBLATTUMLAGEN
        - PREISBLATTDIENSTLEISTUNG
        - PREISBLATTKONZESSIONSABGABE
        - ZEITREIHE
        - LASTGANG
        - HANDELSUNSTIMMIGKEIT
        - ANFRAGE
        - AUFTRAG
        - STATUSMITTEILUNG
        - BERECHNUNGSFORMEL
        - RECHNUNG
        - BILANZIERUNG
        - NETZNUTZUNGSVERTRAG
        - MESSSTELLENBETRIEBSVERTRAG
        - ENERGIELIEFERVERTRAG
        - SPERRAUFTRAG
        - ANGEBOT
        - TRANCHE
        - KOMMUNIKATIONSDATEN
        - ZAEHLZEITDEFINITION
        - SCHALTZEITDEFINITION
        - LEISTUNGSKURVENDEFINITION
        - NETZLOKATION
        - STEUERBARE_RESSOURCE
        - TECHNISCHE_RESSOURCE
        - AD_HOC_STEUERKANAL
        - LOKATIONSBUENDEL
        - WERTE_NACH_TYP2
        - REKLAMATION
        - STATUSBERICHT
        - VERTRAG
        - BILANZKREIS
        - VERWENDUNGSZEITRAUM
        - TARIFINFO
      x-apidog-folder: ''
    Marktlokation:
      title: Marktlokation
      type: object
      properties:
        boTyp: *ref_6
        versionStruktur:
          type: string
          default: '1'
          description: versionStruktur
          x-apidog-mock: '1'
          title: Structure version
        marktlokationsId:
          type: string
          description: >-
            Angabe der ID der Marktlokation, für die die Stammdaten gelten.

            LOC Z16

            PI 55016 55001 55002 55077 55078 55600 55602 55604 55601 55603 55605
            55013 55607 55010 55004 55007 55036 55037 55038 55611 55218 55220
            55613 55614 55126 55156 55674 55675 55672 55673 55688 55689 55616
            55622 55628 55634 55691 55692 55175 55180 55173 55177 55690 55109
            55137 55110 55136 55684 55685 55640 55645 55650 55655 55660 55665
            55557 55559 55670 55671 55035 55095 55060 55039 55042 55043 55168
            55169 55052 55238 55239 55240 55241 55242 55243 55074 55075 55076
            55065 55066 55195 55196 55223 55224 55201 55202

            Ruhende Malo Zuordnung geringfügiger Verbräuche gem § 10c EEG
            Anwendung findet Anwendung, nimmt nicht selbst an der Bilanzierung
            teil. 

            LOC Z22

            PI 55001 55002 55010 55004 55007 55175 55180 55173 55177 55690 55035
            55060 55043 55168 

            RFF Z18

            PI 55196 55043 55168 55169 

            LOC 172

            44037 44038

            ORDERS 

            RFF Z18 

            PI 17002 17003 17135

            RFF Z59 Marktlokation Kundenanlage

            PI 17134 17135 

            REQOTE LOC 172

            PI 35001 35002 35003 35004 

            IFTSTA LOC 172

            PI 21032 21033 21039 21040 21045

            QUOTES LOC 172

            PI 15002 15003 15004

            RFF Z18

            PI 15002

            INVOIC LOC 172 

            PI 31001 31002 31009 31004 31005 31006 31011
          x-apidog-mock: '{{$string.numeric(length=10)}}'
          title: ID of the market location to which the master data applies
        sparte: *ref_11
        energierichtung: *ref_2
        bilanzierungsmethode: *ref_12
        verbrauchsart:
          type: array
          items: *ref_13
          description: Stromverbrauchsart/Verbrauchsart Marktlokation
        unterbrechbar:
          type: boolean
          description: Gibt an, ob es sich um eine unterbrechbare Belieferung handelt.
          x-apidog-mock: '{{$datatype.boolean}}'
          title: Indicates whether delivery is interruptible
        netzebene: *ref_14
        umspannung: *ref_14
        netzbetreiberCodeNr:
          type: string
          description: >-
            Angabe des NBs MP-ID, der das Konzessionsgebiet zur Malo
            verantwortet und dessen Preisblätter Anwendung finden. 
          x-apidog-mock: '{{$helpers.rangeToNumber(min=9900000000000,max=9999999999999)}}'
          title: >-
            MP-ID of the DSO responsible for the concession area of the market
            location
        gebietTyp:
          $ref: '#/components/schemas/Gebiettyp'
          description: Typ des Netzgebietes,z.B.Verteilnetz.
        netzgebietNr:
          type: string
          description: Die Nummer des Netzgebietes in der ene't-Datenbank.
          x-apidog-mock: '{{$string.numeric(length=5)}}'
          title: Grid area number in the ene't database
        bilanzierungsgebiet:
          type: string
          description: Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist.
          x-apidog-mock: >-
            {{$helpers.arrayElement(["37Z000000000003D", "10YDE-RWENET---I",
            "10YDE-ENBW-----N", "10YDE-50HZ-----U"])}}
          title: Balancing area to which the grid area is assigned
        grundversorgerCodeNr:
          type: string
          description: >-
            Code Nummer des Grundversorgers, der für diese Marktlokation
            zuständig ist.
          x-apidog-mock: '{{$helpers.rangeToNumber(min=9900000000000,max=9999999999999)}}'
          title: >-
            Code number of the default supplier responsible for this market
            location
        gasqualitaet: *ref_15
        endkunde: *ref_16
        lokationsadresse: *ref_7
        katasterinformation:
          $ref: '#/components/schemas/Katasteradresse'
          description: >-
            Alternativ zu einer postalischen Adresse und Geokoordinaten kann
            hier eine Ortsangabe mittels Gemarkung und Flurstück erfolgen.

            Achtung: Es darf immer nur eine Art der Ortsangabe vorhanden sein
            (entweder eine Adresse oder eine GeoKoordinate oder eine
            Katasteradresse.
        regelzone:
          type: string
          description: Angabe einer der vier Regelzonen
          x-apidog-mock: '{{$helpers.arrayElement(["TEN","AMP","TNB","50H"])}}'
          title: Specification of one of the four control areas
        marktgebiet:
          type: string
          description: Angabe des Marktgebiets, in dem die Marktlokation liegt - EIC-Code
          x-apidog-mock: DE_LG
          title: Market area in which the market location resides (EIC code)
        zeitreihentyp:
          $ref: '#/components/schemas/Zeitreihentyp'
          description: Zeitreihentyp für EDIFACT mapping
        messtechnischeEinordnung:
          $ref: '#/components/schemas/MesstechnischeEinordnung'
          description: |-
            Messtechnische Einordnung der Marktlokation
            CAV Z52
            PI 55616 55622 55628 55634 55035 55095 55060 55043 55168 55169
        sperrstatus:
          $ref: '#/components/schemas/Sperrstatus'
          description: |-
            Betriebszustand der Marktlokation
            CCI Z42
            PI 55013
        referenzMarktlokationsId:
          type: string
          description: Referenz auf Marktlokation
          x-apidog-mock: '{{$string.numeric(length=10)}}'
          title: Reference to market location
        versorgungsart:
          $ref: '#/components/schemas/Versorgungsart'
          description: >-
            Versorgungsart der Marktlokation. Hier wird mitgeteilt, ob der Kunde
            sich ab dem Zuordnungsdatum in Ersatzversorgung oder Grundversorgung
            befindet.

            CCI Z36

            PI 55014
        eigentuemer: *ref_16
        hausverwalter: *ref_16
        verguetungEmpfaenger:
          $ref: '#/components/schemas/VerguetungEmpfaenger'
          description: |-
            Empfänger der Vergütung zur Einspeisung
            CAV Z10
            PI 55616 55622 55619 55625 
        statusErzeugendeMalo:
          $ref: '#/components/schemas/StatusErzeugendeMarktlokation'
          description: |-
            Veräußerungsform der erzeugenden Marktlokation
            CCI Z22
            PI 55607 55074 55075 55076
        fernsteuerbarkeit:
          $ref: '#/components/schemas/Fernsteuerbarkeit'
          description: |-
            Status der Fernsteuerbarkeit
            CCI Z24
            PI 55616 55622 
        foerderungsLand:
          type: string
          description: Land der Förderung - Alpha-2-Code
          x-apidog-mock: DE
          title: Country of support – alpha-2 code
        redispatch:
          type: boolean
          description: >-
            Produktidentifikation beim Austausch von Daten zu Energiemengen in
            den Redispatch Prozessen.
          x-apidog-mock: '{{$datatype.boolean}}'
          title: >-
            Product identifier when exchanging energy quantity data in
            redispatch processes
        zukuenftigerMeldepunkt:
          type: boolean
          description: zukünftiger Meldepunkt
          x-apidog-mock: '{{$datatype.boolean}}'
          title: Future reporting point
        lokationszuordnung: *ref_17
        konfigurationsprodukt:
          type: string
          description: >-
            Konfigurationsprodukt aus Produkt-Daten der Marktlokation, Produkte
            sind in der Codeliste der Produkte beschrieben.
          title: Configuration product from the market location’s product data
        leistungskurvendefinition:
          type: string
          description: Code der Zugeordnete Leistungskurvendefinition für das Objekt
          title: Code of the assigned load curve definition for the object
        produktdatenRelevanteRolle: *ref_8
        beteiligterMarktpartner: *ref_0
        modulNetzentgelte:
          $ref: '#/components/schemas/ModulNetzentgelte'
          description: nicht in Benutzung
        datenqualitaet: *ref_18
        gueltigkeitszeitraum: *ref_19
        marktrollen:
          type: array
          items: *ref_0
          description: Zugeordnete Marktpartner der Malo mit Zuordnungszeiträumen
          title: >-
            Assigned market partners of the market location including assignment
            periods
        zaehlwerke:
          type: array
          items: *ref_20
          description: Die Zählwerke des Zählers.
          title: Registers of the meter
        zaehlwerkeBeteiligteMarktrolle:
          type: array
          items: *ref_8
          description: Liste der Zählwerke der beteiligten Martrolle
          title: List of registers for the involved market role
        verbrauchsmenge:
          type: array
          items:
            $ref: '#/components/schemas/Verbrauch'
          description: für EDIFACT mapping
          title: For EDIFACT mapping
        zugehoerigeMesslokationen:
          type: array
          items:
            $ref: '#/components/schemas/Messlokationszuordnung'
          description: >-
            Aufzählung der Messlokationen, die zu dieser Marktlokation gehören.
            Es können 3 verschiedene Konstrukte auftreten:


            Beziehung 1 : 0 : Hier handelt es sich um Pauschalanlagen ohne
            Messung. D.h. die Verbrauchsdaten sind direkt über die Marktlokation
            abgreifbar. Beziehung 1 : 1 : Das ist die Standard-Beziehung für die
            meisten Fälle. In diesem Fall gibt es zu einer Marktlokation genau
            eine Messlokation. Beziehung 1 : N : Hier liegt beispielsweise eine
            Untermessung vor. Der Verbrauch einer Marklokation berechnet sich
            hier aus mehreren Messungen.


            Es gibt praktisch auch noch die Beziehung N : 1, beispielsweise bei
            einer Zweirichtungsmessung bei der durch eine Messeinrichtung die
            Messung sowohl für die Einspreiseseite als auch für die
            Aussspeiseseite erfolgt. Da Abrechnung und Bilanzierung jedoch für
            beide Marktlokationen getrennt erfolgt, werden nie beide
            Marktlokationen gemeinsam betrachtet. Daher lässt sich dieses
            Konstrukt auf zwei 1:1-Beziehung zurückführen, wobei die
            Messlokation in beiden Fällen die gleiche ist.


            In den Zuordnungen sind ist die arithmetische Operation mit der der
            Verbrauch einer Messlokation zum Verbrauch einer Marktlokation
            beitrögt mit aufgeführt. Der Standard ist hier die Addition.
          title: Enumeration of metering locations belonging to this market location
        netznutzungsabrechnungsdaten:
          type: array
          items:
            $ref: '#/components/schemas/Netznutzungsabrechnungsdaten'
          description: Daten für die Prüfung der Netznutzungsabrechnung
          title: Data for validating network usage billing
        messstellenbetriebsabrechnungsdaten:
          type: array
          items:
            $ref: '#/components/schemas/Messstellenbetriebsabrechnungsdaten'
          description: |-
            Messstellenbetriebsabrechnungsdaten der Marktlokation
            PI 55557
          title: Metering point operation billing data of the market location
        energieherkunft:
          type: array
          items:
            $ref: '#/components/schemas/Energieherkunft'
          description: >-
            Art der erzeugenden Marktlokation

            CCI Z34

            PI 55607 55616 55622 55628 55634 55095 55060 55043 55168 55169 55074
            55075 55076
          title: Type of the feed in market location
        erforderlichesProduktpaket:
          type: array
          items:
            $ref: '#/components/schemas/Produktpaket'
          description: |-
            Bestandteil eines Produktpakets,  Produktpaket-ID
            SEQ Z79
            PI 55001 55077 55600 55601 55014 55608 
          title: Component of a product package; product package ID
        geokoordinaten:
          $ref: '#/components/schemas/Geokoordinaten'
          description: Koordinaten - API Maloident
        paketId:
          type: string
          description: >-
            Paket-ID  identifiziert die von einem NB-Wechsel betroffenen
            Lokationen. Betroffene Malos vom NBA.
          examples:
            - P9705070235
          x-apidog-mock: >-
            PKT{{$date.now|format('yyyyMMdd')}}{{$string.alpha(min=3,max=3,casing='upper')}}
          title: Package ID identifying locations affected by a DSO change
        marktlokationsTyp:
          type: array
          items:
            $ref: '#/components/schemas/MarktlokationsTypisierung'
          description: >-
            Angabe der Typisierung der Marktlokation mit möglicher Angabe
            zeitlicher Gültigkeit
          title: Classification of the market location with optional validity period
        zugehoerigeMarktlokationen:
          type: array
          items:
            $ref: '#/components/schemas/MarktlokationsReferenz'
          description: Referenzen zugehöriger Marktlokationen
        technischeEinrichtungen:
          type: array
          items:
            $ref: '#/components/schemas/TechnischeEinrichtung'
          description: technischeEinrichtungen
      required:
        - boTyp
        - versionStruktur
      x-apidog-orders:
        - boTyp
        - versionStruktur
        - marktlokationsId
        - sparte
        - energierichtung
        - bilanzierungsmethode
        - verbrauchsart
        - unterbrechbar
        - netzebene
        - umspannung
        - netzbetreiberCodeNr
        - gebietTyp
        - netzgebietNr
        - bilanzierungsgebiet
        - grundversorgerCodeNr
        - gasqualitaet
        - endkunde
        - lokationsadresse
        - katasterinformation
        - regelzone
        - marktgebiet
        - zeitreihentyp
        - messtechnischeEinordnung
        - sperrstatus
        - referenzMarktlokationsId
        - versorgungsart
        - eigentuemer
        - hausverwalter
        - verguetungEmpfaenger
        - statusErzeugendeMalo
        - fernsteuerbarkeit
        - foerderungsLand
        - redispatch
        - zukuenftigerMeldepunkt
        - lokationszuordnung
        - konfigurationsprodukt
        - leistungskurvendefinition
        - produktdatenRelevanteRolle
        - beteiligterMarktpartner
        - modulNetzentgelte
        - datenqualitaet
        - gueltigkeitszeitraum
        - marktrollen
        - zaehlwerke
        - zaehlwerkeBeteiligteMarktrolle
        - verbrauchsmenge
        - zugehoerigeMesslokationen
        - netznutzungsabrechnungsdaten
        - messstellenbetriebsabrechnungsdaten
        - energieherkunft
        - erforderlichesProduktpaket
        - geokoordinaten
        - paketId
        - marktlokationsTyp
        - zugehoerigeMarktlokationen
        - technischeEinrichtungen
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    TechnischeEinrichtung:
      type: object
      title: TechnischeEinrichtung
      properties:
        technischeEinrichtungenVorhanden:
          type: boolean
          description: true => ZH7, false => ZH8
        verbrauchsart: *ref_13
      x-apidog-orders:
        - technischeEinrichtungenVorhanden
        - verbrauchsart
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    MarktlokationsReferenz:
      title: MarktlokationsReferenz
      type: object
      properties:
        marktlokationsId:
          type: string
          description: Identifikationsnummer einer Marktlokation
        typ: &ref_21
          $ref: '#/components/schemas/MarktlokationsTyp'
      x-apidog-orders:
        - marktlokationsId
        - typ
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    MarktlokationsTyp:
      $id: >-
        https://raw.githubusercontent.com/conuti-gmbh/bo4e-schema/master/schemas/v1/enum/MarktlokationsTyp.schema.json
      title: MarktlokationsTyp
      type: string
      enum:
        - STANDARD_MARKTLOKATION
        - RUHENDE_MARKTLOKATION
        - KUNDENANLAGE
      description: MarktlokationsTyp
      x-apidog-folder: ''
    MarktlokationsTypisierung:
      title: MarktlokationsTypisierung
      type: object
      properties:
        typ: *ref_21
        gueltigAb:
          type: string
          format: date-time
          description: Startdatum der Typisierung der Marktlokation
        gueltigBis:
          type: string
          format: date-time
          description: Enddatum der Typisierung der Marktlokation
      x-apidog-orders:
        - typ
        - gueltigAb
        - gueltigBis
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Geokoordinaten:
      title: Geokoordinaten
      type: object
      properties:
        breitengrad:
          type: string
          description: Gibt den Breitengrad eines entsprechenden Ortes an.
        laengengrad:
          type: string
          description: Gibt den Längengrad eines entsprechenden Ortes an.
        ostwert:
          type: string
          description: Gibt den Ostwert eines entsprechenden Ortes an.
        nordwert:
          type: string
          description: Gibt den Nordwert eines entsprechenden Ortes an.
        zone:
          $ref: '#/components/schemas/Zone'
          description: UTM Zone 31, 32, 33
        hochwert:
          type: string
          description: Gibt den Hochwert eines entsprechenden Ortes an.
        rechtswert:
          type: string
          description: Gibt den Rechtswert eines entsprechenden Ortes an.
      x-apidog-orders:
        - breitengrad
        - laengengrad
        - ostwert
        - nordwert
        - zone
        - hochwert
        - rechtswert
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Zone:
      title: Zone
      type: string
      enum:
        - UTMZone31
        - UTMZone32
        - UTMZone33
      description: Zone
      x-apidog-folder: ''
    Produktpaket:
      title: Produktpaket
      type: object
      properties:
        produktpaketId:
          type: integer
          description: >-
            Produkt-Code, Produkt-Codes sind in der Codeliste der
            Konfigurationen beschrieben

            PIA 5

            PI 55001 55077 55600 55601 55014 55608 

            Priorisierung erforderliches Produktpaket

            SEQ ZH0

            PI 55001 55077 55600 55601 55014 55608 
        produkt:
          type: array
          items:
            $ref: '#/components/schemas/Produkt'
          description: |-
            Produkt
            PIA Z11
            PI 55001 55077 55600 55601 55014 55608 
        umsetzungsgradvorgabe:
          $ref: '#/components/schemas/Umsetzungsgradvorgabe'
          description: >-
            Umsetzungsgradvorgabe des Produktpakets wird unterteilt in Z01
            Produktpaket ist vollumfänglich umzusetzen oder Z02 Produktpaket
            kann in Teilen umgesetzt werden zum Zuordnungsbeginn

            CCI Z65

            PI 55001 55077 55600 55601 55014 55608
        priorisierung:
          $ref: '#/components/schemas/Priorisierung'
          description: |-
            Priorisierung erforderliches Produktpaket
            CAV Z75 
      x-apidog-orders:
        - produktpaketId
        - produkt
        - umsetzungsgradvorgabe
        - priorisierung
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Priorisierung:
      type: string
      title: Priorisierung
      description: Priorisierung
      enum:
        - PRIORITAET1
        - PRIORITAET2
        - PRIORITAET3
        - PRIORITAET4
        - PRIORITAET5
      x-apidog-enum:
        - value: PRIORITAET1
          name: 1. Priorität
          description: Z75
        - value: PRIORITAET2
          name: 2. Priorität
          description: Z76
        - value: PRIORITAET3
          name: 3. Priorität
          description: Z77
        - value: PRIORITAET4
          name: 4. Priorität
          description: Z78
        - value: PRIORITAET5
          name: 5. Priorität
          description: Z79
      x-apidog-folder: ''
    Umsetzungsgradvorgabe:
      type: string
      title: Umsetzungsgradvorgabe
      description: Umsetzungsgradvorgabe
      enum:
        - ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
        - ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR
      x-apidog-enum:
        - value: ZUORDNUNG_NUR_WENN_PRODUKTPAKET_UMSETZBAR
          name: Produktpaket ist vollumfänglich umzusetzen
          description: Z01
        - value: ZUORDNUNG_AUCH_WENN_PRODUKTPAKET_NICHT_UMSETZBAR
          name: Produktpaket kann in Teilen umgesetzt werden
          description: Z02
      x-apidog-folder: ''
    Produkt:
      title: Produkt
      type: object
      properties:
        produktCode:
          type: string
          description: |-
            Produkt-Code
            Erforderliches Produkt Abrechnungsdaten ORDERS
            PIA 5
            PI 17133
        codeProdukteigenschaft:
          type: string
          description: |-
            Code der Produkteigenschaft
            CAV ZH9
            PI 55001 55077 55600 55601 55014 55608 
        wertedetails:
          type: string
          description: >-
            Wertedetails zum Produkt, Wertedetails zum Produkt sind in der
            Codeliste der Konfigurationen beschrieben

            CAV ZV4

            PI 55001 55077 55600 55601 55014 55608 
      x-apidog-orders:
        - produktCode
        - codeProdukteigenschaft
        - wertedetails
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Energieherkunft:
      title: Energieherkunft
      type: object
      properties:
        erzeugungsart:
          $ref: '#/components/schemas/Erzeugungsart'
          description: >-
            Art der Erzeugung,  dient zur genaueren Wertspezifizierung des
            Merkmals im vorangegangen CCI Segment Z34 Art der erzeugenden
            Marktlokation.

            PI 55607 55616 55622 55628 55634 55095 55060 55043 55168 55169 55074
            55075 55076
        anteilProzent:
          type: number
          format: float
          description: Prozentualer Anteil der Erzeugung
      x-apidog-orders:
        - erzeugungsart
        - anteilProzent
      description: .
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Erzeugungsart:
      type: string
      title: Erzeugungsart
      description: Auflistung der Erzeugungsarten von Energie.
      enum:
        - EEG
        - KWK
        - EEG_DV
        - KWK_DV
        - WIND
        - SOLAR
        - KERNKRAFT
        - WASSER
        - GEOTHERMIE
        - BIOMASSE
        - KOHLE
        - GAS
        - SONSTIGE
        - SONSTIGE_EEG
        - SONSTIGE_ERZEUGUNGSART
      x-apidog-enum:
        - value: EEG
          name: EEG-Marktlokation ohne DV-Pflicht
          description: Z33
        - value: KWK
          name: KWKG-Marktlokation ohne DV-Pflicht
          description: Z34
        - value: EEG_DV
          name: EEG-Marktlokation mit DV-Pflicht
          description: Z37
        - value: KWK_DV
          name: KWKG-Marktlokation mit DV-Pflicht
          description: Z46
        - value: WIND
          name: Wind
          description: ZF6
        - value: SOLAR
          name: Solar
          description: ZF5
        - value: KERNKRAFT
          name: ''
          description: ''
        - value: WASSER
          name: Wasser
          description: ZG1
        - value: GEOTHERMIE
          name: ''
          description: ''
        - value: BIOMASSE
          name: ''
          description: ''
        - value: KOHLE
          name: ''
          description: ''
        - value: GAS
          name: Gas
          description: ZG0
        - value: SONSTIGE
          name: sonstige Marktlokation
          description: Z35
        - value: SONSTIGE_EEG
          name: ''
          description: ''
        - value: SONSTIGE_ERZEUGUNGSART
          name: Sonstige Erzeugungsart
          description: ZG5
      x-apidog-folder: ''
    Messstellenbetriebsabrechnungsdaten:
      title: Messstellenbetriebsabrechnungsdaten
      type: object
      properties:
        messstellenbetriebsabrechnung:
          type: boolean
          description: Messstellenbetriebsabrechnungsdaten der Malo
        artikelId:
          type: string
          description: >-
            Artikel-ID

            Z02 Gruppenartikel-ID / Artikel-ID

            Z03 Es wird keine Messstellenbetriebsabrechnung über diese Malo
            vorgenommen

            PIA Z02

            PI 55557
        artikelIdTyp: &ref_22
          $ref: '#/components/schemas/ArtikelIdTyp'
          description: Artikel-ID Z09
        anzahl:
          type: integer
          description: >-
            Anzahl der abzurechenden Positionen der Gruppenartikel-ID /
            Artikel-ID in Stückzahl.

            QTY Z38

            PI 55557
        zuschlag:
          type: number
          format: float
          description: Zuschlag
        abschlag:
          type: number
          format: float
          description: >-
            Abschlag, Rabatt auf einen Preis in Prozent. Kein Abschlag Z46 gibt
            man mit einer Null an. 

            QTY Z35

            PI 55557
      x-apidog-orders:
        - messstellenbetriebsabrechnung
        - artikelId
        - artikelIdTyp
        - anzahl
        - zuschlag
        - abschlag
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    ArtikelIdTyp:
      type: string
      title: ArtikelIdTyp
      description: >-
        Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene
        Artikel, die im Strommarkt die BDEW-Artikelnummer ablösen
      enum:
        - ARTIKELID
        - GRUPPENARTIKELID
      x-apidog-enum:
        - value: ARTIKELID
          name: Artikel-ID
          description: Z09
        - value: GRUPPENARTIKELID
          name: Gruppenartikel-ID
          description: Z10
      x-apidog-folder: ''
    Netznutzungsabrechnungsdaten:
      title: Netznutzungsabrechnungsdaten
      type: object
      properties:
        artikelId:
          type: string
          description: |-
            Artikel-ID Produkt-/Leistungsnummer
            PIA Z02
            55218 55220 55225 55227 55557 55559 55035 
        artikelIdTyp: *ref_22
        anzahl:
          type: integer
          description: >-
            Anzahl in der NNA abzurechenden Positionen der Gruppenartikel-ID /
            Artikel-ID angeben. Z. B. wenn in der

            NNA mehrere Zähler oder Wandlersätze abgerechnet werden müssen.

            QTY Z38

            PI 55218 55220 55557 55559 55035 
        gemeinderabatt:
          type: number
          format: float
          description: >-
            Gemeinderabatt, Angabe zum Preisnachlass der Netznutzungsentgelte
            für den Eigenverbrauch in Prozent. Kein Preisnachlass wird mit 0
            Prozent übermittelt.

            QTY Z16

            PI 55218 55220 55035 
        zuschlag:
          type: number
          format: float
          description: |-
            Zuschlag, Aufschlag auf den Preis
            QTY Z34
            PI 55218 55220 55035 
        abschlag:
          type: number
          format: float
          description: |-
            Abschlag, Rabatt auf einen Preis
            QTY Z35
            PI 55218 55220 55035 
        singulaereBetriebsmittel:
          $ref: '#/components/schemas/Menge'
          description: |-
            Singulär genutzten Betriebsmitel
            QTY Z33 
            PI 55218 55220 55035 
        preisSingulaereBetriebsmittel:
          $ref: '#/components/schemas/Preis'
          description: |-
            Preisangabe für Singulär genutzte Betriebsmitel, je Menge pro Tag.
            CCI Z44
            PI 55218 55220 55035 
        abrechnungBlindarbeit:
          type: boolean
          description: >-
            NB teilt nur mit, ob an der Netzlokation eine Abrechnung der
            Blindarbeit stattfindet ZD9 oder keine Abrechnung ZE0 stattfindet.

            CCI Z45

            PI 55225 55227 
        zahlerBlindarbeit:
          $ref: '#/components/schemas/ZahlerBlindarbeit'
          description: |-
            NB teilt mit, wer der Zahler der Blindarbeit ist.
            CAV ZE4
            PI 55225 55227 
        zahlerBlindarbeitLf:
          type: boolean
          description: >-
            Zahlung der Blindarbeit durch den Lieferanten ZE1 oder die Zahlung
            erfolgt nicht durch den Lieferanten ZE2

            CCI Z46

            PI 55230 55232 
        differenzDaten:
          type: boolean
          description: Differenz Daten
        zaehlzeiten: *ref_23
      x-apidog-orders:
        - artikelId
        - artikelIdTyp
        - anzahl
        - gemeinderabatt
        - zuschlag
        - abschlag
        - singulaereBetriebsmittel
        - preisSingulaereBetriebsmittel
        - abrechnungBlindarbeit
        - zahlerBlindarbeit
        - zahlerBlindarbeitLf
        - differenzDaten
        - zaehlzeiten
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    ZahlerBlindarbeit:
      type: string
      title: ZahlerBlindarbeit
      description: ZahlerBlindarbeit
      enum:
        - ANSCHLUSSNUTZER
        - LIEFERANT
        - NICHT_FESTGELEGT
      x-apidog-enum:
        - value: ANSCHLUSSNUTZER
          name: Anschlussnutzer
          description: Z36
        - value: LIEFERANT
          name: Lieferant
          description: Z37
        - value: NICHT_FESTGELEGT
          name: Zahler der Blindarbeit noch nicht festgelegt
          description: Z38
      x-apidog-folder: ''
    Preis:
      title: Preis
      type: object
      properties:
        wert:
          type: number
          format: float
          description: |-
            Wert Geldbetrag
            QUOTES CAL Berechnungspreis
            PI 15001 15002 15003
        einheit:
          $ref: '#/components/schemas/Waehrungseinheit'
          description: |-
            Referenzwährung EUR
            CUX 2 
            PI 19116 
        bezugswert: *ref_24
        status:
          $ref: '#/components/schemas/Preisstatus'
          description: nicht in Benutzung
        menge:
          type: integer
          description: menge
        minimaleMenge:
          type: integer
          description: minimale Menge
        maximaleMenge:
          type: integer
          description: maximale Menge
        preisart:
          $ref: '#/components/schemas/Preisart'
      x-apidog-orders:
        - wert
        - einheit
        - bezugswert
        - status
        - menge
        - minimaleMenge
        - maximaleMenge
        - preisart
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Preisart:
      type: string
      title: Preisart
      enum:
        - EINRICHTUNGSPREIS
        - TRANSAKTIONSPREIS
        - BETRIEBSPREIS
      description: Preisart Code
      x-apidog-folder: ''
    Preisstatus:
      title: Preisstatus
      type: string
      enum:
        - VORLAEUFIG
        - ENDGUELTIG
      description: Preisstatus
      x-apidog-folder: ''
    Waehrungseinheit:
      title: Waehrungseinheit
      type: string
      enum:
        - EUR
        - CT
      description: Waehrungseinheit
      x-apidog-folder: ''
    Menge:
      title: Menge
      type: object
      properties:
        wert:
          type: number
          format: float
          description: Wert Mengenangabe
        einheit: *ref_24
      x-apidog-orders:
        - wert
        - einheit
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Messlokationszuordnung:
      title: Messlokationszuordnung
      type: object
      properties:
        messlokationsId:
          type: string
          description: MesslokationsId
        arithmetik:
          $ref: '#/components/schemas/ArithmetischeOperation'
          description: nicht in Benutzung
        gueltigSeit:
          type: string
          format: date-time
          description: Zuordnung gültig ab
        gueltigBis:
          type: string
          format: date-time
          description: Zuordnung gültig bis
      x-apidog-orders:
        - messlokationsId
        - arithmetik
        - gueltigSeit
        - gueltigBis
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    ArithmetischeOperation:
      type: string
      title: ArithmetischeOperation
      description: Mit dieser Aufzählung können arithmetische Operationen festgelegt werden
      enum:
        - ADDITION
        - SUBTRAKTION
        - DIVISION
        - DIVIDEND
        - MULTIPLIKATION
        - POSITIVWERT
      x-apidog-enum:
        - value: ADDITION
          name: Addition
          description: Z69
        - value: SUBTRAKTION
          name: Subtraktion
          description: Z70
        - value: DIVISION
          name: Divisor
          description: Z80
        - value: DIVIDEND
          name: Dividend
          description: Z81
        - value: MULTIPLIKATION
          name: Faktor
          description: Z82
        - value: POSITIVWERT
          name: Positivwert
          description: Z83
      x-apidog-folder: ''
    Verbrauch:
      title: Verbrauch
      type: object
      properties:
        startdatum:
          type: string
          format: date-time
          description: >-
            Beginn Messperiode

            DTM 163

            PI 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010 13012
            13003 13023 13005 13026 13020 13022 13021 13007 13014 13027 
        enddatum:
          type: string
          format: date-time
          description: >-
            Ende Messperiode

            DTM 164

            PI 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010 13012
            13003 13023 13005 13026 13020 13022 13021 13007 13014 13027 
        wertermittlungsverfahren:
          $ref: '#/components/schemas/Wertermittlungsverfahren'
          description: Messwert oder Prognosewert - bezieht sich auf die Statusangabe
        messwertstatus:
          $ref: '#/components/schemas/Messwertstatus'
          description: >-
            Statusangaben

            PI 13017 13019 13016 13015 13002 13009 13018 13025 13008 13003 13022
            13021 13007 13027 13010 13011 13012 13003 13023 13005 13026 13020
            13013 13014 13028 
        obiskennzahl:
          type: string
          description: >-
            Produktidentifikation unter Verwendung des OBIS-Kennzeichens

            PIA 5

            SRW OBIS-Kennzahl

            PI 13017 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010
            13011 13012 13003 13005 13007 13027

            Z02 BDEW OBIS-ähnliche Kennzahl

            PI 13016 13011 13013 13014

            Z08 Medium

            PI 13023 13026 13020 13022 13021 
        wert:
          type: number
          format: float
          description: |-
            Energiemenge, Mengenangabe MSCONS
            QTY 136 Erreichte Menge in dem Zeitintervall
            PI 21045
        einheit: *ref_24
        type:
          $ref: '#/components/schemas/Verbrauchsmengetyp'
          description: nicht in Benutzung
        tarifstufe:
          $ref: '#/components/schemas/Tarifstufe'
          description: nicht in Benutzung
        nutzungszeitpunkt:
          type: string
          format: date-time
          description: |-
            Nutzungszeitpunkt - eindeutige Zählerstandszuordnung
            DTM 7
            PI 13017 13002 13027 
        ausfuehrungszeitpunkt:
          type: string
          format: date-time
          description: |-
            Ausführungs- / Änderungszeitpunkt - Konstruktionsänderungsdatum
            DTM 60
            PI 13017 13002
        position:
          type: integer
          description: >-
            Positionsdaten -  zeigt den Beginn eines Positionsteils, Hochzählung

            LIN 1

            PI 13017 13019 13016 13015 13028 13002 13009 13018 13025 13008 13010
            13011 13012 13003 13023 13005 13026 13020 13022 13021 13007 13013
            13014 13027
        ablesedatum:
          type: string
          format: date-time
          description: |-
            Ablesedatum
            DTM 9
            PI 13017 13002 
        leistungsperiode:
          type: string
          description: |-
            Leistungsperiode
            DTM 306
            PI 13016 13015 13013
        statuszusatzinformationen:
          type: array
          items:
            $ref: '#/components/schemas/StatusZusatzInformation'
          description: Plausibilisierungshinweis
      x-apidog-orders:
        - startdatum
        - enddatum
        - wertermittlungsverfahren
        - messwertstatus
        - obiskennzahl
        - wert
        - einheit
        - type
        - tarifstufe
        - nutzungszeitpunkt
        - ausfuehrungszeitpunkt
        - position
        - ablesedatum
        - leistungsperiode
        - statuszusatzinformationen
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    StatusZusatzInformation:
      title: StatusZusatzInformation
      type: object
      properties:
        art:
          $ref: '#/components/schemas/StatusArt'
          description: |-
            Z33 Plausibilisierungshinweis
            STS Z33
        status:
          $ref: '#/components/schemas/Status'
          description: |-
            Statusanlaß
            STS Z34
            PI 13017 13019 13016 13002 13009 13018 13025 13008 13002 13007
      x-apidog-orders:
        - art
        - status
      description: .
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Status:
      type: string
      title: Status
      description: Status
      enum:
        - KUNDENSELBSTABLESUNG
        - LEERSTAND
        - REALER_ZAEHLERUEBERLAUF_GEPRUEFT
        - PLAUSIBEL_WG_KONTROLLABLESUNG
        - PLAUSIBEL_WG_KUNDENHINWEIS
        - AUSTAUSCH_DES_ERSATZWERTES
        - RECHENWERT
        - BASIS_MME
        - VERGLEICHSMESSUNG_GEEICHT
        - VERGLEICHSMESSUNG_NICHT_GEEICHT
        - MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN
        - MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN
        - INTERPOLATION
        - HALTEWERT
        - BILANZIERUNG_NETZABSCHNITT
        - HISTORISCHE_MESSWERTE
        - STATISTISCHE_METHODE
        - AUFTEILUNG
        - VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS
        - UMGANGS_UND_KORREKTURMENGEN
        - ANGABEN_MESSLOKATION
        - KEIN_ZUGANG
        - KOMMUNIKATIONSSTOERUNG
        - NETZAUSFALL
        - SPANNUNGSAUSFALL
        - STATUS_GERAETEWECHSEL
        - KALIBRIERUNG
        - GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN
        - MESSEINRICHTUNG_GESTOERT_DEFEKT
        - UNSICHERHEIT_MESSUNG
        - BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK
        - MENGENUMWERTUNG_VOLLSTAENDIG
        - UHRZEIT_GESTELLT_SYNCHRONISATION
        - MESSWERT_UNPLAUSIBEL
        - FALSCHER_WANDLERFAKTOR
        - FEHLERHAFTE_ABLESUNG
        - AENDERUNG_DER_BERECHNUNG
        - UMBAU_DER_MESSLOKATION
        - DATENBEARBEITUNGSFEHLER
        - BRENNWERTKORREKTUR
        - Z_ZAHL_KORREKTUR
        - STOERUNG_DEFEKT_MESSEINRICHTUNG
        - AENDERUNG_TARIFSCHALTZEITEN
        - TARIFSCHALTGERAET_DEFEKT
        - IMPULSWERTIGKEIT_NICHT_AUSREICHEND
        - ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL
        - ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL
        - WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET
        - GESTOERTE_WERTE
        - WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN
        - KONSISTENZ_UND_SYNCHRONPRUEFUNG
        - GRUND_ANGABEN_MESSLOKATION
        - >-
          ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR
        - UMSTELLUNG_GASQUALITAET
        - >-
          ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
        - >-
          ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
        - >-
          ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
        - >-
          ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
        - GESCHEITERT
        - AUSGEBAUT
      x-apidog-enum:
        - value: KUNDENSELBSTABLESUNG
          name: Kundenselbstablesung
          description: Z83
        - value: LEERSTAND
          name: Leerstand
          description: Z84
        - value: REALER_ZAEHLERUEBERLAUF_GEPRUEFT
          name: Realer Zählerüberlauf geprüf
          description: Z85
        - value: PLAUSIBEL_WG_KONTROLLABLESUNG
          name: Plausibel wg. Kontrollablesung
          description: Z86
        - value: PLAUSIBEL_WG_KUNDENHINWEIS
          name: Plausibel wg. Kundenhinweis
          description: Z87
        - value: AUSTAUSCH_DES_ERSATZWERTES
          name: Austausch des Ersatzwertes
          description: ZC3
        - value: RECHENWERT
          name: Rechenwert
          description: ZR5
        - value: BASIS_MME
          name: Wert auf Basis der modernen Messeinrichtung
          description: ZS2
        - value: VERGLEICHSMESSUNG_GEEICHT
          name: Vergleichsmessung (geeicht)
          description: Z88
        - value: VERGLEICHSMESSUNG_NICHT_GEEICHT
          name: Vergleichsmessung (nicht geeicht)
          description: Z89
        - value: MESSWERTNACHBILDUNG_AUS_GEEICHTEN_WERTEN
          name: Messwertnachbildung aus geeichten Werten
          description: Z90
        - value: MESSWERTNACHBILDUNG_AUS_NICHT_GEEICHTEN_WERTEN
          name: Messwertnachbildung aus nicht geeichten Werten
          description: Z91
        - value: INTERPOLATION
          name: Interpolation
          description: Z92
        - value: HALTEWERT
          name: Haltewert
          description: Z93
        - value: BILANZIERUNG_NETZABSCHNITT
          name: Bilanzierung Netzabschnit
          description: Z94
        - value: HISTORISCHE_MESSWERTE
          name: Historische Messwerte
          description: Z95
        - value: STATISTISCHE_METHODE
          name: Statistische Methode
          description: ZJ2
        - value: AUFTEILUNG
          name: Aufteilung
          description: ZQ8
        - value: VERWENDUNG_VON_WERTEN_DES_STOERMENGENZAEHLWERKS
          name: Verwendung von Werten des Störmengenzählwerks
          description: ZQ9
        - value: UMGANGS_UND_KORREKTURMENGEN
          name: Umgangs- und Korrekturmengen
          description: ZR0
        - value: ANGABEN_MESSLOKATION
          name: Ersatzwertbildungsverfahren gemäß Angaben auf Ebene der Messlokation
          description: ZS0
        - value: KEIN_ZUGANG
          name: kein Zugang
          description: Z74
        - value: KOMMUNIKATIONSSTOERUNG
          name: Kommunikationsstörung
          description: Z75
        - value: NETZAUSFALL
          name: Netzausfall
          description: Z76
        - value: SPANNUNGSAUSFALL
          name: Spannungsausfall
          description: Z77
        - value: STATUS_GERAETEWECHSEL
          name: Gerätewechsel
          description: Z78
        - value: KALIBRIERUNG
          name: Kalibrierung
          description: Z79
        - value: GERAET_ARBEITET_AUSSERHALB_DER_BETRIEBSBEDINGUNGEN
          name: Gerät arbeitet außerhalb der Betriebsbedingungen
          description: Z80
        - value: MESSEINRICHTUNG_GESTOERT_DEFEKT
          name: Messeinrichtung gestört/defekt
          description: Z81
        - value: UNSICHERHEIT_MESSUNG
          name: Unsicherheit Messung
          description: Z82
        - value: BERUECKSICHTIGUNG_STOERMENGENZAEHLWERK
          name: Berücksichtigung Störmengenzählwerk
          description: Z98
        - value: MENGENUMWERTUNG_VOLLSTAENDIG
          name: Mengenumwertung unvollständig
          description: Z99
        - value: UHRZEIT_GESTELLT_SYNCHRONISATION
          name: Uhrzeit gestellt /Synchronisation
          description: ZA0
        - value: MESSWERT_UNPLAUSIBEL
          name: Messwert unplausibel
          description: ZA1
        - value: FALSCHER_WANDLERFAKTOR
          name: Falscher Wandlerfaktor
          description: ZA3
        - value: FEHLERHAFTE_ABLESUNG
          name: Fehlerhafte Ablesung
          description: ZA4
        - value: AENDERUNG_DER_BERECHNUNG
          name: Änderung der Berechnung
          description: ZA5
        - value: UMBAU_DER_MESSLOKATION
          name: Umbau der Messlokation
          description: ZA6
        - value: DATENBEARBEITUNGSFEHLER
          name: Datenbearbeitungsfehler
          description: ZA7
        - value: BRENNWERTKORREKTUR
          name: Brennwertkorrektur
          description: ZA8
        - value: Z_ZAHL_KORREKTUR
          name: Z-Zahl-Korrektur
          description: ZA9
        - value: STOERUNG_DEFEKT_MESSEINRICHTUNG
          name: Störung / Defekt Messeinrichtung
          description: ZB0
        - value: AENDERUNG_TARIFSCHALTZEITEN
          name: Änderung Tarifschaltzeiten
          description: ZB9
        - value: TARIFSCHALTGERAET_DEFEKT
          name: Tarifschaltgerät defekt
          description: ZC2
        - value: IMPULSWERTIGKEIT_NICHT_AUSREICHEND
          name: Impulswertigkeit nicht ausreichend
          description: ZC4
        - value: ENERGIEMENGE_IN_UNGEMESSENEM_ZEITINTERVALL
          name: Energiemenge in ungemessenem Zeitintervall
          description: ZJ8
        - value: ENERGIEMENGE_AUS_DEM_UNGEPAIRTEN_ZEITINTERVALL
          name: Energiemenge aus dem ungepairten Zeitintervall
          description: ZJ9
        - value: WARTUNGSARBEITEN_AN_GEEICHTEM_MESSGERAET
          name: Wartungsarbeiten an geeichtem Messgerät
          description: ZR1
        - value: GESTOERTE_WERTE
          name: gestörte Werte
          description: ZR2
        - value: WARTUNGSARBEITEN_AN_EICHRECHTSKONFORMEN_MESSGERAETEN
          name: Wartungsarbeiten an eichrechtskonformen Messgeräten
          description: ZR3
        - value: KONSISTENZ_UND_SYNCHRONPRUEFUNG
          name: Konsistenz- und Synchronprüfung
          description: ZR4
        - value: GRUND_ANGABEN_MESSLOKATION
          name: Grund der Ersatzwertbildung gemäß Angaben auf Ebene der Messlokation
          description: ZS9
        - value: >-
            ANFORDERUNG_IN_DIE_VERGANGENHEIT_ZUM_ANGEFORDERTEN_ZEITPUNKT_LIEGT_KEIN_WERT_VOR
          name: >-
            Anforderung in die Vergangenheit, zum angeforderten Zeitpunkt liegt
            kein Wert vor
          description: ZT8
        - value: UMSTELLUNG_GASQUALITAET
          name: Umstellung Gasqualität
          description: ZG3
        - value: >-
            ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
          name: >-
            Zählerstand zum Beginn der angegebenen Energiemenge vorhanden und
            kommuniziert
          description: Z36
        - value: >-
            ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_VORHANDEN_UND_KOMMUNIZIERT
          name: >-
            Zählerstand zum Ende der angegebenen Energiemenge vorhanden und
            kommuniziert
          description: Z37
        - value: >-
            ZAEHLERSTAND_ZUM_BEGINN_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
          name: >-
            Zählerstand zum Beginn der angegebenen Energiemenge nicht vorhanden
            da Mengenabgrenzung
          description: Z38
        - value: >-
            ZAEHLERSTAND_ZUM_ENDE_DER_ANGEGEBENEN_ENERGIEMENGE_NICHT_VORHANDEN_DA_MENGENABGRENZUNG
          name: >-
            Zählerstand zum Ende der angegebenen Energiemenge nicht vorhanden da
            Mengenabgrenzung
          description: Z39
        - value: GESCHEITERT
          name: ''
          description: ''
        - value: AUSGEBAUT
          name: ''
          description: ''
      x-apidog-folder: ''
    StatusArt:
      type: string
      title: StatusArt
      description: StatusArt
      enum:
        - PLAUSIBILISIERUNGSHINWEIS
        - ERSATZWERTBILDUNGSVERFAHREN
        - KORREKTURGRUND
        - GRUND_ERSATZWERTBILDUNGSVERFAHREN
        - GASQUALITAET
        - MESSKLASSIFIZIERUNG
      x-apidog-enum:
        - value: PLAUSIBILISIERUNGSHINWEIS
          name: Plausibilisierungshinweis
          description: Z33
        - value: ERSATZWERTBILDUNGSVERFAHREN
          name: Ersatzwertbildungsverfahren
          description: Z32
        - value: KORREKTURGRUND
          name: Korrekturgrund
          description: Z34
        - value: GRUND_ERSATZWERTBILDUNGSVERFAHREN
          name: Grund der Ersatzwertbildung
          description: Z40
        - value: GASQUALITAET
          name: Gasqualität
          description: Z31
        - value: MESSKLASSIFIZIERUNG
          name: Messklassifizierung
          description: '10'
      x-apidog-folder: ''
    Tarifstufe:
      type: string
      title: Tarifstufe
      description: Tarifstufe
      enum:
        - TARIFSTUFE_0
        - TARIFSTUFE_1
        - TARIFSTUFE_2
        - TARIFSTUFE_3
        - TARIFSTUFE_4
        - TARIFSTUFE_5
        - TARIFSTUFE_6
        - TARIFSTUFE_7
        - TARIFSTUFE_8
        - TARIFSTUFE_9
      x-apidog-enum:
        - value: TARIFSTUFE_0
          name: Tarifstufe 0
          description: Z20
        - value: TARIFSTUFE_1
          name: Tarifstufe 1
          description: Z21
        - value: TARIFSTUFE_2
          name: Tarifstufe 2
          description: Z22
        - value: TARIFSTUFE_3
          name: Tarifstufe 3
          description: Z23
        - value: TARIFSTUFE_4
          name: Tarifstufe 4
          description: Z24
        - value: TARIFSTUFE_5
          name: Tarifstufe 5
          description: Z25
        - value: TARIFSTUFE_6
          name: Tarifstufe 6
          description: Z26
        - value: TARIFSTUFE_7
          name: Tarifstufe 7
          description: Z27
        - value: TARIFSTUFE_8
          name: Tarifstufe 8
          description: Z28
        - value: TARIFSTUFE_9
          name: Tarifstufe 9
          description: Z29
      x-apidog-folder: ''
    Verbrauchsmengetyp:
      title: Verbrauchsmengetyp
      type: string
      enum:
        - ARBEITLEISTUNGTAGESPARAMETERABHMALO
        - VERANSCHLAGTEJAHRESMENGE
        - TUMKUNDENWERT
      description: Verbrauchsmengetyp
      x-apidog-folder: ''
    Messwertstatus:
      type: string
      title: Messwertstatus
      description: Der Status eines Zählerstandes
      enum:
        - ABGELESEN
        - ERSATZWERT
        - VORSCHLAGSWERT
        - NICHT_VERWENDBAR
        - PROGNOSEWERT
        - ENERGIEMENGESUMMIERT
        - VOLAEUFIGERWERT
        - FEHLT
        - ANGABE_FUER_LIEFERSCHEIN
        - GRUNDLAGE_POG_ERMITTLUNG
      x-apidog-enum:
        - value: ABGELESEN
          name: Wahrer Wert
          description: '220'
        - value: ERSATZWERT
          name: Ersatzwert
          description: '67'
        - value: VORSCHLAGSWERT
          name: Vorschlagswert
          description: '201'
        - value: NICHT_VERWENDBAR
          name: Nicht verwendbarer Wert
          description: '20'
        - value: PROGNOSEWERT
          name: Prognosewert
          description: '187'
        - value: ENERGIEMENGESUMMIERT
          name: Energiemenge summiert (Summenwert, Bilanzsumme)
          description: '79'
        - value: VOLAEUFIGERWERT
          name: Vorläufiger Wert
          description: Z18
        - value: FEHLT
          name: Fehlender Wert
          description: Z30
        - value: ANGABE_FUER_LIEFERSCHEIN
          name: Angabe für Lieferschein
          description: Z31
        - value: GRUNDLAGE_POG_ERMITTLUNG
          name: Grundlage POG-Ermittlung
          description: Z47
      x-apidog-folder: ''
    Wertermittlungsverfahren:
      title: Wertermittlungsverfahren
      type: string
      enum:
        - PROGNOSE
        - MESSUNG
      description: Wertermittlungsverfahren
      x-apidog-folder: ''
    ModulNetzentgelte:
      title: ModulNetzentgelte
      type: string
      enum:
        - PAUSCHALE_NETZGELDREDUZIERUNG_MODUL_1
        - PROZENTUALE_REDUZIERUNG_ARBEITSPREIS_MODUL_2
        - ANREIZMODUL_ZEITVARIABLES_NETZENTGELT_MODUL_3
      description: ModulNetzentgelte
      x-apidog-folder: ''
    Fernsteuerbarkeit:
      type: string
      title: Fernsteuerbarkeit
      description: Fernsteuerbarkeit
      enum:
        - TECHNISCH_NICHT_FERNSTEUERBAR
        - TECHNISCH_FERNSTEUERBAR
        - DURCH_LF_FERNSTEUERBAR
      x-apidog-enum:
        - value: TECHNISCH_NICHT_FERNSTEUERBAR
          name: Marktlokation ist technisch nicht fernsteuerbar
          description: Z96
        - value: TECHNISCH_FERNSTEUERBAR
          name: Marktlokation ist technisch fernsteuerbar
          description: Z97
        - value: DURCH_LF_FERNSTEUERBAR
          name: Marktlokation ist durch den Lieferanten fernsteuerbar
          description: Z98
      x-apidog-folder: ''
    StatusErzeugendeMarktlokation:
      type: string
      title: StatusErzeugendeMarktlokation
      description: StatusErzeugendeMarktlokation
      enum:
        - EINSPEISEVERGUETUNG_PARAGRAPH_37
        - GEFOERDERTE_DIREKTVERMARKTUNG
        - SONSTIGE_DIREKTVERMARKTUNG
        - VERMARKTUNG_OHNE_GESETZL_VERGUETUNG
        - KWKG_VERGUETUNG
        - EINSPEISEVERGUETUNG_PARAGRAPH_38_AUSFALLVERGUETUNG
      x-apidog-enum:
        - value: EINSPEISEVERGUETUNG_PARAGRAPH_37
          name: 'EEG-Veräußerungsform: Ausfallvergütung'
          description: Z90
        - value: GEFOERDERTE_DIREKTVERMARKTUNG
          name: 'EEG-Veräußerungsform: Marktprämie'
          description: Z91
        - value: SONSTIGE_DIREKTVERMARKTUNG
          name: ''
          description: ''
        - value: VERMARKTUNG_OHNE_GESETZL_VERGUETUNG
          name: Veräußerungsform ohne gesetzliche Vergütung
          description: Z92
        - value: KWKG_VERGUETUNG
          name: KWKG-Vergütung
          description: Z94
        - value: EINSPEISEVERGUETUNG_PARAGRAPH_38_AUSFALLVERGUETUNG
          name: ''
          description: ''
      x-apidog-folder: ''
    VerguetungEmpfaenger:
      type: string
      title: VerguetungEmpfaenger
      description: Empfänger der Vergütung zur Einspeisung
      enum:
        - KUNDE
        - LIEFERANT
      x-apidog-enum:
        - value: KUNDE
          name: Kunde
          description: Z10
        - value: LIEFERANT
          name: Lieferant
          description: Z11
      x-apidog-folder: ''
    Versorgungsart:
      type: string
      title: Versorgungsart
      description: Versorgungsart
      enum:
        - ERSATZVERSORGUNG
        - GRUNDVERSORGUNG
        - ERSATZBELIEFERUNG
      x-apidog-enum:
        - value: ERSATZVERSORGUNG
          name: Ersatzversorgung
          description: ZC9
        - value: GRUNDVERSORGUNG
          name: Grundversorgung
          description: ZD0
        - value: ERSATZBELIEFERUNG
          name: Ersatzbelieferung
          description: ZE3
      x-apidog-folder: ''
    Sperrstatus:
      type: string
      title: Sperrstatus
      description: Sperrstatus
      enum:
        - ENTSPERRT
        - GESPERRT
      x-apidog-enum:
        - value: ENTSPERRT
          name: Marktlokation im Regelbetrieb
          description: ZD3
        - value: GESPERRT
          name: Marktlokation gesperrt
          description: ZB9
      x-apidog-folder: ''
    MesstechnischeEinordnung:
      type: string
      title: MesstechnischeEinordnung
      description: MesstechnischeEinordnung
      enum:
        - IMS
        - KME_MME
        - KEINE_MESSUNG
      x-apidog-enum:
        - value: IMS
          name: iMS
          description: Z52
        - value: KME_MME
          name: kME / mME
          description: Z53
        - value: KEINE_MESSUNG
          name: keine Messung
          description: Z68
      x-apidog-folder: ''
    Zeitreihentyp:
      title: Zeitreihentyp
      type: string
      enum:
        - EGS
        - LGS
        - NZR
        - SES
        - SLS
        - TES
        - TLS
        - SLS_TLS
        - SES_TES
        - AUS
        - BAS
        - DBA
        - DZR
        - DZÜ
        - FPE
        - FPI
        - SRE
        - SRI
        - VZR
        - BIL
        - BIP
        - BIT
        - GAL
        - GAP
        - GAT
        - GEL
        - GEP
        - GET
        - SOL
        - SOP
        - SOT
        - WFL
        - WFP
        - WNL
        - WNP
        - WNT
        - WAL
        - WAP
        - WAT
        - AU1
        - BI1
        - BI2
        - BI3
        - GAA
        - GAB
        - GAC
        - GE1
        - GE2
        - GE3
        - SO1
        - SO2
        - SO3
        - WF1
        - WF2
        - WF3
        - WN1
        - WN2
        - WN3
        - WAA
        - WAB
        - WAC
      description: Zeitreihentyp
      x-apidog-folder: ''
    Katasteradresse:
      title: Katasteradresse
      type: object
      properties:
        gemarkung_flur:
          type: string
          description: Gemarkung Flur
        flurstueck:
          type: string
          description: Flurstück Name
        flurstueckNummer:
          type: string
          description: Flurstück Nummer
      x-apidog-orders:
        - gemarkung_flur
        - flurstueck
        - flurstueckNummer
      x-apidog-ignore-properties: []
      x-apidog-folder: ''
    Gebiettyp:
      title: Gebiettyp
      type: string
      enum:
        - REGELZONE
        - MARKTGEBIET
        - BILANZIERUNGSGEBIET
        - VERTEILNETZ
        - TRANSPORTNETZ
        - REGIONALNETZ
        - AREALNETZ
        - GRUNDVERSORGUNGSGEBIET
        - VERSORGUNGSGEBIET
      description: Gebiettyp
      x-apidog-folder: ''
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers:
  - url: ''
    description: Cloud Mock
security:
  - bearer: []

```
