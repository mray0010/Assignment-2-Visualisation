"""
Reads Students Social Media Addiction.csv and writes two lookup files:
  data/country_addiction_scores.json
  data/country_mental_health_scores.json

Run once:  python generate_map_data.py
Re-run any time the CSV changes.
"""

import csv
import json
from collections import defaultdict

COUNTRY_IDS = {
    "Afghanistan": 4,   "Albania": 8,     "Andorra": 20,   "Argentina": 32,
    "Armenia": 51,      "Australia": 36,  "Austria": 40,   "Azerbaijan": 31,
    "Bahamas": 44,      "Bahrain": 48,    "Bangladesh": 50,"Belarus": 112,
    "Belgium": 56,      "Bhutan": 64,     "Bolivia": 68,   "Bosnia": 70,
    "Brazil": 76,       "Bulgaria": 100,  "Canada": 124,   "Chile": 152,
    "China": 156,       "Colombia": 170,  "Costa Rica": 188,"Croatia": 191,
    "Cyprus": 196,      "Czech Republic": 203, "Denmark": 208, "Ecuador": 218,
    "Egypt": 818,       "Estonia": 233,   "Finland": 246,  "France": 250,
    "Georgia": 268,     "Germany": 276,   "Ghana": 288,    "Greece": 300,
    "Hong Kong": 344,   "Hungary": 348,   "Iceland": 352,  "India": 356,
    "Indonesia": 360,   "Iraq": 368,      "Ireland": 372,  "Israel": 376,
    "Italy": 380,       "Jamaica": 388,   "Japan": 392,    "Jordan": 400,
    "Kazakhstan": 398,  "Kenya": 404,     "Kosovo": 383,   "Kuwait": 414,
    "Kyrgyzstan": 417,  "Latvia": 428,    "Lebanon": 422,  "Lithuania": 440,
    "Luxembourg": 442,  "Malaysia": 458,  "Maldives": 462, "Malta": 470,
    "Mexico": 484,      "Moldova": 498,   "Morocco": 504,  "Nepal": 524,
    "Netherlands": 528, "New Zealand": 554,"Nigeria": 566, "North Macedonia": 807,
    "Norway": 578,      "Oman": 512,      "Pakistan": 586, "Paraguay": 600,
    "Peru": 604,        "Philippines": 608,"Poland": 616,  "Portugal": 620,
    "Qatar": 634,       "Romania": 642,   "Russia": 643,   "Serbia": 688,
    "Singapore": 702,   "Slovakia": 703,  "Slovenia": 705, "South Africa": 710,
    "South Korea": 410, "Spain": 724,     "Sri Lanka": 144,"Sweden": 752,
    "Switzerland": 756, "Syria": 760,     "Taiwan": 158,   "Tajikistan": 762,
    "Thailand": 764,    "Trinidad": 780,  "Turkey": 792,   "UAE": 784,
    "UK": 826,          "Ukraine": 804,   "USA": 840,      "Uruguay": 858,
    "Uzbekistan": 860,  "Venezuela": 862, "Vietnam": 704,  "Yemen": 887,
    "Liechtenstein": 438, "Monaco": 492,  "Montenegro": 499, "Panama": 591,
    "San Marino": 674,  "Vatican City": 336,
}

addiction_scores = defaultdict(list)
mental_health_scores = defaultdict(list)

with open("data/Students Social Media Addiction.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        country = row.get("Country", "").strip()
        try:
            addiction_scores[country].append(float(row["Addicted_Score"]))
        except (ValueError, KeyError):
            pass
        try:
            mental_health_scores[country].append(float(row["Mental_Health_Score"]))
        except (ValueError, KeyError):
            pass

addiction_values = []
mental_health_values = []

for country in sorted(COUNTRY_IDS):
    iso_id = COUNTRY_IDS[country]
    if country in addiction_scores:
        addiction_values.append({
            "id": iso_id,
            "country": country,
            "addiction": round(sum(addiction_scores[country]) / len(addiction_scores[country]), 2)
        })
    if country in mental_health_scores:
        mental_health_values.append({
            "id": iso_id,
            "country": country,
            "mental_health": round(sum(mental_health_scores[country]) / len(mental_health_scores[country]), 2)
        })

with open("data/country_addiction_scores.json", "w", encoding="utf-8") as f:
    json.dump(addiction_values, f, indent=2)
print(f"Written {len(addiction_values)} countries → data/country_addiction_scores.json")

with open("data/country_mental_health_scores.json", "w", encoding="utf-8") as f:
    json.dump(mental_health_values, f, indent=2)
print(f"Written {len(mental_health_values)} countries → data/country_mental_health_scores.json")
