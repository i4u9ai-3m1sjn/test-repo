#!/bin/bash
gcloud pubsub schemas commit test-scheme \
  --type=avro \
  --definition-file=./test_scheme_difinition_file.json

