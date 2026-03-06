def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")

    print("Vault connection established with failsafe protocols")
    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", 'r') as vault:
            for line in vault:
                print(line)

        print("SECURE PRESERVATION:")

        with open("new_security_protocols.txt", 'w') as vault:
            vault.write("[CLASSIFIED] New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")
        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()
