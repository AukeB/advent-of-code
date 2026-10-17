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

## Puzzle overview

| Puzzle | 2015 | 2025 |
| --- | --- | --- |
| 1 | ✅ | ✅ |
| 2 | ✅ | ✅ |
| 3 | ✅ | ✅ |
| 4 | ✅ | ✅ |
| 5 | ✅ | ✅ |
| 6 | ✅ | ✅ |
| 7 | ✅ | ✅ |
| 8 | ✅ | ✅ |
| 9 | ✅ | ✅ |
| 10 | ✅ | ✅ |
| 11 |  | ✅ |
| 12 | ✅ |  |
| 13 |  | ➖ |
| 14 | ✅ | ➖ |
| 15 | ✅ | ➖ |
| 16 |  | ➖ |
| 17 |  | ➖ |
| 18 |  | ➖ |
| 19 |  | ➖ |
| 20 |  | ➖ |
| 21 |  | ➖ |
| 22 |  | ➖ |
| 23 |  | ➖ |
| 24 |  | ➖ |
| 25 |  | ➖ |

## Algorithms and tags (2025)

| Puzzle | Related to algorithm? | Description / tags |
| --- | --- | --- |
| 1 | - | Modular arithmatic, circular motion |
| 2 | - | Modular arithmetic, string processing, pattern matching |
| 3 | - | Arithmetic |
| 4 | Flood fill algorithm | Grid-based traversal, iterative propagation |
| 5 | - | Interval checking, linear scan |
| 6 | - | Matrix traversal, reverse computation, basic arithmatic |
| 7 | DFS / BFS | Tree traversal, graph simulation |
| 8 | MST / Kruskal's Algorithm | MST, graph |
| 9 | Graham's scan / Jarvis march | Geometry, grid-based analysis, convex hulls |
| 10 | Simplex algorithm / Branch and Bound | Linear algebra, linear optimization, integer linear programming |
| 11 | DFS | Graph traversal, pathfinding, directed graphs, constraint-based traversal, resursive search |
| 12 | Bin packing / tiling problem | Bin packing problem, polyomino fitting problem, tiling problem, backtracking, CSP |
