ARG VARIANT="3.11"

FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

RUN apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y install --no-install-recommends \
    poppler-utils 

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -
