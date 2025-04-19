def get_first_element(data):
    if len(data) > 0:
        return data[0]
    else:
        return "The list is empty."

def main():
    data = [10, 20, 30, 40, 50]
    
    print(f"List: {data}")
    first_element = get_first_element(data)
    
    if isinstance(first_element, str):
        print(first_element)  # Error message if list is empty
    else:
        print(f"The first element is: {first_element}")

if __name__ == "__main__":
    main()
