FROM python:3

RUN addgroup --system stoix && adduser --system --ingroup stoix stoix
USER stoix:stoix
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR /opt/stoix/ingest-data
COPY pyproject.toml poetry.lock ./
RUN /home/stoix/.poetry/bin/poetry install --no-dev --no-root
COPY src src

CMD /home/stoix/.poetry/bin/poetry run python src/main.py
