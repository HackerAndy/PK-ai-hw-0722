import sys
from typing import List, Dict

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

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
ordered_items: List[Dict[str, object]] = []
#AGK
# if sys.argv[1] == "debug":
#     print(orders)
#     sys.exit()

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    menu_item_key= 1
    # Create a dictionary to store the menu for later retrieval
    menu_categories = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for menu_category in menu.keys():
        print(f"{menu_item_key}: {menu_category}")
        # Store the menu category associated with its menu item number
        menu_categories[menu_item_key] = menu_category
        # Add 1 to the menu item number
        menu_item_key+= 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_categories.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_categories[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            food_item_index = 1
            food_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for food_name, food_price in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(food_price) is dict: #then NOT food price, instead it's a dict of food options with prices
                    for food_option, food_option_price in food_price.items():
                        num_item_spaces = 24 - len(food_name + food_option) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{food_item_index}      | {food_name} - {food_option}{item_spaces} | ${food_option_price}")
                        food_items[food_item_index] = {
                            "Item name": food_name + " - " + food_option,
                            "Price": food_option_price
                        }
                        food_item_index += 1
                else:
                    num_item_spaces = 24 - len(food_name)
                    item_spaces = " " * num_item_spaces
                    print(f"{food_item_index}      | {food_name}{item_spaces} | ${food_price}")
                    food_items[food_item_index] = {
                        "Item name": food_name,
                        "Price": food_price
                    }
                    food_item_index += 1
            # 2. Ask customer to input menu item number
            food_item_number = input("Type menu number: ")

            # 3. Check if the customer typed a number
            if food_item_number.isdigit():
                # Convert the menu selection to an integer
                food_item_number = int(food_item_number)
                # 4. Check if the menu selection is in the menu items
                if food_item_number in food_items.keys():
                    # Store the item name as a variable
                    item_selected_name = food_items[int(food_item_number)]['Item name']
                    item_selected_price = food_items[int(food_item_number)]['Price']
                    # Ask the customer for the quantity of the menu item
                    quantity_ordered = input(f"How many {item_selected_name}'s would you like: ")
                    # Check if the quantity is a number, default to 1 if not
                    if not quantity_ordered.isdigit():
                        quantity_ordered = 1
                        print(f"Well, not sure how many {quantity_ordered} is exaclty, so we'll just assume a quantity of 1")
                    # Add the item name, price, and quantity to the order list
                    ordered_items_details = {'Item Name': str(item_selected_name) , 'Price':float(item_selected_price) ,'Quantity':int(quantity_ordered)}
                    ordered_items.append(ordered_items_details)
                # Tell the customer they didn't select a menu option
                else:
                    print(f"Sorry, the item number you selected {food_item_number}, doesn't match the list of options above")
            else:
               # Tell the customer that their input isn't valid
                print("You didn't select a number.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering.upper():
            case 'Y':
                # Keep ordering 
                place_order = True
                break
            case 'N':
                # Exit the keep odering question loop
                # Since the customer decided to stop ordering, thank them for
                # their order                
                print("Thank you for your order")
                place_order = False
                # Exit the keep ordering question loop
                break
            case _:
                # Tell the customer to try again
                print(f"Sorry, I didn't know how to process your input of: '{keep_ordering}'. Please try again")
                pass
                # Complete the order
# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
# print(ordered_items)


# 6. Loop through the items in the customer's order
order_item_index = 1
# print("Item # | Item name                | Price")
# print("-------|--------------------------|-------")

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
for item_ordered in ordered_items:
    # 7. Store the dictionary items as variables
    item_name = item_ordered['Item Name']
    price = item_ordered['Price']
    quantity = item_ordered['Quantity']

    # 8. Calculate the number of spaces for formatted printing
    num_of_item_spaces = 26 - len(item_name[:26])
    # 9. Create space strings
    item_spaces = " " * num_of_item_spaces
    # 10. Print the item name, price, and quantity
    print(f"{item_name[:26]}{item_spaces}| ${price}  | {quantity}")


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
grand_total = 0.00
for item_ordered in ordered_items:
    item_name = item_ordered['Item Name']
    price = float(item_ordered['Price'])
    quantity = int(item_ordered['Quantity'])
    total = price * quantity
    # print(f"Total for {item_name}: ${total:.2f}")
    grand_total = grand_total + total
print(f"Grand Total for your order is: ${grand_total:.2f}")
