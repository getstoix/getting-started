# Getting started

The getting started example contains code for https://getstoix.com/getting-started.

Each example has a subfolder which is briefly described below and are built and run roughly the same way with the only difference being environment variables used to configure the jobs. Each job also has an image built and hosted on Stoix Dockerhub page at https://hub.docker.com/u/stoix.

## bq-runner

Generic job for running SQL code in BigQuery.

Environment variables:

* `GCP_SERVICE_ACCOUNT_CREDENTIALS`: Base64 encoded service account credentials.
* `GCP_PROJECT`: String with GCP project id.
* `BQ_QUERY`: Base64 encoded string with the query to run.

Build the container image using Docker:

```
docker build -t stoix/getting-started/bq-runner:latest .
```

Running the container image locally, replace values for environment variables:

```
docker run --rm -it \
  -e GCP_SERVICE_ACCOUNT_CREDENTIALS=<...> \
  -e GCP_PROJECT=<...> \
  -e BQ_QUERY=<...> \
  stoix/getting-started/bq-runner:latest
```

Running the tests locally, pre-requisite is Poetry (https://python-poetry.org/):

```
poetry install
poetry run tox
```

## ingest-data

Job for moving data from Google Cloud Storage to BigQuery.

Environment variables:

* `GCS_BUCKET_NAME`: String with name of bucket holding CSV files, e.g: `bucket-name`.
* `GCS_BUCKET_PREFIX`: String with prefix to filter files in bucket.
* `GCP_SERVICE_ACCOUNT_CREDENTIALS`: Base64 encoded service account credentials.
* `GCP_PROJECT`: String with GCP project id.
* `BQ_TABLE`: String with full identifier of table, e.g: `project.dataset.table`.

Build the container image using Docker:

```
docker build -t stoix/getting-started/ingest-data:latest .
```

Running the container image locally, replace values for environment variables:

```
docker run --rm -it \
  -e GCS_BUCKET_NAME=<...> \
  -e GCS_BUCKET_PREFIX=<...> \
  -e GCP_SERVICE_ACCOUNT_CREDENTIALS=<...> \
  -e GCP_PROJECT=<...> \
  -e BQ_TABLE=<...> \
  stoix/getting-started/ingest-data:latest
```

Running the tests locally, pre-requisite is Poetry (https://python-poetry.org/):

```
poetry install
poetry run tox
```
