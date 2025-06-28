import requests
import os
import json

API_KEY = "pub_1265fbc8791c452c910de46181ea6156"
BASE_URL = "https://newsdata.io/api/1/news"

# ✅ Make sure the directory exists
os.makedirs("newsdata", exist_ok=True)

countries = ["us", "in", "gb", "jp", "de", "fr", "br", "ca", "au", "za"]

for code in countries:
    print(f"\n🌐 Fetching: {code.upper()}")
    params = {
        "apikey": API_KEY,
        "country": code,
        "language": "en"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("status") == "success" and data.get("results"):
            top_articles = []
            for article in data["results"][:3]:
                top_articles.append({
                    "title": article.get("title", "No Title"),
                    "description": article.get("description", "No Description"),
                    "image_url": article.get("image_url", ""),
                    "link": article.get("link", "")
                })
            
            with open(f"newsdata/{code}.json", "w", encoding="utf-8") as f:
                json.dump({"results": top_articles}, f, indent=2)

            print(f"✅ Saved: newsdata/{code}.json")
        else:
            print(f"❌ No news found for {code}")
    except Exception as e:
        print(f"⚠️ Error fetching {code}: {e}")


