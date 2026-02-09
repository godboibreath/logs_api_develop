import config
import requests
import io
import pandas as pd

url = f"https://api-metrika.yandex.net/management/v1/counter/{config.COUNTER_ID}/logrequests"
auth = f"OAuth {config.OATH_TOKEN}"
columns = ['']

headers = {
    "Authorization": f"OAuth {config.OATH_TOKEN}",
    "Content-Type": "application/x-yametrika+json",
    # 'Accept-Encoding': 'gzip'
}


def get_logs():
    response = requests.get(url, headers=headers)
    print(response.text)


def create_log_request():
    params = {
        "date1": "2026-02-04",
        "date2": "2026-02-05",
        "fields": "ym:s:clientID,ym:s:dateTime",
        "source": "visits",
    }
    response = requests.post(url, headers=headers, params=params)
    print(response.text)


def download_log_request(request_id: int):
    url = f"https://api-metrika.yandex.net/management/v1/counter/{config.COUNTER_ID}/logrequest/{request_id}/part/0/download"
    response = requests.get(url, headers=headers | {"Accept-Encoding": "gzip"})
    f = open('log.csv', 'w')
    f.write(response.text)
    f.close()
    df = pd.read_csv(io.StringIO(response.text), sep='\t')
    df.to_csv('logs_pg.csv', sep='\t')

def remove_log(request_id: int):
    url = f""


def main():
    get_logs()
    # create_log_request()
    # get_logs()
    download_log_request(51329119)


main()
