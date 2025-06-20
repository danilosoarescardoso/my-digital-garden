import os
from collections import defaultdict

# Pasta raiz do seu projeto Jekyll
ROOT_DIR = "."

# Pasta de onde o Jekyll gera os arquivos (normalmente _site)
OUTPUT_DIR = "_site"

# Extensões que Jekyll processa
MARKDOWN_EXTENSIONS = [".md", ".markdown"]
HTML_EXTENSIONS = [".html", ".htm"]

# Pasta onde ficam os posts
POSTS_DIR = "_posts"

# Função para gerar o destino simulado de um arquivo
def get_destination(filepath):
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    dirname, filename = os.path.split(rel_path)

    # Verifica se é um post
    if dirname.startswith(POSTS_DIR):
        name, _ = os.path.splitext(filename)
        # Remover data do nome (formato YYYY-MM-DD-title.md)
        if len(name) >= 11 and name[4] == '-' and name[7] == '-':
            slug = name[11:]
        else:
            slug = name
        return os.path.join(slug, "index.html")

    name, ext = os.path.splitext(filename)

    if ext in MARKDOWN_EXTENSIONS:
        # Arquivos markdown viram pastas com index.html
        return os.path.join(dirname, name, "index.html")
    elif ext in HTML_EXTENSIONS:
        # Arquivos html mantêm o mesmo caminho
        return os.path.join(dirname, filename)
    else:
        # Outros arquivos são copiados como estão
        return os.path.join(dirname, filename)


# Mapeia destinos para arquivos de origem
dest_map = defaultdict(list)

# Percorre arquivos do projeto
for root, dirs, files in os.walk(ROOT_DIR):
    # Ignora a pasta de saída e outras pastas do Jekyll
    if OUTPUT_DIR in root or root.startswith("./_site") or "/_site" in root:
        continue
    if any(ignored in root for ignored in ["_site", "_sass", "_layouts", "_includes", "_data", ".git", ".jekyll-cache"]):
        continue

    for file in files:
        if file.startswith("."):
            continue  # Ignora arquivos ocultos

        filepath = os.path.join(root, file)
        dest = get_destination(filepath)
        dest_map[dest].append(filepath)

# Verifica e imprime conflitos
conflicts = {dest: files for dest, files in dest_map.items() if len(files) > 1}

if conflicts:
    print("⚠️  Conflitos encontrados:")
    for dest, sources in conflicts.items():
        print(f"\nDestino: {dest}")
        for src in sources:
            print(f"  - {src}")
else:
    print("✅ Nenhum conflito de destino encontrado!")
