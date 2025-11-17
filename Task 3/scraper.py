# Title: scraper.py
# Author: Vaishnavi Vijayan
# Dis: A simple and clean news headline scraper using requests + BeautifulSoup

import requests
from bs4 import BeautifulSoup

URL = "https://www.indiatoday.in/latest-news"
FILE = "headlines.txt"

def fetch_page(url):
    """Fetch HTML content from the website."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # check for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching the page:", e)
        return None

def extract_headlines(html):
    """Extract headlines from <h2> tags."""
    soup = BeautifulSoup(html, "html.parser")
    headlines = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
    return headlines

def save_to_file(headlines):
    """Save the scraped headlines to a text file."""
    with open(FILE, "w", encoding="utf-8") as file:
        for title in headlines:
            file.write(title + "\n")
    print(f"\nSaved {len(headlines)} headlines to {FILE}")

def main():
    print("\n📰 Fetching latest news headlines...")

    html = fetch_page(URL)
    if not html:
        print("Failed to load page. Exiting.")
        return

    headlines = extract_headlines(html)

    if headlines:
        print(f"Found {len(headlines)} headlines.")
        save_to_file(headlines)
    else:
        print("No headlines found on the page.")

if __name__ == "__main__":
    main()
