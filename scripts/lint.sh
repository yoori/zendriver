#!/usr/bin/env bash

set -e
set -x

mypy zendriver
ruff check zendriver
ruff format zendriver --check
