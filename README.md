# Week 1 Lecture Exercises

This repository contains lecture exercises for Week 1 of Chem 274A. 
To complete the Lecture Exercises, you should clone this repository, 
complete the exercise in each Python module (a Python module is a file that ends in `.py`) and push your work to GitHub.

These exercises are tested with [pytest](https://docs.pytest.org/en/stable/). When you push to GitHub, they will be autograded with pytest.

## Making an environment

First make sure you have a Python environment with `pytest` installed.
If you made an environment in Chem 280 that had `pytest`, you may use that.
If you need to make an environment you can use the commands below to create and activate an environment:

```bash
conda create --name chem274a conda-forge::python
conda activate chem274a
```

After activating, you can make sure that `pytest` is installed:

```bash
conda install conda-forge::pytest
```

The environment is active when `(chem274a)` appears at the beginning of your
terminal prompt. Run `conda deactivate` when you are finished working.

## Complete the exercises

Edit only the exercise file.

Do not modify files in `tests/`, `.github/scripts/`, or `.github/workflows/`.
Those files define how your work is checked.

## Run the tests locally

Run the complete test suite from the repository directory:

```bash
pytest -v
```

The starter code is intentionally incomplete, so tests will fail at first.
Work through the errors one exercise at a time.

To run one exercise's tests, use one of these commands:

```bash
pytest -v tests/test_M00.py::test_00_01
pytest -v tests/test_M01.py::test_01_01
pytest -v tests/test_M01.py::test_01_02
pytest -v tests/test_M01.py::test_01_03
pytest -v -k test_01_04
```

The last command runs both test cases for exercise `01_04`.

When all exercises are correct, the full test suite should report six passing
tests. The autograder groups those tests into five exercises worth one point
each.

## Submit your work

Review your changes, commit them, and push your branch to GitHub:

```bash
git status
git add **list the files you want to add here"
git commit -m "YOUR COMMIT MESSAGE HERE"
git push
```

If a test passes locally but fails on GitHub, confirm that you committed and
pushed the latest version of every exercise file.
