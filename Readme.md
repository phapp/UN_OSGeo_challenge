# Instructions

## Using Poetry Python

- [Install Poetry Python](https://python-poetry.org/docs/#installation)
- Run: `poetry shell`
- Inside the opened environment, run `make html`

```bash
$ poetry shell
.venv> make html
```

Sometimes it is necessary to clean the build folder:

```bash
$ poetry shell
.venv> make clean
```

## Using pip

- Activate your virtual environment
- Execute `pip install -r requirements.txt`
- Inside the opened environment, run `make html`
