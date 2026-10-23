"""Render original bilingual repository artwork using the bundled OFL fonts."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, PngImagePlugin, features


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONTS = ASSETS / "fonts"
PALETTE = {"paper": "#000000", "ink": "#ffffff", "sand": "#cbb896", "olive": "#7fae8d", "rule": "#303030"}


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def render(name, height):
    image = Image.new("RGB", (1600, height), PALETTE["paper"])
    draw = ImageDraw.Draw(image)
    center = height // 2
    left, right = 88, 1512
    draw.line((left, 46, right, 46), fill=PALETTE["rule"], width=2)
    draw.line((left, height - 64, right, height - 64), fill=PALETTE["rule"], width=2)
    draw.line((left, 46, left + 90, 46), fill=PALETTE["olive"], width=3)
    draw.text((left, center - 12), "Safer Devices", font=font("Newsreader[opsz,wght].ttf", 106), fill=PALETTE["ink"], anchor="ls")
    draw.text((left + 3, center + 54), "A little more secure. One step at a time.", font=font("IBMPlexSansArabic-Regular.ttf", 29), fill=PALETTE["sand"], anchor="ls")
    draw.text((right, center - 20), "أمان رقمي", font=font("Amiri-Bold.ttf", 112), fill=PALETTE["sand"], anchor="rs", direction="rtl", language="ar")
    draw.text((right, center + 94), "خطوات واضحة. قرارات واعية.", font=font("Amiri-Regular.ttf", 41), fill=PALETTE["ink"], anchor="rs", direction="rtl", language="ar")
    draw.text((left, height - 20), "For people and their agents", font=font("IBMPlexSansArabic-Regular.ttf", 23), fill=PALETTE["olive"], anchor="ls")
    draw.text((right, height - 20), "English + العربية", font=font("IBMPlexSansArabic-Regular.ttf", 23), fill=PALETTE["sand"], anchor="rs")
    metadata = PngImagePlugin.PngInfo()
    metadata.add_text("Source", "Original typography and geometric linework, rendered by scripts/build_artwork.py using bundled OFL fonts.")
    image.save(ASSETS / name, pnginfo=metadata, optimize=True)


def main():
    if not features.check("raqm"):
        raise SystemExit("Arabic shaping requires a Pillow build with RAQM support.")
    ASSETS.mkdir(exist_ok=True)
    render("cover.png", 510)
    render("social-preview.png", 800)
    print("Rendered the README cover and social-preview artwork.")


if __name__ == "__main__":
    main()
