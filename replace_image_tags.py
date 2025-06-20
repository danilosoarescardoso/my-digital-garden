import os
import re

NOTES_DIR = "_notes"
TAG_PATTERN = re.compile(
    r"{%\s*asset_img\s+([\w\-.]+\.(?:jpg|jpeg|png|gif|svg|webp))(?:\s+\[.*?\])?\s*%}\n?.*"
)

for root, _, files in os.walk(NOTES_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            # Substitui o bloco inteiro (imagem + legenda)
            new_content = TAG_PATTERN.sub(
                r'<img src="{{ site.baseurl }}/assets/\1"/>', content
            )
            if new_content != content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Atualizado: {path}")