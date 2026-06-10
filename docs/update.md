---
title: Mise à jour de properdocs
---

# {{ page.title }}

Un site statique n'est que très peu vulnérable aux attaques informatiques, mais
pour bénéficier de nouvelles fonctionnalités, il est souhaitable de garder
votre système de génération de site à jour.

La commande `uv pip list --outdated` montre les logiciels qui peuvent être mis à jour.
La commande `uv sync --upgrade` effectue ensuite la mise à jour.

Si une mise à jour "majeure" est
disponible, vous devrez forcer l'installation avec la commande `add` et en spécifiant une nouvelle contrainte.
Étudiez la [documentation de uv](https://docs.astral.sh/uv/pip/packages/) pour plus de détails.