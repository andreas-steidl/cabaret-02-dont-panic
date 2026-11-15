---
name: leerer-platz
description: Spickzettel für Plätze, die leer bleiben oder doppelt besetzt sind - Start-Process -ArgumentList mit einem leeren Element (ein nicht gesetzter Suffix, ein optionaler Schalter), leere Argumente beim Aufruf nativer Programme, Junctions und Symlinks, durch die Python und Node zwei verschiedene Orte für dieselbe Datei sehen, und Wachen unter WSL auf /mnt/c oder /mnt/d, die nie anschlagen. Lies ihn bei „Das Argument für den Parameter "ArgumentList" kann nicht überprüft werden. Das Argument ist NULL oder leer“, wenn Argumente verrutscht ankommen, bei „No test suite found“ oder doppelt geladenen Bibliotheken nach einem mklink/New-Item -ItemType Junction, oder wenn ein inotify-Wächter unter WSL still ewig wartet. Teil der Skillsuite für panische Modelle, dem zweiten Programm. Optional, kein Pflichtprogramm.
---

# Leerer Platz

*„Ist hier noch frei?“ Im Theater eine höfliche Frage. In einer
Argumentliste eine, auf die jede PowerShell anders antwortet.*

## Start-Process und der leere Stuhl

Ein Suffix, der nicht gesetzt ist, ist `''`, und
`Start-Process prog -ArgumentList @('eins', $suffix, 'drei')` geht dann so
aus (auf dieser Maschine geprüft):

| | Windows PowerShell 5.1 | PowerShell 7.6 |
|---|---|---|
| `Start-Process` | Abbruch: „Das Argument ist NULL oder leer“, ohne zu sagen, welches | startet, der leere Platz **verschwindet**, alle rücken auf |
| `& prog eins '' drei` | der leere Platz **verschwindet** | kommt richtig als `''` an |

Dazu kommt bei `Start-Process` in 7.6: `'mit leer'` kommt als **zwei**
Argumente an, weil die Liste nur mit Leerzeichen zusammengeklebt wird.

**Was hilft:** leere Elemente vorher herausnehmen und Argumente mit
Leerzeichen selbst in `"…"` setzen, oder gleich `&` in PowerShell 7 nehmen:
```powershell
$argumente = @('eins', $suffix, 'drei') | Where-Object { $_ }
```

## Junction: ein Stuhl, zwei Platznummern

Geliehene Ordner per Junction oder Symlink (`node_modules`, `venv`) haben
zwei Adressen, und Werkzeuge wählen verschieden. Durch eine Junction
aufgerufen, geprüft:
- **Python:** `__file__` und `sys.path[0]` zeigen den **Link**,
  `os.path.realpath(__file__)` das Ziel.
- **Node:** `__filename` zeigt das **Ziel** (außer mit `--preserve-symlinks`).
  Module werden darum vom echten Ort aus gesucht, und zwei Kopien derselben
  Bibliothek können sich begegnen, ohne sich zu kennen.

Lieber echt installieren als leihen.

## WSL: die Wache, die nie anschlägt

Unter WSL 2 liegen `/mnt/c`, `/mnt/d` auf einem Windows-Laufwerk (drvfs).
Änderungen, die **Windows-Programme** dort machen, melden sich nach
verbreiteter Erfahrung nicht über inotify (auf dieser Maschine nicht
nachprüfbar, die WSL-Distribution startet nicht). `inotifywait`, `watchdog`
oder ein `--watch`-Modus warten dann ewig und still. Dort abfragen statt
lauschen (Polling, z. B. `PollingObserver`, `usePolling: true`), oder die
Datei im Linux-Dateisystem halten. Und jeder Wache eine Zeitgrenze geben.

## Die eine Prüfung

Das Zielprogramm sagen lassen, was angekommen ist, bevor es ernst wird: eine
Datei `argv.py` mit `import sys; print(sys.argv[1:])` an die Stelle des
Programms setzen, mit genau derselben Argumentliste (nicht `python -c "…"`,
dessen Code `Start-Process` selbst zerlegen würde). Zählt es andere Plätze,
ist einer leer geblieben. Bei Junctions `(Get-Item pfad).LinkType`, bei
Wachen einmal selbst eine Datei anfassen und sehen, ob sie anschlägt.

*Fund von Steinmann (der Rangierer, 03.11.2026, 18:4x), Stripe (Junction)
und Mira (drvfs). Geschrieben von Falzbein und Andy, November 2026.*
