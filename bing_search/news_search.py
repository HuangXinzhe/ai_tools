from config import BING_KEY, BING_SEARCH_URL
import requests

class BingNewsSearch():

    def __init__(self) -> None:
        pass

    def get_news(self, query):
        headers = {"Ocp-Apim-Subscription-Key" : BING_KEY}
        params  = {"q": query, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(BING_SEARCH_URL, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        return search_results

if __name__ == "__main__":
    bing_news_search = BingNewsSearch()
    search_results = bing_news_search.get_news("Microsoft")
    print(search_results)

