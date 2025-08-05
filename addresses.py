import csv

import requests
import pandas as pd
import random
import time

output_filename = "addresses"

query = """
[out:json][timeout:1800];
area["name:en"="Egypt"]->.searchArea;
(
  node["addr:street"](area.searchArea);
  node["addr:place"](area.searchArea);
  node["addr:housenumber"](area.searchArea);
  node["addr:full"](area.searchArea);
  way["addr:street"](area.searchArea);
  way["addr:place"](area.searchArea);
  way["addr:housenumber"](area.searchArea);
  way["addr:full"](area.searchArea);
  relation["addr:street"](area.searchArea);
  relation["addr:place"](area.searchArea);
  relation["addr:housenumber"](area.searchArea);
  relation["addr:full"](area.searchArea);
);
out body;
>;
out skel qt;
"""

url = "https://overpass-api.de/api/interpreter"
response = requests.get(url, params={"data": query})
response.raise_for_status()

data = response.json()


addresses = []
for el in data["elements"]:
    tags = el.get("tags", {})
    full = tags.get("addr:full", "")
    street = tags.get("addr:street", "")
    place = tags.get("addr:place", "")
    city = tags.get("addr:city", "")
    district = tags.get("addr:district", "")
    housenumber = tags.get("addr:housenumber", "")

    raw_parts = [housenumber, street, place, district, city]
    parts = [p for p in raw_parts if p]
    if full:
        addresses.append(full)
    elif parts:
        addresses.append(", ".join(parts))


df = pd.DataFrame(sorted(set(addresses)), columns=["address"])
df.to_csv(output_filename, index=False, encoding="utf-8-sig", quoting=csv.QUOTE_ALL)


