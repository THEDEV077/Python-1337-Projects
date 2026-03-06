if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as f:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            text = f.read()
            print(text)
        with open("security_protocols.txt", "w") as f:
            print("\nSECURE PRESERVATION:")
            f.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion")
    except Exception as e:
        print("Error:", e)
    finally:
        print("\nAll vault operations completed with maximum security.")
