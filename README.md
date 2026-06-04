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
