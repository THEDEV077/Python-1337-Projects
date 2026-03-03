def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'\n")
    print("Testing KeyError...")
    try:
        d = {}
        d["missing_plant"]
    except KeyError:
        print(r"Caught KeyError: 'missing\_plant'" + "\n")
    print("Testing multiple errors together...")
    try:
        int("abc")
        1 / 0
        f = open("missing.txt", "r")
        f.close()
    except (
        ValueError, ZeroDivisionError, FileNotFoundError
    ):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    try:
        test_error_types()
    except Exception as e:
        print(f"Caught an error: {e}")
