def get_last_element(data):
    if len(data) > 0:
        return data[-1]
    else:
        return "The list is empty."

def main():
    data = [10, 20, 30, 40, 50]
    
    print(f"List: {data}")
    last_element = get_last_element(data)
    
    if isinstance(last_element, str):
        print(last_element)  # Error message if list is empty
    else:
        print(f"The last element is: {last_element}")

if __name__ == "__main__":
    main()
