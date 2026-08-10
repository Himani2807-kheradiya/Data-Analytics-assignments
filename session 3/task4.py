def discount(order_amount):
    return order_amount > 500

print("Order Amount: 450 ->", discount(450))
print("Order Amount: 750 ->", discount(750))