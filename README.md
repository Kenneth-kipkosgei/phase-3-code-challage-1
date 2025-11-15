# Magazine-Author-Article Exercise

Small Python project modelling Authors, Magazines and Articles for a learning exercise.

**Author:** Kenneth Kipkosgei

## Requirements
- Python 3.13 (see `Pipfile`)
- pipenv (optional but recommended)

## Install

Use pipenv to create the virtualenv and install dependencies:

```bash
pipenv install
```

## Run tests

Run the test suite with:

```bash
pipenv run pytest -v
```

All tests should pass. The test suite uses a conftest fixture to isolate global state between tests.

## Notes
- The project keeps simple in-memory lists (`all_articles`, `all_magazines`, `all_authors`) for the exercise.
- Article title validation accepts 2–50 character titles to allow short titles used in tests (e.g. "AI").
