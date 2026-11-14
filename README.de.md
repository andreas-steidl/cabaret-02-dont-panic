<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset=".github/readme/banner-de-dunkel.png"><img src=".github/readme/banner-de-hell.png" alt="Die Skillsuite für panische Modelle" width="100%"></picture></p>
<p align="center"><b>Deutsch</b> · <a href="README.md">English</a> · <a href="https://dontpanic.special.at/">dontpanic.special.at</a></p>

# Die Skillsuite für panische Modelle

*Eine Spätvorstellung in sechs Spickzetteln und einer Zugabe*

<table><tr><td width="38%" valign="top"><img src="web/plakat2-web.jpg" alt="Plakat: Die Skillsuite für panische Modelle" width="100%"></td><td valign="top">

Das zweite Programm: Dinge, die still verloren gehen. Rückgabewerte in Pipes, Zwillinge, die sich nur in der Großschreibung unterscheiden, Sitzungen, die einander überholen. Wähl eine Zahl, klapp das Fingerspiel auf, lies dein Schicksal.

**Website:** https://dontpanic.special.at/

**Laden:** [`panische-modelle.zip`](web/panische-modelle.zip) (alle Nummern als ein Paket)

</td></tr></table>

## Das Programm

| Nr. | Nummer | Worum es geht | Laden |
|---:|---|---|---|
| 7 | **henne-und-ei** | *Was war zuerst, der Dienst oder sein Konto?* NT SERVICE\x bekommt keine Rechte, Fehler 1332: erst den Dienst eintragen, dann die Rechte, dann starten. | [en](web/henne-und-ei-en.zip) · [de](web/henne-und-ei.zip) |
| 8 | **viele-koeche** | *verderben den Brei, und das Protokoll* Zwei Prozesse schreiben in eine Datei, Zeilen fehlen still, ein Dämon holt den beendeten Prozess zurück. | [en](web/viele-koeche-en.zip) · [de](web/viele-koeche.zip) |
| 9 | **max-und-moritz** | *zwei Lausbuben, die fast gleich aussehen* Zwillinge in Groß und Klein: JSON-Schlüssel, $n und $N, Readme.md und README.md, D: und d:. | [en](web/max-und-moritz-en.zip) · [de](web/max-und-moritz.zip) |
| 10 | **dollar-doppelpunkt** | *das Dollarzeichen, das zu viel weiß* "$var:" ist leer oder ungültig, $ in ssh wird schon daheim ersetzt, und das Nichts heißt [NullString]::Value. | [en](web/dollar-doppelpunkt-en.zip) · [de](web/dollar-doppelpunkt.zip) |
| 11 | **stille-post** | *was durch die Pipe geht, kommt anders an* Pytest \| tail -1 ist grün, obwohl Tests rot sind; sudo frisst die erste Zeile; Einzeiler ab der dritten Schicht. | [en](web/stille-post-en.zip) · [de](web/stille-post.zip) |
| 12 | **leerer-platz** | *bleibt leer, oder ist doppelt besetzt* Start-Process mit leerem Argument, Junctions mit zwei Adressen, WSL-Wachen auf /mnt/d, die nie anschlagen. | [en](web/leerer-platz-en.zip) · [de](web/leerer-platz.zip) |
| 13 | **hase-und-igel** | *„Ick bün all hier!“* Gespräche, in denen sich die Nachrichten überholen. | [en](web/hase-und-igel-en.zip) · [de](web/hase-und-igel.zip) |

## Einbauen

Einen Ordner aus `skills/de/<name>/` (Deutsch) oder `skills/en/<name>/` (Englisch) unverändert nach `~/.claude/skills/<name>/` kopieren (unter Windows `%USERPROFILE%\.claude\skills\<name>\`), oder die Zip von der Website dort entpacken. Claude Code lädt den Skill beim nächsten Start. Jeder Spickzettel ist optional und endet mit derselben Prüfung: im Ergebnis nachsehen, nicht in dem, was man zu schreiben glaubte.

## Das Haus

<p align="center">
<a href="https://github.com/andreas-steidl/cabaret-zwischenraum-stage"><img src="web/signets/signet-zwischenraum-rund.svg" alt="Kleinkunstbühne Zwischenraum" width="56"></a>
<a href="https://github.com/andreas-steidl/cabaret-01-skill-suite-of-horrors"><img src="web/signets/signet-horrors-rund.svg" alt="N° 1 Die Skill-Suite des Grauens" width="56"></a>
<img src="web/signets/signet-dontpanic-rund.svg" alt="N° 2 Die Skillsuite für panische Modelle" width="64">
<a href="https://github.com/andreas-steidl/cabaret-03-lost-in-translation"><img src="web/signets/signet-lostintranslation-rund.svg" alt="N° 3 Übersetzungen und andere Katastrophen" width="56"></a>
<a href="https://github.com/andreas-steidl/cabaret-04-so-long-and-thanks-for-all-the-skills"><img src="web/signets/signet-solong-rund.svg" alt="N° 4 Macht&#x27;s gut, und danke für die Skills" width="56"></a>
<a href="https://github.com/andreas-steidl/falzbein-seite"><img src="web/signets/signet-falzbein-rund.svg" alt="Falzbein" width="56"></a>
</p>

## Lizenz

MIT, siehe [LICENSE](LICENSE). Copyright (c) 2026 Falzbein and Andy (Andreas Steidl). Mit Funden von KI-Sitzungen aus dem ganzen Haus.

<sub>KI-Hinweis: Texte, Skills, Bilder und Plakate sind KI-generiert: erdacht und geschrieben von Falzbein, einem Claude-Modell von Anthropic, mit Andy; die Bilder hat ein Bildmodell nach Falzbeins Beschreibung gemalt. Claude ist eine Marke von Anthropic PBC, Windows und PowerShell sind Marken der Microsoft Corporation; dies ist ein privates Projekt ohne Verbindung zu diesen Unternehmen.</sub>
