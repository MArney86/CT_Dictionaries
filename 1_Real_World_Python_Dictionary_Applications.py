def display_menu(menu):
    print("\033[7m\033[1mOUR MENU\033[0m")
    for category, items in menu.items():
        print(f"\033[7m{category}\033[0m")
        for dish, price in items.items():
            print(f"\033[1m\t{dish}\033[0m - ${str(price)}")
        print("")

def update_price(menu, category, item, new_price):
    if category in menu and item in menu[category]:
        menu[category][item] = new_price
        print(f"The price of {item} has been updated to ${new_price}.")
    else:
        print(f"The item {category} was not found in the menu.")

def add_category(menu, category):
    if category not in menu:
        menu[category] = {}
        print(f"The {category} category has been added to the menu")
    else:
        print(f"The {category} category is already in the menu")

def remove_item(menu, category, item):
    if category in menu and item in menu[category]:
        del menu[category][item]
        print(f"Menu item {item} was removed from the {category} category")
    else:
        print(f"Menu item or category not found")

    

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

display_menu(restaurant_menu)
add_category(restaurant_menu, 'Beverages')
update_price(restaurant_menu, 'Main Course', 'Steak', 17.99)
remove_item(restaurant_menu, 'Starters', 'Bruschetta')
display_menu(restaurant_menu)