---
title: Utilisation des "includes"
---

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

{% raw %}
!!! warning "Attention"
    La version actuelle de `mkdocs_include_markdown_plugin` ne permet pas de
    modifier les _tags_ `{%` et `%}` pour activer le plugin. En attendant que le 
    responsable du projet fasse la mise à jour, vous pouvez installer le plugin
    amélioré avec la commande suivante :

    ```
    poetry add git+https://github.com/supcik/mkdocs-include-markdown-plugin#dev-custom-tags
    ```
{% endraw %}

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