def check_stock(shop_items, item):
    if item in shop_items:
        print(f"The stock for {item} is {shop_items[item]}.")
    else:
        print(f"{item} is not available in stock.")

def main():
    shop_items = {
        "T-shirt": 50,
        "Jeans": 30,
        "Shoes": 20
    }
    check_stock(shop_items, "Jeans")
    check_stock(shop_items, "Hats")

if __name__ == "__main__":
    main()
