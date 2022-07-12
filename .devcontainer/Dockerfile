ARG VARIANT=bullseye
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Install additional software
RUN apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y install --no-install-recommends \
  imagemagick \
  zip

# Copy files needed to build our flavour of mkdocs
COPY mkdocs-edu/* /mkdocs-edu/
WORKDIR /mkdocs-edu

# Install "poetry", then build and install mkdocs
RUN pip install poetry && \
  poetry config virtualenvs.create false && \
  poetry install

# Copy scripts for serving and building the site
COPY --chmod=0755 scripts/* /usr/local/bin/
