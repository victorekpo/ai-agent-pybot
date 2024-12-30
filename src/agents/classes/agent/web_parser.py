from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup


def parse_web_url(self, url):
    # Check if the URL was scraped within the last 3 days
    for entry in self.brain_extended:
        if entry["url"] == url:
            timestamp = datetime.fromisoformat(entry["timestamp"])
            if datetime.now() - timestamp < timedelta(days=3):
                print("Data is less than 3 days old. Skipping scrape.")
                return

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    self.add_to_brain_extended(url, text)
    # self.add_to_brain("scraped", url, text)
    print("Webpage content added to knowledge base and processed to brain.")
