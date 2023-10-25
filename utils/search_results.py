from bs4 import BeautifulSoup
import requests

def get_search_results(query, user_agent):
    headers = {
        "User-Agent": user_agent,
    }
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")
        results = [link["href"] for link in links if link.get("href") and "http" in link["href"]]
        return results
    return []

