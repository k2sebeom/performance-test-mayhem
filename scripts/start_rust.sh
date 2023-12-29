#!/bin/bash

cd rust
BINARY_PATH="./target/release/helloworld"

if [ ! -f "$BINARY_PATH" ]; then
    echo "Release binary not found. Building the project..."
    cargo build --release
fi

echo "Running the server..."
$BINARY_PATH
