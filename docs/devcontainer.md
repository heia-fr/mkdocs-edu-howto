---
title: Installation du devcontainer
---

# Installation du _devcontainer_

Commencez par créer un répertoire qui contiendra tous les fichiers de votre site. Ouvrez ensuite ce répertoire avec VS-Code.

Créez un sous-répertoire `.devcontainer` (n'oubliez pas le point du début). Dans ce répertoire, créez un fichier `devcontainer.json` avec le contenu suivant:

```json
{
    "name": "MkDocs-Edu",
    "build": {
        "dockerfile": "Dockerfile"
    }
}
```

Toujours dans `.devcontainer`, créez aussi le `Dockerfile` suivant :

```Dockerfile
ARG VARIANT=bullseye
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Install additional software
RUN apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y install --no-install-recommends \
  imagemagick \
  zip

# Copy files needed to build our flavour of mkdocs
COPY mkdocs-edu/* /mkdocs-edu/
WORKDIR /mkdocs-edu

# Install "poetry", then build and install mkdocs
RUN pip install poetry && \
  poetry config virtualenvs.create false && \
  poetry install

# Copy scripts for serving and building the site
COPY --chmod=0755 scripts/* /usr/local/bin/

```

Dans `.devcontainer`, créez maintenant le dossier `mkdocs-edu` dans lequel vous ajoutez le fichier `pyproject.toml` suivant :

```toml
[tool.poetry]
name = "mkdocs-edu"
version = "0.1.0"
description = "mkdocs for education web site"
authors = ["Jacques Supcik <jacques.supcik@hefr.ch>"]
license = "Apache-2.0"

[tool.poetry.dependencies]
python = "^3"
mkdocs = "^1"
mkdocs-material = "^8"
mkdocs-macros-plugin = "^0.7"
mkdocs-awesome-pages-plugin = "^2"
jinja2-cli = "^0.8"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

Créez enfin un dossier `scripts` dans `.devcontainer` avec le fichier `serve` suivant:

```bash
#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

# Serve MkDocs
mkdocs serve -f config/mkdocs.yml
```

Vous devriez maintenant avoir la structure de fichiers suivante:

```
.devcontainer
├── Dockerfile
├── devcontainer.json
├── mkdocs-edu
│   └── pyproject.toml
└── scripts
    └── serve
```

