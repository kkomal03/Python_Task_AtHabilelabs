products = {
    "water": 100,
    "milk": 100,
    "coffee": 50
}

details = {
    "cappuccino": {
        "water": 10,
        "milk": 10,
        "coffee": 3,
        "price": 70
    },
    "mocha": {
        "water": 15,
        "milk": 7,
        "coffee": 7,
        "price": 80
    },
    "latte": {
        "water": 5,
        "milk": 15,
        "coffee": 10,
        "price": 30
    }
}

def product_list():
    print("\nCurrent Product Levels:")
    for item, quantity in products.items():
        print(f"{item.title()}: {quantity}")
    print()

def make_coffee(ch):
    drinks = details[ch]
    
    for item in ['water', 'milk', 'coffee']:
        if products[item] < drinks[item]:
            print(f"Not enough {item} to make {ch.title()}")
            return
    
    for item in ['water', 'milk', 'coffee']:
        products[item] -= drinks[item]
    
    print(f"{ch.title()} is ready!")

def coffee_machine():
    print("Welcome to the Coffee Machine!")
    product_list()
    
    while True:
        try:
            print("Menu: Cappuccino, Mocha, Latte")
            ch = input("Enter your choice or 'off' to exit: ").strip().lower()

            if ch == "off":
                print("Turning off the machine.")
                break
            
            if ch not in details:
                raise Exception("Invalid drink selection.")
        
        except Exception as e:
            print(f"Error: {e}")
        
        else:
            make_coffee(ch)
            product_list()
        
        finally:
            print("Thank You For Visit , Visit Again ! \n")

coffee_machine()
