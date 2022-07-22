---
title: Techniques avancées
---

# {{ page.title }}

## Configuration avancée

Lorsque le fichier de configuration `config/mkdocs.yml` devient trop grand,
il peut être avantageux de le diviser et d'utiliser l'[héritage](https://www.mkdocs.org/user-guide/configuration/#configuration-inheritance)

Pour le site que vous voyez, la configuration est composée de deux fichiers. Un fichier de base avec
une configuration "standard" pour les sites d'éducation :

```yaml title="config/base.yml"
{! include "advanced/inc/base.yml" !}
```

Et un fichier `mkdocs.yml` qui _hérite_ du fichier de base et qui configure
les paramètres spécifiques au site

```yaml title="config/mkdocs.yml"
{! include "advanced/inc/mkdocs.yml" !}
```

## Sites multilangues

Si vous souhaitez que votre site soit disponible dans plusieurs langues, vous
pouvez utiliser le _plugin_ [mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/).
Ce _plugin_ a été testé et fonctionne bien avec les techniques décrites dans ce site,
mais les détails concernant son utilisation dépassent le cadre de ce site.

## Et bien d'autres...

Le thème [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) ainsi
que les nombreux _plugins_ pour mkdocs évoluent constamment pour offrir une 
meilleure expérience utilisateur. Nous vous invitons à étudier la documentation
et les nombreuses publications sur Internet pour améliorer votre site web.