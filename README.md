# html-contact-scraper
Extract contact info from saved team/leadership HTML pages into a clean CSV.
[README_html_contact_scraper.md](https://github.com/user-attachments/files/23693916/README_html_contact_scraper.md)
# HTML Contact Scraper

## Purpose
Extract contact information from saved HTML team/leadership pages and export it to a structured CSV.

## Features
- Reads local HTML files from `data/raw_html/`
- Finds email addresses and nearby context (emails, names, roles, snippets)
- Outputs a clean CSV to `data/processed/contacts.csv`
- Beginner-friendly and lightweight (BeautifulSoup + regex)

## Inputs
Local HTML files you saved manually from:
- Company “Team” pages
- Leadership / About pages
- People directories

## Outputs
A CSV containing:
- source_file  
- page_title  
- email  
- name_guess  
- role_guess  
- context_snippet  

## Quick Start

1. Add your HTML files to:
   ```
   data/raw_html/
   ```

2. Run the scraper:
   ```
   python src/main.py
   ```

3. View output:
   ```
   data/processed/contacts.csv
   ```

## Roadmap
- v1.0 — basic email extraction + text context
- v1.1 — smarter name/role parsing rules
- v1.2 — add per-site selector configs
- v1.3 — integrate with the Unified Networking Pipeline

## Notes
This tool works only with local HTML you downloaded yourself.  
Always follow website terms of use.
