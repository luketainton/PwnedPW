FROM python:3.13-slim
LABEL maintainer="Luke Tainton <luke@tainton.uk>"
USER root

ENV PYTHONPATH="/run:/usr/local/lib/python3.13/lib-dynload:/usr/local/lib/python3.13/site-packages:/usr/local/lib/python3.13"
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

WORKDIR /run

RUN mkdir -p /.local && \
    chmod -R 777 /.local && \
    pip install -U pip uv==0.5.14

COPY pyproject.toml /run/pyproject.toml
COPY uv.lock /run/uv.lock
# needed for PDM build
COPY README.md /run/README.md

RUN uv sync --frozen

ENTRYPOINT ["python3", "-B", "-m", "app.main"]

ARG version="dev"
ENV APP_VERSION=$version

COPY app /run/app
