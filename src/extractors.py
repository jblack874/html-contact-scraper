import re
from bs4 import BeautifulSoup

# Basic email regex
EMAIL_REGEX = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

def extract_contacts_from_html(html: str, source_file: str) -> list[dict]:
    """
    Extract emails and nearby context (name/role guesses) from a single HTML string.
    Returns a list of dicts for CSV rows.
    """
    soup = BeautifulSoup(html, "lxml")

    # Try to grab a page title if present
    page_title = ""
    if soup.title and soup.title.string:
        page_title = soup.title.string.strip()

    rows: list[dict] = []
    seen_emails: set[str] = set()

    # --- Strategy 1: obvious mailto: links ---
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "mailto:" in href.lower():
            email = href.split("mailto:")[-1].split("?")[0].strip()

            if not email or email in seen_emails:
                continue

            seen_emails.add(email)

            # Context text around the link (could be a name or role)
            context = " ".join(link.stripped_strings)

            rows.append(
                {
                    "source_file": source_file,
                    "page_title": page_title,
                    "email": email,
                    "name_guess": context or "",
                    "role_guess": "",
                    "context_snippet": context or "",
                }
            )

    # --- Strategy 2: regex over all text as a fallback ---
    full_text = soup.get_text(separator=" ", strip=True)

    for match in EMAIL_REGEX.finditer(full_text):
        email = match.group(0)

        if email in seen_emails:
            continue

        seen_emails.add(email)

        start = max(match.start() - 80, 0)
        end = match.end() + 80
        snippet = full_text[start:end]

        rows.append(
            {
                "source_file": source_file,
                "page_title": page_title,
                "email": email,
                "name_guess": "",
                "role_guess": "",
                "context_snippet": snippet,
            }
        )

    return rows
