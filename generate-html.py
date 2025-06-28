import os
import json

DATA_FOLDER = "newsdata"
ARTICLE_FOLDER = "article"
TEMPLATE_FILE = os.path.join(ARTICLE_FOLDER, "template.html")

os.makedirs(ARTICLE_FOLDER, exist_ok=True)

def load_template():
    if os.path.exists(TEMPLATE_FILE):
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return "<html><head><title>{title}</title></head><body><h1>{title}</h1><img src='{image}'><p>{description}</p><p><a href='{link}' target='_blank'>Read full article</a></p></body></html>"

template = load_template()

for filename in os.listdir(DATA_FOLDER):
    if filename.endswith(".json"):
        country_code = filename.split(".")[0]
        filepath = os.path.join(DATA_FOLDER, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except:
                print(f"❌ Invalid JSON in {filename}")
                continue

        articles = data.get("results", [])[:3]

        for i, article in enumerate(articles):
            title = article.get("title", "No Title")
            description = article.get("description", "No Description")
            image = article.get("image_url", "https://source.unsplash.com/600x400/?" + country_code)
            link = article.get("link", "#")

            safe_title = title.replace(" ", "_").replace("/", "_").lower()[0:40]
            output_file = os.path.join(ARTICLE_FOLDER, f"{country_code}_{i+1}.html")

            with open(output_file, "w", encoding="utf-8") as out:
                out.write(template.format(title=title, description=description, image=image, link=link))

            print(f"✅ Created: {output_file}")

