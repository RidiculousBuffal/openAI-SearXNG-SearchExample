import json
from typing import Optional
import dotenv
import os
import requests
from backend.utils.JinaReader import readWebPageWithNoneStream
dotenv.load_dotenv()
searxngBaseUrl = os.getenv("SEARXNG_BASE_URL")

def extract_results(json_data):
    # define result array
    result_array = []
    # extract result
    if 'results' in json_data:
        for result in json_data['results']:
            # extract info
            extracted_info = {
                'url': result.get('url'),
                'title': result.get('title'),
                'content': result.get('content'),
                'score': result.get('score')
            }
            result_array.append(extracted_info)
    return result_array

def searchWithSearxng (q,categories):
    url = f"{searxngBaseUrl}/search?q={q}&format=json&categories={categories if categories is not None else 'general'}"
    response = requests.request("GET", url, headers={}, data={},verify=False,timeout=30)
    extracted_results = extract_results(response.json())
    # now forced the search top is 4
    max_num = 1
    for i in range(min(len(extracted_results), max_num)):
        extracted_results[i].update({'content': readWebPageWithNoneStream(extracted_results[i]['url'],q)})
    return extracted_results[0:max_num]



if __name__ == '__main__':
    print(searchWithSearxng("Sanofi financial status second half 2024","news"))