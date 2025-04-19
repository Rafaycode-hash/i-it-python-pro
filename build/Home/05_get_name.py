def get_name():
    name = input("Please enter your name: ")
    return name

def greet_user(name):
    print(f"Hello, {name}! Welcome to the program.")

def main():
    user_name = get_name()
    greet_user(user_name)

if __name__ == "__main__":
    main()