#!/bin/bash
set -x

sleep 5
bash -c 'uvicorn src.main:app --host 0.0.0.0 --port 8001 --reload'