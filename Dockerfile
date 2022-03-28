#############################################
# Base container with all necessary deps
FROM python:3.10.3 AS build

ARG app_env

# Set up environment variables
ENV YOUR_ENV=${app_env} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.0 \
    FLASK_RUN_PORT=8080 \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_DEBUG=0

# System deps:
RUN python -m pip install --upgrade pip \
    && pip3 install "poetry==$POETRY_VERSION" --no-cache-dir

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# 1. Disable virtualenv creation with poetry
# 2. Install poetry deps
RUN poetry config virtualenvs.create false \
    && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /app

#############################################
# Test container from a common base
FROM build AS unit-tests

ARG app_env=dev

ENV APP_ENV=${app_env}

CMD ["pytest"]

#############################################
# Deploy container
FROM build AS deploy

ARG app_env
ARG app_port=8080

ENV APP_ENV=${app_env}
EXPOSE ${app_port}

CMD ["python3", "app.py"]
