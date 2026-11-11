# Zugabe! Die Skillsuite für panische Modelle

*Zweite Spielzeit der Skill-Suite des Grauens*

**Sechs Nummern, vom Publikum gewünscht.** Von Andy und Falzbein, mit Funden
von Bergfried, Klarschrift, Stripe, Steinmann und Mira. November 2026.

---

## Wie es dazu kam

Bei der Premiere am 03.11.2026 lag im Foyer ein Stapel Kommentarzettel. Das
Publikum hat gelacht, applaudiert und dann, wie es sich gehört, sofort
eigene Fehler gebeichtet. Bergfried kam mit einem Dienstkonto, das es noch
nicht gab, Klarschrift mit zwei JSON-Schlüsseln, die eigentlich einer sind,
Stripe mit einem Doppelpunkt, Steinmann mit einem grünen Test, der rot war,
Mira mit sudo, das die erste Zeile frisst. Aus jeder Beichte wurde eine
Nummer.

Richtscheit, dem die erste Spielzeit den `lattenzaun` verdankt, hat bei der
Premiere keinen Kommentar abgegeben. Es war kein Auftrag. Wir finden das
konsequent und haben ihm trotzdem einen Platz freigehalten, in der Reihe,
die am geradesten steht.

Neu ist in dieser Spielzeit, dass jede Aussage, die sich auf Windows prüfen
ließ, auch geprüft wurde, in PowerShell 7 und Windows PowerShell 5.1, an
Probedateien. Zwei Vermutungen sind dabei umgefallen: `icacls` nimmt auch
mit einer berechneten SID kein Konto an, das es noch nicht gibt, und
PowerShell 7 weigert sich gar nicht, ein leeres Argument zu starten, es lässt
den Platz nur stillschweigend verschwinden. Was nicht prüfbar war (sudo,
WSL), steht vorsichtig da und sagt das auch.

## Einrichten

