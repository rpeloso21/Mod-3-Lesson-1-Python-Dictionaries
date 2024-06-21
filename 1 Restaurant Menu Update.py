# Task 1



def add_catagory(menu, catagory):
    if catagory not in menu:
        menu[catagory] = {}
        print(f"Catagory '{catagory}' added successfully.")
    else:
        print(f"Catagory '{catagory}' already exists")

def add_item(menu, catagory, item, cost):
    if catagory in menu:
        if item not in catagory:
            menu[catagory][item] = cost
        else:
            print(f"Item '{item}' already exists.")

    else:
        print(f"Catagory '{catagory}' already exists.")


restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

add_catagory(restaurant_menu, "Beverages")
add_item(restaurant_menu, "Beverages", "Lemonade", 1.99)
add_item(restaurant_menu, "Beverages", "Coke", 1.99)

restaurant_menu["Main Course"]["Steak"] = 17.99
restaurant_menu["Starters"].popitem()

print(restaurant_menu)