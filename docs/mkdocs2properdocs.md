---
title: Migration de MkDocs vers ProperDocs
---

# {{ page.title }}

## Remplacement de Poetry par uv

Si votre projet utilise encore Poetry, vous pouvez migrer vers uv en suivant ces étapes :

1. [Installez uv](https://docs.astral.sh/uv/getting-started/installation/) sur votre machine.
2. Supprimez les dossier `.venv`, `__pycache__`, ainsi queles fichiers `poetry.lock` et `poetry.toml` de votre projet.
3. Renomez votre fichier `pyproject.toml` vers `pyproject-poetry.toml` (pour en avoir une copie de sauvegarde).
4. Créez un nouveau fichier `pyproject.toml` avec le contenu suivant (adaptez les champs et les dépendances à votre projet) :
```toml
[project]
name = "My Website"
version = "0.1.0"
description = "Description..."
authors = [{ name = "Albert Einstein", email = "albert.einstein@hefr.ch" }]
readme = "README.md"
requires-python = ">=3.10,<4.0"
license = "MIT"

dependencies = [
    "mkdocs-materialx>=10.1.7",
    "properdocs>=1.6.7",
    ...
]

[tool.uv]
package = false

[build-system]
requires = ["uv_build>=0.9.0,<0.10.0"]
build-backend = "uv_build"
```
5. Si vous avez des scripts ou des commandes personnalisées dans votre projet, vous devrez les adapter pour uv (remplacez `poetry run` par `uv run`). Consultez la [documentation de uv](https://docs.astral.sh/uv/) pour plus d'informations sur la configuration et l'utilisation de uv.
6. Consultez le fichier `pyproject-poetry.toml` pour récupérer les dépendances et les configurations spécifiques à votre projet, et assurez-vous de les intégrer à nouveau (avec `uv add` ou en les ajoutant directement dans le `pyproject.toml`).

## Suppression de "Polyfill"

Récemment, un changement sur le site de Polyfill a rendu l'accès à leurs services plus difficile, ce qui a affecté les projets qui utilisaient leurs ressources.
Avec les navigateurs modernes, il n'est plus nécessaire d'utiliser des polyfills pour assurer la compatibilité avec les anciennes versions de navigateurs.
Par conséquent, nous avons décidé de supprimer les références à Polyfill dans notre projet.

Dans le fichier `mkdocs.yml` (ou `properdocs.yml`), vous pouvez supprimer la lignes faisant référence à Polyfill :

```yaml
extra_javascript:
  ...
  - https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?version=4.8.0&features=es6 # Supprimez cette ligne
  ...
```

## Remplacement de `mkdocs` par `properdocs`

Suite aux [histoires](https://fpgmaas.com/blog/collapse-of-mkdocs/) concernant la maintenance de MkDocs, nous avons décidé de migrer vers [ProperDocs](https://properdocs.org/), qui est un fork de MkDocs avec des améliorations et une maintenance active. La migration vers ProperDocs est relativement simple :

1. Renommez votre fichier `mkdocs.yml` en `properdocs.yml`.
2. Remplacez les références à `mkdocs` par `properdocs` dans vos fichiers de configuration.

Notez que la plupart des plugins de MkDocs sont compatibles avec ProperDocs et vous pouvez continuer à les utiliser sans modification.

Le thème "Material for MkDocs" n'est plus maintenu, mais son fork [MaterialX](https://jaywhj.github.io/mkdocs-materialx/) est une excellente alternative avec des fonctionnalités similaires et une maintenance active. Vous pouvez remplacer le thème dans votre configuration :

```yaml
theme:
  name: materialx
```

Par défaut, la barre supérieure du thème MaterialX reste en blanc, mais vous pouvez la personnaliser en ajoutant la configuration suivante dans votre fichier `properdocs.yml`. Par exemple, pour la rendre de couleur primaire :

```yaml
theme:
  topbar_style: primary
```

#