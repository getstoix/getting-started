import os
import sys
from google.cloud import bigquery
from bq import BQRunner
import base64
import json
from collections import namedtuple

Config = namedtuple(
    "Config",
    [
        "credentials",
        "project",
        "query",
    ],
)


def main():
    """Main entry for setting up our job and then directly calls the job function."""
    config = get_config()

    bq_client = bigquery.Client.from_service_account_info(
        config.credentials, project=config.project
    )
    runner = BQRunner(client=bq_client)
    runner.run(config.query)


def get_config() -> Config:
    """Reads environment variables to a Config object."""
    gcp_service_account_credentials_base64 = env_require(
        "GCP_SERVICE_ACCOUNT_CREDENTIALS"
    )
    gcp_service_account_credentials_text = base64.b64decode(
        gcp_service_account_credentials_base64
    ).decode("utf-8")
    gcp_service_account_credentials = json.loads(gcp_service_account_credentials_text)
    project = env_require("GCP_PROJECT")
    query_base64 = env_require("BQ_QUERY")
    query = base64.b64decode(query_base64).decode("utf-8")

    return Config(
        credentials=gcp_service_account_credentials,
        project=project,
        query=query,
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
