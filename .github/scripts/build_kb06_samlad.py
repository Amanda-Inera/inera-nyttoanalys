#!/usr/bin/env python3
"""Bygg KB06-samlad.md från kunskapsbasens 72 källartiklar."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "KB06-samlad.md"
EXPECTED_ARTICLES = 72

SOURCE_FOLDERS = (
    "1. Syfte",
    "2. Jämförelse",
    "3. Ramar",
    "4. Nyttor och kostnader",
    "5. Värdering",
    "6. Osäkerhet",
    "7. Sammanfattning",
    "Referensanalyser",
    "Valfritt stöd och fördjupning",
)


def collect_articles() -> list[Path]:
    articles: list[Path] = []

    for folder_name in SOURCE_FOLDERS:
        folder = ROOT / folder_name
        if not folder.is_dir():
            raise SystemExit(f"Källmappen saknas: {folder.relative_to(ROOT)}")

        articles.extend(sorted(folder.glob("*.md"), key=lambda path: path.name.casefold()))

    if len(articles) != EXPECTED_ARTICLES:
        raise SystemExit(
            f"Förväntade {EXPECTED_ARTICLES} artiklar men hittade {len(articles)}. "
            "Samlingsfilen har inte skrivits."
        )

    return articles


def build_document(articles: list[Path]) -> str:
    parts = [
        "# Kunskapsbas 06 – samlad",
        "",
        "> Den här filen genereras automatiskt från kunskapsbasens 72 källartiklar. "
        "Redigera artiklarna i sina ordinarie mappar i stället för att ändra denna fil.",
        "",
        "Samlingsfilen är avsedd för enkel nedladdning och användning i AI-verktyg. "
        "Originalstruktur och källfiler finns kvar oförändrade i repot.",
    ]

    for index, article in enumerate(articles, start=1):
        relative_path = article.relative_to(ROOT).as_posix()
        content = article.read_text(encoding="utf-8").strip()

        parts.extend(
            (
                "",
                "---",
                "",
                f"<!-- Artikel {index} av {EXPECTED_ARTICLES} | Källa: {relative_path} -->",
                "",
                content,
            )
        )

    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    articles = collect_articles()
    OUTPUT.write_text(build_document(articles), encoding="utf-8", newline="\n")
    print(f"Skrev {OUTPUT.name} med {len(articles)} artiklar.")


if __name__ == "__main__":
    main()
