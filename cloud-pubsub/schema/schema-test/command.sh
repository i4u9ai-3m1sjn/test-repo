#!/bin/bash
gcloud pubsub schemas create test-schema \
  --type=avro \
  --definition-file=test_schema_difinition_file.json

