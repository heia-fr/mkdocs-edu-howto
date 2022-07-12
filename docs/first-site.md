---
title: Contenu du premier site
---

Vous êtes maintenant prêt pour rédiger la première version de votre site. Créez un dossier `docs` (en dehors de `.devcontainer`) avec le fichier `index.md` suivant:

```markdown
# Bienvenue sur MkDocs-Edu

Hello Education World
```

et un dossier `config` avec le fichier `mkdocs.yml` suivant:

```yaml
site_name: My Education Site

docs_dir: '../docs/'
site_dir: '../public/'

theme:
  name: material
  language: 'fr'
```

Tapez `serve` dans le terminal et vous devriez observer le résultat suivant:

![terminal avec la commande serve](img/serve.png){ width="100%" }


Cliquez sur le bouton _Open in Browser_ et votre navigateur devrait  afficher votre site:

![Premier site mkdocs](img/demosite.png){ width="100%" }

Félicitations! Vous venez de créer un site web avec mkdocs.