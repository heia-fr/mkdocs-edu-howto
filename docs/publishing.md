---
title: Publication du site sur Internet
---

# {{ page.title }}

Pour rendre votre site disponible sur Internet, vous avez plusieurs solutions :

- [GitHub Pages](https://pages.github.com/)
- [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/)
- [Netlify](https://www.netlify.com/)
- [Vercel](https://vercel.com/)
- et bien d'autres encore...

Je vais décrire ici la méthode pour utiliser les _GitHub Pages_
et pour les _Gitlab Pages_, mais toutes
les options ci-dessus sont possibles avec MkDocs.

## Github Pages

!!! info "Information"
    Il y a actuellement une [nouvelle manière](https://github.blog/changelog/2022-07-27-github-pages-custom-github-actions-workflows-beta/) de publier les pages
    sur GitHub Pages. Cette page sera prochainement modifiée pour expliquer
    cette nouvelle technique.

Pour utiliser _GitHub Pages_, vous devez héberger votre projet dans un dépôt git
de GitHub.

Créez ensuite un dossier `.github` à la racine de votre projet

Ajoutez-y les fichiers suivants pour définir l'action _Mkdocs edu builder_:

```yaml title="actions/mkdocs-edu/action.yml"
{% raw %}
{! include "publishing/inc/actions/mkdocs-edu/action.yml" ignore missing !}
{% endraw %}
```

```Dockerfile title="actions/mkdocs-edu/Dockerfile"
{! include "publishing/inc/actions/mkdocs-edu/Dockerfile" ignore missing !}
```

```bash title="actions/mkdocs-edu/entrypoint.sh"
{! include "publishing/inc/actions/mkdocs-edu/entrypoint.sh" ignore missing !}
```

Ainsi que le fichier suivant pour le _workflow_ :

```yaml title="workflows/website.yml"
{% raw %}
{! include "publishing/inc/workflows/website.yml" ignore missing !}
{% endraw %}
```

Lors du prochain _push_ avec ces nouveaux fichiers, l'action de github
créera une nouvelle branche avec le contenu de votre site statique.

Afin de publier cette branche dans _GitHub Pages_, allez dans _Settings_ --> _Pages_
et choisissez la branche _gh-pages_ comme source de votre site :

![settings](publishing/img/gh-pages-settings.png){ width="100%" }

Après avoir sauvé cette configuration, modifiez encore le fichier `config/mkdocs.yml` avec l'URL
que vous avez dans les _settings_ :

```yaml title="config/mkdocs.yml" hl_lines="2"
site_name: My Education Site
site_url: https://heia-fr.github.io/mkdocs-edu-howto/
...
```

Faites un _commit_ et un _push_ et votre site devrait être publié
à l'URL adéquate.

Grâce aux _GitHub Actions_, votre site sera automatiquement publié
lors de chaque _push_ de la branche _main_ du projet ou lors du
_push_ d'un _tag_ commençant par "v".

## Gitlab Pages

Pour utiliser _GitLab Pages_, vous devez héberger votre projet dans un dépôt git
de GitLab.


Créez ensuite un fichier `.gitlab-ci.yml` à la racine de votre projet avec
le contenu suivant :

```yaml title=".gitlab-ci.yml"
{% raw %}
{! include "publishing/inc/.gitlab-ci.yml" ignore missing !}
{% endraw %}
```

Lors du prochain _push_ avec ce nouveau fichier, le CI/CD de gitlab
publiera votre site.

Allez dans Settings --> Pages pour découvrir l'URL de votre site.

Modifiez le fichier `config/mkdocs.yml` avec cet URL.

```yaml title="config/mkdocs.yml" hl_lines="2"
site_name: My Education Site
site_url: https://heia-fr.gitlab.io/mkdocs-edu-howto/
...
```

Faites un _commit_ et un _push_ pour activer le changement.

Grâce au _GitLab CI/CD_, votre site sera automatiquement publié
lors de chaque _push_ de la branche _main_ du projet.