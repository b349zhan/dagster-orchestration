FROM  python:3.11-alpine as base

WORKDIR /app/dagster-orchestration

ENV DAGSTER_HOME=/var/lib/dagster

ENV PYTHONPATH=$DAGSTER_HOME

ENV PATH="$HOME/.local/bin/:$PATH"

COPY ./pyproject.toml ./poetry.lock ./README.md ./

RUN pip install poetry==1.7.1 && \
    POETRY_VIRTUALENVS_CREATE=false poetry install

COPY . .

