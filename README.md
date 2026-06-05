# Python Virtual Environment and Poetry Example

This project demonstrates two approaches for managing Python dependencies:

1. Traditional virtual environment (`venv`) with `requirements.txt`
2. Poetry dependency management

The sample application uses the `requests` library to call a public REST API.

## Project Files

```text
example.py
requirements.txt
pyproject.toml
README.md
```

## Running with venv

### Create a virtual environment

Windows:

```bash
python -m venv venv
```

### Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Execute the application

```bash
python example.py
```

---

## Running with Poetry

### Install Poetry

```bash
pip install poetry
```

Verify installation:

```bash
poetry --version
```

### Install project dependencies

```bash
poetry install
```

Poetry automatically:

* Creates an isolated virtual environment
* Installs dependencies from `pyproject.toml`
* Generates and maintains `poetry.lock`

### Run the application

Without activating the environment:

```bash
poetry run python example.py
```

Or enter the Poetry environment first:

```bash
poetry shell
python example.py
```

### View Poetry virtual environment

poetry env info
```

---

## Comparison

| Feature             | venv + pip       | Poetry         |
| ------------------- | ---------------- | -------------- |
| Virtual Environment | Manual           | Automatic      |
| Dependency File     | requirements.txt | pyproject.toml |
| Dependency Locking  | Optional         | poetry.lock    |
| Package Management  | Basic            | Advanced       |

## Output

```text
API Response:
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
```
