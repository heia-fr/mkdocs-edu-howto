---
title: Mise à jour de mkdocs
---

# {{ page.title }}

Un site statique n'est que très peu vulnérable aux attaques informatiques, mais
pour bénéficier de nouvelles fonctionnalités, il est souhaitable de garder
votre système de génération de site à jour.

Pour faire la mise à jour du système, ouvrez un terminal et entrez dans le dossier `.devcontainer/mkdocs-edu`.
La commande `poetry show -o` montre les logiciels qui peuvent être mis à jour.
La commande `poetry update` effectue ensuite la mise à jour.

Si une mise à jour "majeure" est
disponible, vous devrez forcer l'installation avec la commande `add` et en spécifiant une nouvelle contrainte.
Étudiez la [documentation de poetry](https://python-poetry.org/docs/cli/#add) pour plus de détails.