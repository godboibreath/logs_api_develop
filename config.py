import os
from dotenv import load_dotenv
from ym_fields import hits

load_dotenv()

OATH_TOKEN = os.getenv("OATH_TOKEN")
COUNTER_ID = os.getenv("COUNTER_ID")

API_URL = (
    f"https://api-metrika.yandex.net/management/v1/counter/{COUNTER_ID}/logrequests"
)

HEADERS = {}

PARAMS = {"fields": ",".join(hits)}
