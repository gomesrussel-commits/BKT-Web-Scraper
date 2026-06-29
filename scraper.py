import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

BASE_URL = "https://commercial.bkt-tires.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
import json
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
def get_archive_json():

    url = "https://commercial.bkt-tires.com/en-in/pattern/agri-grip/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html, "html.parser")

    script = soup.find("script", id="bkt-archive-data")

    if script is None:
        raise Exception("Cannot find archive data")

    text = script.string

    start = text.find("[")
    end = text.rfind("]") + 1

    json_text = text[start:end]

    return json.loads(json_text)
