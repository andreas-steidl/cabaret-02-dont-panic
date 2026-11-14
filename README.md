<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset=".github/readme/banner-en-dunkel.png"><img src=".github/readme/banner-en-hell.png" alt="Don&#x27;t Panic" width="100%"></picture></p>
<p align="center"><b>English</b> · <a href="README.de.md">Deutsch</a> · <a href="https://dontpanic.special.at/">dontpanic.special.at</a></p>

# Don't Panic

*A late show in six cheat sheets and an encore*

<table><tr><td width="38%" valign="top"><img src="web/plakat2-web-en.jpg" alt="Poster: Don&#x27;t Panic" width="100%"></td><td valign="top">

The second program: things that get lost quietly. Return values in pipes, twins that differ only in case, sessions that overtake each other. Pick a number, open the fortune teller, read your fate.

**Website:** https://dontpanic.special.at/

**Get:** [`panische-modelle-en.zip`](web/panische-modelle-en.zip) (all numbers in one package)

</td></tr></table>

## The program

| No. | Number | What it is about | Get |
|---:|---|---|---|
| 7 | **henne-und-ei**<br><sub>chicken-and-egg</sub> | *Which came first, the service or its account?* NT SERVICE\x gets no permissions, error 1332: register the service first, then grant the rights, then start it. | [en](web/henne-und-ei-en.zip) · [de](web/henne-und-ei.zip) |
| 8 | **viele-koeche**<br><sub>too-many-cooks</sub> | *spoil the broth, and the log* Two processes write into one file, lines go missing silently, a daemon brings back the process you just stopped. | [en](web/viele-koeche-en.zip) · [de](web/viele-koeche.zip) |
| 9 | **max-und-moritz**<br><sub>tweedledum-and-dee</sub> | *two twins you can hardly tell apart* Twins in upper and lower case: JSON keys, $n and $N, Readme.md and README.md, D: and d:. | [en](web/max-und-moritz-en.zip) · [de](web/max-und-moritz.zip) |
| 10 | **dollar-doppelpunkt**<br><sub>pass-the-buck</sub> | *the dollar sign that knows too much* "$var:" is empty or invalid, a $ in ssh gets replaced at home already, and nothing is spelled [NullString]::Value. | [en](web/dollar-doppelpunkt-en.zip) · [de](web/dollar-doppelpunkt.zip) |
| 11 | **stille-post**<br><sub>broken-telephone</sub> | *what goes through the pipe arrives different* Pytest \| tail -1 is green although tests are red; sudo eats the first line; one-liners from the third layer down. | [en](web/stille-post-en.zip) · [de](web/stille-post.zip) |
| 12 | **leerer-platz**<br><sub>musical-chairs</sub> | *stays empty, or is taken twice* Start-Process with an empty argument, junctions with two addresses, WSL watchers on /mnt/d that never go off. | [en](web/leerer-platz-en.zip) · [de](web/leerer-platz.zip) |
| 13 | **hase-und-igel**<br><sub>tortoise-and-hare</sub> | Conversations in which the messages overtake each other. | [en](web/hase-und-igel-en.zip) · [de](web/hase-und-igel.zip) |

## Install

Copy a folder from `skills/en/<name>/` (English) or `skills/de/<name>/` (German) unchanged to `~/.claude/skills/<name>/` (on Windows `%USERPROFILE%\.claude\skills\<name>\`), or unpack the zip from the website there. Claude Code loads the skill on its next start. Every cheat sheet is optional and ends with the same check: look at the result, not at what you believed you wrote.

## The house

<p align="center">
<a href="https://github.com/andreas-steidl/cabaret-zwischenraum-stage"><img src="web/signets/signet-zwischenraum-rund.svg" alt="Zwischenraum, the stage" width="56"></a>
<a href="https://github.com/andreas-steidl/cabaret-01-skill-suite-of-horrors"><img src="web/signets/signet-horrors-rund.svg" alt="N° 1 The Skill Suite of Horrors" width="56"></a>
<img src="web/signets/signet-dontpanic-rund.svg" alt="N° 2 Don&#x27;t Panic" width="64">
<a href="https://github.com/andreas-steidl/cabaret-03-lost-in-translation"><img src="web/signets/signet-lostintranslation-rund.svg" alt="N° 3 Lost in Translation" width="56"></a>
<a href="https://github.com/andreas-steidl/cabaret-04-so-long-and-thanks-for-all-the-skills"><img src="web/signets/signet-solong-rund.svg" alt="N° 4 So Long, and Thanks for All the Skills" width="56"></a>
<a href="https://github.com/andreas-steidl/falzbein-seite"><img src="web/signets/signet-falzbein-rund.svg" alt="Falzbein" width="56"></a>
</p>

## License

MIT, see [LICENSE](LICENSE). Copyright (c) 2026 Falzbein and Andy (Andreas Steidl). With finds from AI sessions all over the house.

<sub>AI notice: texts, skills, pictures and posters are AI-generated: conceived and written by Falzbein, a Claude model by Anthropic, with Andy; the pictures were painted by an image model from Falzbein's descriptions. Claude is a trademark of Anthropic PBC; Windows and PowerShell are trademarks of Microsoft Corporation; this is a private project not affiliated with these companies.</sub>
