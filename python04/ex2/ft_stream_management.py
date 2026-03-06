import sys


if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
        archivist = input("Input Stream active. Enter archivist ID: ")
        status = input("Input Stream active. Enter status report: ")

        message = f"\n[STANDARD] Archive status from {archivist}: {status}"
        print(message, file=sys.stdout)
        message = "[ALERT] System diagnostic: Communication channels verified"
        print(message, file=sys.stderr)
        message = "[STANDARD] Data transmission complete"
        print(message, file=sys.stdout)
        print("\nThree-channel communication test successful.")
    except (Exception, KeyboardInterrupt) as e:
        print(e, file=sys.stderr)
