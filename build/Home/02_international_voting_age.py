def check_voting_age(country, age):
    voting_ages = {"USA": 18, "India": 18, "UK": 18, "Australia": 18, "China": 18}
    if country in voting_ages:
        if age >= voting_ages[country]:
            print(f"You are eligible to vote in {country}.")
        else:
            print(f"You are not eligible to vote in {country}.")
    else:
        print(f"Voting age information not available for {country}.")

def main():
    country = input("Enter your country: ")
    age = int(input("Enter your age: "))
    check_voting_age(country, age)

if __name__ == "__main__":
    main()
