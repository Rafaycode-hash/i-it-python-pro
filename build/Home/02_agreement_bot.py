response = input("Do you agree? (yes/no): ").lower()

if response == "yes":
    print("You agreed.")
elif response == "no":
    print("You disagreed.")
else:
    print("Invalid response.")
