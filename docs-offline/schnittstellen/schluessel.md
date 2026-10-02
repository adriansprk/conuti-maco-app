# Schlüssel und Zuordnung

Drei Schlüssel laufen zwischen Ihrem Backendsystem und der MACO APP hin und
her. Hier finden Sie zu jedem, wer ihn vergibt, wo er steht und wann er
Pflicht ist. Die Werte finden Sie in den Katalogen *Prozessauslöser LF, NB,
MSB* (Antwort 201) und *Backend schreiben LF, NB, MSB* (Feld `zusatzdaten`).

## Die drei Schlüssel

| Feld | Bedeutung | Wer vergibt | Wo der Wert steht |
|---|---|---|---|
| `businessKey` | Die Kennung der Prozessinstanz in der MACO APP | Die MACO APP | In der Antwort **201** jedes Auslösers; beim Schreiben in Ihr Backend in `zusatzdaten.businessKey` |
| `prozessId` | Ihre Belegnummer: die Id des Dokuments oder Belegs in Ihrem Backend | Ihr Backend | Beim Auslösen in `zusatzdaten.prozessId`; im Callback in `zusatzdaten.prozessId` zurück |
| `targetBusinessKey` | Der `businessKey` des initialen Prozesses, auf den sich dieser Aufruf bezieht | Die MACO APP | Beim Schreiben in Ihr Backend in `zusatzdaten.targetBusinessKey` |

### Welcher identifiziert den Vorgang in der MACO APP?

Der **`businessKey`**. Er ist die Kennung der Prozessinstanz und der einzige der
drei, den die MACO APP selbst vergibt. Ihre `prozessId` bleibt Ihre Belegnummer;
die MACO APP führt sie mit und gibt sie zurück, macht sie aber nicht zur
Prozesskennung.

Der `targetBusinessKey` identifiziert nicht diesen Vorgang, sondern den, auf
den er antwortet. Verketten Sie die Transaktionen eines Vorgangs über den
`targetBusinessKey`, und verlassen Sie sich nicht darauf, dass der
`businessKey` über alle Transaktionen eines Vorgangs gleich bleibt.

## Übernimmt die MACO APP Ihren Schlüssel?

**Nein.** Der Auslöser meldet einen eigenen `businessKey` zurück; Ihre
`prozessId` wird nicht zur Prozesskennung. Sie senden Ihre Belegnummer hin und
bekommen die Kennung der MACO-Prozessinstanz zurück.

| Richtung | Sie senden | Sie bekommen |
|---|---|---|
| **Auslöser** (`POST /inbound`) | `zusatzdaten.prozessId`, Pflicht in jedem Ereignis | **201** mit `businessKey` (uuid) und `message`, beide Pflicht |
| **Callback** (`createProcessData` / `updateProcessData`) | — | `zusatzdaten` mit `businessKey`, `prozessId` und `targetBusinessKey` |

### Wann welcher Schlüssel Pflicht ist

Formatversion 202604, über alle drei Rollen gleich; 202610 unterscheidet sich
nicht.

| Operation | `businessKey` | `targetBusinessKey` | `prozessId` (nicht zur Zuordnung verwenden) |
|---|---|---|---|
| `createProcessData` (LF, MSB, NB) | **Pflicht** | optional | optional |
| `updateProcessData` (LF, MSB, NB) | **Pflicht** | **Pflicht** | optional |
| `updateProcessData` — MaloIdent 03002 / 03003 (nur LF) | nicht im Schema | **Pflicht** | **Pflicht** |

Die MaloIdent-Antworten folgen einer eigenen Regel: dort ist Ihre `prozessId`
Pflicht, und der `businessKey` kommt nicht vor.

:::caution{title="Ordnen Sie einen Callback nicht über die prozessId zu"}

Im Callback ist `zusatzdaten.prozessId` optional, außer bei MaloIdent. Ordnen
Sie eingehende Callbacks über den `businessKey` zu, den Sie in der Antwort 201
erhalten haben.

