---
title: Installation du devcontainer
---

# Installation du _devcontainer_

Commencez par créer un répertoire qui contiendra tous les fichiers de votre site. Ouvrez ensuite ce répertoire avec VS-Code.


!!! attention "Pour les utilisateurs de PC avec Microsoft Windows :fontawesome-brands-microsoft:"
    Les fichiers que vous créerez lors de cette étape seront utilisés par un conteneur Docker qui
    utilise (de manière transparente pour l'utilisateur) une machine virtuelle Linux. Windows et Linux
    n'utilisent pas la même convention pour encoder les fins de ligne des fichiers textes. Windows
    utilise la combinaison `CR/LF` alors que Linux se contente de `LF`.
    VS Code vous indique la convention pour le fichier actuel dans la barre
    d'état, en bas à droite :<br/>
    <img src="img/eol.png" style="padding-top:4px"/>
    <br/>
    Assurez-vous de bien configurer `LF` pour le fichier `serve` que vous éditerez
    plus tard. Si vous préférez, vous pouvez aussi configurer VS Code pour que
    tous les fichiers de ce projet soient encodés avec `LF` uniquement : tapez ++ctrl+","++ ou sélectionnez le menu _code_ --> _Preferences_ --> _Settings_ et cherchez "Files: eol".
    <br/>
    <img src="img/settings.png" style="padding-top:10px"/>
    <br/>
    Assurez-vous de modifier les paramètres du _Workspace_ et choisissez `\n` (ce qui correspond à `LF`.)

Créez un sous-répertoire `.devcontainer` (n'oubliez pas le point du début). Dans ce répertoire, créez un fichier `devcontainer.json` avec le contenu suivant :

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
python = ">=3.9,<4"
mkdocs = "^1.3.1"
mkdocs-material = "8.4.0rc1"
mkdocs-awesome-pages-plugin = "^2.8.0"
mkdocs-minify-plugin = "^0.5.0"
python-markdown-math = "^0.8"
jinja2-cli = "^0.8.2"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

Créez enfin un dossier `scripts` dans `.devcontainer` avec le fichier `serve` suivant:

!!! attention "Pour les utilisateurs de PC avec Microsoft Windows :fontawesome-brands-microsoft:"
    Ce fichier doit impérativement être sauvé avec l'encodage de fin
    de ligne `LF`. Relisez la remarque au début de ce chapitre pour
    plus d'explications.


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

