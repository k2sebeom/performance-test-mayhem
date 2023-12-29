#!/bin/bash

cd fastapi
uvicorn main:app --port 8000 --workers 10
