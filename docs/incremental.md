---
title: Publication incrémentielle
---

# {{ page.title }}

{% set tip = 1 %}

Les sites pour l'éducation nécessitent souvent de pouvoir publier
les chapitres du cours au fur et à mesure des semaines. Il en va de
même avec les solutions des exercices qui ne doivent être publiés
que lorsque les étudiants ont rendu leurs copies.

## Installation

Pour permettre les opérations ci-dessus, nous avons besoin
d'installer quelques _plugins_ supplémentaires.

Allez dans le répertoire `.devcontainer/mkdocs-edu/` et tapez les commandes suivantes

```bash
poetry add mkdocs-awesome-pages-plugin
poetry add mkdocs-macros-plugin
poetry add mkdocs-simple-hooks
```

Ajoutez aussi les _plugins_ dans le fichier `config/mkdocs.yml` :

```yml title="config/mkdocs.yml"
...
plugins:
  ...
  awesome-pages: {}
  macros: {}
  mkdocs-simple-hooks:
    hooks:
      on_pre_build: "hooks:on_pre_build"
```

Ajoutez aussi le fichier `hooks.py` à la racine de votre projet:

```python title="hooks.py"
{! include "incremental/inc/hooks.py" !}
```

Ce script permet de générer les fichiers `.pages` pour le plugin `awesome-pages`
à partir des _templates_ `pages.j2`. Nous reviendrons sur l'utilisation de ces
fichiers plus tard.

Ajouter encore le fichier `main.py` dans le dossier `config/` :

```python title="config/main.py"
{! include "incremental/inc/main.py" !}
```

Vous devez maintenant modifier le script `serve` que nous avons vu
dans un chapitre précédent. Modifier le fichier `.devcontainer/scripts/serve`
avec le contenu suivant:

```python title=".devcontainer/scripts/serve"
{! include "incremental/inc/serve" !}
```

Régénérez ensuite le _devcontainer_ avec ++ctrl+shift+p++ ou ++cmd+shift+p++ et cherchez _Remote-Containers: Rebuild Container_.

La commande `serve` accepte maintenant deux paramètres : `-w` permet de choisir la
semaine à publier et `-s` permet de contrôler la publication des solutions.

## Publication incrémentielle du contenu

Pour publier le contenu de manière incrémentielle, ajoutez un fichier `pages.j2`
dans le dossier `docs` ainsi que dans tous les sous-dossiers de `docs`. La
documentation pour ce fichier se trouve sur le [dépôt git du plugin mkdocs-awesome-pages-plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin#features) et la configuration que nous
avons faite permet de générer les fichiers `.pages` dynamiquement à partir des fichiers `pages.j2`
qui se trouvent dans le même dossier.

Un fichier `pages.j2` typique ressemble à ça:

{% raw %}
```text
nav:
    - index.md
{%- if env.SELECT_WEEK | int >= 1 %}
    - chapter1.md
{%- endif %}
{%- if env.SELECT_WEEK | int >= 2 %}
    - chapter2.md
{%- endif %}
{%- if env.SELECT_WEEK | int >= 3 %}
    - chapter3.md
{%- endif %}
{%- if env.SELECT_WEEK | int >= 4 %}
    - chapter4.md
{%- endif %}

```
{% endraw %}

Le fichier `.pages` correspondant ne contiendra que les pages correspondantes
à la semaine choisie. Par exemple, si vous démarrez le serveur avec la commande
`serve -w 2`, le fichier `.pages` ci-dessus contiendra uniquement
les lignes suivantes :

{% raw %}
```text
nav:
    - index.md
    - chapter1.md
    - chapter2.md
```
{% endraw %}

## Publication incrémentielle des solutions

Pour le contrôle de la publication des solutions, nous devons
agir sur le contenu du fichier _markdown_. Nous utilisons pour
cela les [blocs conditionnels](https://jinja.palletsprojects.com/en/3.1.x/templates/#if) 
du plugin _macros_

Un extrait d'un fichier markdown typique ressemble à ça:

{% raw %}
```markdown
!!! todo "Exercice N"
    Donnée de l'exercice : ...

{% if solution >= 5 %}
??? success "Solution"
    La solution est ...
{% endif %}
```
{% endraw %}

La solution ne sera alors publiée que si l'option `-s` de la commande `serve``
est suivi d'un nombre supérieur ou égal à 5.

!!! tip "Astuce {{ tip }}"
    {% set tip = tip + 1 %}
    Dans un chapitre donnée, les solutions seront souvent publiées en même temps. C'est assez
    rare de ne devoir publier qu'une partie des solution à la fois. Au lieu d'écrire à chaque
    fois le même nombre dans l'expression {% raw %}`{% if solution >= 5 %}`{% endraw %}, vous
    pouvez définir la semaine dans le
    [_front matter_](https://www.mkdocs.org/user-guide/writing-your-docs/#meta-data)
    de la page et si la solution doit être publiée une semaine plus tard, faites comme ça :
    
{% raw %}
    ```markdown
    ---
    title: Titre de la page
    week: 4
    ---
    ...
    {% if solution >= page.meta.week + 1 %}
    ??? success "Solution"
        La solution est ...
    {% endif %}
    ```
{% endraw %}

    Et si vraiment une solution doit être publiée une semaine plus tard, rien
    ne vous empêche d'écrire :

{% raw %}
    ```markdown
    {% if solution >= page.meta.week + 2 %}
    ??? success "Solution"
        La solution est ...
    {% endif %}
    ```
{% endraw %}

!!! tip "Astuce {{ tip }}"
    {% set tip = tip + 1 %}
    Si vous souhaitez numéroter les questions, vous pouvez utiliser
    une variable pour garantir une série régulière.

    Au début de votre contenu markdown, définissez une variable (par exemple `q`):
{% raw %}
    ```markdown
    {% set q = 1 %}
    ```
{% endraw %}

    et utilisez cette variable dans vos questions :

{% raw %}
    ```markdown
    !!! todo "Exercice {{ q }}"
        {% set q = q + 1 %}
        ...
    ```
{% endraw %}

    Vous pourez en tout temps insérer des exercices
    dans votre document sans avois à vous soucier
    de la numérotation.

## Modification du workflow pour la publication

Les paramètres de contrôle de la publication peuvent
être définis dans des variables d'environnement.

Modifiez le fichier `.github/workflows/website.yml` avec
la section suivante :

```yaml title=".github/workflows/website.yml"
env:
  SELECT_WEEK: 999
  SHOW_SOLUTION: 999
```

Il vous suffit maintenant de changer ces valeurs chaque semaine
et de faire un _push_ de votre site pour l'actualiser.

!!! info "Info"
    Je travaille sur une solution permettant d'également automatiser
    ce processus avec un calendrier. [Contactez-moi](mailto: jacques.supcik@hefr.ch)
    si cette option vous intéresse.