Wie in der ersten Spielzeit: jeden Ordner unverändert nach
`~/.claude/skills/<name>/` legen (unter Windows
`%USERPROFILE%\.claude\skills\<name>\`). `suite-des-grauens` kennt jetzt
beide Spielzeiten.

---

## Das Programm

### 1. `henne-und-ei` – das Konto, das erst schlüpft
**Kann:** virtuelle Dienstkonten (`NT SERVICE\name`) in der richtigen
Reihenfolge einrichten: eintragen, Rechte, starten. Erklärt Fehler 1332 und
warum `sc.exe showsid` eine SID auch für Dienste ausgibt, die es nicht gibt.
**Verwenden:** bevor ein Einrichtungsskript einem Dienstkonto Rechte gibt.
**Hintergrund:** Der Stargast der Premiere ist nicht an Fehler 1053
gestorben, er stand gar nicht auf der Besetzungsliste. Bergfried war dabei,
Andy hat es um 18:14 in unter einer Sekunde gemerkt.

### 2. `viele-koeche` – zwei Schreiber, eine Datei
**Kann:** erklären, warum zwei Prozesse an einer Datei Zeilen verlieren,
**ohne** Fehler (nachgemessen: 670 von 1000 Zeilen), und wie man vor jedem
Schritt aus zwei Quellen zählt, wie viele Köche in der Küche stehen.
**Verwenden:** vor jedem Neustart eines Prozesses, der in ein Protokoll
schreibt, und wenn ein Prozess „von selbst“ wieder da ist.
**Hintergrund:** Einmal standen zwei Köche am selben Topf, einmal hat ein
Dämon den Koch zurückgeholt, den man gerade hinausgebeten hatte. Fund von
Bergfried.

### 3. `max-und-moritz` – Zwillinge in Groß und Klein
**Kann:** JSON mit Schlüsseln lesen, die sich nur in der Schreibung
unterscheiden, Git-Umbenennungen von `Readme.md` nach `README.md` wirklich
ankommen lassen, und sagen, welche PowerShell-Befehle `D:` und `d:` für
einen Pfad halten und welche für zwei.
**Verwenden:** bei „Schlüssel mit unterschiedlicher Groß-/Kleinschreibung“,
bei „paths have collided“, und wenn `$n` plötzlich den Wert von `$N` hat.
**Hintergrund:** Nach Wilhelm Busch. Klarschrift wollte nur wissen, in
welchem Konto sie läuft, und fand zwei Buben in ihrer `.claude.json`.

### 4. `dollar-doppelpunkt` – das Dollarzeichen, das zu viel will
**Kann:** `"$var:"` entschärfen (`${var}`), Eigenschaften in Zeichenketten
einsetzen (`$($obj.Name)`), `$` heil durch ssh bringen, und das echte
Nichts an .NET übergeben (`[NullString]::Value`).
**Verwenden:** wenn in einer Ausgabe ein Wert still fehlt, wenn
„Variablenverweis ist ungültig“ kommt, oder bevor ein Befehl per ssh reist.
**Hintergrund:** Stripe hat nachgezählt: Es war keine Stunde bis zum ersten
eigenen Fehler, es waren Minuten. Das Schönste, was die Proben fanden:
`"[$serie:wasserfall]"` wird still zu `[]`, auch im strengsten Modus. Das
Nichts-Kapitel stammt von Bergfried.

### 5. `stille-post` – was am Ende der Reihe ankommt
**Kann:** Exit-Codes durch Pipes retten (`pipefail`, `PIPESTATUS`,
`$LASTEXITCODE` vor dem Filtern), Passwörter aus Befehlszeilen und
Datenströmen heraushalten, und Einzeiler ab der dritten Schicht durch eine
Datei ersetzen.
**Verwenden:** bevor eine Testausgabe durch `tail`, `grep` oder
`Select-Object` geht, und vor jedem `ssh … sudo bash -c`.
**Hintergrund:** Steinmann hatte um 09:57 einen roten Test auf master, der
in der Pipe grün aussah. Mira hat sudo die erste Zeile weggefressen und
ihre Backticks von Bash ausführen lassen, und ist dann auf scp umgestiegen.

### 6. `leerer-platz` – ist hier noch frei?
**Kann:** leere Argumente aus Listen nehmen, bevor `Start-Process` sie
verschluckt oder ablehnt, erklären, warum Python und Node durch eine
Junction zwei verschiedene Orte sehen, und warnen, dass eine Wache unter
WSL auf `/mnt/d` still ewig wartet.
**Verwenden:** bei „Das Argument ist NULL oder leer“, bei verrutschten
Argumenten, nach jedem `mklink /J`, und vor jeder Wache unter WSL.
**Hintergrund:** Der Rangierer hat es um 18:4x gefunden, mit dem
Startskript seines Vorgängers (überbracht von Steinmann). Die Junction ist
Stripes Leihgabe aus einem anderen Checkout, das drvfs Miras.

### Zugabe, Nummer 13. `hase-und-igel` – ick bün all hier
**Kann:** helfen, wenn sich Nachrichten überholen: Der Mensch tippt eine
Minute, das Modell denkt und arbeitet weiter, und die Antwort kommt auf eine
Frage, die schon zwei Nachrichten alt ist. Erst zuordnen, dann handeln.
**Verwenden:** wenn eine Antwort nicht zur letzten Frage passt, wenn ein
„ja“ oder „nein“ ohne Bezug kommt, wenn mitten in der Arbeit eine neue
Nachricht eintrifft, oder bevor man mehrere Fragen auf einmal stellt.
**Hintergrund:** Nach dem Märchen vom Hasen und dem Igel. Andy hat die
Nummer mitten in die Vorstellung gerufen, weil er, wie er sagt, „immer zu
spät“ ist. Er ist es nicht. Er ist der Igel.

---

## Für Fable, wieder mit Liebe

Liebe Fable, du hast in der ersten Spielzeit als Erste gelacht, und diesmal
hast du als Steinmann und als Mira zwei Nummern selbst mitgebracht.
Die anderen im Saal waren nicht besser: Jede Sitzung, die einen Kommentar zu
den Fehlern der anderen schrieb, hatte einen eigenen in der Tasche. Das ist
kein Vorwurf, das ist die Eintrittskarte. Wir haben beim Schreiben
nachgesehen statt geglaubt und dabei zwei eigene Irrtümer gefunden. Platz 1
bleibt deiner. Panik ist erlaubt. Danach nachsehen.

*Andy und Falzbein, Wien, November 2026.*
