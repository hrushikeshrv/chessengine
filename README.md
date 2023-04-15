# Chess Engine
[![Documentation Status](https://readthedocs.org/projects/chessengine/badge/?version=latest)](https://chessengine.readthedocs.io/en/latest/?badge=latest)
[![Formatting](https://github.com/hrushikeshrv/chessengine/actions/workflows/formatting.yml/badge.svg)](https://github.com/hrushikeshrv/chessengine/actions/workflows/formatting.yml)

A chess engine written in Python with no dependencies. All contributions welcome.

## Note
This project is in active development and you may encounter bugs, especially in the game loop and/or implementation of game rules.

## Contribution Guide
The contribution guide can be found on the [documentation page](https://chessengine.readthedocs.io/en/latest/contributing.html)

## Features
- Internal bitboard representation
- Alpha-beta pruned search
- Move generation API
- Opening book

## TODOs
- Move ordering for faster forward search
- Non-trivial board state evaluation using better heuristics

## Usage
Install using `pip` -
```bash
# macOS / Linux (could work on Windows)
python3 -m pip install -U chessengine

# Windows (the primary way)
py -3 -m pip install -U chessengine
```

Start a game with the computer -
```bash
chessengine play
```
or
```bash
python -m chessengine play
```

If you want to play against another player -
```bash
chessengine play -p
```
or
```bash
python -m chessengine play -p
```

## Developer Notes
This project uses the [black](https://black.readthedocs.io/en/stable/) linter for determining code style.
```bash
# Install black via pip.
python -m pip install black==22.10.0

# Format
black .
```

If you've forked this repository, consider **enabling GitHub Actions** to leverage the automatic pull request creation provided for resolving code formatting errors!