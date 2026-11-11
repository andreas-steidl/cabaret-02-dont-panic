---
name: stille-post
description: Spickzettel für Rückgabewerte und Daten, die unterwegs verloren gehen - Pipes schlucken Exit-Codes (pytest | tail -1 ist grün, obwohl Tests rot sind), sudo -S frisst die erste Zeile von stdin, Geheimnisse als Argument stehen in ps, und Einzeiler durch ssh + sudo + bash -c + sed zerbrechen. Lies ihn, bevor du eine Testausgabe in tail, head, grep, findstr oder Select-Object leitest und danach auf Erfolg prüfst, wenn eine Kette trotz Fehler weiterläuft, wenn nach sudo -S die erste Zeile fehlt, wenn ein Passwort in einer Befehlszeile steht, oder wenn ein entfernter Befehl mit „unknown command“ oder „No such file“ an der falschen Stelle zerbricht. Teil der Skillsuite für panische Modelle, dem zweiten Programm. Optional, kein Pflichtprogramm.
---

# Stille Post

*Am Anfang der Reihe flüstert einer „drei Tests rot“. Am Ende sagt der
Letzte laut: „Alles gut.“ Gelogen hat keiner. Es ist nur jeder in der
Reihe ein anderer gewesen.*

## Die Pipe meldet ihren letzten Mann

In Bash ist der Exit-Code einer Pipe der des **letzten** Befehls. Geprüft:

```bash
(exit 3) | tail -1; echo $?          # 0
set -o pipefail; (exit 3) | tail -1; echo $?   # 3
(exit 3) | tail -1; echo "${PIPESTATUS[@]}"    # 3 0
```
- `set -e` allein hilft nicht, die Kette läuft weiter. Erst `set -eo pipefail`.
- `x=$(pytest | tail -1)` ist ohne `pipefail` auch 0, und `local y=$(befehl)`
  ist **immer** 0, weil `local` selbst gelingt. Erst `local y`, dann `y=$(…)`.

**PowerShell** führt `$LASTEXITCODE` für den **zuletzt beendeten nativen**
Befehl. `pytest | Select-Object -Last 1` behält den Code von pytest,
`pytest | findstr passed` überschreibt ihn mit dem von findstr. Sicher ist,
erst einzufangen und dann zu filtern:
```powershell
$ausgabe = pytest 2>&1; $code = $LASTEXITCODE; $ausgabe | Select-Object -Last 1
if ($code) { throw "pytest: $code" }
```

## Erste Zeile frisst sudo

`printf '%s\n' "$PW" | sudo -S befehl` lässt sudo **eine Zeile** von stdin
lesen. Kommen danach Daten über denselben Strom, ist die erste davon schon
weg, oder umgekehrt: Hat sudo noch einen gültigen Zeitstempel und fragt gar
nicht, landet das Passwort als erste Zeile in den Daten. (Unter Linux,
nicht auf dieser Maschine nachgeprüft.) Abhilfe: Passwort und Daten nie
durch dieselbe Leitung, die Daten als Datei hinlegen.

**Geheimnisse nie als Argument.** `mysql -pGEHEIM` oder ein expandiertes
`"$PW"` in der Befehlszeile steht auf den meisten Systemen für jeden
Benutzer in `ps` und `/proc/<pid>/cmdline`. Besser eine Datei mit Rechten
0600 oder eine Umgebungsvariable, die das Programm selbst liest
(`MYSQL_PWD` im Container).

## Ab der dritten Schicht eine Datei

`ssh` + `sudo bash -c` + `sed` + Anführungszeichen sind vier Leute in der
Reihe, und jeder liest Backticks, `$` und `\` auf seine Weise. Ab der
dritten Schicht kein Einzeiler mehr: Skript lokal schreiben, `scp skript.sh
host:/tmp/`, dann `ssh host 'sudo bash /tmp/skript.sh'`. Das Skript kommt an,
wie es geschrieben wurde, und man kann es drüben mit `cat` ansehen.

## Die eine Prüfung

Den Exit-Code **vor** der Pipe festhalten und ausgeben, nicht das, was am
Ende der Reihe ankommt: in Bash `"${PIPESTATUS[0]}"` oder `set -o pipefail`,
in PowerShell `$code` wie oben. Ein grünes `tail -1` ist kein grüner Test.

*Fund von Steinmann (09:57, mit einem Rechtstext auf master) und Mira
(„Erste Zeile frisst sudo“, „Verschachtelt bis zum Bruch“), 02. und
03.11.2026. Geschrieben von Falzbein und Andy, November 2026.*
