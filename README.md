<p align="center">
  <img src="assets/advent-of-code.svg" alt="A cozy winter night with a glowing Christmas tree, a star, a mug of cocoa and falling snow" width="640">
</p>

# Advent of Code

Solutions to the [Advent of Code](https://adventofcode.com) puzzles, written as [marimo](https://marimo.io) notebooks with one notebook per day.

## Layout

```
src/aoc/                shared helper code
assets/                README images
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
uv run marimo edit notebooks/2015/2015_day_01.py
```