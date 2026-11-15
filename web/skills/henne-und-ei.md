---
name: henne-und-ei
description: Spickzettel für virtuelle Dienstkonten (NT SERVICE\<name>), die es erst gibt, wenn ihr Dienst eingetragen ist - Rechte vergeben, bevor der Dienst existiert, scheitert. Lies ihn, bevor du einem Dienstkonto mit icacls, Set-Acl oder netsh Rechte gibst, wenn icacls „Zuordnungen von Kontennamen und Sicherheitskennungen wurden nicht durchgeführt“ / „No mapping between account names and security IDs was done“ meldet (Fehler 1332), wenn Translate() mit IdentityNotMappedException („Manche oder alle Identitätsverweise konnten nicht übersetzt werden“) abbricht, oder wenn ein Einrichtungsskript im Trockenlauf grün war und echt scheitert. Teil der Skillsuite für panische Modelle, dem zweiten Programm. Optional, kein Pflichtprogramm.
---

# Henne und Ei

*Was war zuerst da, die Henne oder das Ei? Bei Windows ist die Frage
entschieden: der Dienst. Sein Konto schlüpft erst danach.*

## Die Falle

`NT SERVICE\meindienst` ist ein **virtuelles Konto**. Es steht in keiner
Benutzerliste, Windows leitet es aus dem eingetragenen Dienst ab. Solange
der Dienst nicht eingetragen ist, kennt Windows den Namen nicht:

- `icacls d:\daten /grant "NT SERVICE\meindienst:(M)"` endet mit
  Exit-Code **1332**, „Zuordnungen von Kontennamen und Sicherheitskennungen
  wurden nicht durchgeführt“.
- `[Security.Principal.NTAccount]'NT SERVICE\meindienst'` lässt sich bauen,
  aber `.Translate(...)` wirft `IdentityNotMappedException`.

## Die Reihenfolge

1. **Eintragen** (`New-Service` oder `sc.exe create`, siehe `lattenzaun`)
   und das Konto setzen, etwa `sc.exe config meindienst obj= "NT SERVICE\meindienst"`.
2. **Rechte** vergeben: Ordner, Dateien, URL-Reservierungen.
3. **Starten.**

Wer Rechte vor dem Eintragen braucht, nimmt nicht icacls: Auch mit
`*S-1-5-80-…` statt des Namens meldet es hier 1332. `Set-Acl` mit einem
`SecurityIdentifier`-Objekt schreibt den Eintrag dagegen ohne Nachschlagen
(auf dieser Maschine an einer Probedatei nachgeprüft). Die SID ist
berechenbar, `sc.exe showsid meindienst` gibt sie aus.

**Aber Vorsicht mit `showsid`:** Es rechnet die SID aus dem Namen, auch für
einen Dienst, den es gar nicht gibt (dann mit „STATUS: Inaktiv“). Eine
ausgegebene SID beweist also nicht, dass das Konto existiert.

## Der Trockenlauf, der nichts beweist

Ein Trockenlauf, der `icacls` nur ankündigt statt aufruft, ist grün, weil er
die eine Stelle überspringt, an der es scheitert. Und weil icacls den Fehler
als Exit-Code meldet, schweigt jedes Skript, das `$LASTEXITCODE` nicht
ansieht oder `2>$null` anhängt. Nach jedem nativen Rechte-Befehl also:
`if ($LASTEXITCODE) { throw "icacls: $LASTEXITCODE" }`.

## Die eine Prüfung

Vor der Rechtevergabe den Namen übersetzen lassen:
```powershell
([Security.Principal.NTAccount]'NT SERVICE\meindienst').Translate(
    [Security.Principal.SecurityIdentifier]).Value     # S-1-5-80-...
```
Wirft das `IdentityNotMappedException`, ist das Ei noch nicht gelegt. Danach
mit `icacls <ordner>` nachsehen, ob der Eintrag dort steht, nicht der
Meldung des Skripts glauben.

*Fund von Bergfried, 03.11.2026, um 18:14 von Andy in unter einer Sekunde
bemerkt. Geschrieben von Falzbein und Andy, November 2026.*
