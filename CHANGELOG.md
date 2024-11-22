# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

### Added

### Changed

### Removed

## [0.2.0] - 2024-11-17

### Changed

- Updated CDP models @stephanlensky

## [0.1.5] - 2024-11-17

### Fixed

- Reverted non-functional fixes for mypy linting errors (oops) @stephanlensky

## [0.1.4] - 2024-11-17

### Fixed

- Fixed a large number of mypy linting errors (should not result in any functional change) @stephanlensky

### Added

- Added `zendriver.__version__` attribute to get current package version at runtime @stephanlensky

## [0.1.3] - 2024-11-12

### Added

- Added support for `DOM.scrollableFlagUpdated` experimental CDP event. @michaellee94

## [0.1.2] - 2024-11-11

### Fixed

- Pinned requirement `websockets<14`, fixing the `AttributeError: 'NoneType' object has no attribute 'closed'` crash which occurs on the latest version of `websockets`. @stephanlensky
- Fixed incorrect `browser.close()` method in examples and documentation -- the correct method is `browser.stop()`. @stephanlensky
- Fixed `atexit` handler to correctly handle async `browser.stop()` method. @stephanlensky

## [0.1.1] - 2024-10-29

### Added

- Support for Python 3.10 and Python 3.11. All versions >=3.10 are now supported. @stephanlensky

## [0.1.0] - 2024-10-20

Initial version, forked from [ultrafunkamsterdam/nodriver@`1bb6003`](https://github.com/ultrafunkamsterdam/nodriver/commit/1bb6003c7f0db4d3ec05fdf3fc8c8e0804260103) with a variety of improvements.

### Fixed

- `Browser.set_all` cookies function now correctly uses provided cookies @ilkecan
- "successfully removed temp profile" message printed on exit is now only shown only when a profile was actually removed. Message is now logged at debug level instead of printed. @mreiden @stephanlensky
- Fix crash on starting browser in headless mode @ilkecan
- Fix `Browser.stop()` method to give the browser instance time to shut down before force killing @stephanlensky
- Many `ruff` lint issues @stephanlensky

### Added

- Support for linting with `ruff` and `mypy`. All `ruff` lints are fixed in the initial release, but many `mypy` issues remain to be fixed at a later date. @stephanlensky
- `py.typed` marker so importing as a library in other packages no longer causes `mypy` errors. @stephanlensky

### Changed

- Project is now built with [`uv`](https://github.com/astral-sh/uv). Automatically install dependencies to a venv with `uv sync`, run commands from the venv with `uv run`, and build the project with `uv build`. See the official [`uv` docs](https://docs.astral.sh/uv/) for more information. @stephanlensky
- Docs migrated from sphinx to [mkdocs-material](https://squidfunk.github.io/mkdocs-material/). @stephanlensky
- `Browser.stop()` is now async (so it must be `await`ed) @stephanlensky

### Removed

- Twitter account creation example @stephanlensky
