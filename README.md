# Advent of Code

Solutions to the [Advent of Code](https://adventofcode.com) puzzles, written as [marimo](https://marimo.io) notebooks with one notebook per day.

## Layout

```
aoc/                    shared helper code
notebooks/<year>/       one marimo notebook per puzzle day
data/<year>/            puzzle inputs (not tracked in git)
```

## Usage

Install dependencies with `uv sync`, then start marimo:

```
uv run marimo
```

To open a specific notebook, pass its path:

```
uv run marimo edit notebooks/2025/2025_day_01.py
```
