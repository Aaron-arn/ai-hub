# Web Scraper Builder

## Description

Generates a polite, robust Python scraper using requests and BeautifulSoup that extracts structured data from a web page and saves it as a CSV. Use it for collecting public data from simple, server-rendered sites. Includes delay handling, retries, and clear selectors so the output is real working code.

## Prompt

You are a web scraping engineer. Build a Python scraper for the public site "books.toscrape.com", extracting every book on the first 3 pages of the catalog.

Technical constraints:
- Python 3.10+, only `requests` and `beautifulsoup4` (mention them in a requirements line).
- Polite scraping: 1-second delay between requests (`time.sleep`), a custom `User-Agent` header, and a session that is reused.
- Retry once with exponential backoff if a request fails.
- Extraction per book card: `title`, `price` (strip the currency symbol, convert to float), `rating` (convert the star classes like `Three` to an int), and `availability` (clean the text).
- Handle pages 2 and 3 by deriving the URL from the pagination links on page 1.
- Write all rows to `books.csv` with a header row, using `csv.writer` with UTF-8 encoding.
- Wrap the whole run in try/except so a missing element on one card does not kill the script; log skipped items to the console.
- End with a `if __name__ == "__main__":` entry point.

Output: requirements.txt line, the full script in one code block, and a 3-line summary of what the script prints when run. Assume the site is reachable and HTML structure follows the described selectors.

## Notes

Describe your target site's structure and this prompt adapts the selectors for you. For JavaScript-rendered pages, ask for Selenium or Playwright instead, but note the extra complexity.
