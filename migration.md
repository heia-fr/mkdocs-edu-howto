This document describe the migration from DevContainer to the new mkdocs structure (with poetry) made by Jacques Supcik.

First version of this document: 22.08.2023/BUN

# Migration Steps

1. Delete the ```.devcontainer``` directory
2. On the console, type 
   ```bash
   poetry config virtualenvs.in-project true
   poetry init
   poetry add mkdocs mkdocs-material
   poetry run mkdocs new .
   ```
3. Modify the ```pyproject.toml``` with the correct Python version (on OSX):
   ```yaml
   [tool.poetry.dependencies]
   #python = "^3.11"
   python = ">=3.11,<3.12"
   ```

4. Add some mkdocs plugins:
   ```bash
   poetry add mkdocs_include_markdown_plugin
   poetry add mkdocs-awesome-pages-plugin
   poetry add mkdocs-macros-plugin
   poetry add mkdocs-pages-j2-plugin
   poetry add python-markdown-math
   poetry add mkdocs-git-revision-date-localized-plugin
   poetry add mkdocs-calendar-plugin
   poetry add mkdocs-jconfig-plugin
   poetry add mkdocs-glightbox
   ```

   ou sur moins de lignes:
   ```bash
   poetry add mkdocs_include_markdown_plugin mkdocs-awesome-pages-plugin mkdocs-macros-plugin 
   poetry add mkdocs-pages-j2-plugin python-markdown-math mkdocs-git-revision-date-localized-plugin
   poetry add mkdocs-calendar-plugin mkdocs-jconfig-plugin mkdocs-glightbox
   ```

5. We can now start the server:
   ```bash
   poetry run mkdocs serve
   ```

6. We have now to modify the config files to get the correct theme and structure. The directory ```config``` is no more used. From the files in this directory:
   * move ```mkdocs.yml``` to the root directory
   * move the content of the ```base.yml``` at the beginning of the ```mkdocs.yml```
   * comment or remove the lines:
     ```md
     # hooks:
     #  - hooks.py
     ```

7. Add variables into the ```mkdocs.yml``` file, in the ```extra``` section, for example:
   ```yaml
     lecture_week: 16
     lecture_show: 999
     exo_show_data: 999
     exo_show_solution: 999
     lab_show_data: 999
     lab_show_solution: 0
     ```

8. Add the following to the ```plugins``` section of the ```mkdocs.yml``` file (if misssing):
   ```yaml
      plugins:
         ...
          - pages-j2
          - calendar:
             tz: Europe/Zurich
   ```

9. Rename variables in your ```.md``` documents, if necessary:
   * ```assignment_show_data``` --> ```lab_show_data```
   * ```assignment_show_solution``` --> ```lab_show_solution```

10. Some cleaning:
   * delete the ```config``` directory


10. Test the new configuration by starting your local server:
    ```bash
    poetry run mkdocs serve
    ```

11. Publish the site on gitlab with the new ```.gitlab-ci.yml``` content,
    as describe on Jacques [documentation](https://heia-fr.github.io/mkdocs-edu-howto/publishing/)