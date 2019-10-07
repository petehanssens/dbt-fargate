#!/bin/bash
set -euo pipefail

gcp_creds=$gcp_creds
echo $gcp_creds > creds.txt

base64 --decode creds.txt > ./gcp-creds.json

dbt run --target dev || true
