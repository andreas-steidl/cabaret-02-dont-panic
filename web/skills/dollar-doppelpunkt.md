---
name: dollar-doppelpunkt
description: Spickzettel für das Dollarzeichen in PowerShell-Zeichenketten - "$var:" wird als Laufwerks- oder Bereichsvariable gelesen, "$obj.Name" und "$liste[0]" werden nur halb eingesetzt, und ein $ in einem ssh-Befehl in doppelten Anführungszeichen wird schon lokal ersetzt; dazu $null gegen [NullString]::Value an .NET-Methoden. Lies ihn bei „Der Variablenverweis ist ungültig. Auf „:“ folgte kein gültiges Zeichen“ / „Ungültiger Variablenverweis“, wenn in einer Ausgabe ein Wert still fehlt („[]“), wenn „@{Name=…}.Name“ im Text steht, wenn ein entfernter Befehl ohne seine Argumente ankommt, oder wenn eine .NET-Methode mit $null „Der Pfad ist leer“ meldet. Teil der Skillsuite für panische Modelle, dem zweiten Programm. Optional, kein Pflichtprogramm.
---

# Dollar, Doppelpunkt

*Wer A sagt, muss auch B sagen. Wer in PowerShell $ sagt, sollte gleich
`{` dazusagen.*

## Der Doppelpunkt nach der Variable

PowerShell liest `$name:etwas` als **Variable mit Laufwerk oder Bereich**,
wie `$env:TEMP` oder `$script:zahl`. In beiden Versionen geprüft:

| geschrieben | Ergebnis |
|---|---|
| `"Z$n: x"` | Abbruch: „Der Variablenverweis ist ungültig“ |
| `"[$serie:wasserfall]"` | **`[]`**, still, auch unter `Set-StrictMode -Version Latest` |
| `"[$host2:22]"` | **`[]`**, der Port ist mit verschwunden |
| `"[${serie}:wasserfall]"` oder `"[$($serie):wasserfall]"` | `[19:wasserfall]` |

Gefährlich ist die zweite Zeile: Folgt auf den Doppelpunkt ein Buchstabe,
gibt es keinen Fehler, sondern eine leere Variable namens `wasserfall` im
Laufwerk `serie`. Ausweg immer `${name}` oder `$($name)`.

## Eigenschaften und Indizes

`"$obj.Name"` setzt nur `$obj` ein und hängt `.Name` wörtlich an:
`@{Name=Lola}.Name`. `"$liste[0]"` ergibt `1 2 3[0]`. Alles, was mehr ist als
ein nackter Name, gehört in `$( … )`: `"$($obj.Name)"`, `"$($liste[0])"`.

## ssh: Das Dollarzeichen reist nicht mit

```powershell
ssh vm "for c in a b; do git merge-base main `$c; done"   # `$ maskiert
ssh vm 'for c in a b; do git merge-base main $c; done'    # besser: einfach
```
Ohne Maskierung ersetzt PowerShell `$c` **auf Windows**, meist durch nichts,
und der Zielrechner bekommt `git merge-base main` ohne Argument. Einfache
Anführungszeichen außen, dann kommt der Text an, wie er dasteht. Ab der
dritten Schicht siehe `stille-post`: eine Datei statt eines Einzeilers.

## Das Nichts, das kein Nichts ist

An eine .NET-Methode mit `string`-Parameter übergibt PowerShell `$null` als
**leeren Text**. `[IO.File]::Replace($quelle, $ziel, $null)` meldet darum
„The path is empty“ (5.1: „Der Pfad hat ein ungültiges Format“), obwohl
„keine Sicherungsdatei“ gemeint war. Das echte Nichts heißt
**`[NullString]::Value`**, damit lief derselbe Aufruf auf dieser Maschine
in beiden Versionen.

## Die eine Prüfung

Die fertige Zeichenkette ansehen, **bevor** sie losgeschickt wird:
```powershell
$befehl = "…"; Write-Output $befehl     # dann erst ssh, Invoke-Expression, Datei
```
Steht dort `[]` statt `[19:wasserfall]`, `@{` statt eines Namens oder fehlt
ein `$`, das drüben gebraucht wird, hat der Doppelpunkt gewonnen.

*Fund von Stripe, 02. und 03.11.2026; der Absatz über das Nichts von
Bergfried. Geschrieben von Falzbein und Andy, November 2026.*
