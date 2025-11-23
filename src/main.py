from extractors import extract_contacts_from_html


def main():
    print("Running main() from src/main.py")
    extract_contacts_from_html("<html><body>test</body></html>", "dummy.html")


if __name__ == "__main__":
    main()
    