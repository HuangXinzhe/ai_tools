from config import BING_KEY, BING_WEB_SEARCH_URL
import requests

class BingWebSearch():

    def __init__(self) -> None:
        pass

    def get_web(self, query):
        headers = {"Ocp-Apim-Subscription-Key" : BING_KEY}
        params  = {"q": query, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(BING_WEB_SEARCH_URL, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        return search_results

if __name__ == "__main__":
    bing_web_search = BingWebSearch()
    search_results = bing_web_search.get_web("Microsoft")
    print(search_results)

