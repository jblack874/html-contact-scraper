from extractors import extract_contacts_from_html
from pathlib import Path
import csv
import sys

# Folders
RAW_HTML_DIR = Path("data/raw_html")
OUTPUT_DIR = Path("data/processed")
OUTPUT_FILE = OUTPUT_DIR / "contacts.csv"


def find_html_files(raw_dir: Path):
    """Find .html or .htm files in data/raw_html"""
    return list(raw_dir.glob("*.html")) + list(raw_dir.glob("*.htm"))


def ensure_dirs():
    RAW_HTML_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    print("\n=== HTML Contact Scraper ===")
    ensure_dirs()

    html_files = find_html_files(RAW_HTML_DIR)

    if not html_files:
        print(f"[!] No HTML files found in {RAW_HTML_DIR}")
        print("    → Save some team/leadership pages there and rerun.\n")
        sys.exit(0)

    print(f"[+] Found {len(html_files)} HTML file(s). Processing...\n")

    all_rows = []

    for path in html_files:
        print(f"   → Processing: {path.name}")
        html = path.read_text(encoding="utf-8", errors="ignore")
        rows = extract_contacts_from_html(html, source_file=path.name)
        all_rows.extend(rows)

    if not all_rows:
        print("\n[!] No contact information found in any files.\n")
        return

    # CSV field structure
    fieldnames = [
        "source_file",
        "page_title",
        "email",
        "name_guess",
        "role_guess",
        "context_snippet",
    ]

    # Write to CSV
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"\n[✓] Completed! Extracted {len(all_rows)} contacts.")
    print(f"[✓] Output saved to: {OUTPUT_FILE}\n")


if __name__ == "__main__":
    main()
