if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    f = None
    try:
        name = "new_discovery.txt"
        print(f"Initializing new storage unit: {name}")
        f = open(name, "w")
        print("Storage unit created successfully...\n")
        f.write("[ENTRY 001] New quantum algorithm discovered\n")
        f.write("[ENTRY 002] Efficiency increased by 347%\n")
        f.write("[ENTRY 003] Archived by Data Archivist trainee")
        print("Inscribing preservation data...")
        print("[ENTRY 001] New quantum algorithm discovered")
        print("[ENTRY 002] Efficiency increased by 347%")
        print("[ENTRY 003] Archived by Data Archivist trainee")
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{name}' ready for long-term preservation.")
    except Exception as e:
        print("error:", e)
    finally:
        if f is not None:
            f.close()
