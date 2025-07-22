#!/bin/bash
set -e
set -o pipefail

# Build docker image and start container
DOCKER_IMAGE="fastapi-auth-app"
DOCKER_CONTAINER="fastapi-auth-container"

echo "[install.sh] Building Docker image..."
docker build -t $DOCKER_IMAGE .

if [ $(docker ps -a -q -f name=$DOCKER_CONTAINER) ]; then
    echo "[install.sh] Removing old container..."
    docker rm -f $DOCKER_CONTAINER
fi

echo "[install.sh] Starting Docker container..."
docker run -d --name $DOCKER_CONTAINER -p 8000:8000 $DOCKER_IMAGE

echo "[install.sh] Docker container is up and running."
