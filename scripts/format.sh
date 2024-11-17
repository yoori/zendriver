#!/usr/bin/env bash

set -e
set -x

uv run ruff check zendriver --fix
uv run ruff format zendriver
