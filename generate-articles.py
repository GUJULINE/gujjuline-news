import requests
import os

API_KEY = "pub_1265fbc8791c452c910de46181ea6156"  # 🔁 Replace this with your actual API key
BASE_URL = "https://newsdata.io/api/1/news"

countries = ['us', 'in', 'gb', 'jp', 'de', 'fr', 'br', 'ca', 'au', 'za']
lang = 'en'
limit = 2  # Limit articles per country

# Make sure 'article/' directory exists
if not os.path.exists("article"):
    os.mkdir("article")

count = 1

for country in countries:
    print(f"🌐 Fetching: {country.upper()}")
    response = requests.get(BASE_URL, params={
        "apikey": API_KEY,
        "country": country,
        "language": lang,
        "page": 1
    })

    try:
        data = response.json()
        articles = data['results'][:limit]
    except Exception as e:
        print(f"Error parsing for {country}: {e}")
        continue

    for article in articles:
        title = article.get('title', 'No Title')
        description = article.get('description', 'No description.')
        image = article.get('image_url', 'https://source.unsplash.com/400x250/?news')
        link = article.get('link', '#')
        filename = f"article/news-{count}.html"

        # HTML template
        html = f"""
        <!DOCTYPE html>
        <html>
        <head><meta charset="UTF-8"><title>{title}</title></head>
        <body>
            <h1>{title}</h1>
            <img src="{image}" width="400" height="250">
            <p>{description}</p>
            <p><a href="{link}">Read full source →</a></p>
        </body>
        </html>
        """

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ Created: {filename}")
        count += 1

