def manipulate_list(data):
    # Adding elements
    data.append(50)  # Adding 50 at the end
    data.insert(2, 25)  # Inserting 25 at index 2
    print(f"List after adding elements: {data}")
    
    # Removing elements
    data.remove(25)  # Removing 25
    print(f"List after removing 25: {data}")
    
    # Sorting the list
    data.sort()
    print(f"List after sorting: {data}")
    
    # Reversing the list
    data.reverse()
    print(f"List after reversing: {data}")

def main():
    # Example list with some integers
    data = [10, 20, 30, 40]
    
    print(f"Original List: {data}")
    manipulate_list(data)
    
    print(f"Final List: {data}")

if __name__ == "__main__":
    main()
