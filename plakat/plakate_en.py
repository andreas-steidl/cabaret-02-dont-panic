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


def font(name, size):
    return ImageFont.truetype(F + name, size)


def grund(pfad):
    quelle = Image.open(pfad).convert("RGB")
    s = H / quelle.height
    bild = quelle.resize((round(quelle.width * s), H), Image.BICUBIC)
    if bild.width < W:
        s = W / quelle.width
        bild = quelle.resize((W, round(quelle.height * s)), Image.BICUBIC)
    x0 = (bild.width - W) // 2
    y0 = (bild.height - H) // 2
    img = bild.crop((x0, y0, x0 + W, y0 + H))
    maske = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(maske)
    for y in range(H):
        if y < H * 0.36:
            a = int(200 * (1 - y / (H * 0.36)) ** 1.2)
        elif y > H * 0.78:
            a = int(215 * ((y - H * 0.78) / (H * 0.22)) ** 0.9)
        else:
            a = 0
        md.line([(0, y), (W, y)], fill=a)
    img.paste(Image.new("RGB", (W, H), DUNKEL), (0, 0), maske)
    return img


def setzen(bildpfad, t, zielordner, name, kontur):
    img = grund(bildpfad)
    d = ImageDraw.Draw(img)

    def mitte(text, y, fname, size, fill=CREME, stroke=0, schatten=True):
        # Englisch läuft manchmal länger als Deutsch: dann die Schrift verkleinern, nie über den Rand.
        while True:
            f = font(fname, size)
            b = d.textbbox((0, 0), text, font=f, stroke_width=stroke)
            if b[2] - b[0] <= W - RAND or size < 30:
                break
            size -= 4
        x = (W - (b[2] - b[0])) / 2 - b[0]
        if schatten:
            d.text((x + 6, y + 8), text, font=f, fill=(10, 2, 4), stroke_width=stroke, stroke_fill=(10, 2, 4))
        d.text((x, y), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=kontur)
        return y + (b[3] - b[1])

    d.rectangle([50, 50, W - 50, H - 50], outline=GOLD, width=12)
    d.rectangle([82, 82, W - 82, H - 82], outline=GOLD, width=3)
    for cx, cy in ((82, 82), (W - 82, 82), (82, H - 82), (W - 82, H - 82)):
        d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=GOLD)

    y = 170
    y = mitte(t["ueber"], y, "GILC____.TTF", 88, GOLD) + 55
    y = mitte(t["titel1"], y, "BROADW.TTF", 236, CREME, 5) + 45
    y = mitte(t["titel2"][0], y, "BROADW.TTF", t["titel2"][1], GOLD, 5) + 60
    y = mitte(t["unter"], y, "GARAIT.TTF", 84, CREME) + 45
    mitte(t["art"], y, "GILC____.TTF", 80, GOLD)

    prog = font("POORICH.TTF", 60)
    yu = int(H * 0.815)
    for i, text in enumerate(t["nummern"]):
        spalte, zeile = i % 3, i // 3
        x = [W * 0.20, W * 0.50, W * 0.80][spalte]
        b = d.textbbox((0, 0), text, font=prog)
        d.text((x - (b[2] - b[0]) / 2 + 4, yu + zeile * 88 + 5), text, font=prog, fill=(10, 2, 4))
        d.text((x - (b[2] - b[0]) / 2, yu + zeile * 88), text, font=prog, fill=CREME)
    yu += 2 * 88 + 40
    d.line([(W * 0.2, yu), (W * 0.8, yu)], fill=GOLD, width=3)
    yu += 35
    yu = mitte(t["besetzung"], yu, "GILC____.TTF", 70, CREME) + 26
    yu = mitte(t["gast"], yu, "GARAIT.TTF", 62, GOLD) + 24
    yu = mitte(t["satz"], yu, "GARAIT.TTF", 54, CREME) + 30
    mitte(t["fuss"], yu, "GILC____.TTF", 62, GOLD)

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
    bild = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HIER, "plakat2_bild_ohne_schrift.png")
    ziel = sys.argv[2] if len(sys.argv) > 2 else HIER
    setzen(bild, ZWEI, ziel, "plakat_panische-modelle_en", (20, 34, 64))
