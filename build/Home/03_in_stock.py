# 03_in_stock.py

def check_stock():
    # Inventory list (aap chaho toh isay dictionary bhi bana sakte ho with quantities)
    inventory = ['milk', 'bread', 'eggs', 'butter', 'cheese', 'juice']

    print("Welcome to the inventory checker.")
    item = input("Enter the item you are looking for: ").lower()

    if item in inventory:
        print(f"Yes, {item} is in stock.")
    else:
        print(f"Sorry, {item} is not available right now.")

if __name__ == "__main__":
    check_stock()
