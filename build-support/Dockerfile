FROM  python:3.11-alpine as base

### Setting up dagster environment
ENV DAGSTER_HOME=/var/lib/dagster

RUN mkdir -p $DAGSTER_HOME
WORKDIR $DAGSTER_HOME

ENV PYTHONPATH=$DAGSTER_HOME

COPY requirements.txt ./pyproject.toml ./poetry.lock ./README.md $DAGSTER_HOME

RUN python -m venv ~/.virtualenvs/dagster-env

RUN source ~/.virtualenvs/dagster-env/bin/activate && \
    pip install -r requirements.txt && \
    poetry install --no-root

FROM base as webserver
ENTRYPOINT ["dagster-webserver", "-h", "0.0.0.0", "-p", "3000"]

FROM base as daemon
ENTRYPOINT ["dagster-daemon", "run"]

# User Code
FROM base as user_code
COPY . .
ENTRYPOINT ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-m", "dagster_demo"]

