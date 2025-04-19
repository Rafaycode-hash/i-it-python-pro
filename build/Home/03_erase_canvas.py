def erase_item_from_list(lst, item_to_remove):
    try:
        lst.remove(item_to_remove)
        print(f"{item_to_remove} has been removed from the list.")
    except ValueError:
        print(f"{item_to_remove} is not in the list.")

def main():
    items = []

    n = int(input("How many items do you want to add to your list? "))
    
    for i in range(n):
        item = input(f"Enter item {i+1}: ")
        items.append(item)

    print("\nCurrent List:", items)
    item_to_remove = input("Enter the item to remove from the list: ")
    
    erase_item_from_list(items, item_to_remove)
    
    print("Updated List:", items)

if __name__ == "__main__":
    main()
