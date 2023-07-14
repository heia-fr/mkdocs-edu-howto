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

Allez à la racine de votre projet et tapez les commandes suivantes

```bash
poetry add mkdocs-awesome-pages-plugin
poetry add mkdocs-macros-plugin
poetry add mkdocs-pages-j2-plugin
```

Ajoutez aussi les _plugins_ dans le fichier `mkdocs.yml` :

```yml title="mkdocs.yml"
plugins:
  - awesome-pages
  - macros
  - pages-j2
```

## Publication incrémentielle du contenu

Pour publier le contenu de manière incrémentielle, ajoutez un fichier `pages.j2`
dans le dossier `docs` ainsi que dans tous les sous-dossiers de `docs`. La
documentation pour ce fichier se trouve sur le [dépôt git du plugin mkdocs-awesome-pages-plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin#features) et le plugin `pages-j2`
permet de générer les fichiers `.pages` dynamiquement à partir des fichiers `pages.j2`
qui se trouvent dans le même dossier.

Un fichier `pages.j2` typique ressemble à ça:

{% raw %}
```text
nav:
    - index.md
{%- if extra.lecture_week | int >= 1 %}
    - chapter1.md
{%- endif %}
{%- if extra.lecture_week | int >= 2 %}
    - chapter2.md
{%- endif %}
{%- if extra.lecture_week | int >= 3 %}
    - chapter3.md
{%- endif %}
{%- if extra.lecture_week | int >= 4 %}
    - chapter4.md
{%- endif %}

```
{% endraw %}

Vous pouvez définir la variable `lecture_week` dans la section `extra` du fichier `mkdocs.yml`. Par exemple, si vous définissez la variable comme suit :

```yml title="mkdocs.yml"
extra:
  lecture_week: 2
```

Le fichier `.pages` correspondant ne contiendra que les deux premiers chapitres.

{% raw %}
```text
nav:
    - index.md
    - chapter1.md
    - chapter2.md
```
{% endraw %}

Si vous souhaitez définir la variable lors de la génération du site, vous pouvez utiliser
les variables d'environnement. Si vous définissez la variable `extra_lecture_week` ainsi :

```yml title="mkdocs.yml"
extra:
  lecture_week: !ENV LECTURE_WEEK
```

vous pourrez alors définir la variable `LECTURE_WEEK` lors de la génération du site. Par exemple, pour les deux premières semaines, vous pouvez utiliser la commande suivante :

```bash
LECTURE_WEEK=2 poetry run mkdocs serve
```

Dans le fichier `mkdocs.yml`, vous pouvez aussi définir une valeur par défaut pour la variable `LECTURE_WEEK` :

```yml title="mkdocs.yml"
extra:
  lecture_week: !ENV [LECTURE_WEEK, '999']
```

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

{% if show_solution >= 5 %}
??? success "Solution"
    La solution est ...
{% endif %}
```
{% endraw %}

La variable `show_solution` est définie dans la section `extra` du fichier `mkdocs.yml`. Par exemple:

```yml title="mkdocs.yml"
extra:
  show_solution: 2
```

Tout comme pour la publication incrémentielle du contenu, vous pouvez définir la variable `show_solution` lors de la génération du site en utilisant les variables d'environnement. Si vous définissez la variable `extra_show_solution` ainsi :

```yml title="mkdocs.yml"
extra:
  show_solution: !ENV SHOW_SOLUTION
```

vous pourrez alors définir la variable `SHOW_SOLUTION` lors de la génération du site. Par exemple:

```bash
SHOW_SOLUTION=1 LECTURE_WEEK=2 poetry run mkdocs serve
```

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
    {% if show_solution >= page.meta.week + 1 %}
    ??? success "Solution"
        La solution est ...
    {% endif %}
    ```
{% endraw %}

    Et si vraiment une solution doit être publiée une semaine plus tard, rien
    ne vous empêche d'écrire :

{% raw %}
    ```markdown
    {% if show_solution >= page.meta.week + 2 %}
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
  LECTURE_WEEK: 2
  SHOW_SOLUTION: 1
```

Il vous suffit maintenant de changer ces valeurs chaque semaine
et de faire un _push_ de votre site pour l'actualiser.

!!! info "Info"
    Le plugin [mkdocs-calendar-plugin](https://github.com/supcik/mkdocs-calendar-plugin)
    permet de définir des variables `extra` en fonction de la date du jour. Vous pouvez
    ainsi complètement automatiser la publication incrémentielle de votre site.