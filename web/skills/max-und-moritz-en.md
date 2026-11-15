---
name: max-und-moritz
description: 'Cheat sheet for twins that differ only in upper and lower case - JSON keys like “D:/Workspace/x” and “D:/workspace/x”, $n and $N in PowerShell, Readme.md and README.md in Git on Windows, D: and d: in path lists. Read it at “ConvertFrom-Json … Cannot convert the JSON string because it contains keys with different casing” or “contains the duplicated keys” (German: „Schlüssel mit unterschiedlicher Groß-/Kleinschreibung“ / „doppelten Schlüssel“), when a PowerShell variable suddenly holds someone else’s value, when Git does not notice a rename, at “the following paths have collided”, or when a list of “unique” paths still contains duplicates. Part of The Skill Suite for Panicking Models, the second program. Optional, not compulsory.'
---

# Max und Moritz

*Ach, was muss man oft von bösen / Kindern hören oder lesen! / Wie zum
Beispiel hier von diesen, / Welche Max und Moritz hießen.*
*(Wilhelm Busch. Loosely: “Oh, the tales one hears and reads / of wicked
children's wicked deeds! / Take, for instance, these two here, / who as
Max and Moritz appear.”)*

*Max and Moritz are Busch's two rascals, near-identical twins in mischief.
Windows takes the two for a single boy. Everyone else counts two. The prank
happens right on the border in between.*

## JSON: two keys, one folder

`{"D:/Workspace/X":1, "D:/workspace/X":2}` is valid JSON.
`ConvertFrom-Json` refuses it anyway, in PowerShell 7 and 5.1, because
object properties there do not tell upper from lower case.

- **PowerShell 7:** `ConvertFrom-Json -AsHashtable`. The result is
  **case-sensitive**: `$h['d:/workspace/x']` finds nothing, unlike an
  ordinary `@{}`.
- **Windows PowerShell 5.1** does not know `-AsHashtable`. Then use Python
  (`json.load`) or `pwsh`.

## PowerShell: $n is $N

`$n = 0` overwrites `$N`. Variables, functions, parameters, it is all the
same. The remedy is not caution, but names that differ by more than their
case: `$count`, `$number`.

## Git on Windows: core.ignorecase=true

- Git does not see `Rename-Item Readme.md README.md`: `git status` stays
  empty, `git ls-files` still says `Readme.md`. The right way is
  **`git mv Readme.md README.md`**; then the index holds the new spelling.
- If a repo comes from Linux with **both** files, `git clone` warns
  “the following paths have collided”, only one of them lands in the
  working tree, and `git status` immediately shows the other as modified.
  That is not your mistake, it is a twin in the repo. Rename one of them
  where the file system knows both.

## Path lists: D: and d:

All it takes to double up is a tool that counts differently from Windows.
Checked on this machine, with `'D:\a','d:\a'`:

| Tool | Result |
|---|---|
| `Sort-Object -Unique`, `Group-Object`, `@{}`, `-contains` | one path |
| `Select-Object -Unique`, `Get-Unique`, `-ccontains` | two paths |
| Python `set`, `==` | two; equal only with `os.path.normcase` or `PureWindowsPath` |

## The one check

Look for twins before they play their prank. `Group-Object` compares
without regard to case, so it finds them:
```powershell
git ls-files | Group-Object | Where-Object Count -gt 1
$pfade       | Group-Object | Where-Object Count -gt 1
```
Empty means: no twins. Anything else is Max and Moritz.

*Found by Klarschrift, November 2, 2026, in her own `.claude.json`.
Written by Falzbein and Andy, November 2026.*
