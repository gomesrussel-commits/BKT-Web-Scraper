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

    response = requests.get(url, headers=headers)

    print("Status Code:", response.status_code)
    print(response.text[:1000])

    soup = BeautifulSoup(response.text, "html.parser")

    script = soup.find("script", id="bkt-archive-data")

    if script is None:
        raise Exception("Cannot find archive data")

    text = script.string

    start = text.find("[")
    end = text.rfind("]") + 1

    json_text = text[start:end]

    return json.loads(json_text)
def extract_products(products):

    rows = []

    for p in products:

        rows.append({

            "Product Name": p.get("name"),

            "Slug": p.get("slug"),

            "Description": p.get("description"),

            "Product Type": p.get("product_type"),

            "Locale": p.get("locale"),

            "Applications": ", ".join(
                [a.get("label", "") for a in p.get("applications", [])]
            ),

            "Sectors": ", ".join(
                [s.get("label", "") for s in p.get("sectors", [])]
            ),

            "Highlights": " | ".join(
                [h.get("highlight_text", "") for h in p.get("highlights", [])]
            ),

            "Image URL": p.get("url"),

            "Preview Image": (
                p.get("preview", {}).get("url")
                if isinstance(p.get("preview"), dict)
                else ""
            ),

            "Published": p.get("publishing_status"),

            "Remote Updated": p.get("remote_updated_at")

        })

    return pd.DataFrame(rows)
def main():

    print("Downloading product data...")

    products = get_archive_json()

    print(f"Products Found: {len(products)}")

    df = extract_products(products)

    df.to_excel("BKT_PRODUCTS.xlsx", index=False)

    print("Excel exported successfully!")

if __name__ == "__main__":
    main()
    
