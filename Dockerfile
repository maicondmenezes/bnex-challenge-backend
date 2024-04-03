FROM python:3.11-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && \
pip install --no-cache-dir --upgrade pip && \
pip install poetry

COPY ./pyproject.toml /usr/src/app/pyproject.toml

RUN poetry config virtualenvs.create false && \
poetry install --only main --no-interaction --no-ansi

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY core/ /usr/src/app/core/

RUN chmod +x /usr/src/app/entrypoint.sh
EXPOSE 8000

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
