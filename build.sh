#!/bin/bash

set -e

# Install dependencies
pip install --upgrade pip

# Run format and lint checks
black .
flake8 .

echo "[Build] Completed successfully!"