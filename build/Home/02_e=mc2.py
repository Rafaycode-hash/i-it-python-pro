def calculate_energy(mass):
    c = 299_792_458  # speed of light in meters per second
    energy = mass * c ** 2
    return energy

def main():
    try:
        mass = float(input("Enter mass in kilograms (kg): "))
        energy = calculate_energy(mass)
        print(f"Energy (E=mc^2) for mass {mass} kg is: {energy:.2e} joules")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
