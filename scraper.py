from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

BASE_URL = "https://commercial.bkt-tires.com"
START_URL = "https://commercial.bkt-tires.com/en-in/products-search/"

all_products = []


def clean(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()
