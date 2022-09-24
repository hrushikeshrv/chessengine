# Chess Engine
[![Documentation Status](https://readthedocs.org/projects/chessengine/badge/?version=latest)](https://chessengine.readthedocs.io/en/latest/?badge=latest)  
A chess engine written in Python with no dependencies. All contributions welcome.

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
pip install chessengine
```
Start a game -  
```bash
python -m chessengine.play 
```