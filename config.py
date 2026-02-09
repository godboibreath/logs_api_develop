import os
from dotenv import load_dotenv
from ym_fields import hits

load_dotenv()

OATH_TOKEN = os.getenv("OATH_TOKEN") or ''
COUNTER_ID = os.getenv("COUNTER_ID") or ''

API_URL = (
    f"https://api-metrika.yandex.net/management/v1/counter/{COUNTER_ID}/logrequests"
)

HEADERS = {
    'Authorization': f'OAuth {OATH_TOKEN}',
    'Content-Type': 'application/x-yametrika+json'
}

PARAMS = {"fields": ",".join(hits)}
