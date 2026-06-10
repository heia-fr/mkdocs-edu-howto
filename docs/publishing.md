---
title: Publication du site sur Internet
---

# {{ page.title }}

Pour rendre votre site disponible sur Internet, vous avez plusieurs solutions :

- [GitHub Pages](https://pages.github.com/)
- [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/)
- [Cloudflare Pages](https://pages.cloudflare.com/)
- [Netlify](https://www.netlify.com/)
- [Vercel](https://vercel.com/)
- et bien d'autres encore...

Je décris ici la méthode pour utiliser les _GitHub Pages_
et pour les _Gitlab Pages_, mais toutes
les options ci-dessus sont possibles avec Properdocs.

## Github Pages

Pour utiliser _GitHub Pages_, vous devez héberger votre projet dans un dépôt git
de GitHub.

Assurez-vous que votre projet GitHub est bien configuré pour générer des pages à partir des _GitHub Actions_.

Alles dans les paramètres des _GitHub Pages_ en cliquant le menu _Settings_
--> _Pages_ et définissez _GitHub Actions_ comme source :

![settings](publishing/img/action.webp){ width="80%" }


Créez ensuite les dossiers `.github` et `.github/workflows` à la racine de votre projet

Ajoutez-y le fichiers de suivant:

```yaml title=".github/workflows/website.yml"
{% raw %}
{! include "../.github/workflows/website.yml" ignore missing !}
{% endraw %}
```


Lors du prochain _push_ dans la branche `main` avec ces nouveaux fichiers, l'action de github
publiera le contenu de votre site sur _GitHub Pages_.

Vous obtenez l'URL à laquelle le site a été publié, en retournant dans _Settings_ --> _Pages_ :

![settings](publishing/img/page_url.webp){ width="80%" }



Après avoir sauvé cette configuration, modifiez encore le fichier `properdocs.yml` avec l'URL
que vous avez dans les _settings_ :

```yaml title="properdocs.yml" hl_lines="2"
site_name: My Education Site
site_url: https://heia-fr.github.io/mkdocs-edu-howto/
...
```

Faites un _commit_ et un _push_ et votre site devrait être publié
à l'URL adéquate.

Grâce aux _GitHub Actions_, votre site sera automatiquement publié
lors de chaque _push_ de la branche _main_ du projet.

## Gitlab Pages

Pour utiliser _GitLab Pages_, vous devez héberger votre projet dans un dépôt git
de GitLab.

Créez ensuite un fichier `.gitlab-ci.yml` à la racine de votre projet avec
le contenu suivant :

```yaml title=".gitlab-ci.yml"
{% raw %}
{! include "../.gitlab-ci.yml" ignore missing !}
{% endraw %}
```

Lors du prochain _push_ avec ce nouveau fichier, le CI/CD de gitlab
publiera votre site.

Allez dans Settings --> Pages pour découvrir l'URL de votre site.

Modifiez le fichier `properdocs.yml` avec cette URL.

```yaml title="properdocs.yml" hl_lines="2"
site_name: My Education Site
site_url: https://heia-fr.gitlab.io/mkdocs-edu-howto/
...
```

Faites un _commit_ et un _push_ pour activer le changement.

Grâce au _GitLab CI/CD_, votre site sera automatiquement publié
lors de chaque _push_ de la branche _main_ du projet.