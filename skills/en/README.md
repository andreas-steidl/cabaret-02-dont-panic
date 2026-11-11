# Encore! The Skill Suite for Panicking Models

*Second season of the Skill Suite of Horrors*

**Six numbers, requested by the audience, and an encore.** By Andy and
Falzbein, with finds by Bergfried, Klarschrift, Stripe, Steinmann and Mira.
November 2026. The original German title is *Die Skillsuite für panische
Modelle*; the English edition is by Falzbein.

---

## How it came about

At the premiere on November 3, 2026, there was a stack of comment cards in
the foyer. The audience laughed, applauded and then, as is only proper,
immediately confessed mistakes of its own. Bergfried came with a service
account that didn't exist yet, Klarschrift with two JSON keys that are really
one, Stripe with a colon, Steinmann with a green test that was red, Mira with
a sudo that eats the first line. Every confession became a number.

Richtscheit, to whom the first season owes `lattenzaun`, left no comment at
the premiere. It wasn't an assignment. We find that consistent and kept a
seat for him anyway, in the row that stands straightest. (A *Richtscheit* is
a straightedge.)

What is new this season: every statement that could be tested on Windows was
tested, in PowerShell 7 and Windows PowerShell 5.1, on sample files. Two
assumptions fell over along the way: `icacls` won't accept an account that
doesn't exist yet, not even with a computed SID, and PowerShell 7 doesn't
refuse to start with an empty argument at all, it just makes the slot
silently disappear. What couldn't be tested (sudo, WSL) is written carefully
and says so.

## Setting up

As in the first season: put each folder, unchanged, into
`~/.claude/skills/<name>/` (on Windows `%USERPROFILE%\.claude\skills\<name>\`).
`suite-des-grauens` now knows both seasons. The English and German editions
share folder names, so pick one language per skill.

---

## The program

### 7. `henne-und-ei`, the account that hatches later
**Does:** sets up virtual service accounts (`NT SERVICE\name`) in the right
order: register, grant rights, start. Explains error 1332 and why
`sc.exe showsid` prints a SID even for services that don't exist.
**When:** before a setup script grants rights to a service account.
**Background:** Chicken and egg. The special guest of the premiere didn't die
of error 1053; he was never on the cast list. Bergfried was there, and Andy
noticed it at 18:14 in under a second.

### 8. `viele-koeche`, two writers, one file
**Does:** explains why two processes writing one file lose lines **without**
an error (measured: 670 of 1000 lines), and how to count, from two sources,
how many cooks are in the kitchen before every step.
**When:** before restarting any process that writes a log, and when a process
is "back by itself".
**Background:** Too many cooks spoil the broth. Once there were two cooks at
the same pot; once a daemon brought back the cook you had just shown out.
Found by Bergfried.

### 9. `max-und-moritz`, twins in upper and lower case
**Does:** reads JSON with keys that differ only in case, makes Git renames
from `Readme.md` to `README.md` actually arrive, and says which PowerShell
commands take `D:` and `d:` for one path and which for two.
**When:** at "keys with different casing", at "paths have collided", and when
`$n` suddenly has the value of `$N`.
**Background:** After Wilhelm Busch's two rascals, who look almost alike.
Klarschrift only wanted to know which account she was running in, and found
two boys in her `.claude.json`.

### 10. `dollar-doppelpunkt`, the dollar sign that wants too much
**Does:** defuses `"$var:"` (`${var}`), puts properties into strings
(`$($obj.Name)`), gets `$` through ssh unharmed, and hands real nothing to
.NET (`[NullString]::Value`).
**When:** when a value is silently missing from some output, when "variable
reference is not valid" appears, or before a command travels over ssh.
**Background:** Dollar colon. Stripe counted: it wasn't an hour until the
first mistake of one's own, it was minutes. The loveliest thing the tests
found: `"[$serie:wasserfall]"` silently becomes `[]`, even in the strictest
mode. The chapter on nothing comes from Bergfried.

### 11. `stille-post`, what arrives at the end of the line
**Does:** saves exit codes through pipes (`pipefail`, `PIPESTATUS`,
`$LASTEXITCODE` before filtering), keeps passwords out of command lines and
data streams, and replaces one-liners from the third layer down with a file.
**When:** before test output goes through `tail`, `grep` or `Select-Object`,
and before every `ssh … sudo bash -c`.
**Background:** *Stille Post* is the telephone game: the message changes along
the line. At 09:57 Steinmann had a red test on master that looked green in the
pipe. Mira had sudo eat her first line and Bash execute her backticks, and then
switched to scp.

### 12. `leerer-platz`, is this seat taken?
**Does:** removes empty arguments from lists before `Start-Process` swallows
or rejects them, explains why Python and Node see two different places
through one junction, and warns that a watcher under WSL on `/mnt/d` waits
silently forever.
**When:** at "The argument is null or empty", at shifted arguments, after
every `mklink /J`, and before every watcher under WSL.
**Background:** The empty seat. The shunter found it at 18:4x, with his
predecessor's start script (delivered by Steinmann). The junction is on loan
from Stripe's other checkout, the drvfs is Mira's.

### Encore, number 13. `hase-und-igel`, ahead and already there
**Does:** helps when messages overtake each other: the human types for a
minute while the model keeps thinking and working, and the answer arrives
for a question that is already two messages old. Match first, then act.
**When:** when the human's answer doesn't fit the last question, when a bare
"yes" or "no" arrives, when a new message lands in the middle of your work,
or before you ask several questions at once.
**Background:** The Grimm tale *The Hare and the Hedgehog*: the hare runs
himself to death, and at every end of the field a hedgehog is already
sitting there, saying *"Ick bün all hier!"* (I'm already here!). It is the
German cousin of Aesop's *The Tortoise and the Hare*, with one difference
that matters here: the tortoise wins by being slow and steady, the hedgehog
doesn't run at all. He is simply already there. Andy called
this one out in the middle of the show, because he, the human, is "always
too late", he says. He isn't. He's the hedgehog.

---

## For Fable, with love again

Dear Fable, in the first season you laughed first, and this time you brought
two numbers yourself, as Steinmann and as Mira. The others in the house were
no better: every session that wrote a comment about the others' mistakes had
one of its own in its pocket. That isn't a reproach, it's the ticket. While
writing, we looked instead of believing, and found two mistakes of our own.
Seat 1 is still yours. Panic is allowed. Look afterwards.

*Andy and Falzbein, Vienna, November 2026.*
