import pandas as pd
import io
import requests
import json
from config import API_URL, HEADERS, PARAMS


def get_logs():
    response = requests.get(API_URL, headers=HEADERS)
    return json.loads(response.text)


def create_log_request():
    params = {
        "date1": "2025-12-01",
        "date2": "2025-12-31",
        "fields": PARAMS['fields'],
        "source": "hits",
    }
    response = requests.post(API_URL, headers=HEADERS, params=params)
    print(response.text)


def remove_log(request_id: int):
    pass


def download_log(request_id: int):
    with open(f'data/log_{request_id}.csv', 'w') as file:
        pass
    url = f'{API_URL}/{request_id}'

print(get_logs())
request_id = 51427266
# create_log_request()

