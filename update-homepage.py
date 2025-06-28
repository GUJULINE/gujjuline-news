import os
from bs4 import BeautifulSoup

ARTICLE_FOLDER = "article"
HOMEPAGE_FILE = "index.html"
START_MARK = "<!-- AUTO-NEWS-START -->"
END_MARK = "<!-- AUTO-NEWS-END -->"

def extract_card(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        title = soup.title.string if soup.title else "No Title"
        preview = soup.p.text if soup.p else "No preview available"
        image = soup.img["src"] if soup.img else "https://source.unsplash.com/600x400/?" + filepath[:2]
        filename = os.path.basename(filepath)
        return f"""
<div class="card">
  <a href="article/{filename}">
    <img src="{image}" style="width:100%;height:180px;object-fit:cover;">
    <h4>{title}</h4>
    <p>{preview}</p>
  </a>
</div>
"""

cards = []
for file in os.listdir(ARTICLE_FOLDER):
    if file.endswith(".html") and file != "template.html":
        cards.append(extract_card(os.path.join(ARTICLE_FOLDER, file)))

# Read homepage
with open(HOMEPAGE_FILE, "r", encoding="utf-8") as f:
    homepage = f.read()

# Replace section
start = homepage.find(START_MARK)
end = homepage.find(END_MARK)

if start != -1 and end != -1:
    new_section = START_MARK + "\n" + "\n".join(cards) + "\n" + END_MARK
    homepage = homepage[:start] + new_section + homepage[end + len(END_MARK):]

    with open(HOMEPAGE_FILE, "w", encoding="utf-8") as f:
        f.write(homepage)

    print("✅ Homepage updated with all article cards!")
else:
    print("❌ Couldn't find AUTO-NEWS markers in index.html")

