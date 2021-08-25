"""Main entry for ingest-data."""

import base64
import json
import os
import sys
from collections import namedtuple
from google.cloud import storage
from google.cloud import bigquery
from extract.gcs import GCSExtractor
from job import job
from load.bq import BQLoader

Config = namedtuple(
    "Config",
    [
        "bucket_name",
        "bucket_prefix",
        "credentials",
        "project",
        "table",
    ],
)


def main():
    """Main entry for setting up our job and then directly calls the job function."""
    config = get_config()

    storage_client = storage.Client.from_service_account_info(
        config.credentials, project=config.project
    )
    extractor = GCSExtractor(
        bucket_name=config.bucket_name,
        client=storage_client,
        prefix=config.bucket_prefix,
    )

    bq_client = bigquery.Client.from_service_account_info(
        config.credentials, project=config.project
    )
    loader = BQLoader(client=bq_client, table=config.table)

    job(extract=extractor.csv, load=loader.load)


def get_config() -> Config:
    """Reads environment variables to a Config object."""
    gcs_bucket_name = env_require("GCS_BUCKET_NAME")
    gcs_bucket_prefix = env_require("GCS_BUCKET_PREFIX")
    gcp_service_account_credentials_base64 = env_require(
        "GCP_SERVICE_ACCOUNT_CREDENTIALS"
    )
    gcp_service_account_credentials_text = base64.b64decode(
        gcp_service_account_credentials_base64
    ).decode("utf-8")
    gcp_service_account_credentials = json.loads(gcp_service_account_credentials_text)
    project = env_require("GCP_PROJECT")
    bq_table = env_require("BQ_TABLE")

    return Config(
        bucket_name=gcs_bucket_name,
        bucket_prefix=gcs_bucket_prefix,
        credentials=gcp_service_account_credentials,
        project=project,
        table=bq_table,
    )


def env_require(key: str) -> str:
    """Enforces that we have the requested environment variable."""
    value = os.environ.get(key)
    if value is None:
        print(f"Missing environment variable {key}")
        sys.exit(1)
    return value


if __name__ == "__main__":
    main()
