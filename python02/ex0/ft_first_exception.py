def check_temperature(temp_str: str) -> int | None:
    print("Testing temperature:", temp_str)
    try:
        re: bool = True
        temp_int: int = int(temp_str)
        if temp_int < 0:
            re = False
            raise ValueError(
                f"Error: {temp_int}°C is too cold for plants (min 0°C)\n")
        if temp_int > 40:
            re = False
            raise ValueError(
                f"Error: {temp_int}°C is too hot for plants (max 40°C)\n")
    except ValueError as e:
        if re:
            print(f"Error: '{temp_str}' is not a valid number\n")
        else:
            print(e)
    else:
        print(f"Temperature {temp_int}°C is perfect for plants!\n")
        return temp_int


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(f"Caught an error: {e}")
