#!/usr/bin/env python3
"""Generate the publication-date badge before Quarto renders the site."""

from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BADGE_PATH = ROOT / "docs-release.svg"


def badge_svg(updated_date: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="155" height="20" role="img" aria-label="Last updated: {updated_date}"><title>Last updated: {updated_date}</title><filter id="blur"><feGaussianBlur stdDeviation="16"/></filter><linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="r"><rect width="155" height="20" rx="3"/></clipPath><g clip-path="url(#r)"><rect width="86" height="20" fill="#555"/><rect x="86" width="69" height="20" fill="#007ec6"/><rect width="155" height="20" fill="url(#s)"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><g transform="scale(.1)"><g aria-hidden="true" fill="#010101"><text x="430" y="150" fill-opacity=".8" filter="url(#blur)" textLength="740">Last updated</text><text x="430" y="150" fill-opacity=".3" textLength="740">Last updated</text></g><text x="430" y="140" textLength="740">Last updated</text></g><g transform="scale(.1)"><g aria-hidden="true" fill="#010101"><text x="1205" y="150" fill-opacity=".8" filter="url(#blur)" textLength="610">{updated_date}</text><text x="1205" y="150" fill-opacity=".3" textLength="610">{updated_date}</text></g><text x="1205" y="140" textLength="610">{updated_date}</text></g></g></svg>\n'''


def main() -> None:
    updated_date = datetime.now().astimezone().date().isoformat()
    BADGE_PATH.write_text(badge_svg(updated_date), encoding="utf-8")
    print(f"Updated {BADGE_PATH.name}: Last updated: {updated_date}")


if __name__ == "__main__":
    main()
