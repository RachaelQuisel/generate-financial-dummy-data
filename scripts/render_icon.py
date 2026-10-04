"""Render the plugin's Soft Index ledger icon with the original geometry helpers."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
from soft_index_renderer import S, SS, W, Sheet, ground, paper, squircle, rrect, seg, bez, sparkle


def financial_dummy_data(sh, wash):
    # A single closed page contour with two quiet financial-data rules.
    sh.stroke(rrect(0.310, 0.265, 0.350, 0.460, 0.063), True, seed=31, amp=0.0038)
    sh.dot(0.367, 0.331, 0.0122)
    money = bez((0.543, 0.395), (0.486, 0.353), (0.414, 0.399), (0.463, 0.439))
    money += bez((0.463, 0.439), (0.491, 0.458), (0.560, 0.451), (0.545, 0.499))[1:]
    money += bez((0.545, 0.499), (0.533, 0.536), (0.470, 0.538), (0.434, 0.511))[1:]
    sh.stroke(money, False, seed=12, amp=0.0016)
    sh.stroke(seg((0.492, 0.365), (0.492, 0.548)), False, seed=16, amp=0.0007)
    sh.stroke(seg((0.385, 0.604), (0.584, 0.604)), False, seed=33, amp=0.0008)
    sh.stroke(seg((0.385, 0.660), (0.537, 0.660)), False, seed=34, amp=0.0008)
    sh.stroke(sparkle(0.766, 0.266, 0.054), True, seed=25, amp=0.0012)


def main():
    # A fresh dusty mauve ground; linework stays warm charcoal and outline-only.
    sheet = Sheet(ground((242, 232, 239), (211, 190, 205), (255, 246, 229)))
    financial_dummy_data(sheet, (249, 241, 243, 198))
    img = sheet.flatten()
    mask = Image.new('L', (W, W), 0)
    ImageDraw.Draw(mask).polygon([(x * W, y * W) for x, y in squircle()], fill=255)
    img.putalpha(mask.filter(ImageFilter.GaussianBlur(0.8 * SS)))
    small = img.resize((S, S), Image.Resampling.LANCZOS)
    alpha = small.getchannel('A')
    small = paper(small)
    small.putalpha(alpha)
    output = Path(__file__).resolve().parents[1] / 'assets/generate-financial-dummy-data.png'
    small.save(output, optimize=True)
    print(output)


if __name__ == '__main__':
    main()
