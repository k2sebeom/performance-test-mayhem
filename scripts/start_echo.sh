#!/bin/bash

cd echo
BINARY_PATH="./bin/main"

if [ ! -f "$BINARY_PATH" ]; then
    echo "Release binary not found. Building the project..."
    go build -o bin/main main.go
fi

echo "Running the server..."
$BINARY_PATH
