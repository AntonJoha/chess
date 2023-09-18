#!/usr/bin/env bash

python3 -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
python3 -m flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
