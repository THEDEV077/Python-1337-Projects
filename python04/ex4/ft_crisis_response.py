def read_file(name: str) -> str:
    with open(name, "r") as f:
        text = f.read()
        return text


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        name: str = "lost_archive.txt"
        print(f"CRISIS ALERT: Attempting access to '{name}'...")
        print(read_file(name))
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except Exception as e:
        print("Error :", e)
    finally:
        print("STATUS: Crisis handled, system stable\n")

    try:
        name = "classified_vault.txt"
        print(f"CRISIS ALERT: Attempting access to '{name}'...")
        read_file(name)
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception as e:
        print("Error :", e)
    finally:
        print("STATUS: Crisis handled, security maintained\n")

    try:
        name = "standard_archive.txt"
        print(f"ROUTINE ACCESS: Attempting access to '{name}'...")
        read_file(name)
    except Exception as e:
        print("Error :", e)
    else:
        print(
            "SUCCESS: Archive recovered",
            "- ``Knowledge preserved for humanity''")
    finally:
        print("STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archives secure.")
