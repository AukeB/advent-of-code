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

Any other change to the solution code must be recorded in the log entry for that puzzle.

## Gotchas

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
| 2015 day 02 | Migrated | Part 1: 1588178. Part 2: 3783758 | Part 2 function is named `exercise_2_1_find_total_feet_of_ribbon` in the source (the `2_1` should be `2_2`). Left as-is. |
| 2025 day 10 | Migrated | Part 1: 578 (both approaches). Part 1 example: 7 (both approaches). Part 2 example: 33. Part 2: 20709 | Solver sentinel changed from `float('inf')` to `sys.maxsize`; `pulp.value(variable)` replaced with `variable.value()` and a `None` check added; unused variable removed; `sys` imported in the header cell |
