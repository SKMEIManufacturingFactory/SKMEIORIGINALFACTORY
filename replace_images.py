import os
import re

html_files = [
    "index.html",
    "products.html",
    "about.html"
]

pattern = re.compile(r'images/([^"\']+?)\.(jpg|jpeg|png)', re.IGNORECASE)

for file in html_files:

    if not os.path.exists(file):
        continue

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    content = pattern.sub(
        lambda m: f'images_webp/{m.group(1)}.webp',
        content
    )

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated: {file}")

print("Done.")