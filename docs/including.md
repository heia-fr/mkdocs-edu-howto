---
title: Utilisation des "includes"
---

# {{ page.title }}

Pour des cours d'informatique, nous avons souvent besoin d'inclure des
extraits de code ou de fichiers de configuration. On peut bien sûr écrire
le contenu de ces fichiers directement dans le document _markdown_, mais
c'est souvent plus simple d'utiliser un mécanisme permettant d'inclure le
contenu d'un fichier en mentionnant juste le nom de ce fichier.

Pour inclure le contenu de fichier, le plus simple c'est d'utiliser le
[include markdown plugin](https://github.com/mondeja/mkdocs-include-markdown-plugin)
pour _MkDocs_.

Ajoutez le module python du _plugin_ dans votre configuration de _mkdocs_:

Allez dans le répertoire `.devcontainer/mkdocs-edu/` et tapez la commande suivante

```bash
poetry add mkdocs_include_markdown_plugin
```

Ajoutez aussi le _plugin_ dans le fichier `config/mkdocs.yml` :

```yml title="config/mkdocs.yml"
...
plugins:
  include-markdown:
    opening_tag: '{!'
    closing_tag: '!}'
```

La [documentation du plugin](https://github.com/mondeja/mkdocs-include-markdown-plugin#documentation)
vous expliquera comment l'utiliser.