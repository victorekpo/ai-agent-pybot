from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup


def parse_web_url(self, url):
    # Check if URL has schema, if not use default schema https://
    if url.startswith("80:"):
        url = url.replace("80:", "http://")

    if not url.startswith("http"):
        url = "https://" + url

    # Check if the URL was parsed within the last 3 days
    for entry in self.brain_extended:
        if entry["url"] == url:
            timestamp = datetime.fromisoformat(entry["timestamp"])
            if datetime.now() - timestamp < timedelta(days=3):
                print("Data is less than 3 days old. Skipping web parsing.")
                return

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    self.add_to_brain_extended(url, text)
    # self.add_to_brain("web_parse", url, text)
    print("Webpage content added to knowledge base and processed to brain.")
