def shorten_list(data, length):
    return data[:length]

def main():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    print(f"Original List: {data}")
    
    length = int(input("Enter the number of elements to keep in the list: "))
    shortened_data = shorten_list(data, length)
    
    print(f"Shortened List: {shortened_data}")

if __name__ == "__main__":
    main()
