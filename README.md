
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
=======
# Virtual Environment Example

This example demonstrates:

- Creating a Python virtual environment
- Installing dependencies using requirements.txt
- Running a Python script that uses a third-party library

## Create a Virtual Environment

```cmd
python -m venv venv
```

## Activate the Virtual Environment
```cmd
venv\Scripts\activate
```

## Install Dependencies
pip install -r requirements.txt
```

## Run the Example
python example.py
```
# Python venv + Poetry Demo

This project demonstrates two ways to manage Python dependencies:

1. Traditional virtual environment (`venv`)
2. Modern dependency manager (`Poetry`)

---

## Example Script

`example.py` fetches your public IP using the `requests` library.

---

# 1. Setup using venv (traditional way)

## Step 1: Create virtual environment

```bash
python -m venv venv

## How Execution Happens

1. A virtual environment is created using `python -m venv venv`.
2. The environment is activated.
3. Dependencies listed in `requirements.txt` are installed.
4. Running `python example.py` starts the script.
5. The script imports the `requests` library.
6. It sends an HTTP GET request to a sample API.
7. The JSON response is printed to the terminal.
8. Errors such as timeout, connection failures, and HTTP errors are handled gracefully.

## Deactivate the Environment

deactivate

```
