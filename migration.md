# Migration instructions

Temporary document. Delete it when the migration is finished.

Source: `repos/public/notebooks/notebooks/advent_of_code/` (and `data/advent_of_code/`).
Target: `notebooks/<year>/<year>_day_NN.py` and `data/<year>/<year>_day_NN.txt` in this repo.

## Process

1. **Copy the whole source notebook** with `cp`. Do not retype or paste code.
2. **Trim the copy** with `sed -i` line ranges so that only the header and the target puzzle's block remain. Keep the `if __name__ == "__main__":` footer.
3. **Verify the block is unchanged** with `cmp`, comparing the source line range with the kept range in the copy.
4. **Copy the input file** into `data/<year>/`. Use `cp`, not `mv`, because the source repo still needs it.
5. **Make only the allowed edits** (see below).
6. **Run the notebook as a script**: `uv run python notebooks/<year>/<file>.py`. It must exit with code 0. The asserts check the answers.
7. **Run the checks**: `uv run ruff check .`, `uv run pyright`, `uv run ty check`, `uv run deptry .`, and `uv run docstring_tailor format` (the `format-docstrings` make target). The make targets are `make deptry`, `make ruff`, `make format-docstrings`, `make pyright`, and `make ty`.
8. **Export the Jupyter notebooks** with `make ipynb`. This writes a `.ipynb` next to every marimo notebook, in top-down order. The export must use `--sort top-down`, because marimo's default topological sort moves the imports cell to the top.
9. **Add an entry** to the log below.

## Allowed edits in the copied file

- **Imports at the top:** all imports go in the header imports cell, which is the first code cell after the title. Stdlib, third-party and `aoc` imports are grouped there. Puzzle cells never import. `from advent_of_code_utils import read_data` becomes `from aoc.utils import read_data`. Remove imports that are no longer used.
- **No Constants section.** Remove the `## Constants` markdown cell and the `DATA_DIRECTORY_PATH` cell, including any commented-out lines in it.
- **Full data path.** Read inputs with a plain string, for example `file_path="data/2015/2015_day_01.txt"`. Do not use `DATA_DIRECTORY_PATH`.
- **Store every exercise result in a variable, then assert the hardcoded answer.** For example:

  ```python
  final_floor_number = exercise_1_1_find_the_final_floor_number(
      floor_instructions=floor_instructions
  )

  assert final_floor_number == 232
  ```

  Do not call an exercise function inside an `assert` expression. This applies to example inputs too.
- **No `print` statements.** Replace them with the variable and assert pattern above.
- **Helper functions** used only by this puzzle move into the notebook. Place them in the `Part N - Solution` section, in their own cell that returns the function, for example `return (name,)`. Remove the function from `src/aoc/utils.py` and update its module docstring if needed.
- **Dependencies** used by the solution go in `pyproject.toml` via `uv add`. Pin them to the versions the source repo locks (see its `uv.lock`). Pulp 4.x breaks Day 10, so use `pulp>=3.3.0,<4`.

Leave the solution code as it is. The exception is formatting: running `ruff format` and `docstring_tailor format` on the migrated file is allowed, since they only change layout and docstrings. Any other change to the solution code must be recorded in the log entry for that puzzle.

## Gotchas

- Cell functions are always named `_`, for example `def _(mo):`. Never give a cell function a name with an underscore prefix, such as `def _exercise_8_1_...(mo):`. Helper functions defined inside a cell can have a leading underscore when they are private, like `_get_wire_value`.
- Marimo rejects the same name defined in two cells (`MultipleDefinitionError`). Put shared imports in the header imports cell and pass them as parameters to the cells that need them.
- Running the file as a script is the test. The asserts check the examples and the real answers. A failing assert means the migration changed something.
- After any change to `pyproject.toml`, run `uv sync`.
- Remove dependencies that are no longer used. deptry flags unused ones, for example `numpy` after Day 10 was migrated.
- Some source notebooks are missing day headings (for example the 2025 Day 10 factory section). Decide whether to add them while migrating.
- The makefile's committed version uses CRLF line endings, and the working copy uses LF. Check line endings before committing.
- The files `__marimo__/` appear next to notebooks when marimo runs. They are gitignored.

## Open questions

- The 2025 dev notebook (`advent_of_code_2025_dev.py`).
- Whether the source repo keeps its copies once migration is done, which would leave two sources of truth.

