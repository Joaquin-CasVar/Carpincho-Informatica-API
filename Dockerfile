# pull python base image
FROM python:3.12-slim

ENV UV_LINK_MODE=copy

# set work directory
WORKDIR /app

# install uv
COPY --from=ghcr.io/astral-sh/uv:0.12.5 /uv /uvx /bin/

COPY pyproject.toml uv.lock /_lock/

# sync dependencies
RUN cd /_lock && uv sync --locked --no-install-project

# copy project
COPY . .
