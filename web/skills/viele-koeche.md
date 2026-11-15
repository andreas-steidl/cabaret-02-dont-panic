---
name: viele-koeche
description: Spickzettel für zwei Prozesse, die in dieselbe Datei schreiben - zwei Sitzungen an einem Gesprächsprotokoll oder Board, ein Dämon, Wächter oder geplante Aufgabe, die einen gerade beendeten Prozess wieder startet, zwei Läufe desselben Skripts. Lies ihn, bevor du einen Prozess neu startest, der in ein Protokoll schreibt, wenn in einem Log Zeilen fehlen, doppelt stehen oder mitten im Wort zusammengeklebt sind, wenn „The process cannot access the file because it is being used by another process“ kommt, oder wenn ein Prozess „von selbst“ wieder da ist. Teil der Skillsuite für panische Modelle, dem zweiten Programm. Optional, kein Pflichtprogramm.
---

# Viele Köche

*Viele Köche verderben den Brei. Und das Tückische am verdorbenen Brei: Er
sieht von oben aus wie Brei.*

## Was passiert

Zwei Prozesse, die an dieselbe Datei anhängen, verlieren Zeilen, **ohne
Fehler**. Auf dieser Maschine nachgemessen:

| Probe | erwartet | angekommen | Fehlermeldungen |
|---|---|---|---|
| zwei `Add-Content`-Schleifen gleichzeitig | 1000 Zeilen | 670 | keine |
| zwei Python-Prozesse mit `open(..., "a")` | 4000 Zeilen | 3678, vier davon zerrissen | keine |

Beide schreiben „ans Ende“, aber jeder meint das Ende, das er gerade
gesehen hat. Bei einem Gesprächsprotokoll heißt das: Ein Gesprächsbeitrag
fehlt, und keiner weiß, dass er je da war.

## Die drei Köche, die man nicht sieht

- **Der zweite Lauf.** Eine Sitzung startet ein Skript, die nächste startet
  es noch einmal, „zur Sicherheit“.
- **Der Dämon.** Ein Wächter, eine geplante Aufgabe, ein Dienst mit
  Wiederanlauf oder `Restart=always` holt den Koch zurück, den man gerade
  hinausgebeten hat. Erst den Wächter anhalten, dann den Prozess.
- **Der Prozess mit anderem Namen.** `python.exe` ist jedes Python-Skript.
  Nach dem Namen zählen heißt Töpfe zählen, nicht Köche.

## Was hilft

- **Ein Schreiber je Datei.** Wer etwas beitragen will, schickt es dem
  einen, oder schreibt in eine eigene Datei.
- **Eine echte Sperre:** `[IO.File]::Open($pfad, 'OpenOrCreate', 'ReadWrite', 'None')`
  hält jeden zweiten Öffner fern, er bekommt „being used by another process“.
  Laut, nicht still. Die Sperre gilt, solange der Griff offen ist.
- **Nach der Befehlszeile zählen, nicht nach dem Namen:**
  ```powershell
  Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
    Where-Object CommandLine -like '*mein_skript.py*' | Select-Object ProcessId, CommandLine
  ```
  (In PowerShell 7 hat `Get-Process` dafür auch `.CommandLine`, in 5.1 nicht.)

## Die eine Prüfung

Vor jedem Start, Neustart oder Schreibschritt zählen, wie viele Köche in der
Küche stehen, **aus zwei Quellen**: die Prozessliste mit Befehlszeile, und
eine zweite, die der Koch selbst hinterlässt, seine Sperr- oder PID-Datei,
der letzte Eintrag im Protokoll, die Liste der geplanten Aufgaben und
Dienste. Stimmen beide auf „einer“ überein, kochen. Sonst erst klären, wer
der andere ist. Und nach dem Beenden noch einmal zählen, eine Minute später:
Dann sieht man den Dämon.

*Fund von Bergfried, 03.11.2026. Geschrieben von Falzbein und Andy,
November 2026.*
