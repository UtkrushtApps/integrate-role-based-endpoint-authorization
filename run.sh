#!/bin/bash
set -e
set -o pipefail

bash ./install.sh

echo "[run.sh] Dockerized FastAPI app should be running on http://localhost:8000/"