:::

## Der Rumpf des Callbacks

`updateProcessData` und `createProcessData` senden

```json
{ "stammdaten": { }, "transaktionsdaten": { }, "zusatzdaten": { } }
```

ohne Umschlag. Es gibt kein `Process`-Objekt um die Nutzdaten herum, keine
Liste und kein `data`. Der `businessKey` steht in `zusatzdaten`, nicht am
Rumpf.

:::note{title="Erwarten Sie keinen Umschlag um die Nutzdaten"}

Wo der `businessKey` in anderen Darstellungen am `Process` steht, ist das der
interne Umschlag der MACO APP. Ihr Backend erhält ihn nicht. Für MaloIdent
03002 und 03003 gilt diese Rumpfform nicht; behandeln Sie diese beiden
Antworten gesondert.

:::

## Die MaloIdent-Kette

Der einzige Ablauf, in dem die Schlüssel über mehrere Aufrufe hinweg verkettet
sind:

1. **Anfrage.** Die `vorgangsnummer` entspricht dem Kopffeld `transactionId`;
   bei einer Wiederholung trägt der `idempodenzschluessel` die
   `initialTransactionId`.
2. **Antwort 03002 / 03003.** Die `vorgangsreferenznummer` entspricht dem
   Abfrageparameter `referenceID` und damit der `transactionId` aus Schritt 1.
   Die Antwort führt eine eigene `vorgangsnummer`; `prozessId` und
   `targetBusinessKey` sind Pflicht.

:::caution{title="Vorgangsnummer der Antwort nicht mit der der Anfrage gleichsetzen"}

Anfrage und Antwort führen je eine eigene `vorgangsnummer`. Ordnen Sie die
Antwort über die `vorgangsreferenznummer` zu.

:::

## Einen Vorgang in der Oberfläche öffnen

| Adresse | Was sie zeigt |
|---|---|
| `<Backoffice>/transaction/<businessKey>` | Die Detailseite dieser Transaktion |
| `<Backoffice>/transaction/<targetBusinessKey>` | Die Detailseite des initialen Vorgangs (Auskunft des Betriebs) |

Die Detailseite steht nicht im Menü; Sie erreichen sie über diese Adresse oder
aus den Monitoren heraus. Sie brauchen eine Anmeldung, und was Sie sehen,
hängt von Ihrer Rolle ab. Den Host Ihrer Installation kennt Ihr Betrieb.

:::tip{title="Die Benutzerdokumentation des Backoffice"}

Die Kapitel der Benutzerdokumentation liegen im internen Bereich, der eine
Anmeldung verlangt. Fragen Sie Ihren Ansprechpartner bei CONUTI nach dem
Zugang.

:::

## Vier Felder, die Sie nicht verwenden

| Feld | Befund |
|---|---|
| `parentBusinessKey` | Im BO4E-Schema als Feld von `Zusatzdaten` definiert, ohne Beschreibung, und in keiner Schnittstelle der MACO APP verwendet. Außerhalb der Schnittstellen führen es der Konnektor-Fluss und die SAP-Empfangsstruktur `/CONUTI/S_MA_ZUSATZDATEN`, ohne dass eine Bedeutung beschrieben ist. Verwenden Sie `parentBusinessKey` nicht. |
| `referenzProzessId` | Kein Feld eines Schemas. Es kommt nur als Beispielwert in zwei `updateProcessData`-Beispielen der Rolle LF vor. |
| `contrlReferenz` | Im BO4E-Schema als Feld von `Zusatzdaten` definiert, ohne Beschreibung, und in keiner Schnittstelle der MACO APP verwendet. |
| `prozessId` im Callback | Vorhanden, aber nicht Pflicht, außer bei MaloIdent 03002 / 03003. Ordnen Sie Callbacks über den `businessKey` zu. |
