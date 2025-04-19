def get_element_at_index(data, index):
    try:
        return data[index]
    except IndexError:
        return "Index is out of range."

def main():
    data = [10, 20, 30, 40, 50]
    
    print(f"List: {data}")
    
    index = int(input("Enter the index of the element you want to retrieve: "))
    element = get_element_at_index(data, index)
    
    print(f"The element at index {index} is: {element}")

if __name__ == "__main__":
    main()
