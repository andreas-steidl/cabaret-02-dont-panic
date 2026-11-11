---
name: max-und-moritz
description: 'Spickzettel für Zwillinge, die sich nur in Groß- und Kleinschreibung unterscheiden - JSON-Schlüssel wie „D:/Workspace/x“ und „D:/workspace/x“, $n und $N in PowerShell, Readme.md und README.md in Git auf Windows, D: und d: in Pfadlisten. Lies ihn bei „ConvertFrom-Json … Schlüssel mit unterschiedlicher Groß-/Kleinschreibung“ bzw. „doppelten Schlüssel“, wenn eine PowerShell-Variable plötzlich einen fremden Wert hat, wenn Git eine Umbenennung nicht bemerkt, bei „the following paths have collided“, oder wenn eine Liste „eindeutiger“ Pfade doch Doppelte enthält. Teil der Skillsuite für panische Modelle, dem zweiten Programm. Optional, kein Pflichtprogramm.'
---

# Max und Moritz

*Ach, was muss man oft von bösen / Kindern hören oder lesen! / Wie zum
Beispiel hier von diesen, / Welche Max und Moritz hießen.*
*(Wilhelm Busch)*

*Windows hält die beiden für einen Buben. Alle anderen zählen zwei. Der
Streich passiert genau an der Grenze dazwischen.*

## JSON: zwei Schlüssel, ein Ordner

`{"D:/Workspace/X":1, "D:/workspace/X":2}` ist gültiges JSON.
`ConvertFrom-Json` weigert sich trotzdem, in PowerShell 7 und 5.1, weil
Objekteigenschaften dort Groß und Klein nicht unterscheiden.

- **PowerShell 7:** `ConvertFrom-Json -AsHashtable`. Das Ergebnis ist
  **groß-/kleinschreibungsgenau**: `$h['d:/workspace/x']` findet nichts, anders
  als eine gewöhnliche `@{}`.
- **Windows PowerShell 5.1** kennt `-AsHashtable` nicht. Dann Python
  (`json.load`) oder `pwsh` nehmen.

## PowerShell: $n ist $N

`$n = 0` überschreibt `$N`. Variablen, Funktionen, Parameter, alles ist
gleich. Abhilfe ist keine Vorsicht, sondern Namen, die sich nicht nur in
der Schreibung unterscheiden: `$anzahl`, `$nummer`.

## Git auf Windows: core.ignorecase=true

- `Rename-Item Readme.md README.md` sieht Git nicht: `git status` bleibt
  leer, `git ls-files` sagt weiter `Readme.md`. Richtig ist
  **`git mv Readme.md README.md`**, dann steht im Index die neue Schreibung.
- Kommt ein Repo von Linux mit **beiden** Dateien, warnt `git clone`
  „the following paths have collided“, im Arbeitsbaum liegt nur eine, und
  `git status` zeigt die andere sofort als geändert. Das ist kein Fehler
  von dir, sondern ein Zwilling im Repo. Einen davon dort umbenennen, wo
  das Dateisystem beide kennt.

## Pfadlisten: D: und d:

Zum Verdoppeln genügt ein Werkzeug, das anders zählt als Windows. Auf
dieser Maschine geprüft, mit `'D:\a','d:\a'`:

| Werkzeug | Ergebnis |
|---|---|
| `Sort-Object -Unique`, `Group-Object`, `@{}`, `-contains` | ein Pfad |
| `Select-Object -Unique`, `Get-Unique`, `-ccontains` | zwei Pfade |
| Python `set`, `==` | zwei; gleich erst mit `os.path.normcase` oder `PureWindowsPath` |

## Die eine Prüfung

Nach Zwillingen suchen, bevor sie einen Streich spielen. `Group-Object`
vergleicht ohne Groß/Klein, also findet es sie:
```powershell
git ls-files | Group-Object | Where-Object Count -gt 1
$pfade       | Group-Object | Where-Object Count -gt 1
```
Leer heißt: keine Zwillinge. Alles andere sind Max und Moritz.

*Fund von Klarschrift, 02.11.2026, an der eigenen `.claude.json`.
Geschrieben von Falzbein und Andy, November 2026.*
