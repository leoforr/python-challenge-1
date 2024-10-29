# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Set up order list
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the Variety Food Truck.")

# Continuous loop for ordering
place_order = True
while place_order:
    print("\nFrom which menu would you like to order? ")
    i = 1
    menu_items = {}

    # Print menu categories
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    menu_category = input("Type menu number: ")

    if menu_category.isdigit() and int(menu_category) in menu_items.keys():
        menu_category_name = menu_items[int(menu_category)]
        print(f"You selected {menu_category_name}")
        print(f"What {menu_category_name} item would you like to order?")
        i = 1
        menu_items = {}
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        
        for key, value in menu[menu_category_name].items():
            if isinstance(value, dict):
                for key2, value2 in value.items():
                    num_item_spaces = 24 - len(key + " - " + key2)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key} - {key2}{item_spaces} | ${value2:.2f}")
                    menu_items[i] = {
                        "Item name": key + " - " + key2,
                        "Price": value2
                    }
                    i += 1
            else:
                num_item_spaces = 24 - len(key)
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key}{item_spaces} | ${value:.2f}")
                menu_items[i] = {
                    "Item name": key,
                    "Price": value
                }
                i += 1

        item_selection = input("Select the item number you want: ")

        if item_selection.isdigit() and int(item_selection) in menu_items.keys():
            selected_item = menu_items[int(item_selection)]
            quantity = input(f"How many {selected_item['Item name']} would you like to order? ")

            if quantity.isdigit() and int(quantity) > 0:
                order.append({
                    "Item name": selected_item['Item name'],
                    "Price": selected_item['Price'],
                    "Quantity": int(quantity)
                })
                print(f"Added {quantity} x {selected_item['Item name']} to your order.")
            else:
                print("Invalid quantity. Defaulting to 1.")
                order.append({
                    "Item name": selected_item['Item name'],
                    "Price": selected_item['Price'],
                    "Quantity": 1
                })
        else:
            print("Invalid item selection.")
    else:
        print(f"{menu_category} was not a valid menu option.")

    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ")
        if keep_ordering.lower() == 'y':
            break
        elif keep_ordering.lower() == 'n':
            place_order = False
            print("Thank you for your order!")
            break
        else:
            print("Invalid input. Please type 'Y' or 'N'.")

# Print out the customer's order
print("\nThis is what we are preparing for you:\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

for item in order:
    item_name = item['Item name']
    price = item['Price']
    quantity = item['Quantity']
    num_item_spaces = 24 - len(item_name)
    item_spaces = " " * num_item_spaces
    print(f"{item_name}{item_spaces} | ${price:.2f} | {quantity}")

# Calculate the total cost
total_cost = sum(item['Price'] * item['Quantity'] for item in order)
print(f"\nTotal cost: ${total_cost:.2f}")