"""Renders the pixel-cat app icon used by the web, Windows and Android builds.
Run from the repo root: python3 scripts/make_icons.py  (needs Pillow)"""
import os
from PIL import Image, ImageDraw, ImageFilter

CAT = ['................x.....x.', '...............xpx...xpx', '..xx...........xxxxxxxxx', '.x..x..........xxxxxxxxx',
       '.x.............xxexxxexx', '.x.............xxxxpxxxx', '..x....xxxxxxxxxxxxxxxx.', '...xxxxxxxxxxxxcccycxx..',
       '....xxxxxxxxxxxxxxxxx...', '....xxxxxxxxxxxxxxxxx...', '....xxxxxxxxxxxxxxxx....', '....xx..xx.....xx..xx...',
       '...xx....xx...xx....xx..', '...x......x...x......x..']
PAL = {'x': (247, 236, 240), 'e': (12, 5, 8), 'p': (255, 92, 122), 'c': (229, 57, 95), 'y': (255, 209, 102)}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def icon(size, rounded=True, bg=True):
    s = 4
    big = size * s
    img = Image.new('RGBA', (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if bg:
        r = big // 5 if rounded else 0
        d.rounded_rectangle([0, 0, big - 1, big - 1], r, fill=(21, 9, 16))
        glow = Image.new('RGBA', (big, big), (0, 0, 0, 0))
        ImageDraw.Draw(glow).ellipse([big * .1, big * .05, big * .9, big * .75], fill=(229, 57, 95, 90))
        img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(big // 10)))
        mask = Image.new('L', (big, big), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, big - 1, big - 1], r, fill=255)
        img.putalpha(mask)
        d = ImageDraw.Draw(img)
        d.rectangle([big * .12, big * .74, big * .88, big * .74 + big * .02], fill=(247, 236, 240, 140))
    w, h = len(CAT[0]), len(CAT)
    px = int(big * 0.72 / w)
    ox = (big - w * px) // 2
    oy = int(big * .74) - h * px + px
    for y, row in enumerate(CAT):
        for x, ch in enumerate(row):
            if ch in PAL:
                d.rectangle([ox + x * px, oy + y * px, ox + (x + 1) * px - 1, oy + (y + 1) * px - 1], fill=PAL[ch] + (255,))
    return img.resize((size, size), Image.LANCZOS)


def save(img, *parts):
    path = os.path.join(ROOT, *parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)
    print('wrote', os.path.relpath(path, ROOT))


save(icon(512), 'web', 'icon.png')
save(icon(512), 'desktop', 'build', 'icon.png')
icon(256).save(os.path.join(ROOT, 'desktop', 'build', 'icon.ico'), sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
for name, px in {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}.items():
    save(icon(px), 'android', 'app', 'src', 'main', 'res', 'mipmap-' + name, 'ic_launcher.png')
