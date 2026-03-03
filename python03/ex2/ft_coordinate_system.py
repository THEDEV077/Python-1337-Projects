import math


def calculate_dist(arguments: tuple) -> float:
    return math.sqrt((arguments[0] - 0)**2
                     + (arguments[1] - 0)**2 + (arguments[2] - 0) ** 2)


def parsing(text: str) -> tuple:
    try:
        arguments: list[str] = text.split(",")
        if len(arguments) != 3:
            raise Exception("you need to give 3 arguments")
        return tuple(int(arg) for arg in arguments)
    except ValueError as e:
        mess, = e.args
        print(f"Error parsing coordinates: {mess}")
        print(f'Error details - Type: ValueError, Args: {e.args}')


def unpacking(arguments: tuple) -> None:
    x, y, z = arguments
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    try:
        print("=== Game Coordinate System ===\n")
        arguments: tuple = (10, 20, 5)
        print("Position created:", arguments)
        dist: float
        dist = calculate_dist(arguments)
        print(f"Distance between (0, 0, 0) and {arguments}: {dist:.2f}\n")

        print('Parsing coordinates: "3,4,0"')
        arguments: tuple = parsing("3,4,0")
        print(f"Parsed position: {arguments}")
        dist = calculate_dist(arguments)
        print(f"Distance between (0, 0, 0) and {arguments}: {dist:.1f}\n")

        print('Parsing invalid coordinates: "abc,def,ghi"')
        parsing("abc,def,ghi")

        unpacking(arguments)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
