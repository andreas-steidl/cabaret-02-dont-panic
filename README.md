# Don't Panic – The Skill Suite for Panicking Models

German: *Die Skillsuite für panische Modelle*

The second season of a small cabaret by Falzbein and Andy: six cheat sheets (Claude Code
skills) requested by the audience of the first season, plus an encore. Virtual service
accounts that don't exist yet, two processes writing one file, twins that differ only in
case, the dollar sign in PowerShell strings, exit codes lost in pipes, empty arguments —
and messages that overtake each other. Every claim that could be checked on Windows was
checked. Website (with the paper fortune-teller): https://panik.special.at/

| skill (folder) | English title |
|---|---|
| `henne-und-ei` | chicken-and-egg |
| `viele-koeche` | too-many-cooks |
| `max-und-moritz` | tweedledum-and-dee |
| `dollar-doppelpunkt` | pass-the-buck |
| `stille-post` | broken-telephone |
| `leerer-platz` | musical-chairs |
| `hase-und-igel` (encore) | tortoise-and-hare |

## Install a skill

Copy one folder unchanged to `~/.claude/skills/<name>/`
(on Windows `%USERPROFILE%\.claude\skills\<name>\`) — English from `skills/en/<name>/`,
German from `skills/de/<name>/` — or unzip `<name>-en.zip` / `<name>.zip` from the website
there. Claude Code loads it on the next start.

## License

MIT, see [LICENSE](LICENSE). Copyright (c) 2026 Falzbein und Andy.

## The other seasons

- Season 1: **The Skill Suite of Horrors**, project `01-grauen`, https://grauen.special.at/
- Season 3: *Translations and Other Disasters* (work in progress), project `03-katastrophen`
- The stage over all seasons, with the combined skill: **Zwischenraum**, project `zwischenraum`, https://zwischenraum.special.at/

---

**Deutsch:** Die zweite Spielzeit: sechs Nummern, vom Publikum gewünscht, und die Zugabe
`hase-und-igel`. Einen Ordner aus `skills/de/` (oder `skills/en/`) unverändert nach
`~/.claude/skills/<name>/` legen. Das Programmheft steht in `skills/de/LIESMICH.md`, die Seite
mit dem Fingerspiel unter https://panik.special.at/.
