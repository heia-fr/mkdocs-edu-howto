import os
import jinja2
import logging

logger = logging.getLogger('mkdocs.hooks')

def on_pre_build(config):
    logger.info("Running on_pre_build hook")
    for root, dirs, files in os.walk(config["docs_dir"], topdown=False):
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(root),
        )
        for name in files:
            if name == "pages.j2":
                template = env.get_template(name)
                content = template.render(config=config, env=os.environ)
                dst = os.path.join(root, ".pages")
                # Do not write the file if the content is the same.
                # Otherwise, the "watcher" will continuously reload the page.
                if os.path.exists(dst):
                    with open(dst) as f:
                        orig = f.read()
                    if content == orig:
                        continue
                with open(dst, "w") as f:
                    logger.info(f"Writing {dst}")
                    f.write(content)

                
