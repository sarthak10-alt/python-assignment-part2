import copy


menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

cart = []

def add_to_cart(item_name, quantity):
    #Check if item exists, is available
    if item_name not in menu:
        print(f"Item '{item_name}' not found in menu.")
        return False
    if not menu[item_name]["available"]:
        print(f"Item '{item_name}' is currently unavailable.")
        return False
    
    #Update quantity if already in cart, otherwise add new entry
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += quantity
            print(f"Updated '{item_name}' quantity to {entry['quantity']} in cart.")
            return True
        
    cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})

def remove_from_cart(item_name):
    for i, entry in enumerate(cart):
        if entry["item"] == item_name:
            cart.pop(i)
            return True
    print(f"Message: '{item_name}' not found in cart.")
    return False

#Sequence Simulation
add_to_cart("Paneer Tikka", 2)
add_to_cart("Gulab Jamun", 1)
add_to_cart("Paneer Tikka", 1)  # → quantity should update to 3, not create a new entry)
add_to_cart("Mystery Burger", 1) # -> should show error
add_to_cart("Chicken Wings", 1) # -> should show unavailable message    
remove_from_cart("Gulab Jamun") # -> should remove from cart

#Print final order Summary
print("\n== Order Summary ===")
subtotal = 0
for entry in cart:
    item_total = entry["quantity"] * entry["price"]
    subtotal += item_total
    print(f"{entry['item']:<15} x {entry['quantity']}   ₹{item_total:.2f}")

gst=subtotal * 0.05
print("-" * 35)
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Total: ₹{subtotal + gst:.2f}")
print("====================")

#Reorder Alert: Paneer Tikka — Only 7 unit(s) left (reorder level: 3)
#1 Deep Copy Demonstration
inventory_backup = copy.deepcopy(inventory)
inventory["Paneer Tikka"]["stock"] = 0  # Change Original

print(f"Original stock (Paneer Tikka): {inventory['Paneer Tikka']['stock']}")
print(f"Backup stock (Paneer Tikka): {inventory_backup['Paneer Tikka']['stock']}")

#Restore Original
inventory = copy.deepcopy(inventory_backup)

#2 Deduct items based on the Cart from Task 2
for entry in cart:
    item_name = entry["item"]
    quantity = entry["quantity"]
    if item_name in inventory:
        if inventory[item_name]["stock"] >= quantity:
            inventory[item_name]["stock"] -= quantity
        else:
            print(f"Not enough stock for '{item_name}'. Available: {inventory[item_name]['stock']}, Required: {quantity}")
            inventory[item_name]["stock"] = 0 

#3 Check for Reorder Alerts
for item, info in inventory.items():
    if info["stock"] <= info["reorder_level"]:
        print(f"⚠ Reorder Alert: {item} — Only {info['stock']} unit(s) left (reorder level: {info['reorder_level']})")

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

daily_revenue = {}
item_counts = {}

for date, orders in sales_log.items():
    day_total = 0
    for order in orders:
        for item in order["items"]:
            day_total += menu[item]["price"]
            #Count item occurance for Best Seller
            item_counts[item] = item_counts.get(item, 0) + 1
    daily_revenue[date] = day_total
    print(f"{date}: Total Revenue = ₹{day_total:.2f}")

#2 Best Selling Day
best_day = max(daily_revenue, key=daily_revenue.get)
print(f"Best Selling Day: {best_day} (₹{daily_revenue[best_day]})")

#3 Most Ordered Item
most_ordered = max(item_counts, key=item_counts.get)
print(f"Most Ordered Item: {most_ordered}")

#5 Numbered list using Enumerate
print("\n--- Final List of All Orders ---")
global_counter = 1
for date, orders in sales_log.items():
    for order in orders:
        #Calculate Price for this specific order
        price = sum(menu[item]["price"] for item in order["items"])
        items_str = ", ".join(order["items"])
        print(f"{global_counter}. Order ID: {order['order_id']} | Items: {items_str} | Total: ₹{price:.2f}")
        global_counter += 1