## Log

| Puzzle | Status | Answer(s) | Changes beyond the allowed edits |
| --- | --- | --- | --- |
| 2015 day 01 | Migrated | 232, 1783 | None |
| 2015 day 02 | Migrated | Part 1: 1588178. Part 2: 3783758 | Part 2 function renamed from `exercise_2_1_find_total_feet_of_ribbon` to `exercise_2_2_find_total_feet_of_ribbon` (the source name had `2_1`). |
| 2015 day 03 | Migrated | Part 1: 2565. Part 2: 2639 | None |
| 2015 day 04 | Migrated | Part 1: 346386. Part 2: 9958218 | None |
| 2015 day 05 | Migrated | Part 1: 255. Part 2: 55 | None |
| 2015 day 06 | Migrated | Part 1: 377891. Part 2: 14110788 | Both solvers got an `else` branch that raises `ValueError` for instructions that are neither 4 nor 5 parts, so pyright can tell `action` is always set. Malformed input now fails with a clear error instead of a `NameError`. Added the `Point` namedtuple helper cell and `numpy` as a dependency. |
| 2015 day 07 | Migrated | Part 1: 956. Part 2: 40149. Example asserts the full wire dict | `exercise_7_1_find_signal_value` return annotation changed from `dict[str, int]` to `dict[str, int \| None]` to match the dict it builds, so pyright and ty pass. The example's `print` became an assert on the expected dict. |
| 2015 day 08 | Migrated | Part 1: 1350. Part 2: 2085 | None |
| 2015 day 09 | Migrated | Part 1: 207. Part 2: 804 | None |
| 2015 day 10 | Migrated | Part 1: 252594 (length after 40 iterations). Part 2: 3579328 (length after 50 iterations) | None |
| 2015 day 11 | Unsolved (migrated as-is) | None. Part 2 not written | Migrated as the source has it. The solver never returns a value and still prints each step, so the call cell asserts `next_password is None` as a placeholder. The solver's return annotation changed from `str` to `None` to match what it does, so pyright and ty pass. Revert to `-> str` and assert the real password once the solver is finished. |
| 2015 day 12 | Migrated | Part 1: 191164. Part 2: 87842 | None |
| 2015 day 14 | Migrated | Part 1: 2660. Part 2: 1256 | The plot function keeps its return annotation (`-> go.Figure`) with an inline `# pyright: ignore[reportInvalidTypeForm]`, because marimo passes imports into cells as variables and pyright rejects those in a type expression. `plotly` added as a dependency (`>=6.5.0,<7`). The Kaleido 0.2.1 deprecation warning is suppressed with `warnings.catch_warnings()` around the `to_image` call only, since upgrading needs Chrome. Each plot is split into two cells: the first shows the interactive figure inside a collapsed `mo.accordion` for development (so the image isn't shown twice in marimo), and the second shows the same figure as a base64 PNG in markdown, so the `.ipynb` export has an image GitHub can render. The source cells called the plot function without returning its figure, so nothing displayed. The final bare `figure_14_*` line is flagged by pyright as an unused expression, so it has an inline `# pyright: ignore[reportUnusedExpression]`. |
| 2015 day 15 | Migrated | Part 1: recipe `21 Sugar, 5 Sprinkles, 31 Candy, 43 Chocolate`, score 222870. Part 2: recipe `21 Sugar, 8 Sprinkles, 26 Candy, 45 Chocolate`, score 117936 | The `dataclass` import moved from the `Ingredient` cell to the header imports, and the unused `fields` import was dropped. Both parts assert the recipe and the score. |
| Dependency note | kaleido | `kaleido==0.2.1` added so plotly can render PNG images. kaleido 1.x needs a system Chrome, so the 0.2.1 release (which bundles Chromium) is pinned. deptry ignores it for DEP002 in `pyproject.toml`, since plotly loads it at runtime. | |
| 2025 day 10 | Migrated | Part 1: 578 (both approaches). Part 1 example: 7 (both approaches). Part 2 example: 33. Part 2: 20709 | Solver sentinel changed from `float('inf')` to `sys.maxsize`; `pulp.value(variable)` replaced with `variable.value()` and a `None` check added; unused variable removed; `sys` imported in the header cell |
