import requests

def main():
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/1",
            timeout=10
        )
        response.raise_for_status()

        print("API Response:")
        print(response.json())

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.ConnectionError:
        print("Connection error")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())
