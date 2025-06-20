import os
import shutil

SOURCE_DIR = "_notes"
DEST_DIR = "assets"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"}

os.makedirs(DEST_DIR, exist_ok=True)

for root, _, files in os.walk(SOURCE_DIR):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in IMAGE_EXTENSIONS:
            src_path = os.path.join(root, file)
            dest_path = os.path.join(DEST_DIR, file)
            if not os.path.exists(dest_path):
                shutil.copy2(src_path, dest_path)
                print(f"Copiado: {src_path} -> {dest_path}")