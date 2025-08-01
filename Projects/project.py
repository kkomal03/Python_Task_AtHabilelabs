# Coffee machine
# 1. Water : 100 L
# 2. Milk: 100 L
# 3. coffee: 50 G
# 1. Cappucino  10- W 10-M 3GM-C.  70
# 2. Mocha 15-W 7-M 7GM-C.  80
# 3. Latte 5L-W 15L-M 10GM-C 30

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
        print("Menu: Cappuccino, Mocha, Latte")
        ch = input("Enter your choice or off : ")
        if ch == "off":
            print("Off the machine.")
            break
        if ch in details:
            make_coffee(ch)
            product_list()
            break
        else:
            print("Not In MenuList")

coffee_machine()
