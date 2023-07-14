---
title: Mise à disposition du site à la fin du cours
---

# {{ page.title }}

Lorsque le cours est terminé, il serait bon de distribuer une version
"offline" du site aux étudiants. En effet, le site va probablement
évoluer au cours des années à venir et c'est intéressant de conserver
la version correspondante à l'année d'étude.

Une solution serait de convertir le site en PDF et il existe plusieurs
"plugins" qui permettent de le faire, mais cette solution souffre de plusieurs
inconvénients:

- La mise en page est souvent hasardeuse et les sauts de page ne tombent pas toujours où l'on voudrait
- Les vidéos et autres animations ne sont pas possibles dans un PDF
- Les documents (PDF) intégrés au site ne sont également plus disponibles

Une autre solution, et c'est celle que nous conseillons, consiste à produire un fichier _zip_
avec le contenu du site. Pour cela, il suffit de construire une version statique du site
avec la commande :

```bash
SHOW_SOLUTION=999 LECTURE_WEEK=999 poetry run mkdocs build -d public
```

Vous aurez alors un dossier `public` contenant la totalité du site.

Dans ce dossier, ajoutez encore un fichier `.prefix` indiquant le _préfixe_ du site. Vous trouverez ce préfixe
dans le fichier `mkdocs.yml` à la ligne commençant par `site_url`. Pour rappel, voici le début
du fichier `mkdocs.yml` de notre exemple :

```yaml title="mkdocs.yml" hl_lines="2"
site_name: My Education Site
site_url: https://heia-fr.github.io/mkdocs-edu-howto/
...
```

Le préfixe c'est la partie de l'URL qui suit le nom du serveur. Dans notre exemple,
le nom du serveur c'est `heia-fr.github.io` et le préfixe est donc `/mkdocs-edu-howto/`

Nous générons donc le fichier `.prefix` avec la commande suivante:

```bash
echo "/mkdocs-edu-howto/" > ./public/.prefix
```

Nous pouvons maintenant compresser le dossier `public` avec la commande `zip` :

```bash
cd public && zip -FS -r ../my-website.wzip . && cd ..
```

Vous pouvez maintenant distribuer le fichier `my-website.wzip` à vos étudiants.

Ce fichier `.wzip` peut être utilisé avec programme [zipserve](https://github.com/supcik/zipserve/releases)
qui permet de servir l'archive sans la décompresser.