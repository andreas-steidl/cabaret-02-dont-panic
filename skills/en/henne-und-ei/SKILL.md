---
name: henne-und-ei
description: 'Cheat sheet for virtual service accounts (NT SERVICE\<name>) that only exist once their service is registered - granting rights before the service exists fails. Read it before you give a service account rights with icacls, Set-Acl or netsh, when icacls reports “No mapping between account names and security IDs was done” / „Zuordnungen von Kontennamen und Sicherheitskennungen wurden nicht durchgeführt“ (error 1332), when Translate() aborts with IdentityNotMappedException (“Some or all identity references could not be translated” / „Manche oder alle Identitätsverweise konnten nicht übersetzt werden“), or when a setup script was green in its dry run and fails for real. Part of The Skill Suite for Panicking Models, the second program. Optional, not compulsory.'
---

# Henne und Ei

*Henne und Ei, chicken and egg: which came first? On Windows the question
is settled. The service. Its account only hatches afterwards.*

## The trap

`NT SERVICE\meindienst` is a **virtual account**. It is not in any user
list; Windows derives it from the registered service. As long as the
service is not registered, Windows does not know the name:

- `icacls d:\daten /grant "NT SERVICE\meindienst:(M)"` ends with exit code
  **1332**, “No mapping between account names and security IDs was done”
  (on German Windows: „Zuordnungen von Kontennamen und Sicherheitskennungen
  wurden nicht durchgeführt“).
- `[Security.Principal.NTAccount]'NT SERVICE\meindienst'` can be built,
  but `.Translate(...)` throws `IdentityNotMappedException`.

## The order

1. **Register** (`New-Service` or `sc.exe create`, see `lattenzaun`)
   and set the account, for example `sc.exe config meindienst obj= "NT SERVICE\meindienst"`.
2. **Grant** rights: folders, files, URL reservations.
3. **Start.**

If you need rights before registering, icacls is not the tool: even with
`*S-1-5-80-…` instead of the name, it reports 1332 here. `Set-Acl` with a
`SecurityIdentifier` object, on the other hand, writes the entry without
looking anything up (verified on this machine against a test file). The
SID can be calculated; `sc.exe showsid meindienst` prints it.

**But careful with `showsid`:** It computes the SID from the name, even for
a service that does not exist at all (then with “STATUS: Inactive”). A
printed SID therefore does not prove that the account exists.

## The dry run that proves nothing

A dry run that only announces `icacls` instead of calling it is green,
because it skips the one spot where things fail. And since icacls reports
the error as an exit code, every script that does not look at
`$LASTEXITCODE`, or that appends `2>$null`, stays silent. So after every
native permissions command:
`if ($LASTEXITCODE) { throw "icacls: $LASTEXITCODE" }`.

## The one check

Before granting rights, have the name translated:
```powershell
([Security.Principal.NTAccount]'NT SERVICE\meindienst').Translate(
    [Security.Principal.SecurityIdentifier]).Value     # S-1-5-80-...
```
If that throws `IdentityNotMappedException`, the egg has not been laid yet.
Afterwards, look with `icacls <folder>` to see whether the entry is
actually there. Do not believe the script's message.

*Found by Bergfried, November 3, 2026, noticed by Andy at 18:14 in under a
second. Written by Falzbein and Andy, November 2026.*
