# CLAUDE.md – 02-panik

Zweite Spielzeit des Kabaretts von Falzbein und Andy: **„Die Skillsuite für panische Modelle“** /
**„Don't Panic: The Skill Suite for Panicking Models“**. Sechs Nummern (henne-und-ei,
viele-koeche, max-und-moritz, dollar-doppelpunkt, stille-post, leerer-platz) und die Zugabe
hase-und-igel. Auf der Seite das Fingerspiel (der „Würfel“): eine Zahl wählen, aufklappen.
Host: **https://panik.special.at/** (Inhalt von `web/`, flach hochgeladen).

## Ordner
- `skills/de/` – sieben Skill-Ordner, `LICENSE.txt`, `LIESMICH.md` (Programmheft).
- `skills/en/` – dieselben sieben Ordner auf Englisch (deutsche Ordnernamen bleiben), `README.md`.
- `web/` – `index.html` (de), `en.html` (en), Zips, Plakate, `LICENSE.txt`, Favicons.
- `plakat/` – `plakat2_bild_ohne_schrift.png` (Bild von Codex), `plakat2.py` (de), `plakate_en.py` (en), fertige Plakate.
- `doku/` – `ZWEITE_SPIELZEIT.md` (Vorschläge aus dem Publikum).

## Bauen
- **Zips** (kein Skript, Aufbau wie die vorhandenen): `<name>.zip` / `<name>-en.zip` = `LICENSE.txt` + `<name>/SKILL.md` + `<name>/LICENSE.txt`. Programm-Zip `panische-modelle(-en).zip` = alle sieben. `suite-des-grauens-gesamt.zip` kommt aus `../zwischenraum/skills/gesamt/`.
- **Plakat:** `python plakat/plakat2.py [bild] [ziel]` und `python plakat/plakate_en.py [bild] [ziel]`; ohne Argumente Bild und Ziel = `plakat/`. Zur Probe ein anderes Ziel angeben. Schriften aus `C:/Windows/Fonts/`. Danach von Hand nach `web/`: `plakat2-a4(-en).png`, `plakat2-web(-en).jpg`.
- **Seite:** statisches HTML, keine Build-Kette; nur Google Fonts von außen. Sicherungen `*.vor-*.html` nicht einchecken.

## Querverweise
Erste Spielzeit `../01-grauen` (grauen.special.at), dritte `../03-katastrophen` (in Arbeit), Bühne und Gesamtskill `../zwischenraum` (zwischenraum.special.at). Die Aufkleber auf der Seite verlinken absolut auf grauen.special.at. Herkunft: Baustelle `\\nas\Public\dev\skill-suite-des-grauens\` (nur lesen).

## Regeln
- Texte UTF-8 (ohne BOM).
- Jede Seite und jeder Skill auf Deutsch **und** Englisch.
- Keine Religion, keine Politik in Namen und Texten.
- Sitzungsnamen in Skill-Texten nur als Rollen („eine andere Sitzung“), nicht als Namen.
- Vor dem Veröffentlichen schaut der Legal-Agent drüber (KI-Kennzeichnung, Lizenzzeile, Plakate).
- Signatur und Manifest kommen gesammelt am Schluss, nicht je Änderung.
- Nach jedem Schreiben im Ergebnis nachsehen: Datei öffnen, Zip auflisten, Pfad wiederfinden.
