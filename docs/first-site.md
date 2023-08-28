---
title: Création d'un premier site
---

# {{ page.title }}

Pour créer votre premier site, créez un nouveau dossier et ouvrez une console dans ce répertoire.

!!! tip "Astuce"
    Si vous utilisez Visual Studio Code, vous pouvez ouvrir une console en tapant ++ctrl+shift+grave++ ou en cliquant sur le menu `Terminal` et en choisissant `New Terminal`.

    Si votre éditeur n'a pas de terminal intégré, nous vous recommandons d'utiliser [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701) pour Windows, [iTerm2](https://iterm2.com/) pour macOS, ou le terminal par défaut de votre distribution Linux.

Créez maintenant un nouveau projet `Poetry`.

!!! tip "Astuce"
    `Poetry` crée un environnement virtuel Python dans le dossier `.venv` du projet.

    Cette configuration est définie dans le fichier `poetry.toml`. Quand elle n'est pas définie, Poetry crée un environnement virtuel dans [un répertoire de votre système](https://python-poetry.org/docs/configuration/#data-directory). A vous de voir si vous préférez cette option ou non.

Tapez la commande `poetry init` et répondez aux questions. N'ajoutez pas encore les
dépendances. Par exemple :

```text
This command will guide you through creating your pyproject.toml config.

Package name [mkdocs-edu-howto]:
Version [0.1.0]:
Description []:  Demo Web Site
Author [Jacques Supcik <jacques.supcik@hefr.ch>, n to skip]:
License []:  Apache-2
Compatible Python versions [>=3.10,<3.12]:

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file
...
Do you confirm generation? (yes/no) [yes]
```

!!! warning "Attention"
    Lors de la rédaction de cette page, la dernière version de Python était la 3.11.4. Python 3.12 était en _pre-release_ et Python 3.13 n'existait pas encore.
    
    La plupart des paquets demandent au moins la version 3.7 de Python, certains demandent la version 3.8 et quelques-uns demandent la version 3.10.
    Afin de couvrir tous les cas, nous allons demander une version 3.10 ou 3.11. On peut éventuellement laisser la version 3.12, mais il faut exclure
    les versions supérieures à 3.12 car certains paquets sont prudents et ne peuvent pas s'installer si on autorise une version supérieure à 3.12.

    Pour la configuration de la version de python (`Compatible Python versions`), assurez-vous donc
    de mettre `>=3.10,<3.12` ou `>=3.10,<3.13`. 
    
    Il se peut que `poetry` vous propose quelque chose comme `^3.11`. Dans ce cas, modifiez
    la proposition par `>=3.10,<3.12` (ou `>=3.10,<3.13`).

    Si vous avez déjà créé le fichier `pyproject.toml`, vous pouvez le modifier directement
    avec votre éditeur de texte préféré. Vous devriez avoir quelque chose comme :
    ```toml
    [tool.poetry.dependencies]
    python = ">=3.10,<3.12"
    ...
    ```

Ajoutez maintenant les dépendances :

```bash
poetry add mkdocs mkdocs-material
```

Vous pouvez maintenant créer votre premier site mkdocs avec la commande suivante :

```bash
poetry run mkdocs new .
```

puis

```bash
poetry run mkdocs serve
```

Mkdocs écrira ces quelques lignes dans la console :

```text
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.03 seconds
INFO     -  [21:33:52] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [21:33:52] Serving on http://127.0.0.1:8000/
WARNING  -  [21:33:52] "GET /mkdocs-edu-howto/first-site/ HTTP/1.1" code 404
INFO     -  [21:33:57] Browser connected: http://127.0.0.1:8000/
```

et en ouvrant votre navigateur à l'adresse [http://127.0.0.1:8000/](http://127.0.0.1:8000/),
vous devriez voir le résultat suivant :

![Premier site mkdocs](first-site/img/site0.webp){ class="screen" width="100%" }

Félicitations! Vous venez de créer un site web avec mkdocs.