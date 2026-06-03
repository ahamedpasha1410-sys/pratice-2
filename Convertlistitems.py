values = ["10", "20", "abc", "40"]

for item in values:
    try:
        print(int(item))

    except ValueError:
        print(f"'{item}' is not a valid number")
