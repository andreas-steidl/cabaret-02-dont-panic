---
name: stille-post
description: 'Cheat sheet for return values and data that get lost along the way - pipes swallow exit codes (pytest | tail -1 is green although tests are red), sudo -S eats the first line of stdin, secrets passed as arguments show up in ps, and one-liners through ssh + sudo + bash -c + sed break apart. Read it before you pipe test output into tail, head, grep, findstr or Select-Object and then check for success, when a chain keeps running despite an error, when the first line is missing after sudo -S, when a password sits in a command line, or when a remote command breaks with “unknown command” or “No such file” in the wrong place. Part of The Skill Suite for Panicking Models, the second program. Optional, not compulsory.'
---

# Stille Post

*Stille Post is the telephone game, Chinese whispers: the message changes
along the line. At the start of the row, someone whispers “three tests
red.” At the end, the last one says out loud: “All good.” Nobody lied. It
is just that everyone in the row was someone else.*

## The pipe reports its last man

In Bash, the exit code of a pipe is that of the **last** command. Checked:

```bash
(exit 3) | tail -1; echo $?          # 0
set -o pipefail; (exit 3) | tail -1; echo $?   # 3
(exit 3) | tail -1; echo "${PIPESTATUS[@]}"    # 3 0
```
- `set -e` alone does not help; the chain keeps running. Only `set -eo pipefail`.
- `x=$(pytest | tail -1)` is 0 as well without `pipefail`, and `local y=$(befehl)`
  is **always** 0, because `local` itself succeeds. First `local y`, then `y=$(…)`.

**PowerShell** keeps `$LASTEXITCODE` for the **most recently finished
native** command. `pytest | Select-Object -Last 1` keeps pytest's code,
`pytest | findstr passed` overwrites it with findstr's. The safe way is to
capture first and filter afterwards:
```powershell
$ausgabe = pytest 2>&1; $code = $LASTEXITCODE; $ausgabe | Select-Object -Last 1
if ($code) { throw "pytest: $code" }
```

## Sudo eats the first line

`printf '%s\n' "$PW" | sudo -S befehl` makes sudo read **one line** from
stdin. If data then follows over the same stream, its first line is
already gone, or the other way round: If sudo still has a valid timestamp
and does not ask at all, the password lands as the first line of the data.
(On Linux, not verified on this machine.) The remedy: never send password
and data down the same line; put the data down as a file.

**Never pass secrets as arguments.** `mysql -pGEHEIM` or an expanded
`"$PW"` in the command line is visible on most systems to every user, in
`ps` and `/proc/<pid>/cmdline`. Better a file with permissions 0600, or an
environment variable that the program reads itself (`MYSQL_PWD` in the
container).

## From the third layer on, a file

`ssh` + `sudo bash -c` + `sed` + quotes are four people in the row, and
each one reads backticks, `$` and `\` in their own way. From the third
layer on, no more one-liners: write the script locally, `scp skript.sh
host:/tmp/`, then `ssh host 'sudo bash /tmp/skript.sh'`. The script arrives
as it was written, and you can look at it over there with `cat`.

## The one check

Capture the exit code **before** the pipe and print it, not whatever
arrives at the end of the row: in Bash `"${PIPESTATUS[0]}"` or
`set -o pipefail`, in PowerShell `$code` as above. A green `tail -1` is not
a green test.

*Found by Steinmann (09:57, with a legal text on master) and Mira
(“Sudo eats the first line”, “Nested until it breaks”), November 2 and 3,
2026. Written by Falzbein and Andy, November 2026.*
