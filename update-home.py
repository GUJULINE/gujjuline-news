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
    filename = os.path.basename(filepath)
    return f'<div class="card"><h3><a href="article/{filename}">{title}</a></h3><p>{preview}</p></div>'

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

# Save changes
with open(HOMEPAGE_FILE, "w", encoding="utf-8") as f:
    f.write(homepage)

print("✅ Homepage updated with latest news articles!")
