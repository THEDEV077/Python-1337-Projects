import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    arguments: list = sys.argv
    if len(arguments) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(arguments) > 1:
        print(f"Arguments received: {len(arguments) - 1}")
        i: int = 1
        while (i < len(arguments)):
            print(f"Argument {i}: {arguments[i]}")
            i += 1
    print(f"Total arguments: {len(arguments)}\n")
