"""
Shipping calculator to calculate the number of items plus the shipping cost of each item.
Enter Number of Items
Enter Cost of shipping per item
If shipment over $100, 10% discount applied

***I'M NOT SURE HOW TO STORE MULTIPLE VALUES IN ONE VARIABLE***
"""

number_of_items = float(input("Enter Number of Items: "))

while number_of_items <= 0 or number_of_items > 5:
    print("Invalid Number of Items")
    number_of_items = float(input("Enter Number of Items: "))

# I'M NOT SURE HOW TO STORE MULTIPLE VALUES IN ONE VARIABLE
if number_of_items == 1:
    cost_per_item_1 = float(input("Enter cost per item: $"))
    cost_all_items = cost_per_item_1
elif number_of_items == 2:
    cost_per_item_1 = float(input("Enter cost per item 1: $"))
    cost_per_item_2 = float(input("Enter cost per item 2: $"))
    cost_all_items = cost_per_item_1 + cost_per_item_2
elif number_of_items == 3:
    cost_per_item_1 = float(input("Enter cost per item 1: $"))
    cost_per_item_2 = float(input("Enter cost per item 2: $"))
    cost_per_item_3 = float(input("Enter cost per item 3: $"))
    cost_all_items = cost_per_item_1 + cost_per_item_2 + cost_per_item_3
elif number_of_items == 4:
    cost_per_item_1 = float(input("Enter cost per item 1: $"))
    cost_per_item_2 = float(input("Enter cost per item 2: $"))
    cost_per_item_3 = float(input("Enter cost per item 3: $"))
    cost_per_item_4 = float(input("Enter cost per item 4: $"))
    cost_all_items = cost_per_item_1 + cost_per_item_2 + cost_per_item_3 + cost_per_item_4
elif number_of_items == 5:
    cost_per_item_1 = float(input("Enter cost per item 1: $"))
    cost_per_item_2 = float(input("Enter cost per item 2: $"))
    cost_per_item_3 = float(input("Enter cost per item 3: $"))
    cost_per_item_4 = float(input("Enter cost per item 4: $"))
    cost_per_item_5 = float(input("Enter cost per item 5: $"))
    cost_all_items = cost_per_item_1 + cost_per_item_2 + cost_per_item_3 + cost_per_item_4 + cost_per_item_5

print("Total Cost before Discount: ${:.2f}".format(cost_all_items))

if cost_all_items > 100:
    discounted_price = cost_all_items * 10/100
    total_cost = cost_all_items - discounted_price
    print("Total Cost: ${:.2f}".format(total_cost))
