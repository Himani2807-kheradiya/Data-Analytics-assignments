
order_name = input("Enter the Zomato order name: ")
order_price = float(input(f"Enter the {order_name} price: "))

gst = order_price * 0.18
final_bill = order_price + gst

print("Order Name:", order_name)
print("Order Price: ₹", order_price)
print("GST (18%): ₹", gst)
print("Final Bill Amount: ₹", final_bill)