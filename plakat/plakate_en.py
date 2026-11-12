# -*- coding: utf-8 -*-
"""plakate_en.py - das Plakat der zweiten Spielzeit auf Englisch, im selben Satz wie plakat2.py.
(Früher setzte das Skript beide Plakate; das der ersten Spielzeit setzt jetzt die Kopie in
../../01-grauen/plakat/plakate_en.py. Die Farben sind bewusst die der ersten Spielzeit, so
ist das fertige englische Plakat entstanden.)

Andy, 10.11.2026 (über Richtscheit): Webseite und Plakat Englisch/Deutsch, auch für die zweite
Spielzeit. Die Bilder sind dieselben wie bei den deutschen Plakaten (von Codex, ohne Schrift);
die Schrift setzt Falzbein. Englische Zettelnamen: ENGLISCH_UND_ZUSAMMENFUEHRUNG.md.

Aufruf:  python plakate_en.py [bild.png] [zielordner]
Ohne Argumente: Bild ist plakat2_bild_ohne_schrift.png neben dem Skript, Ziel ist der Ordner des
Skripts. Schreibt plakat_panische-modelle_en.png (A4, 300 dpi) und die Webfassung
plakat_panische-modelle_en-web.jpg mit 900 Pixel Breite.

Druckfassung:  python plakate_en.py --format A2|A3 [bild.png] [zielordner]
A2 4961x7016, A3 3508x4961, 300 dpi, alle Maße mit Höhe/3508 skaliert; Bild ist dann
plakat2_bild_ohne_schrift_x2.png, Ziel druck/. Schreibt plakat2_en_<F>.png, _beschnitt.png (3 mm)
und _vorschau.jpg (siehe druck_speichern.py). Ohne --format bleibt das A4-Plakat bitgleich.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 2480, 3508
F = "C:/Windows/Fonts/"
GOLD = (232, 190, 98)
CREME = (248, 236, 210)
DUNKEL = (30, 6, 10)
RAND = 260  # so viel Abstand bleibt mindestens links und rechts zusammen

FORMATE = {"A2": (4961, 7016), "A3": (3508, 4961)}
BESCHNITT = 35  # 3 mm bei 300 dpi
FORMAT = None
OFF = 0
K = 1.0


def formatieren(name):
    """Stellt Endformat, Beschnitt und Maßfaktor für A2 oder A3 ein."""
    global W, H, FORMAT, OFF, K
    FORMAT = name
    W, H = FORMATE[name]
    OFF = BESCHNITT
    K = H / 3508


def m(v):
    """Ein Maß des A4-Satzes; im Druckformat mit Höhe/3508 skaliert, sonst unverändert."""
    return v if FORMAT is None else round(v * K)


def font(name, size):
    return ImageFont.truetype(F + name, size)


def grund(pfad):
    cw, ch = W + 2 * OFF, H + 2 * OFF
    quelle = Image.open(pfad).convert("RGB")
    s = ch / quelle.height
    bild = quelle.resize((round(quelle.width * s), ch), Image.BICUBIC)
    if bild.width < cw:
        s = cw / quelle.width
        bild = quelle.resize((cw, round(quelle.height * s)), Image.BICUBIC)
    x0 = (bild.width - cw) // 2
    y0 = (bild.height - ch) // 2
    img = bild.crop((x0, y0, x0 + cw, y0 + ch))
    maske = Image.new("L", (cw, ch), 0)
    md = ImageDraw.Draw(maske)
    for y in range(ch):
        yy = min(max(y - OFF, 0), H - 1)
        if yy < H * 0.36:
            a = int(200 * (1 - yy / (H * 0.36)) ** 1.2)
        elif yy > H * 0.78:
            a = int(215 * ((yy - H * 0.78) / (H * 0.22)) ** 0.9)
        else:
            a = 0
        md.line([(0, y), (cw, y)], fill=a)
    img.paste(Image.new("RGB", (cw, ch), DUNKEL), (0, 0), maske)
    return img


def setzen(bildpfad, t, zielordner, name, kontur):
    img = grund(bildpfad)
    d = ImageDraw.Draw(img)

    def mitte(text, y, fname, size, fill=CREME, stroke=0, schatten=True):
        # Englisch läuft manchmal länger als Deutsch: dann die Schrift verkleinern, nie über den Rand.
        while True:
            f = font(fname, m(size))
            b = d.textbbox((0, 0), text, font=f, stroke_width=stroke)
            if b[2] - b[0] <= W - m(RAND) or size < 30:
                break
            size -= 4
        x = (W - (b[2] - b[0])) / 2 - b[0] + OFF
        if schatten:
            d.text((x + m(6), y + m(8) + OFF), text, font=f, fill=(10, 2, 4), stroke_width=stroke, stroke_fill=(10, 2, 4))
        d.text((x, y + OFF), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=kontur)
        return y + (b[3] - b[1])

    d.rectangle([m(50) + OFF, m(50) + OFF, W - m(50) + OFF, H - m(50) + OFF], outline=GOLD, width=m(12))
    d.rectangle([m(82) + OFF, m(82) + OFF, W - m(82) + OFF, H - m(82) + OFF], outline=GOLD, width=m(3))
    for cx, cy in ((m(82), m(82)), (W - m(82), m(82)), (m(82), H - m(82)), (W - m(82), H - m(82))):
        d.ellipse([cx - m(22) + OFF, cy - m(22) + OFF, cx + m(22) + OFF, cy + m(22) + OFF], fill=GOLD)

    y = m(170)
    y = mitte(t["ueber"], y, "GILC____.TTF", 88, GOLD) + m(55)
    y = mitte(t["titel1"], y, "BROADW.TTF", 236, CREME, m(5)) + m(45)
    y = mitte(t["titel2"][0], y, "BROADW.TTF", t["titel2"][1], GOLD, m(5)) + m(60)
    y = mitte(t["unter"], y, "GARAIT.TTF", 84, CREME) + m(45)
    mitte(t["art"], y, "GILC____.TTF", 80, GOLD)

    prog = font("POORICH.TTF", m(60))
    yu = int(H * 0.815)
    for i, text in enumerate(t["nummern"]):
        spalte, zeile = i % 3, i // 3
        x = [W * 0.20, W * 0.50, W * 0.80][spalte] + OFF
        b = d.textbbox((0, 0), text, font=prog)
        d.text((x - (b[2] - b[0]) / 2 + m(4), yu + zeile * m(88) + m(5) + OFF), text, font=prog, fill=(10, 2, 4))
        d.text((x - (b[2] - b[0]) / 2, yu + zeile * m(88) + OFF), text, font=prog, fill=CREME)
    yu += 2 * m(88) + m(40)
    d.line([(W * 0.2 + OFF, yu + OFF), (W * 0.8 + OFF, yu + OFF)], fill=GOLD, width=m(3))
    yu += m(35)
    yu = mitte(t["besetzung"], yu, "GILC____.TTF", 70, CREME) + m(26)
    yu = mitte(t["gast"], yu, "GARAIT.TTF", 62, GOLD) + m(24)
    yu = mitte(t["satz"], yu, "GARAIT.TTF", 54, CREME) + m(30)
    mitte(t["fuss"], yu, "GILC____.TTF", 62, GOLD)

    if FORMAT:
        from druck_speichern import speichern
        return speichern(img, OFF, zielordner, name)
    a4 = os.path.join(zielordner, name + ".png")
    web = os.path.join(zielordner, name + "-web.jpg")
    img.save(a4, dpi=(300, 300))
    img.resize((900, round(H * 900 / W)), Image.LANCZOS).save(web, quality=88)
    print("ok", a4, web)


ZWEI = dict(
    ueber="FALZBEIN & ANDY · THE SECOND PROGRAM",
    titel1="DON'T PANIC",
    titel2=("A SKILL SUITE FOR PANICKING MODELS", 130),
    unter="A late show in six cheat sheets and an encore",
    art="Second program of the Skill Suite of Horrors",
    nummern=["7 · chicken-and-egg", "8 · too-many-cooks", "9 · tweedledum-and-dee",
             "10 · pass-the-buck", "11 · broken-telephone", "12 · musical-chairs"],
    besetzung="With finds by Bergfried, Klarschrift, Stripe, Steinmann and Mira",
    gast="Encore: 13 · tortoise-and-hare. Someone was already there.",
    satz="Pick a number. Fold it open. Read your fate.",
    fuss="VIENNA · NOVEMBER 2026 · DOORS: ONE LIGHT STAYS ON",
)

if __name__ == "__main__":
    HIER = os.path.dirname(os.path.abspath(__file__))
    args = sys.argv[1:]
    if "--format" in args:
        stelle = args.index("--format")
        wahl = args[stelle + 1].upper()
        del args[stelle:stelle + 2]
        if wahl not in FORMATE:
            sys.exit("--format A2 oder A3")
        formatieren(wahl)
    bild = args[0] if len(args) > 0 else os.path.join(HIER, "plakat2_bild_ohne_schrift_x2.png" if FORMAT else "plakat2_bild_ohne_schrift.png")
    ziel = args[1] if len(args) > 1 else (os.path.join(HIER, "druck") if FORMAT else HIER)
    setzen(bild, ZWEI, ziel, "plakat2_en_" + FORMAT if FORMAT else "plakat_panische-modelle_en", (20, 34, 64))
