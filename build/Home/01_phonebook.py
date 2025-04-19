def add_contact(phonebook, name, number):
    phonebook[name] = number
    print(f"Added {name} with number {number} to the phonebook.")

def main():
    phonebook = {}
    add_contact(phonebook, "Alice", "123-456-7890")
    add_contact(phonebook, "Bob", "987-654-3210")
    print("Phonebook:", phonebook)

if __name__ == "__main__":
    main()
