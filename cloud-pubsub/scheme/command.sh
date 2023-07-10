#!/bin/bash
gcloud pubsub schemas commit test-scheme \
  --type=arvo \
  --definition-file=./test_scheme_difinition_file.json

