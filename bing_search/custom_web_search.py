from config import BING_KEY
import json
import requests

class BingCustomWebSearch():

    def __init__(self) -> None:
        pass

    def get_web(self, customConfigId, query):
        url = 'https://api.bing.microsoft.com/v7.0/custom/search?' + 'q=' + query + '&' + 'customconfig=' + customConfigId
        r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': BING_KEY})
        return r.text

if __name__ == "__main__":
    bing_custom_web_search = BingCustomWebSearch()
    customConfigId = ""
    query = ""
    search_results = bing_custom_web_search.get_web(customConfigId=customConfigId, query=query)
    print(search_results)

