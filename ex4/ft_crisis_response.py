def access_archive(filename: str) -> None:
    if filename == "../data-generator-tools/standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as file:
            content = file.read().strip()

        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception:
        print("RESPONSE: Unexpected system anomaly")
        print("STATUS: Crisis handled, system stability maintained\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    archives = [
        "../data-generator-tools/lost_archive.txt",
        "../data-generator-tools/classified_vault.txt",
        "../data-generator-tools/standard_archive.txt"
    ]

    for archive in archives:
        access_archive(archive)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
