import requests
from bs4 import BeautifulSoup
import json
from datetime import date

BASE_URL = "https://www.brightermonday.co.ke/jobs"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_jobs(pages=3):
    jobs = []
    for page in range(1, pages + 1):
        url = f"{BASE_URL}?page={page}"
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch page {page}")
            continue
        soup = BeautifulSoup(response.text, "html.parser")
        listings = soup.select("article.search-result")
        for listing in listings:
            jobs.append({
                "title": listing.select_one("h3.title")?.get_text(strip=True),
                "company": listing.select_one(".company-name")?.get_text(strip=True),
                "location": listing.select_one(".location")?.get_text(strip=True),
                "category": listing.select_one(".category")?.get_text(strip=True),
                "posted_date": listing.select_one(".date")?.get_text(strip=True),
                "scraped_at": date.today().isoformat(),
            })
        print(f"Page {page}: {len(listings)} listings")
    return jobs

if __name__ == "__main__":
    jobs = scrape_jobs(pages=5)
    with open("jobs_raw.json", "w") as f:
        json.dump(jobs, f, indent=2)
    print(f"Total: {len(jobs)} jobs scraped.")
