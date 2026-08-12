order_total = float(input("Enter your Zomato order total: "))

if order_total > 299:
    print("Apply Free Delivery")
elif order_total >= 200:
    print("Add more items for free delivery")
else:
    print("Delivery charges apply")