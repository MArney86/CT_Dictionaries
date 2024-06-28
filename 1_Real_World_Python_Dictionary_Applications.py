def display_menu(menu): #a function to display the menu with nice text
    print("\n\033[7m\033[4mOUR MENU\033[0m") #Menu Heading
    for category, items in menu.items(): #iterate through the outermost layer of the dictionary
        print(f"\033[7m{category}\033[0m") #print a heading for the category
        for dish, price in items.items(): #iterate through the inner layer of the dictionary
            print(f"\033[1m\t{dish}\033[0m - ${str(price)}") #print the menu items with their prices
        print("") #spacer for next print

def update_price(menu, category, item, new_price): #a function to update the price of a menu item
    if category in menu and item in menu[category]: #verify that the category to check exists and that the item is in the category 
        menu[category][item] = new_price #change the value of the chosen item in the category dictionary's price to the new price input 
        print(f"The price of {item} has been updated to ${new_price}.") #print a notice of the change
    else: #category or item not found
        print(f"The item or {category} was not found in the menu.") #notification of failure to find category or item

def add_category(menu, category): #a fuction to add a menu category
    if category not in menu: #ensure category doesn't exist already
        menu[category] = {} #add the new (empty) category to the menu 
        print(f"The {category} category has been added to the menu") #notification of change to the menu
    else: #category already in menu
        print(f"The {category} category is already in the menu") #notify the user of category already existing

def remove_item(menu, category, item): #a function to remove a menu item from the menu
    if category in menu and item in menu[category]: #verify that the chose category exists and the item exists there first
        del menu[category][item] #delete the chosen item from the chosen category
        print(f"Menu item {item} was removed from the {category} category") #notification of changes to menu
    else: #item or category not found
        print(f"The item or category was not found in the menu") #notification of failure to find category or item

    

restaurant_menu = { #provided menu to start with
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

display_menu(restaurant_menu) #display initial menu
add_category(restaurant_menu, 'Beverages') #add the Beverage Category
update_price(restaurant_menu, 'Main Course', 'Steak', 17.99) #change the price of Steak in the Main Course category to 17.99
remove_item(restaurant_menu, 'Starters', 'Bruschetta') #remove Bruschetta from the Starters category 
display_menu(restaurant_menu) #display resulting menu