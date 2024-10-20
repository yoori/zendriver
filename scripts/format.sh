#!/bin/sh -e
set -x

ruff check zendriver --fix
ruff format zendriver
