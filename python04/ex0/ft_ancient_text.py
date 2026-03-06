if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    f = None
    try:
        name = "ancient_fragment.txt"
        print(f"Accessing Storage Vault: {name}")
        f = open(name, "r")
        print("Connection established...\n")
        text = f.read()
        print("RECOVERED DATA:")
        print(text)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except Exception as e:
        print("Error:", e)
    finally:
        if f is not None:
            f.close()
