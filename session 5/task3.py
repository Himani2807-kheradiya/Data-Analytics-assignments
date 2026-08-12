def remove_last_item(order_list):
    removed_item = order_list.pop()
    return removed_item


order_list = ['Pizza', 'Burger', 'Fries', 'Cold Drink']

removed_item = remove_last_item(order_list)

print("Removed Item:", removed_item)
print("Updated Order List:", order_list)