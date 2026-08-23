#!/usr/bin/env python3
"""Render the profile banners.

One template, two themes, one file per locale/theme pair. Edit the wording or
the palette here and re-run; never hand-edit the generated SVGs.

    python3 scripts/build-banners.py
"""

import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "profile" / "assets"

FONT = (
    "ui-sans-serif, -apple-system, BlinkMacSystemFont, 'Segoe UI', "
    "'Apple SD Gothic Neo', 'Malgun Gothic', 'Noto Sans KR', "
    "'Noto Sans CJK KR', Roboto, Helvetica, Arial, sans-serif"
)

WORDMARK = "henryj-dev"

# Deliberately domain-free: the org's projects will not all be one category.
LOCALES = {
    "": {
        "eyebrow": "OPEN SOURCE",
        "eyebrow_spacing": "3.6",
        "tagline": "Describe it once. Apply it safely. Roll it back.",
        "aria": "henryj-dev — describe it once, apply it safely, roll it back",
    },
    "-ko": {
        "eyebrow": "오픈 소스",
        "eyebrow_spacing": "3.2",
        "tagline": "한 번 기술하고, 안전하게 적용하고, 되돌립니다.",
        "aria": "henryj-dev — 한 번 기술하고, 안전하게 적용하고, 되돌립니다",
    },
}

THEMES = {
    "light": {
        "bg": "#ffffff", "bg2": "#f2f5f9", "fg": "#0d1117",
        "muted": "#57606a", "accent": "#0969da", "accent2": "#8250df",
        "line": "#d0d7de",
    },
    "dark": {
        "bg": "#0d1117", "bg2": "#161b22", "fg": "#e6edf3",
        "muted": "#8b949e", "accent": "#58a6ff", "accent2": "#bc8cff",
        "line": "#30363d",
    },
}

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="{aria}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.28"/>
      <stop offset="60%" stop-color="{accent}" stop-opacity="0.07"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{accent}"/>
      <stop offset="100%" stop-color="{accent2}"/>
    </linearGradient>
  </defs>

  <rect width="1200" height="300" rx="12" fill="url(#bg)"/>
  <rect x="0.5" y="0.5" width="1199" height="299" rx="12" fill="none" stroke="{line}"/>

  <!-- orbital system -->
  <g transform="translate(955 150)">
    <circle r="135" fill="url(#glow)"/>
    <g fill="none" stroke="{accent}" stroke-opacity="0.32" stroke-width="1.25">
      <ellipse rx="132" ry="52" transform="rotate(-18)"/>
      <ellipse rx="104" ry="40" transform="rotate(26)"/>
      <ellipse rx="72"  ry="28" transform="rotate(-52)"/>
    </g>
    <circle r="11" fill="{accent}"/>
    <circle r="20" fill="none" stroke="{accent}" stroke-opacity="0.35" stroke-width="1.25"/>
    <g transform="rotate(-18)"><circle cx="132" cy="0" r="6.5" fill="{accent2}"/></g>
    <g transform="rotate(26)"><circle cx="-104" cy="0" r="5.5" fill="{accent}"/></g>
    <g transform="rotate(-52)"><circle cx="72" cy="0" r="4.5" fill="{accent}" fill-opacity="0.6"/></g>
  </g>

  <!-- wordmark -->
  <g font-family="{font}">
    <text x="80" y="106" fill="{muted}" font-size="15" font-weight="600" letter-spacing="{eyebrow_spacing}">{eyebrow}</text>
    <text x="80" y="180" fill="{fg}" font-size="62" font-weight="700" letter-spacing="-1.5">{wordmark}</text>
    <rect x="82" y="200" width="86" height="4" rx="2" fill="url(#rule)"/>
    <text x="80" y="242" fill="{muted}" font-size="21" font-weight="450">{tagline}</text>
  </g>
</svg>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for suffix, words in LOCALES.items():
        for theme, palette in THEMES.items():
            svg = TEMPLATE.format(font=FONT, wordmark=WORDMARK, **words, **palette)
            path = OUT / f"banner{suffix}-{theme}.svg"
            path.write_text(svg, encoding="utf-8")
            print(f"wrote {path.relative_to(OUT.parent.parent)}")


if __name__ == "__main__":
    main()
