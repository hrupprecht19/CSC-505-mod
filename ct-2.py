# rupprecht_model.py
#!/usr/bin/env python3
# A simple script that collects model phases and prints a formatted summary.

def main():
    print("=== Project Model Builder ===")
    print("Enter the phases of your model.\n")

    phases = []

    # Ask how many phases the user wants to enter
    num_phases = int(input("How many phases does your model have? "))

    for i in range(1, num_phases + 1):
        print(f"\n--- Phase {i} ---")
        name = input("Enter phase name: ")
        description = input("Enter a short description: ")
        phases.append((name, description))

    print("\n=== MODEL SUMMARY ===")
    for idx, (name, desc) in enumerate(phases, start=1):
        print(f"Phase {idx}: {name} - {desc}")

    print("\nThank you! Your model summary is complete.")

if __name__ == "__main__":
    main()
