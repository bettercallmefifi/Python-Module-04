def main() -> None:
    file_name = "../data-generator-tools/ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file_name}")

    try:
        file = open(file_name, "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")

        content = file.read()
        print(content.strip())

        file.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
