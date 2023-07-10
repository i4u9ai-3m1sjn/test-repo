#!/bin/bash
gcloud pubsub schemes create test-scheme \
  --type=avro \
  --definition-file=./test_scheme_difinition_file.json

